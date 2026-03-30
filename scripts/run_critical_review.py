#!/usr/bin/env python3
"""
AIXS Critical Review via GPT-4o-search-preview with web search.
Splits into 3 queries for token management, combines results.
"""

import os
import sys
import time
from datetime import datetime
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")

client = OpenAI(api_key=API_KEY)

QUERIES = {
    "business_model": {
        "title": "Part 1: Business Model Critique (ビジネスモデル批判)",
        "prompt": """あなたはVC(ベンチャーキャピタル)の厳しいパートナーです。以下のスタートアップ案を徹底的に批判してください。数字の根拠を持って反論してください。

AIXS概要: GPU+HPC+量子+ロボット+実験装置を統合したR&D compute platform。少人数スタートアップ。最初はToC（個人・小規模チーム向け）。

批判すべきポイント:
1. GPU再販ビジネスの粗利率は通常10-20%。これで事業は成り立つのか？具体的な数字で示せ
2. Modal, RunPod, Lambda等がすでに強い市場にどうやって参入するのか？後発劣位を数字で定量化せよ
3. 「異種R&D資源統合」は本当にユーザーが求めているのか？需要の証拠はあるのか？
4. ToC（個人向け）のGPUクラウドは薄利。なぜToB先行ではなくToC先行なのか？これは間違いではないか？
5. 日本のスタートアップがグローバルGPUクラウド市場で勝てた事例はあるか？なぜ勝てないのか？
6. GPU価格が下落し続ける中、プラットフォームレイヤーの価値は本当にあるのか？
7. 「AIエージェントからの操作」は差別化になるか？他社もすぐ追随できるのでは？

各批判に対して、最新の市場データを用いて定量的に論じてください。Web検索して最新の数字を引用してください。"""
    },
    "pricing": {
        "title": "Part 2: Pricing Model Critique (価格戦略批判)",
        "prompt": """あなたはSaaS pricing expertです。以下のGPUクラウドスタートアップの価格戦略を批判してください。

市場状況: H100の価格は$1.99/hr(RunPod)〜$12.29/hr(Azure)。個人向けGPUクラウドのARPUは通常$50-200/月。

批判すべきポイント:
1. 個人向けGPU従量課金で月間ARPUを$100以上にできるのか？研究者の実際の利用パターンデータを示せ
2. フリーミアムモデルのGPUクラウドは成り立つか？無料GPU提供のコストは？Colabとの差別化は？
3. 「GPU+ワークフロー統合」に追加WTPがあるという根拠は？W&B, MLflow等は無料で使える
4. サブスクリプション vs 従量課金、GPUクラウドではどちらが生存に有利か？実例で示せ
5. クレジット制は本当に有効か？クレジット失効による売上の水増しは持続可能か？
6. 日本市場のWTPは米国の何割程度か？日本で先行する価格戦略は正しいか？

最新の市場データ、ARPUベンチマーク、転換率データを引用してください。"""
    },
    "competitive_moat": {
        "title": "Part 3: Competitive Moat Critique (競争優位性批判)",
        "prompt": """あなたは競争戦略の専門家です。以下のスタートアップのMoat（競争優位性の堀）構築戦略を批判してください。

AIXS: GPU+異種R&D資源統合プラットフォーム。少人数スタートアップ。

批判すべきポイント:
1. ネットワーク効果：GPU marketplace のネットワーク効果は本当に強いのか？Vast.aiの事例を分析せよ
2. スイッチングコスト：実験ログやワークフローのロックインは実際どの程度か？Docker/K8sの標準化で可搬性が高い
3. 技術的優位：「異種資源統合」の技術的難易度は高いが、それは参入障壁になるか？大企業が本気出したら？
4. ブランド：研究者コミュニティでブランドを構築するのにどれくらいかかるか？HuggingFaceの成長速度データ
5. 規模の経済：GPU調達で大手に勝てるのか？CoreWeaveの調達コストとの比較
6. 制度的障壁：政府認証やデータ主権は少人数スタートアップが取得できるのか？期間とコスト

各批判に最新データと数字を用いてください。Web検索して実例を引用してください。"""
    }
}


def extract_citations(message):
    """Extract URL citations from message annotations."""
    citations = []
    if hasattr(message, 'annotations') and message.annotations:
        for annotation in message.annotations:
            if hasattr(annotation, 'url_citation') and annotation.url_citation:
                url = annotation.url_citation.url
                title = getattr(annotation.url_citation, 'title', '') or ''
                citations.append({"url": url, "title": title})
            elif hasattr(annotation, 'url') and annotation.url:
                citations.append({"url": annotation.url, "title": ""})
    return citations


def run_query(key, query_info):
    """Run a single query against GPT-4o-search-preview."""
    print(f"\n{'='*60}")
    print(f"Running: {query_info['title']}")
    print(f"{'='*60}")
    start = time.time()

    try:
        response = client.chat.completions.create(
            model="gpt-4o-search-preview",
            web_search_options={"search_context_size": "high"},
            messages=[{"role": "user", "content": query_info["prompt"]}],
            timeout=300
        )

        elapsed = time.time() - start
        print(f"  Completed in {elapsed:.1f}s")

        message = response.choices[0].message
        content = message.content or ""
        citations = extract_citations(message)

        usage = response.usage
        print(f"  Tokens - prompt: {usage.prompt_tokens}, completion: {usage.completion_tokens}, total: {usage.total_tokens}")

        return {
            "title": query_info["title"],
            "content": content,
            "citations": citations,
            "elapsed": elapsed,
            "tokens": {
                "prompt": usage.prompt_tokens,
                "completion": usage.completion_tokens,
                "total": usage.total_tokens
            }
        }

    except Exception as e:
        elapsed = time.time() - start
        print(f"  ERROR after {elapsed:.1f}s: {e}")
        return {
            "title": query_info["title"],
            "content": f"Error: {e}",
            "citations": [],
            "elapsed": elapsed,
            "tokens": {"prompt": 0, "completion": 0, "total": 0}
        }


def build_markdown(results):
    """Combine all results into a single markdown document."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_tokens = sum(r["tokens"]["total"] for r in results)
    total_time = sum(r["elapsed"] for r in results)

    lines = []
    lines.append("# AIXS Critical Review (Adversarial Analysis)")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append(f"Model: gpt-4o-search-preview (web search enabled, search_context_size: high)")
    lines.append(f"Total tokens used: {total_tokens:,}")
    lines.append(f"Total API time: {total_time:.1f}s")
    lines.append("")
    lines.append("---")
    lines.append("")

    all_citations = []

    for result in results:
        lines.append(f"## {result['title']}")
        lines.append("")
        lines.append(result["content"])
        lines.append("")

        if result["citations"]:
            all_citations.extend(result["citations"])

        lines.append(f"*Query time: {result['elapsed']:.1f}s | Tokens: {result['tokens']['total']:,}*")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Deduplicated citations appendix
    if all_citations:
        lines.append("## Appendix: All URL Citations")
        lines.append("")
        seen = set()
        for i, c in enumerate(all_citations, 1):
            url = c["url"]
            if url not in seen:
                seen.add(url)
                title = c["title"] if c["title"] else url
                lines.append(f"{i}. [{title}]({url})")
        lines.append("")

    return "\n".join(lines)


def main():
    print("AIXS Critical Review - GPT-4o-search-preview with Web Search")
    print("=" * 60)

    results = []
    for key, query_info in QUERIES.items():
        result = run_query(key, query_info)
        results.append(result)

    # Build and save markdown
    md = build_markdown(results)
    output_path = "/Users/kumacmini/research-materials/critical_review_gpt.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"\n{'='*60}")
    print(f"Results saved to: {output_path}")
    print(f"Total tokens: {sum(r['tokens']['total'] for r in results):,}")
    print(f"Total time: {sum(r['elapsed'] for r in results):.1f}s")


if __name__ == "__main__":
    main()
