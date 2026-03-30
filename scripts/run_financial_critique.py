#!/usr/bin/env python3
"""
GPT-5.4-pro financial critique queries for AIXS GPU cloud startup.
Runs 2 queries concurrently using OpenAI Responses API with web_search_preview.
Uses extended timeout (1800s) via httpx to handle long web search operations.
"""

import concurrent.futures
import datetime
import json
import os
import sys
import traceback
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")

# Create httpx client with 1800s (30 min) timeout to handle long web search operations
http_client = httpx.Client(
    timeout=httpx.Timeout(1800.0, connect=60.0),
)

client = OpenAI(
    api_key=API_KEY,
    timeout=1800.0,
    http_client=http_client,
)

QUERY_1_BENCHMARKS = """GPUクラウドスタートアップの財務データを徹底的に調べてください。Web検索で最新データを使ってください。

1. RunPodの財務データ
- ARR（最新）、成長率、チーム人数、調達額、粗利率推定
- ユーザー数、ARPU推定

2. Modalの財務データ
- 評価額、ARR推定、チーム人数、粗利率推定

3. CoreWeaveの財務データ
- 売上$5.1B(2025)、粗利率35%、営業利益率

4. Lambda Labsの財務データ
- ARR $500M、チーム人数、粗利率推定

5. Vast.aiの財務データ
- ARR推定（$2.2Mとの情報あり）、ユーザー数12万、手数料率

6. 研究者向けSaaSのベンチマーク
- 月次churn rate中央値
- ARPU中央値
- フリーミアム転換率中央値
- LTV中央値
- CAC中央値

7. GPUクラウドのユニットエコノミクス実態
- H100 1台の年間コスト（減価償却+電力+コロケーション）
- H100 1台を$2.50/hrで売った場合の年間収益（稼働率70%）
- 粗利計算

全て定量データで。推定値は「推定」と明記。"""

QUERY_2_PRICING_CRITIQUE = """以下のAIXSの価格プランを、GPUクラウド業界の実データに基づいて批判的にレビューしてください。

プラン:
- Free: $0（T4 20hr/月）
- Starter: $29（A100 5hr含む）
- Pro: $99（H100 25hr含む）
- Team: $79/人（H100 15hr含む）
- Power: $299（H100 100hr含む）

批判的に検証すべき点：

1. Pro $99でH100 25hr: H100の調達コストが$2.50/hrとすると原価$62.50。粗利$36.50（37%）。しかし実際はインフラ運用費、サポート、SaaS機能開発費も乗る。本当に黒字か？

2. Power $299でH100 100hr: 原価$250+。ほぼ赤字。「ヘビーユーザーほど赤字」問題。

3. そもそも研究者がH100を月25hr使うか？実際の利用パターンデータは？
- Google Colabのデータ：平均利用時間は？
- RunPodの平均利用時間は？

4. ARPU $85/月の想定は現実的か？
- Google Colab Pro+は$50/月で多くの研究者には十分
- RunPodの従量課金で月$50-100程度が多数派では？

5. フリーミアム転換率3%は現実的か？
- Spotify: 27%、Slack: 30%（ただしこれらはGPUクラウドとは全く異なる）
- 開発者ツール系の転換率は？

6. 月次churn 8%は正しいか？
- 研究者は学期/年度単位で利用パターンが変わる
- 実際は季節性が非常に強いのでは？

7. 「SaaS機能（実験管理等）に$20-30/月のWTPがある」は本当か？
- W&B Free tier: 無料で十分な機能
- MLflow: 完全無料OSS
- この追加WTPの根拠は？

改善提案を5つ以上、定量データ付きで。"""


def log(msg):
    print(f"[{datetime.datetime.now().isoformat()}] {msg}", flush=True)


def run_query(query_name: str, query_text: str) -> dict:
    """Run a single query against GPT-5.4-pro Responses API."""
    log(f"Starting {query_name}...")
    try:
        response = client.responses.create(
            model="gpt-5.4-pro",
            tools=[{"type": "web_search_preview"}],
            input=query_text,
        )
        result_text = response.output_text
        log(f"Completed {query_name} ({len(result_text)} chars)")

        # Save individual result immediately
        safe_name = query_name.replace(" ", "_").replace(":", "")
        ind_path = f"/Users/kumacmini/research-materials/gpt54pro_{safe_name}.json"
        with open(ind_path, "w", encoding="utf-8") as f:
            json.dump({"name": query_name, "status": "success", "text": result_text}, f, ensure_ascii=False, indent=2)
        log(f"Individual result saved to {ind_path}")

        return {"name": query_name, "status": "success", "text": result_text}
    except Exception as e:
        error_msg = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
        log(f"FAILED {query_name}: {error_msg}")
        return {"name": query_name, "status": "error", "text": error_msg}


def main():
    log("Launching 2 GPT-5.4-pro queries concurrently (timeout: 1800s each)...")

    queries = [
        ("Query 1: GPU Cloud Startup Financial Benchmarks", QUERY_1_BENCHMARKS),
        ("Query 2: AIXS Pricing Critique", QUERY_2_PRICING_CRITIQUE),
    ]

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_to_name = {
            executor.submit(run_query, name, text): name
            for name, text in queries
        }
        for future in concurrent.futures.as_completed(future_to_name):
            name = future_to_name[future]
            results[name] = future.result()
            log(f"Received result for: {name} ({results[name]['status']})")

    # Save raw JSON
    json_path = "/Users/kumacmini/research-materials/gpt54pro_financial_critique_raw.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    log(f"Raw JSON saved to {json_path}")

    # Build markdown
    md_lines = [
        "# GPT-5.4-pro 財務モデル批判的レビュー",
        "Model: gpt-5.4-pro",
        "調査日: 2026-03-28",
        "",
        "---",
        "",
    ]

    for name, _text in queries:
        r = results.get(name, {"status": "missing", "text": "No result"})
        md_lines.append(f"## {name}")
        md_lines.append("")
        if r["status"] == "success":
            md_lines.append(r["text"])
        else:
            md_lines.append(f"**ERROR**: {r['text']}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_path = "/Users/kumacmini/research-materials/gpt54pro_financial_critique.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    log(f"Markdown saved to {md_path}")

    # Check for errors
    errors = [r for r in results.values() if r["status"] != "success"]
    if errors:
        log(f"WARNING: {len(errors)} query(ies) failed!")
        sys.exit(1)
    else:
        log("All queries completed successfully.")


if __name__ == "__main__":
    main()
