#!/usr/bin/env python3
"""Query GPT-5.4-pro in 4 smaller parts to avoid timeout on large web searches."""

import os
import sys
import time
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
OUTPUT_PATH = "/Users/kumacmini/research-materials/gpt54pro_startup_speed.md"

QUERIES = [
    {
        "label": "Part 1: AI Coding/Search Startup Speed",
        "query": """Web検索で2025-2026年のAIスタートアップの成長速度を調べてください。以下の企業について、創業日、PMF到達、ARR到達を具体的な日付と数字で報告してください：

1. Cursor (Anysphere): 創業年、ARR $100M到達時期、ユーザー数推移
2. Bolt.new: ローンチ時期、ユーザー数到達マイルストーン
3. Lovable: ローンチ時期、成長速度
4. Devin (Cognition AI): 発表時期、GA時期、有料顧客獲得時期
5. Perplexity AI: 創業時期、ARR $100M到達時期
6. Windsurf (Codeium): 成長速度、ユーザー数
7. v0 by Vercel: ローンチ時期、初期収益
8. Claude Code by Anthropic: ローンチ時期、普及速度

各社について確認できた具体的数字を全て列挙してください。"""
    },
    {
        "label": "Part 2: GPU/ML Cloud Startup Speed",
        "query": """Web検索で2022-2026年のGPU/MLインフラスタートアップの成長速度を調べてください：

1. RunPod: 創業年(2022頃)、ARR推移、$120M ARR到達時期
2. Modal: 創業年、ARR推移、推定$50M ARR到達時期
3. Together AI: 創業年、成長速度、資金調達額と時期
4. Replicate: 創業年、成長速度、ユーザー数

各社の具体的な数字（ARR、ユーザー数、成長率）を報告してください。"""
    },
    {
        "label": "Part 3: AI Startup Speed Norms 2025-2026",
        "query": """Web検索で2024-2026年のAIスタートアップの「普通のスピード」を調べてください：

1. Y Combinator 2024-2025バッチのAIスタートアップ統計（PMF到達率、速度）
2. AIスタートアップの典型的なtime-to-PMF（2024-2026年のデータや記事）
3. 「速い」AIスタートアップの基準（何ヶ月で何ユーザー/何MRR？）
4. 最近のAIスタートアップで「遅すぎて失敗した」具体的事例（2024-2025年）
5. AI startup failure rate、speed-to-market statistics

具体的なデータと情報源を示してください。"""
    },
    {
        "label": "Part 4: Kill Criteria Redesign",
        "query": """AIスタートアップのKill Criteria（撤退基準）を再設計してください。

前提データ（先の調査結果から）：
- Cursor: 創業約2年でARR $100M
- Bolt.new/Lovable: ローンチ数ヶ月で急成長
- Perplexity: 約2年でARR $100M
- RunPod: 約3年でARR $120M
- 2025年のAI市場は非常に速い

現在のAIXS Kill Criteria:
- 6ヶ月: 有料ユーザー10人未満→ピボット

質問：
1. 「6ヶ月で有料10人」は2025-2026年のAIスタートアップとして遅すぎるか？
2. 以下の各マイルストーンで何を達成すべきか、具体的な数字で提案してください：
   - Week 2: 達成すべきこと
   - Month 1: 達成すべきこと
   - Month 2: 達成すべきこと
   - Month 3: 達成すべきこと（最初のピボット判断ポイント）
   - Month 6: 達成すべきこと（Go/No-Go判断）
3. 各マイルストーンに具体的なKPI（ユーザー数、MRR、リテンション率、NPS等）を設定
4. ピボット vs 継続 vs 撤退の判断フレームワーク

根拠を示しながら提案してください。"""
    },
]


def run_query(client, label, query):
    """Run a single streaming query and return the text."""
    print(f"\n{'='*60}", flush=True)
    print(f"  {label}", flush=True)
    print(f"{'='*60}", flush=True)
    start_time = time.time()

    stream = client.responses.create(
        model="gpt-5.4-pro",
        tools=[{"type": "web_search_preview"}],
        input=query,
        stream=True,
    )

    text = ""
    chunk_count = 0
    event_count = 0

    for event in stream:
        event_count += 1
        event_type = getattr(event, "type", "unknown")

        if event_type == "response.output_text.delta":
            text += event.delta
            chunk_count += 1
            if chunk_count == 1:
                print(f"  [{time.time()-start_time:.0f}s] First text chunk!", flush=True)
            if chunk_count % 200 == 0:
                print(f"  [{time.time()-start_time:.0f}s] {chunk_count} chunks, {len(text)} chars", flush=True)
        elif event_type == "keepalive" and event_count % 5 == 0:
            print(f"  [{time.time()-start_time:.0f}s] Still searching... (event #{event_count})", flush=True)
        elif event_type == "response.failed":
            print(f"  FAILED: {event}", flush=True)

    elapsed = time.time() - start_time
    print(f"  Done: {event_count} events, {chunk_count} text chunks, {len(text)} chars in {elapsed:.0f}s", flush=True)
    return text, elapsed


def main():
    client = OpenAI(
        api_key=API_KEY,
        timeout=httpx.Timeout(900.0, connect=60.0),
    )

    results = []
    total_start = time.time()

    for i, q in enumerate(QUERIES):
        try:
            text, elapsed = run_query(client, q["label"], q["query"])
            results.append((q["label"], text, elapsed))
        except Exception as e:
            print(f"\n  ERROR on {q['label']}: {type(e).__name__}: {e}", flush=True)
            results.append((q["label"], f"[ERROR: {e}]", 0))

    total_elapsed = time.time() - total_start

    # Combine and save
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# GPT-5.4-pro: AI Startup Speed Research (2025-2026)\n\n")
        f.write(f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"> Model: gpt-5.4-pro with web_search_preview\n")
        f.write(f"> Total query time: {total_elapsed:.1f}s ({len(results)} queries)\n\n")
        f.write("---\n\n")

        for label, text, elapsed in results:
            f.write(f"## {label}\n\n")
            f.write(f"> Query time: {elapsed:.1f}s\n\n")
            f.write(text)
            f.write("\n\n---\n\n")

    total_chars = sum(len(t) for _, t, _ in results)
    print(f"\n{'='*60}", flush=True)
    print(f"ALL DONE: {total_chars} total chars in {total_elapsed:.0f}s", flush=True)
    print(f"Saved to: {OUTPUT_PATH}", flush=True)
    print(f"{'='*60}", flush=True)


if __name__ == "__main__":
    main()
