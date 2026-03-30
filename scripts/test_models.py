#!/usr/bin/env python3
"""Test which models work with web_search_preview."""
import os
import time
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")

client = OpenAI(api_key=API_KEY, timeout=httpx.Timeout(300.0, connect=60.0))

MODELS = ["gpt-4.1", "o4-mini"]

for model in MODELS:
    print(f"\n{'='*50}", flush=True)
    print(f"Testing {model} with web_search_preview...", flush=True)
    start = time.time()
    try:
        stream = client.responses.create(
            model=model,
            tools=[{"type": "web_search_preview"}],
            input="What is Cursor IDE's current ARR in 2025? Give specific numbers.",
            stream=True,
        )
        text = ""
        for event in stream:
            etype = getattr(event, "type", "?")
            if etype == "response.output_text.delta":
                text += event.delta
            elif etype == "keepalive":
                elapsed = time.time() - start
                if elapsed > 120:
                    print(f"  [{elapsed:.0f}s] TIMEOUT - still searching, skipping model", flush=True)
                    break
                print(f"  [{time.time()-start:.0f}s] keepalive", flush=True)

        elapsed = time.time() - start
        print(f"  Result: {len(text)} chars in {elapsed:.0f}s", flush=True)
        if text:
            print(f"  Preview: {text[:300]}", flush=True)
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}", flush=True)

print("\nDone testing models.", flush=True)
