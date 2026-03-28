#!/usr/bin/env python3
"""
Run 5 sequential queries to GPT-5.4-pro via OpenAI Responses API
for deep regional GPU usage research.
"""

import os
import time
import sys
from datetime import datetime
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
MODEL = 'gpt-5.4-pro'
OUTPUT_PATH = '/Users/kumacmini/research-materials/gpt54pro_regional_gpu_usage.md'

client = OpenAI(api_key=API_KEY, timeout=1800.0)

# Define the 5 queries
queries = [
    {
        "title": "Query 1: アメリカのGPU利用実態",
        "section_header": "## 1. アメリカのGPU利用実態",
        "input": """あなたはAI計算資源の市場調査アナリストです。アメリカにおけるAI用途のGPU利用実態を、以下の観点で徹底的に調査してください。必ずWeb検索で最新データ（2025-2026年）を引用してください。

## 1. GPUをどのように利用しているか
以下の利用経路それぞれについて、利用者数・規模・重要度を定量的に示してください：
- ハイパースケーラークラウド（AWS/GCP/Azure）：市場シェア、AI向けGPUインスタンスの利用率
- AI特化GPUクラウド（CoreWeave/Lambda/RunPod等）：ユーザー数、成長率
- 大学の共有GPUクラスター：主要大学（MIT, Stanford, CMU, UT Austin等）のGPU保有台数
- 国のスーパーコンピュータ（NAIRR, ACCESS, DOE国立研究所）：GPU数、利用者数、年間割当規模
- 企業のオンプレGPUクラスター：Meta, Google, Microsoft等の自社GPU数
- スタートアップ向けクラウドクレジット：AWS Activate, Google for Startups等の規模
- 個人利用（Colab, Kaggle, Vast.ai等）：利用者数

## 2. 何のお金を使っているか
以下の資金源別に、AI GPU利用の資金規模を可能な限り定量化：
- NSF/NIH/DOE等の公的研究費：AI関連のGPU計算費用の年間総額推定
- 大学予算（内部資金）
- 企業R&D予算：Fortune 500のAI計算投資
- VC/スタートアップ資金：AI VC総額のうちcompute費用の割合（推定40-60%）
- スタートアップクレジット（AWS Activate $100K, Google $350K等）：年間発行総額推定
- 自費（個人研究者/学生）：Colab Pro ($10-50/月)の利用者数
- 共同研究費/受託研究費

## 3. 政府の施策・独自の取り組み
- NAIRR（National AI Research Resource）：現在の規模、GPU数、利用者数、今後の計画
- ACCESS（旧XSEDE）：割当規模、申請プロセス
- DOE Genesis Mission：$320M投資の詳細
- CHIPS Act のAI計算への影響
- CalCompute（カリフォルニア州のパブリックGPU）：進捗
- 各大学への連邦政府GPU投資
- NVIDIA Inception等の民間プログラム
- 輸出規制による国内GPU供給への影響

## 4. 研究者の実際のGPU調達パターン
- 典型的な大学院生がGPUを使う場合の経路（大学クラスター→Colab→クラウド→NAIRR）
- 研究グループのGPU予算の典型的な規模
- 研究費（NSF grant等）の中でGPU計算に充てられる割合

全て定量データ（数字、$額、GPU台数、利用者数）を含めてください。"""
    },
    {
        "title": "Query 2: EU・UKのGPU利用実態",
        "section_header": "## 2. EU・UKのGPU利用実態",
        "input": """EU（ドイツ、フランス、オランダ等を含む）とUKにおけるAI用途のGPU利用実態を調査してください。Web検索で最新データを使ってください。

## 1. GPUの利用経路
- ハイパースケーラー（米国系AWS/GCP/Azure）のEU利用：市場シェア、データ主権の問題
- EU発のGPUクラウド（Nscale、Nebius EU、OVHcloud等）：規模、ユーザー数
- EuroHPC（汎欧州スパコン基盤）：LUMI, Leonardo, MareNostrum 5等のGPU数、AI利用割合
- EuroHPC AI Factories（19箇所）：各拠点のGPU数、アクセス条件、無料枠
- 各国の大学クラスター：ドイツ（JUWELS）、UK（Isambard-AI, Dawn）等
- 企業のオンプレ：EU大手企業のAI計算投資

## 2. 資金源
- Horizon Europe：AI研究への配分額
- ERC（European Research Council）：個人グラントのGPU費用
- 各国の研究助成機関（DFG, ANR, UKRI等）：GPU計算費用の助成
- InvestAI計画：EUR 200B目標の内訳
- EU VC市場：米国との比較（6% vs 61%）
- 大学予算
- 企業R&D

## 3. 政府施策・独自の取り組み
- EuroHPC AI Factories：19+13拠点、スタートアップ/SME向け無料GPU枠の詳細
- GenAI4EU：EUR 700M の詳細
- EU AI Act のcompute要件への影響
- GAIA-X / 主権クラウド政策
- GDPR / データ越境規制のGPU利用への影響
- UK AIRR Programme：Isambard-AI（5,448 GH200）、Dawn等
- UK Sovereign AI Fund：GBP 500M の使途
- 各国独自のAI計算支援（フランスJean Zay、ドイツGauss Centre等）

## 4. 研究者のGPU調達パターン
- EU研究者の典型的なGPU利用経路
- EuroHPC割当の実際（申請から利用までの期間、審査基準）
- データ主権要件によるGPU選択への制約

全て定量データで。"""
    },
    {
        "title": "Query 3: 中国のGPU利用実態",
        "section_header": "## 3. 中国のGPU利用実態",
        "input": """中国におけるAI用途のGPU利用実態を調査してください。特に米国輸出規制の影響に注目。Web検索で最新データを使ってください。

## 1. GPUの利用経路
- 中国国内クラウド（Alibaba Cloud, Tencent Cloud, Huawei Cloud, Baidu Cloud）：AI GPU市場シェア
- 国産GPU/アクセラレータ（Huawei Ascend 910C, Biren, Moore Threads, Cambricon）：性能比較（H100比何%）、導入台数
- 地方政府の計算プラットフォーム：主要都市（北京、上海、深圳等）のAI計算基盤
- 大学の計算資源：清華大学、北京大学、中科院等のGPU保有
- 国のスパコン（天河、曙光等）：AI向けGPU構成
- 企業のオンプレ（ByteDance, Baidu, Alibaba等）：推定GPU保有台数

## 2. 資金源
- 算力券（compute vouchers）：30都市以上の詳細（上海 RMB 600M/年、深圳 RMB 500M/年等）
- 国家自然科学基金（NSFC）
- 科技部（MOST）予算
- 地方政府AI予算
- 企業R&D（Alibaba, Tencent, ByteDance等のAI投資額）
- VC/スタートアップ（中国AI VC市場規模）

## 3. 政府施策・独自の取り組み
- 東数西算（East Data West Computing）：規模、進捗
- 算力券制度の詳細（補助率10-80%、対象者、利用条件）
- 国産GPU推進政策：政府補助施設での国産チップ義務化
- 米国輸出規制の影響：H100/A100入手不可後の代替戦略
- GPU稼働率問題（30%）：過剰投資の実態
- GPU価格70%下落の背景

## 4. 研究者のGPU調達パターン
- 中国の研究者はどうやってGPUを使うか
- 算力券の実際の利用体験
- 輸出規制による研究への影響"""
    },
    {
        "title": "Query 4: 日本のGPU利用実態",
        "section_header": "## 4. 日本のGPU利用実態",
        "input": """日本におけるAI用途のGPU利用実態を調査してください。Web検索で最新データ（2025-2026年）を使ってください。

## 1. GPUの利用経路
- 米国ハイパースケーラー（AWS/GCP/Azure）の日本利用：日本市場シェア、日本リージョンのGPU構成
- 国内GPUクラウド：さくらインターネット（高火力/DOK）、GPUSOROBAN（ハイレゾ）、GMO GPUクラウド、IDCフロンティア
- ABCI 3.0（産総研）：H200 6,128台、利用料金（¥330-660/GPU-hr）、利用者数、利用条件
- 富岳（理研）：AI利用の状況、GPU対応計画（富岳NEXT）
- HPCI/mdx：GPU構成、利用状況
- 大学の計算資源：東大、京大、東工大等の情報基盤センターGPU
- 企業オンプレ：ソフトバンク（SB Intuitions）、NTT、NEC等のGPU保有

## 2. 資金源
- 科研費（KAKENHI）：年間¥2,379億のうちGPU計算に使える割合
- NEDO助成金：AI関連の計算資源助成
- JST（CREST, PRESTO, ACT-X, Moonshot）：GPU計算費用
- GENIAC：¥339億、30+プロジェクト、参加者
- 経産省AI計算基盤整備：¥1.23T（FY2026、4倍増）
- さくらインターネットへの政府補助（¥501億）、KDDI（¥102億）
- 大学予算
- 企業R&D予算：日本の企業R&D ¥23T（FY2024）
- 個人利用（Colab等）

## 3. 政府施策・独自の取り組み
- 国のAI基本計画：5年間¥1兆
- GENIAC（Generative AI Accelerator Challenge）の詳細と成果
- 経産省クラウドプログラム補助金：¥1,146B+
- ABCI 3.0の位置づけと課題
- 富岳NEXT計画（2029-2030、GPU搭載）
- mdx（データプラットフォームクロスイノベーション）
- ISMAP認証と政府調達
- 半導体戦略（Rapidus等）とGPU国産化
- 各大学の情報基盤センターGPU共同利用制度

## 4. 研究者の実際のGPU調達パターン
- 日本の大学院生がGPUを使う典型的な経路
  - まずColab無料→Colab Pro→研究室のGPU→ABCI申請→クラウド（科研費で）
- ABCIの利用体験（申請から利用まで、ポイント制、年度制約）
- 科研費でクラウドGPUを使う際の手続き
- 日本の研究者特有の課題（英語サービスの壁、クレカ決済の困難さ、年度予算制約）"""
    },
    {
        "title": "Query 5: その他の重要地域",
        "section_header": "## 5. その他の重要地域",
        "input": """以下の地域のAI GPU利用実態を簡潔に調査してください。Web検索で最新データを使ってください。

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
    },
]


def run_query(idx, query_info):
    """Run a single query against GPT-5.4-pro with web_search_preview."""
    print(f"\n{'='*70}", flush=True)
    print(f"[{idx+1}/5] {query_info['title']}", flush=True)
    print(f"{'='*70}", flush=True)
    sys.stdout.flush()

    start = time.time()
    try:
        response = client.responses.create(
            model=MODEL,
            tools=[{'type': 'web_search_preview'}],
            input=query_info['input'],
        )
        result = response.output_text
        elapsed = time.time() - start

        # Token usage
        usage_str = ""
        if hasattr(response, 'usage') and response.usage:
            usage = response.usage
            inp = getattr(usage, 'input_tokens', 0) or 0
            out = getattr(usage, 'output_tokens', 0) or 0
            usage_str = f" | Tokens: {inp}+{out}={inp+out}"

        print(f"  -> OK: {len(result)} chars in {elapsed:.1f}s{usage_str}", flush=True)
        return result
    except Exception as e:
        elapsed = time.time() - start
        print(f"  -> ERROR after {elapsed:.1f}s: {type(e).__name__}: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return f"[Error: {type(e).__name__}: {e}]"


def main():
    print(f"Starting regional GPU usage research with {MODEL}", flush=True)
    print(f"Output: {OUTPUT_PATH}", flush=True)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
    sys.stdout.flush()

    results = []
    for idx, q in enumerate(queries):
        result = run_query(idx, q)
        results.append((q, result))
        # Small delay between queries
        if idx < len(queries) - 1:
            print("  Waiting 3s before next query...", flush=True)
            time.sleep(3)

    # Build output markdown
    header = (
        "# GPT-5.4-pro 地域別GPU利用実態調査\n\n"
        "Model: gpt-5.4-pro (Responses API + web_search_preview)\n"
        "調査日: 2026-03-28\n\n"
        "---\n\n"
    )

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(header)
        for q, result in results:
            f.write(f"{q['section_header']}\n\n")
            f.write(result)
            f.write("\n\n---\n\n")

    print(f"\n{'='*70}", flush=True)
    print(f"All 5 queries complete. Output saved to: {OUTPUT_PATH}", flush=True)
    total_chars = sum(len(r) for _, r in results)
    print(f"Total output: {total_chars} chars", flush=True)
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", flush=True)


if __name__ == '__main__':
    main()
