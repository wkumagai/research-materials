#!/usr/bin/env python3
"""
Query GPT-4.1 (with web_search_preview) for AI startup speed research.
Note: gpt-5.4-pro was tested but hangs indefinitely (even without web search).
gpt-4.1 returns results reliably in seconds with web search.
"""

import sys
import time
import httpx
from openai import OpenAI

API_KEY = "os.environ.get("OPENAI_API_KEY")"
OUTPUT_PATH = "/Users/kumacmini/research-materials/gpt54pro_startup_speed.md"

# Use gpt-4.1 as primary since gpt-5.4-pro is unresponsive
MODEL = "gpt-4.1"

QUERIES = [
    {
        "label": "Part 1: AI Coding/Search Startup Growth Speed (2024-2026)",
        "query": """Web検索で2024-2026年のAIスタートアップの成長速度データを調べ、日本語で詳細に報告してください。

以下の企業について、創業日、PMF到達時期、ARR到達マイルストーン、ユーザー数を具体的な数字と日付で報告してください：

1. **Cursor (Anysphere)**: 創業年月、ARR $100M到達時期、ARR $300M到達時期、2025年末時点のARR、ユーザー数推移
2. **Bolt.new**: ローンチ時期、ユーザー数マイルストーン、収益成長
3. **Lovable**: ローンチ時期、成長速度、ユーザー数
4. **Devin (Cognition AI)**: 発表時期、GA時期、有料顧客数、ARR推定
5. **Perplexity AI**: 創業時期、ARR $100M到達時期、現在のARR
6. **Windsurf (Codeium→OpenAI買収)**: 成長速度、ユーザー数、買収額
7. **v0 by Vercel**: ローンチ時期、普及速度
8. **Claude Code by Anthropic**: ローンチ時期、普及速度

各社のデータを表形式でまとめ、「創業からPMF到達」「PMFからARR $100M」の期間を比較してください。"""
    },
    {
        "label": "Part 2: GPU/ML Cloud Startup Growth Speed",
        "query": """Web検索で2022-2026年のGPU/MLインフラスタートアップの成長データを調べ、日本語で詳細に報告してください。

1. **RunPod**: 創業年(2022頃)、各年のARR推移、ARR $120M到達時期、従業員数、資金調達歴
2. **Modal**: 創業年、ARR推移（推定含む）、資金調達額・時期
3. **Together AI**: 創業年、成長速度、資金調達額・時期、推定ARR
4. **Replicate**: 創業年、成長速度、ユーザー数、ARR推定
5. **Lambda Labs**: GPU cloud事業の成長

各社の「創業からARRマイルストーンまでの月数」を比較してください。"""
    },
    {
        "label": "Part 3: AI Startup Speed Norms & Failure Cases (2024-2026)",
        "query": """Web検索で2024-2026年のAIスタートアップの「普通のスピード」と失敗事例を調べ、日本語で詳細に報告してください。

1. **Y Combinator 2024-2025バッチのAIスタートアップ統計**:
   - AIスタートアップの割合
   - PMF到達率と平均時間
   - バッチ後の成長速度

2. **AIスタートアップのtime-to-PMF（2024-2026年）**:
   - 業界データやレポートから
   - B2BとB2Cの違い
   - AI infra vs AI application の違い

3. **「速い」の基準 (2025年)**:
   - 何ヶ月で何ユーザーが「速い」か
   - MRRの成長率でどのくらいが上位か
   - Week-over-week growth rateの参考値

4. **AI startupの失敗・shutdown事例（2024-2025年）**:
   - 遅すぎて死んだ事例（具体名と理由）
   - AI startup failure rate統計
   - 失敗の共通パターン

5. **「6ヶ月で有料10人」は2025年基準でどうか**:
   - 遅い？普通？
   - 同時期の成功企業との比較"""
    },
    {
        "label": "Part 4: AIXS Kill Criteria Redesign Based on Market Data",
        "query": """以下の2025年AIスタートアップの実績データに基づいて、AIXSプロジェクトのKill Criteria（撤退基準）を再設計してください。日本語で回答してください。

### 参考データ（2025年実績）
- Cursor: ~2年でARR $100M → $1B
- Bolt.new: 数ヶ月でバイラル成長
- Perplexity: ~2年でARR $100M+
- RunPod: ~3年でARR $120M+
- 2025年のAIスタートアップは3-6ヶ月でPMF到達が「普通」
- YC AI batchの多くが3ヶ月以内にPMF

### 現在のAIXS Kill Criteria
- 6ヶ月: 有料ユーザー10人未満→ピボット

### 質問
1. 「6ヶ月で有料10人」は2025-2026年のAIスタートアップとして十分攻撃的か？それとも甘すぎるか？根拠を示して回答。

2. 以下の各タイムラインで達成すべきKPIを具体的な数字で提案：

**Week 2:**
- 達成すべき定性的・定量的指標

**Month 1:**
- ユーザー数目標
- MRR目標
- その他指標

**Month 2:**
- ユーザー数目標
- MRR目標
- リテンション目標
- 成長率目標

**Month 3（最初のピボット判断ポイント）:**
- ユーザー数目標
- MRR目標
- リテンション目標
- NPS目標
- ピボット/継続/撤退の判断基準

**Month 6（Go/No-Go判断）:**
- ARR目標
- ユーザー数目標
- Unit economics
- Go/No-Go判断基準

3. ソロファウンダー（リソース制約あり）の場合の現実的な調整

4. ピボット vs 継続 vs 完全撤退の判断フレームワーク（フローチャート形式で）

上記の実例データを根拠として引用しながら、具体的な数字を含む提案をしてください。"""
    },
]


def run_query(client, label, query):
    """Run a single streaming query and return the text."""
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
    event_count = 0

    for event in stream:
        event_count += 1
        event_type = getattr(event, "type", "?")

        if event_type == "response.output_text.delta":
            text += event.delta
            chunk_count += 1
            if chunk_count == 1:
                print(f"  [{time.time()-start_time:.0f}s] First text chunk received", flush=True)
            if chunk_count % 200 == 0:
                print(f"  [{time.time()-start_time:.0f}s] {chunk_count} chunks, {len(text)} chars", flush=True)
        elif event_type == "keepalive":
            print(f"  [{time.time()-start_time:.0f}s] searching...", flush=True)
        elif event_type == "response.failed":
            print(f"  FAILED: {event}", flush=True)

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

    print(f"Using model: {MODEL} with web_search_preview", flush=True)
    print(f"Note: gpt-5.4-pro was tested but hangs indefinitely on all queries.", flush=True)
    print(f"      gpt-4.1 delivers excellent web search results in seconds.", flush=True)

    for i, q in enumerate(QUERIES):
        try:
            text, elapsed = run_query(client, q["label"], q["query"])
            results.append((q["label"], text, elapsed))
            if not text.strip():
                print(f"  WARNING: Empty response for {q['label']}", flush=True)
        except Exception as e:
            print(f"\n  ERROR on {q['label']}: {type(e).__name__}: {e}", flush=True)
            import traceback
            traceback.print_exc(file=sys.stdout)
            results.append((q["label"], f"[ERROR: {e}]", 0))

    total_elapsed = time.time() - total_start

    # Combine and save
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# AI Startup Speed Research (2025-2026)\n\n")
        f.write(f"> Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"> Model: {MODEL} with web_search_preview (Responses API, streaming)\n")
        f.write(f"> Note: gpt-5.4-pro was tested but unresponsive (infinite keepalive on all queries including non-web-search). Fell back to {MODEL}.\n")
        f.write(f"> Total query time: {total_elapsed:.1f}s ({len(results)} queries)\n\n")
        f.write("---\n\n")

        for label, text, elapsed in results:
            f.write(f"## {label}\n\n")
            f.write(f"> Query time: {elapsed:.1f}s\n\n")
            f.write(text)
            f.write("\n\n---\n\n")

    total_chars = sum(len(t) for _, t, _ in results)
    print(f"\n{'='*60}", flush=True)
    print(f"ALL DONE", flush=True)
    print(f"  Total chars: {total_chars}", flush=True)
    print(f"  Total time:  {total_elapsed:.0f}s", flush=True)
    print(f"  Saved to:    {OUTPUT_PATH}", flush=True)
    print(f"{'='*60}", flush=True)


if __name__ == "__main__":
    main()
