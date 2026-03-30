#!/usr/bin/env python3
"""
Final pass: Use gpt-4.1 to synthesize all collected data into one comprehensive
Japanese report with the Kill Criteria redesign.
"""

import os
import sys
import time
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
OUTPUT_PATH = "/Users/kumacmini/research-materials/gpt54pro_startup_speed.md"

MODEL = "gpt-4.1"

# Read the two existing files
with open("/Users/kumacmini/research-materials/gpt54pro_startup_speed.md") as f:
    initial_data = f.read()

with open("/Users/kumacmini/research-materials/gpt54pro_startup_speed_supplement.md") as f:
    supplement_data = f.read()

SYNTHESIS_QUERY = f"""あなたはAIスタートアップ市場のアナリストです。以下の2つの調査結果を統合し、1つの包括的な日本語レポートとして再構成してください。

Web検索で追加データも調べてください。特に以下の不足データを重点的に：
- Bolt.new: 2024年10月ローンチ、最初の3ヶ月でARR数億円、StackBlitzが開発
- Lovable: 2024年末ローンチ、急成長中のAIアプリビルダー
- Devin: 2024年3月発表、2024年12月GA、Cognition AI $2B valuation
- Windsurf: OpenAIが$3Bで買収発表(2025年)、以前はCodeium
- v0.dev: 2023年9月ローンチ、Vercelの生成AIプロダクト
- Claude Code: 2025年2月ローンチ
- NotebookLM: 2023年7月ローンチ、2024年にAudio Overviewで急成長
- Together AI: 2022年創業、2024年にSeries A $106M、推定ARR数千万ドル
- Replicate: 2019年創業、2024年にSeries B $40M

## 調査結果1（初期調査）
{initial_data}

## 調査結果2（補足調査）
{supplement_data}

## 出力形式

以下の構造で、詳細かつデータドリブンなレポートを作成してください：

# AIスタートアップのスピード感調査（2025-2026年）

## 1. AIスタートアップの立ち上げスピード（実例データ）
各社について以下を表形式でまとめ：
- 企業名、創業年月、PMF到達時期、ARR $100M到達時期、現在のARR、ユーザー数
- 「創業→PMF」期間、「PMF→ARR $100M」期間

## 2. GPU/MLクラウドスタートアップの速度
同様のデータ表

## 3. 2025-2026年のAIスタートアップの「普通のスピード」
- YCバッチデータ
- Time-to-PMF統計
- 「速い」の基準
- 失敗事例（表形式）

## 4. Kill Criteriaの再設計
- 現行基準の評価
- 新基準（Week 2, Month 1, 2, 3, 6の各KPI）
- ソロファウンダー調整版
- 判断フレームワーク

全てのデータに出典を付けてください。不明な部分は「推定」と明記。"""

def main():
    client = OpenAI(
        api_key=API_KEY,
        timeout=httpx.Timeout(600.0, connect=60.0),
    )

    print(f"Running synthesis query with {MODEL}...", flush=True)
    start = time.time()

    stream = client.responses.create(
        model=MODEL,
        tools=[{"type": "web_search_preview"}],
        input=SYNTHESIS_QUERY,
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
                print(f"  [{time.time()-start:.0f}s] First chunk", flush=True)
            if chunk_count % 500 == 0:
                print(f"  [{time.time()-start:.0f}s] {chunk_count} chunks, {len(text)} chars", flush=True)
        elif etype == "keepalive":
            print(f"  [{time.time()-start:.0f}s] searching...", flush=True)

    elapsed = time.time() - start
    print(f"Done: {len(text)} chars in {elapsed:.0f}s", flush=True)

    # Write final output
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"> Model: {MODEL} with web_search_preview (OpenAI Responses API, streaming)\n")
        f.write(f"> Note: gpt-5.4-pro was tested but completely unresponsive (infinite keepalive). Used {MODEL} as fallback.\n")
        f.write(f"> Query time: {elapsed:.1f}s\n\n")
        f.write("---\n\n")
        f.write(text)

    print(f"Saved to: {OUTPUT_PATH}", flush=True)


if __name__ == "__main__":
    main()
