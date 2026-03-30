#!/usr/bin/env python3
"""Query 1: America GPU usage research via GPT-5.4-pro."""
import os
import time, sys
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
client = OpenAI(api_key=API_KEY, timeout=1800.0)

PROMPT = """あなたはAI計算資源の市場調査アナリストです。アメリカにおけるAI用途のGPU利用実態を、以下の観点で徹底的に調査してください。必ずWeb検索で最新データ（2025-2026年）を引用してください。

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

OUT = '/Users/kumacmini/research-materials/gpu_q1_usa.md'

print(f"[Q1] Starting at {time.strftime('%H:%M:%S')}", flush=True)
start = time.time()
try:
    response = client.responses.create(
        model='gpt-5.4-pro',
        tools=[{'type': 'web_search_preview'}],
        input=PROMPT,
    )
    result = response.output_text
    elapsed = time.time() - start
    print(f"[Q1] OK: {len(result)} chars in {elapsed:.1f}s", flush=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"[Q1] Saved to {OUT}", flush=True)
except Exception as e:
    elapsed = time.time() - start
    print(f"[Q1] ERROR after {elapsed:.1f}s: {e}", flush=True)
    import traceback
    traceback.print_exc()
