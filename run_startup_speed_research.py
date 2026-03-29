#!/usr/bin/env python3
"""Query GPT-5.4-pro via Responses API with streaming to research AI startup speeds."""

import sys
import time
from openai import OpenAI

API_KEY = "os.environ.get("OPENAI_API_KEY")"
OUTPUT_PATH = "/Users/kumacmini/research-materials/gpt54pro_startup_speed.md"

QUERY = """2025-2026年のAIスタートアップの実際のスピード感を調査してください。Web検索で具体的なデータを集めてください。

## 1. AIスタートアップの立ち上げスピード（実例）
以下の企業が、創業からPMF・初期収益に到達するまでの期間を調べてください：
- Cursor: いつ創業し、いつARR $100Mに到達したか
- Bolt.new/Lovable: いつローンチし、いつ何ユーザーに到達したか
- Devin (Cognition AI): いつ発表し、いつ有料顧客を獲得したか
- Perplexity AI: 創業からARR $100M到達までの期間
- Windsurf (Codeium): 成長速度
- v0 by Vercel: ローンチから初期収益までの期間
- Anthropic Claude Code: ローンチから普及までの速度
- NotebookLM: Googleがどれくらいで立ち上げたか

## 2. GPU/MLクラウドスタートアップの速度
- RunPod: 創業(2022)からARR $120M(2025)まで何ヶ月か
- Modal: 創業からARR $50M推定まで何ヶ月か
- Together AI: 初期成長速度
- Replicate: 初期成長速度

## 3. 2025-2026年のAIスタートアップの「普通のスピード」
- YCのAIスタートアップバッチのデータ（何社が3ヶ月でPMF？）
- AI startupの典型的なtime-to-PMF（2024-2026年データ）
- 「6ヶ月で有料10人」は遅いのか普通なのか
- AI分野で今「速い」とされるスピード感は？
- 最近のAIスタートアップで「遅すぎて死んだ」事例

## 4. Kill Criteriaの再設計
上記データを踏まえて、AIXSのKill Criteriaを再設計してください：

現在のKill Criteria:
- 6ヶ月: 有料ユーザー10人未満→ピボット

これは2025-2026年のAIスタートアップとしては遅すぎるか？
もっと攻撃的なKill Criteriaを提案してください：

- Week 2: 何が達成されるべきか
- Month 1: 何が達成されるべきか
- Month 2: 何が達成されるべきか
- Month 3: 何が達成されるべきか（最初のピボット判断ポイント）
- Month 6: 何が達成されるべきか（Go/No-Go判断）

各マイルストーンに具体的な数字（ユーザー数、MRR、リテンション等）を設定。
根拠として上記の実例データを引用。"""


def main():
    client = OpenAI(api_key=API_KEY, timeout=1800)

    print("Starting GPT-5.4-pro streaming query (with web_search_preview)...", flush=True)
    print("This may take several minutes as the model performs web searches.\n", flush=True)
    start_time = time.time()

    try:
        print(f"[{time.time()-start_time:.1f}s] Creating streaming request...", flush=True)
        stream = client.responses.create(
            model="gpt-5.4-pro",
            tools=[{"type": "web_search_preview"}],
            input=QUERY,
            stream=True,
        )

        print(f"[{time.time()-start_time:.1f}s] Stream created, reading events...", flush=True)

        text = ""
        chunk_count = 0
        event_count = 0
        for event in stream:
            event_count += 1
            event_type = getattr(event, "type", "unknown")

            if event_count <= 5 or event_count % 100 == 0:
                print(f"  [{time.time()-start_time:.1f}s] Event #{event_count}: {event_type}", flush=True)

            if event_type == "response.output_text.delta":
                text += event.delta
                chunk_count += 1
                if chunk_count % 100 == 0:
                    elapsed = time.time() - start_time
                    print(f"  ... received {chunk_count} text chunks, {len(text)} chars, {elapsed:.0f}s elapsed", flush=True)

        elapsed = time.time() - start_time
        print(f"\nStreaming complete: {event_count} events, {chunk_count} text chunks, {len(text)} chars, {elapsed:.1f}s total", flush=True)

        if not text.strip():
            print("WARNING: Received empty response!", flush=True)
            sys.exit(1)

        # Save to file
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(f"# GPT-5.4-pro: AI Startup Speed Research (2025-2026)\n\n")
            f.write(f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"> Model: gpt-5.4-pro with web_search_preview\n")
            f.write(f"> Query time: {elapsed:.1f}s\n\n")
            f.write("---\n\n")
            f.write(text)

        print(f"\nSaved to: {OUTPUT_PATH}", flush=True)
        print(f"File size: {len(text)} characters", flush=True)

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n[{elapsed:.1f}s] ERROR: {type(e).__name__}: {e}", file=sys.stderr, flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
