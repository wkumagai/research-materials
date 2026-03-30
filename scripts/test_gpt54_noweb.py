#!/usr/bin/env python3
"""Test gpt-5.4-pro without web search, and try with web search using different search config."""
import os
import time
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")

client = OpenAI(api_key=API_KEY, timeout=httpx.Timeout(600.0, connect=60.0))

# Test 1: gpt-5.4-pro WITHOUT web search
print("Test 1: gpt-5.4-pro without web search...", flush=True)
start = time.time()
try:
    stream = client.responses.create(
        model="gpt-5.4-pro",
        input="What do you know about Cursor IDE's ARR growth in 2024-2025?",
        stream=True,
    )
    text = ""
    for event in stream:
        etype = getattr(event, "type", "?")
        if etype == "response.output_text.delta":
            text += event.delta
        elif etype == "keepalive":
            print(f"  [{time.time()-start:.0f}s] keepalive", flush=True)
    print(f"  Result: {len(text)} chars in {time.time()-start:.0f}s", flush=True)
    print(f"  Preview: {text[:300]}", flush=True)
except Exception as e:
    print(f"  ERROR: {type(e).__name__}: {e}", flush=True)

# Test 2: gpt-5.4-pro with web_search_preview using search_context_size=low
print("\n\nTest 2: gpt-5.4-pro with web_search_preview (search_context_size=low)...", flush=True)
start = time.time()
try:
    stream = client.responses.create(
        model="gpt-5.4-pro",
        tools=[{"type": "web_search_preview", "search_context_size": "low"}],
        input="What is Cursor IDE's ARR in 2025?",
        stream=True,
    )
    text = ""
    for event in stream:
        etype = getattr(event, "type", "?")
        if etype == "response.output_text.delta":
            text += event.delta
        elif etype == "keepalive":
            elapsed = time.time() - start
            print(f"  [{elapsed:.0f}s] keepalive", flush=True)
            if elapsed > 300:
                print("  TIMEOUT after 5min, breaking", flush=True)
                break
    print(f"  Result: {len(text)} chars in {time.time()-start:.0f}s", flush=True)
    if text:
        print(f"  Preview: {text[:300]}", flush=True)
except Exception as e:
    print(f"  ERROR: {type(e).__name__}: {e}", flush=True)

print("\nDone.", flush=True)
