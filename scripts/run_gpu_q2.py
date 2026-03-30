#!/usr/bin/env python3
"""Query 2: EU/UK GPU usage research via GPT-5.4-pro."""
import os
import time, sys
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
client = OpenAI(api_key=API_KEY, timeout=1800.0)

PROMPT = """EU（ドイツ、フランス、オランダ等を含む）とUKにおけるAI用途のGPU利用実態を調査してください。Web検索で最新データを使ってください。

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

OUT = '/Users/kumacmini/research-materials/gpu_q2_eu_uk.md'

print(f"[Q2] Starting at {time.strftime('%H:%M:%S')}", flush=True)
start = time.time()
try:
    response = client.responses.create(
        model='gpt-5.4-pro',
        tools=[{'type': 'web_search_preview'}],
        input=PROMPT,
    )
    result = response.output_text
    elapsed = time.time() - start
    print(f"[Q2] OK: {len(result)} chars in {elapsed:.1f}s", flush=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"[Q2] Saved to {OUT}", flush=True)
except Exception as e:
    elapsed = time.time() - start
    print(f"[Q2] ERROR after {elapsed:.1f}s: {e}", flush=True)
    import traceback
    traceback.print_exc()
