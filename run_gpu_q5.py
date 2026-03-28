#!/usr/bin/env python3
"""Query 5: Other regions GPU usage research via GPT-5.4-pro."""
import os
import time, sys
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
client = OpenAI(api_key=API_KEY, timeout=1800.0)

PROMPT = """以下の地域のAI GPU利用実態を簡潔に調査してください。Web検索で最新データを使ってください。

各地域について：利用経路、主な資金源、政府施策、独自の取り組みを簡潔に。

1. カナダ：Digital Research Alliance、AICAF（$300M、66%補助）、Mila/Vector Institute
2. 韓国：KISTI、KRW 4T国立AIセンター計画、サムスン/SK等のGPU投資
3. インド：IndiaAI Mission（$1.25B）、38,000+政府管理GPU、Yotta/E2E Networks
4. UAE：Stargate UAE、Core42、MGX $100B+パイプライン
5. サウジアラビア：HUMAIN 18,000 GB300、$100B Project Transcendence
6. シンガポール：NSCC、ASPIRE 2A+、NAIS 2.0 S$1B
7. イスラエル：Nebius国立スパコン4,000 B200、Innovation Authority、NVIDIA最大非米R&D拠点
8. 台湾：NCHC、TSMC関連、NT$190B AI Infrastructure Initiatives

各地域の「AIXSにとっての意味」も1-2行で。"""

OUT = '/Users/kumacmini/research-materials/gpu_q5_others.md'

print(f"[Q5] Starting at {time.strftime('%H:%M:%S')}", flush=True)
start = time.time()
try:
    response = client.responses.create(
        model='gpt-5.4-pro',
        tools=[{'type': 'web_search_preview'}],
        input=PROMPT,
    )
    result = response.output_text
    elapsed = time.time() - start
    print(f"[Q5] OK: {len(result)} chars in {elapsed:.1f}s", flush=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"[Q5] Saved to {OUT}", flush=True)
except Exception as e:
    elapsed = time.time() - start
    print(f"[Q5] ERROR after {elapsed:.1f}s: {e}", flush=True)
    import traceback
    traceback.print_exc()
