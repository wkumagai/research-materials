#!/usr/bin/env python3
"""Quick test of gpt-5.4-pro with web search."""
import os
import time
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")

client = OpenAI(api_key=API_KEY, timeout=httpx.Timeout(300.0, connect=60.0))

print("Test: gpt-5.4-pro with simple web search query...", flush=True)
start = time.time()

stream = client.responses.create(
    model="gpt-5.4-pro",
    tools=[{"type": "web_search_preview"}],
    input="What is Cursor IDE's ARR as of 2025? Give me specific numbers from web search.",
    stream=True,
)

text = ""
for event in stream:
    etype = getattr(event, "type", "?")
    if etype == "response.output_text.delta":
        text += event.delta
    elif etype == "keepalive":
        print(f"  [{time.time()-start:.0f}s] keepalive", flush=True)
    elif etype not in ("response.created", "response.in_progress", "response.output_item.added",
                        "response.content_part.added", "response.output_item.done",
                        "response.content_part.done", "response.completed"):
        print(f"  [{time.time()-start:.0f}s] {etype}", flush=True)

print(f"\nDone in {time.time()-start:.0f}s, {len(text)} chars", flush=True)
print(text[:500], flush=True)
