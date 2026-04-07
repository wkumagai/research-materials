#!/usr/bin/env python3
"""Patch a Jupyter notebook to replace CUDA device references with MPS.

Usage:
    python patch_cuda_to_mps.py <notebook.ipynb> [--output <patched.ipynb>]

If --output is not specified, the notebook is modified in place.

This script handles the following replacements in code cells:
  - torch.device("cuda") -> torch.device("mps")
  - torch.device('cuda') -> torch.device('mps')
  - .to("cuda")          -> .to("mps")
  - .to('cuda')          -> .to('mps')
  - .cuda()              -> .to("mps")
  - device = "cuda"      -> device = "mps"
  - device = 'cuda'      -> device = 'mps'
  - torch.cuda.is_available() -> torch.backends.mps.is_available()
  - "cuda:0"             -> "mps"
  - 'cuda:0'             -> 'mps'
  - "cuda"               -> "mps" (in device context)
  - 'cuda'               -> 'mps' (in device context)

It also removes or comments out lines that are CUDA-only and will fail on MPS:
  - torch.cuda.synchronize() lines
  - torch.cuda.empty_cache() lines (replaced with torch.mps.empty_cache())
"""

import argparse
import json
import re
import sys
from pathlib import Path


def patch_source_line(line: str) -> str:
    """Apply CUDA-to-MPS replacements to a single source line."""

    # Skip comment-only lines
    stripped = line.lstrip()
    if stripped.startswith("#"):
        return line

    # torch.cuda.is_available() -> torch.backends.mps.is_available()
    line = line.replace("torch.cuda.is_available()", "torch.backends.mps.is_available()")

    # torch.cuda.synchronize() -> torch.mps.synchronize()
    line = re.sub(r"torch\.cuda\.synchronize\(\)", "torch.mps.synchronize()", line)

    # torch.cuda.empty_cache() -> torch.mps.empty_cache()
    line = re.sub(r"torch\.cuda\.empty_cache\(\)", "torch.mps.empty_cache()", line)

    # torch.cuda.device_count() -> 1 (MPS has one device)
    line = re.sub(r"torch\.cuda\.device_count\(\)", "1", line)

    # .cuda() method calls -> .to("mps")
    line = re.sub(r"\.cuda\(\)", '.to("mps")', line)

    # torch.device("cuda:N") or torch.device('cuda:N')
    line = re.sub(r"""torch\.device\(["']cuda:\d+["']\)""", 'torch.device("mps")', line)

    # torch.device("cuda") or torch.device('cuda')
    line = re.sub(r"""torch\.device\(["']cuda["']\)""", 'torch.device("mps")', line)

    # .to("cuda:N") or .to('cuda:N')
    line = re.sub(r"""\.to\(["']cuda:\d+["']\)""", '.to("mps")', line)

    # .to("cuda") or .to('cuda')
    line = re.sub(r"""\.to\(["']cuda["']\)""", '.to("mps")', line)

    # device = "cuda:N" or device = 'cuda:N'
    line = re.sub(r"""(device\s*=\s*)["']cuda:\d+["']""", r'\1"mps"', line)

    # device = "cuda" or device = 'cuda'
    line = re.sub(r"""(device\s*=\s*)["']cuda["']""", r'\1"mps"', line)

    # "cuda" if torch... patterns -> "mps" if torch...
    line = re.sub(
        r"""["']cuda["'](\s+if\s+torch)""",
        r'"mps"\1',
        line,
    )

    # Remaining generic "cuda" -> "mps" in common patterns
    # e.g., output_device="cuda" or output_device='cuda'
    line = re.sub(r"""(output_device\s*=\s*)["']cuda(:\d+)?["']""", r'\1"mps"', line)

    return line


def patch_notebook(notebook_path: Path, output_path: Path | None = None) -> dict:
    """Patch a notebook file, returning a summary of changes."""
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells_modified = 0
    lines_modified = 0

    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue

        source = cell.get("source", [])
        new_source = []
        cell_changed = False

        for line in source:
            new_line = patch_source_line(line)
            if new_line != line:
                cell_changed = True
                lines_modified += 1
            new_source.append(new_line)

        if cell_changed:
            cell["source"] = new_source
            cells_modified += 1

    dest = output_path or notebook_path
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")

    return {
        "notebook": str(notebook_path),
        "output": str(dest),
        "cells_modified": cells_modified,
        "lines_modified": lines_modified,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Patch a Jupyter notebook to replace CUDA device references with MPS."
    )
    parser.add_argument("notebook", type=Path, help="Path to the notebook file")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output path (default: modify in place)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files",
    )
    args = parser.parse_args()

    if not args.notebook.exists():
        print(f"Error: {args.notebook} does not exist", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        # In dry-run mode, read and report but do not write
        with open(args.notebook, "r", encoding="utf-8") as f:
            nb = json.load(f)
        for i, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            for j, line in enumerate(cell.get("source", [])):
                new_line = patch_source_line(line)
                if new_line != line:
                    print(f"Cell {i}, line {j}:")
                    print(f"  - {line.rstrip()}")
                    print(f"  + {new_line.rstrip()}")
        sys.exit(0)

    result = patch_notebook(args.notebook, args.output)
    print(
        f"Patched {result['notebook']} -> {result['output']}: "
        f"{result['cells_modified']} cells, {result['lines_modified']} lines modified"
    )


if __name__ == "__main__":
    main()
