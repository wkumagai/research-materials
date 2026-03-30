#!/usr/bin/env python3
"""Combine Q1-Q5 results into a single markdown file."""
import os

BASE = '/Users/kumacmini/research-materials'
OUTPUT = os.path.join(BASE, 'gpt54pro_regional_gpu_usage.md')

sections = [
    ("## 1. アメリカのGPU利用実態", os.path.join(BASE, 'gpu_q1_usa.md')),
    ("## 2. EU・UKのGPU利用実態", os.path.join(BASE, 'gpu_q2_eu_uk.md')),
    ("## 3. 中国のGPU利用実態", os.path.join(BASE, 'gpu_q3_china.md')),
    ("## 4. 日本のGPU利用実態", os.path.join(BASE, 'gpu_q4_japan.md')),
    ("## 5. その他の重要地域", os.path.join(BASE, 'gpu_q5_others.md')),
]

header = """# GPT-5.4-pro 地域別GPU利用実態調査

Model: gpt-5.4-pro (Responses API + web_search_preview)
調査日: 2026-03-28

---

"""

with open(OUTPUT, 'w', encoding='utf-8') as out:
    out.write(header)
    for title, path in sections:
        out.write(f"{title}\n\n")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            out.write(content)
            print(f"  OK: {title} ({len(content)} chars from {os.path.basename(path)})")
        else:
            out.write("[Query result not yet available]\n")
            print(f"  MISSING: {title} ({os.path.basename(path)})")
        out.write("\n\n---\n\n")

print(f"\nCombined output saved to: {OUTPUT}")
