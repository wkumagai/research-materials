#!/usr/bin/env python3
"""
AIXS Comprehensive Analysis via GPT-5.4-pro Responses API with web_search_preview.
Uses STREAMING to keep connections alive during long reasoning phases.
Runs 7 queries sequentially, saves progress incrementally.
"""

import json
import os
import re
import sys
import time
from datetime import datetime

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")

client = OpenAI(
    api_key=API_KEY,
    timeout=httpx.Timeout(connect=60.0, read=1800.0, write=60.0, pool=60.0),
)

MODEL = "gpt-5.4-pro"
OUTPUT_PATH = "/Users/kumacmini/research-materials/gpt54pro_comprehensive_analysis.md"
PROGRESS_PATH = "/Users/kumacmini/research-materials/.gpt54pro_progress.json"

QUERIES = [
    {
        "id": 1,
        "title": "Query 1: Big Tech Convergence Threat (大手テック企業の統合プラットフォーム脅威)",
        "prompt": """2025-2026年における以下の大手テック企業のR&D・AI統合プラットフォーム戦略を、最新の発表・ロードマップ・決算情報から分析してください。AWS SageMaker+Braket+RoboMaker統合、Google Vertex AI+Quantum AI+DeepMind AI Co-Scientist、Microsoft Azure ML+Azure Quantum+GitHub Copilot、NVIDIA DGX Cloud+Omniverse+CUDA Quantum。各社について最新発表、R&D統合の証拠、AIXSへの脅威度(1-10)、参入タイムライン推定を含めてください。"""
    },
    {
        "id": 2,
        "title": "Query 2: Adjacent Market Invasion (隣接分野からの参入リスク)",
        "prompt": """以下の隣接分野企業がR&D compute platformに参入するリスク。Weights & Biases（CoreWeaveに$1.7Bで買収）後の展開、Databricks/MLflow 3.0のフルスタック化、Emerald Cloud Lab/Benchling、FutureHouse/Sakana AI/Sciloop、SkyPilot/dstack/Anyscale(Ray)/Modal。各社の最新状況、資金調達額、評価額、AIXSとの関係を調べてください。"""
    },
    {
        "id": 3,
        "title": "Query 3: Defensive Strategies for Startups vs Big Tech (スタートアップの防御戦略)",
        "prompt": """大手が参入してきたときに生き残ったDevToolsスタートアップの事例を10個以上（Datadog, Snowflake, MongoDB, Elastic, Confluent, HashiCorp, Twilio, Stripe, Zoom, Slack等）。各社がどう対応したか、ARR・市場シェア・ユーザー数の実データ。AIXSに適用可能な防御戦略トップ5。"""
    },
    {
        "id": 4,
        "title": "Query 4: Hidden Competitors & Emerging Threats (見落とされた競合と新興脅威)",
        "prompt": """2024-2026年に新登場のGPU cloud/R&D platformスタートアップ（大型調達したもの）、中国発グローバルGPU cloud（AutoDL, MatPool等）、OSSスタック（K8s+Ray+MLflow+JupyterHub）でAIXSと同等のことができるか、エッジAI/モデル小型化/量子コンピュータによるGPU需要減少リスク。"""
    },
    {
        "id": 5,
        "title": "Query 5: AIXS Unit Economics Deep Dive (ユニットエコノミクス詳細)",
        "prompt": """H100 SXMの現在のOEM/中古/リース価格、データセンターラック費用、電力コスト、GPUクラウドスタートアップの粗利率実データ（CoreWeave/Lambda/RunPod）、H100を$3/hrで販売した場合の月間損益計算、マーケットプレイスモデルの手数料率ベンチマーク。"""
    },
    {
        "id": 6,
        "title": "Query 6: VC Critique with Numbers (VCによる数字付き批判)",
        "prompt": """AIXSを投資案件として批判。GPU再販粗利10-20%問題、後発劣位の定量化、異種R&D統合の需要証拠、ToC先行の是非、日本スタートアップのグローバル勝率、AIバブル崩壊リスク。各批判に最新市場データを引用。"""
    },
    {
        "id": 7,
        "title": "Query 7: Rebuttal with Evidence (証拠に基づく反論)",
        "prompt": """Query 6の各批判に対する反論。マーケットプレイス手数料モデル、未サーブ顧客セグメント、Lab-as-a-Service市場成長、PLG ToC→ToB事例（Slack/Figma/HuggingFace）、日本発グローバルDevTools、ジェヴォンズのパラドックス。

具体的に反論すべき批判:
1. GPU再販粗利10-20%問題 → マーケットプレイス手数料モデル（20-30%テイクレート）で粗利構造が異なる
2. 後発劣位 → 未サーブ顧客セグメント（学術研究者、小規模ラボ）の規模データ
3. 異種R&D統合の需要 → Lab-as-a-Service市場の成長率、研究者のワークフロー調査データ
4. ToC先行の是非 → PLG成功事例（Slack/Figma/HuggingFace/Notion）のToC→ToB転換データ
5. 日本スタートアップのグローバル勝率 → 日本発グローバルDevToolsの成功事例
6. AIバブル崩壊リスク → ジェヴォンズのパラドックス、GPU需要の構造的成長データ

各反論に最新の市場データ、数字、事例を引用してください。"""
    },
]


def log(msg):
    """Print with timestamp and flush."""
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def extract_citations_from_response(response):
    """Extract URL citations from Responses API output (annotation objects)."""
    citations = []
    if hasattr(response, 'output') and response.output:
        for item in response.output:
            if hasattr(item, 'content') and item.content:
                for content_block in item.content:
                    if hasattr(content_block, 'annotations') and content_block.annotations:
                        for annotation in content_block.annotations:
                            url = getattr(annotation, 'url', None)
                            title = getattr(annotation, 'title', '') or ''
                            if url:
                                citations.append({"url": url, "title": title})
    return citations


def extract_citations_from_text(text):
    """Extract URL citations embedded in markdown text as ([title](url)) or [title](url)."""
    citations = []
    seen = set()
    # Match markdown links: [title](url)
    for match in re.finditer(r'\[([^\]]*)\]\((https?://[^\s\)]+)\)', text):
        title = match.group(1)
        url = match.group(2)
        if url not in seen:
            seen.add(url)
            citations.append({"url": url, "title": title})
    return citations


def run_query_streaming(query_info):
    """Run a single query using streaming to keep connection alive.

    Streaming is essential for gpt-5.4-pro with web_search_preview because:
    - The reasoning phase can take 10-20 minutes before any output
    - Without streaming, the HTTP connection may time out or be killed
    - Streaming provides keepalive events during the reasoning phase
    """
    log(f"Starting: {query_info['title']}")
    start = time.time()

    try:
        stream = client.responses.create(
            model=MODEL,
            tools=[{"type": "web_search_preview"}],
            input=query_info["prompt"],
            stream=True,
        )

        event_count = 0
        search_count = 0
        text_parts = []
        usage_info = {"input": 0, "output": 0, "total": 0}
        completed_response = None

        for event in stream:
            event_count += 1
            etype = getattr(event, 'type', 'unknown')

            if etype == 'response.output_text.delta':
                delta = getattr(event, 'delta', '')
                if delta:
                    text_parts.append(delta)
            elif etype == 'response.web_search_call.completed':
                search_count += 1
                elapsed = time.time() - start
                log(f"  Web search #{search_count} completed ({elapsed:.0f}s)")
            elif etype == 'response.completed':
                elapsed = time.time() - start
                log(f"  Response completed ({elapsed:.0f}s, {event_count} events, {search_count} searches)")
                completed_response = getattr(event, 'response', None)

        elapsed = time.time() - start
        content = ''.join(text_parts)

        # Try to get citations from the completed response object first
        citations = []
        if completed_response:
            citations = extract_citations_from_response(completed_response)
            # Get usage info
            if hasattr(completed_response, 'usage') and completed_response.usage:
                u = completed_response.usage
                usage_info = {
                    "input": getattr(u, 'input_tokens', 0) or 0,
                    "output": getattr(u, 'output_tokens', 0) or 0,
                    "total": (getattr(u, 'input_tokens', 0) or 0) + (getattr(u, 'output_tokens', 0) or 0),
                }
            # If no content from deltas, try output_text
            if not content and hasattr(completed_response, 'output_text'):
                content = completed_response.output_text or ""

        # Fallback: extract citations from the text itself (markdown links)
        if not citations and content:
            citations = extract_citations_from_text(content)

        log(f"  Tokens - input: {usage_info['input']}, output: {usage_info['output']}, total: {usage_info['total']}")
        log(f"  Content: {len(content)} chars, Citations: {len(citations)}, Searches: {search_count}")

        return {
            "id": query_info["id"],
            "title": query_info["title"],
            "content": content,
            "citations": citations,
            "elapsed": elapsed,
            "tokens": usage_info
        }

    except Exception as e:
        elapsed = time.time() - start
        log(f"  ERROR after {elapsed:.1f}s: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc(file=sys.stderr)
        return {
            "id": query_info["id"],
            "title": query_info["title"],
            "content": f"Error: {type(e).__name__}: {e}",
            "citations": [],
            "elapsed": elapsed,
            "tokens": {"input": 0, "output": 0, "total": 0}
        }


def build_markdown(results):
    """Combine all results into a single markdown document."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_tokens = sum(r["tokens"]["total"] for r in results)
    total_time = sum(r["elapsed"] for r in results)

    lines = []
    lines.append("# AIXS Comprehensive Competitive Analysis & Market Research")
    lines.append("")
    lines.append(f"**Generated**: {now}")
    lines.append(f"**Model**: gpt-5.4-pro (Responses API with web_search_preview)")
    lines.append(f"**Queries**: 7 sequential searches")
    lines.append(f"**Total tokens used**: {total_tokens:,}")
    lines.append(f"**Total API time**: {total_time:.1f}s")
    lines.append("")
    lines.append("> This analysis upgrades the previous gpt-4o-search-preview runs with gpt-5.4-pro for higher quality reasoning and more comprehensive web search results.")
    lines.append("")
    lines.append("---")
    lines.append("")

    all_citations = []

    for result in results:
        lines.append(f"# {result['title']}")
        lines.append("")
        lines.append(result["content"])
        lines.append("")

        if result["citations"]:
            lines.append(f"### URL Citations ({result['title'].split(':')[0]})")
            lines.append("")
            seen_in_query = set()
            for c in result["citations"]:
                url = c["url"]
                if url not in seen_in_query:
                    seen_in_query.add(url)
                    title = c["title"] if c["title"] else url
                    lines.append(f"- [{title}]({url})")
            lines.append("")
            all_citations.extend(result["citations"])

        lines.append(f"*Query time: {result['elapsed']:.1f}s | Tokens: {result['tokens']['total']:,}*")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Deduplicated citations appendix
    if all_citations:
        lines.append("# Appendix: All URL Citations (Deduplicated)")
        lines.append("")
        seen = set()
        idx = 0
        for c in all_citations:
            url = c["url"]
            if url not in seen:
                seen.add(url)
                idx += 1
                title = c["title"] if c["title"] else url
                lines.append(f"{idx}. [{title}]({url})")
        lines.append("")

    return "\n".join(lines)


def save_progress(results):
    """Save intermediate progress to JSON for crash recovery."""
    serializable = []
    for r in results:
        serializable.append({
            "id": r["id"],
            "title": r["title"],
            "content": r["content"],
            "citations": r["citations"],
            "elapsed": r["elapsed"],
            "tokens": r["tokens"],
        })
    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)


def load_progress():
    """Load previously saved progress if available."""
    if os.path.exists(PROGRESS_PATH):
        try:
            with open(PROGRESS_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def main():
    log("AIXS Comprehensive Analysis - GPT-5.4-pro (STREAMING MODE)")
    log(f"Model: {MODEL}")
    log(f"Queries: {len(QUERIES)}")

    # Check for resumable progress
    existing = load_progress()
    completed_ids = {r["id"] for r in existing}
    if completed_ids:
        log(f"Found progress for queries: {sorted(completed_ids)}")

    results = list(existing)

    for query_info in QUERIES:
        if query_info["id"] in completed_ids:
            log(f"Skipping already completed: {query_info['title']}")
            continue

        result = run_query_streaming(query_info)
        results.append(result)

        # Save progress after each query
        save_progress(results)
        log(f"  Progress saved ({len(results)}/{len(QUERIES)} done)")

        # Save intermediate markdown
        md = build_markdown(sorted(results, key=lambda r: r["id"]))
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(md)
        log(f"  Intermediate markdown saved")

        # Small delay between queries
        if query_info["id"] < len(QUERIES):
            log("  Waiting 5s before next query...")
            time.sleep(5)

    # Final save
    results_sorted = sorted(results, key=lambda r: r["id"])
    md = build_markdown(results_sorted)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(md)

    # Clean up progress file
    if os.path.exists(PROGRESS_PATH):
        os.remove(PROGRESS_PATH)

    total_tokens = sum(r["tokens"]["total"] for r in results_sorted)
    total_time = sum(r["elapsed"] for r in results_sorted)
    successful = sum(1 for r in results_sorted if not r["content"].startswith("Error:"))

    log("=" * 80)
    log(f"DONE! Results saved to: {OUTPUT_PATH}")
    log(f"Total tokens: {total_tokens:,}")
    log(f"Total time: {total_time:.1f}s")
    log(f"Successful queries: {successful}/{len(QUERIES)}")


if __name__ == "__main__":
    main()
