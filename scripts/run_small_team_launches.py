#!/usr/bin/env python3
"""Research small-team startup launches using GPT-5.4-pro with streaming Responses API."""

import os
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from secrets
load_dotenv("/Users/kumacmini/Library/CloudStorage/Dropbox/secrets/.env")
API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    print("ERROR: OPENAI_API_KEY not found", flush=True)
    sys.exit(1)

OUTPUT_PATH = "/Users/kumacmini/research-materials/gpt54pro_small_team_launches.md"

QUERY = """少人数（1-5人）のスタートアップで、初期の立ち上げに成功したAI/DevTools/GPUクラウド企業の事例を調べてください。大型資金調達前の「ローンチ前〜初期」にフォーカスしてください。Web検索で具体的データを集めてください。

## 特に調べたい企業
以下の企業について、それぞれ：
- ローンチ前に何をしていたか（開発期間、プロトタイプ、β版）
- ローンチ時の資金（自己資金？シード？いくら？）
- ローンチ時のチーム人数
- ローンチからtraction獲得までの期間
- 最初のユーザーをどう獲得したか
- ローンチ後1ヶ月/3ヶ月/6ヶ月のユーザー数/MRR

### GPU/MLインフラ系
1. RunPod: 創業者Zhen Wang、2022年創業。少人数でスタート。ローンチ前に何を準備？初期資金は？最初のGPUはどう調達？Redditでの口コミ戦略の詳細。
2. Vast.ai: P2P GPUマーケットプレイス。2020年創業。初期チーム規模は？どうやって供給者（GPUホスト）を最初に集めた？
3. Lightning AI: PyTorch Lightning作者。OSSコミュニティからどうプラットフォーム化した？

### AI DevTools系（少人数で爆発的成長）
4. Cursor: Anysphere社、2023年。創業時4人。初期に何を作ったか。$100M ARRまでの詳細タイムライン。ローンチ前の準備は？
5. Bolt.new: StackBlitz社。少人数チーム。2024年10月ローンチ。1週間で$1M ARR。ローンチ前に何をしていた？
6. Lovable (旧GPT Engineer): 2024年ローンチ。1週間で$1M ARR。初期チーム何人？資金は？
7. Replicate: 2020年創業。Docker for MLの思想。初期チーム2-3人。最初のユーザーはどう獲得？

### 日本のDevTools/インフラ系
8. 日本の少人数DevToolsスタートアップの事例はあるか？1-3人で立ち上げてtractionを得た例。

## 各社に共通するパターンの抽出
- ローンチ前の共通行動（OSS公開？waitlist？β版？）
- 初期資金の中央値
- ローンチから最初の有料ユーザーまでの中央値
- 最初の100人をどう集めたか
- 少人数で成功した企業の共通特徴

## AIXSへの具体的示唆
- 3人チーム・$500Kシードの条件で、上記事例から学べること
- ローンチまでに最低限やるべき5つのこと
- ローンチ初週にやるべきこと
- 最初の10人/100人をどう獲得するか

具体的な数字とタイムラインを含めてください。"""


def main():
    client = OpenAI(api_key=API_KEY, timeout=1800)

    print("Starting GPT-5.4-pro streaming query (with web_search_preview)...", flush=True)
    print("This may take 10-30 minutes as the model performs extensive web searches.\n", flush=True)
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
        last_log_time = start_time

        for event in stream:
            event_count += 1
            event_type = getattr(event, "type", "unknown")
            now = time.time()

            # Log first 10, every 100th, and key event types, or every 60s
            should_log = (
                event_count <= 10
                or event_count % 100 == 0
                or "error" in event_type
                or "completed" in event_type
                or "failed" in event_type
                or now - last_log_time >= 60
            )
            if should_log:
                print(f"  [{now - start_time:.1f}s] Event #{event_count}: {event_type}", flush=True)
                last_log_time = now

            if event_type == "response.output_text.delta":
                text += event.delta
                chunk_count += 1
                if chunk_count % 100 == 0:
                    elapsed = now - start_time
                    print(f"  ... received {chunk_count} text chunks, {len(text)} chars, {elapsed:.0f}s elapsed", flush=True)

        elapsed = time.time() - start_time
        print(f"\nStreaming complete: {event_count} events, {chunk_count} text chunks, {len(text)} chars, {elapsed:.1f}s total", flush=True)

        if not text.strip():
            print("WARNING: Received empty response!", flush=True)
            sys.exit(1)

        # Save to file
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(f"# Small-Team Startup Launch Research (GPT-5.4-pro)\n\n")
            f.write(f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"> Model: gpt-5.4-pro with web_search_preview\n")
            f.write(f"> Duration: {elapsed:.1f}s\n\n")
            f.write("---\n\n")
            f.write(text)

        print(f"\nSaved to: {OUTPUT_PATH}", flush=True)
        print(f"File size: {len(text)} characters", flush=True)

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n[{elapsed:.1f}s] ERROR: {type(e).__name__}: {e}", flush=True)
        import traceback
        traceback.print_exc(file=sys.stdout)
        # Save partial result if available
        if text:
            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                f.write(f"# Small-Team Startup Launch Research (GPT-5.4-pro) [PARTIAL]\n\n")
                f.write(f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"> Model: gpt-5.4-pro with web_search_preview\n")
                f.write(f"> Duration: {elapsed:.1f}s (PARTIAL - error occurred)\n\n")
                f.write("---\n\n")
                f.write(text)
            print(f"\nPartial result saved to: {OUTPUT_PATH} ({len(text)} chars)", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
