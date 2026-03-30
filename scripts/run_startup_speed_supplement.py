#!/usr/bin/env python3
"""Supplementary queries for data gaps in the initial research."""

import os
import sys
import time
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
OUTPUT_PATH = "/Users/kumacmini/research-materials/gpt54pro_startup_speed_supplement.md"

MODEL = "gpt-4.1"

QUERIES = [
    {
        "label": "Supplement A: Perplexity AI, Bolt.new, Lovable growth data",
        "query": """Search the web for specific growth metrics of these AI startups. Report ALL numbers you find in English:

1. Perplexity AI:
- When was it founded? (search: "Perplexity AI founded" "Perplexity AI ARR" "Perplexity revenue 2024 2025")
- What is its ARR? When did it reach $100M ARR?
- How many users does it have?
- What funding rounds and valuations?

2. Bolt.new (by StackBlitz):
- When did Bolt.new launch? (search: "Bolt.new launch date" "Bolt.new users" "Bolt.new growth")
- How many users/projects created?
- Revenue/ARR data?

3. Lovable.dev:
- When did it launch? (search: "Lovable.dev launch" "Lovable AI growth" "Lovable users")
- Growth metrics?
- Revenue data?

4. Devin by Cognition AI:
- When was Devin announced? (search: "Devin AI launch date" "Cognition AI Devin GA" "Devin pricing")
- When was it generally available?
- How many paying customers?
- Funding data?

Report every number and date you can find from web search."""
    },
    {
        "label": "Supplement B: Windsurf, v0, Claude Code, NotebookLM, Together AI, Replicate",
        "query": """Search the web for specific growth metrics of these companies. Report ALL numbers and dates:

1. Windsurf (formerly Codeium):
- Search: "Windsurf Codeium users" "Codeium ARR" "OpenAI acquires Windsurf" "Windsurf acquisition price"
- Users, ARR, acquisition details?

2. v0 by Vercel:
- Search: "v0.dev launch" "v0 Vercel users" "v0 revenue"
- Launch date, users, revenue?

3. Claude Code by Anthropic:
- Search: "Claude Code launch" "Claude Code users" "Anthropic Claude Code"
- Launch date, adoption metrics?

4. NotebookLM by Google:
- Search: "NotebookLM launch" "NotebookLM users" "NotebookLM growth"
- Launch timeline, user numbers?

5. Together AI:
- Search: "Together AI funding" "Together AI ARR" "Together AI revenue 2024 2025"
- Founding date, funding rounds, ARR estimates?

6. Replicate:
- Search: "Replicate funding" "Replicate ARR" "Replicate users"
- Founding date, metrics?

Report every concrete number and date you find."""
    },
    {
        "label": "Supplement C: AI startup failures 2024-2025 specific examples",
        "query": """Search the web for specific AI startup failures and shutdowns in 2024-2025. I need concrete examples:

Search terms: "AI startup shutdown 2024" "AI startup failed 2025" "AI company closed" "AI startup pivot" "AI startup graveyard"

For each failure, report:
- Company name
- What they did
- When they shut down/pivoted
- Why (too slow? no PMF? ran out of money?)
- How much they had raised

Also search for:
- "AI startup failure rate 2024 2025"
- "AI bubble burst 2025"
- "AI startup survival rate"
- Statistics on how many AI startups fail

Also find specific data on:
- "YC batch AI startup survival rate"
- "AI startup time to PMF median"
- "startup speed benchmarks 2025"

Report all concrete data points."""
    },
]


def run_query(client, label, query):
    print(f"\n{'='*60}", flush=True)
    print(f"  {label}", flush=True)
    print(f"{'='*60}", flush=True)
    start_time = time.time()

    stream = client.responses.create(
        model=MODEL,
        tools=[{"type": "web_search_preview"}],
        input=query,
        stream=True,
    )

    text = ""
    chunk_count = 0
    for event in stream:
        etype = getattr(event, "type", "?")
        if etype == "response.output_text.delta":
            text += event.delta
            chunk_count += 1
            if chunk_count == 1:
                print(f"  [{time.time()-start_time:.0f}s] First text chunk", flush=True)
            if chunk_count % 200 == 0:
                print(f"  [{time.time()-start_time:.0f}s] {chunk_count} chunks, {len(text)} chars", flush=True)
        elif etype == "keepalive":
            print(f"  [{time.time()-start_time:.0f}s] searching...", flush=True)

    elapsed = time.time() - start_time
    print(f"  Done: {len(text)} chars in {elapsed:.0f}s", flush=True)
    return text, elapsed


def main():
    client = OpenAI(
        api_key=API_KEY,
        timeout=httpx.Timeout(600.0, connect=60.0),
    )

    results = []
    total_start = time.time()

    for q in QUERIES:
        try:
            text, elapsed = run_query(client, q["label"], q["query"])
            results.append((q["label"], text, elapsed))
        except Exception as e:
            print(f"  ERROR: {type(e).__name__}: {e}", flush=True)
            results.append((q["label"], f"[ERROR: {e}]", 0))

    total_elapsed = time.time() - total_start

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# Supplementary Startup Speed Data\n\n")
        f.write(f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"> Model: {MODEL} with web_search_preview\n")
        f.write(f"> Total time: {total_elapsed:.1f}s\n\n---\n\n")

        for label, text, elapsed in results:
            f.write(f"## {label}\n\n> Query time: {elapsed:.1f}s\n\n")
            f.write(text)
            f.write("\n\n---\n\n")

    total_chars = sum(len(t) for _, t, _ in results)
    print(f"\nALL DONE: {total_chars} chars in {total_elapsed:.0f}s", flush=True)
    print(f"Saved to: {OUTPUT_PATH}", flush=True)


if __name__ == "__main__":
    main()
