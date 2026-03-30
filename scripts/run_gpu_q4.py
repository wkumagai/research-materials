#!/usr/bin/env python3
"""Query 4: Japan GPU usage research via GPT-5.4-pro."""
import os
import time, sys
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
client = OpenAI(api_key=API_KEY, timeout=1800.0)

PROMPT = """日本におけるAI用途のGPU利用実態を調査してください。Web検索で最新データ（2025-2026年）を使ってください。

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

OUT = '/Users/kumacmini/research-materials/gpu_q4_japan.md'

print(f"[Q4] Starting at {time.strftime('%H:%M:%S')}", flush=True)
start = time.time()
try:
    response = client.responses.create(
        model='gpt-5.4-pro',
        tools=[{'type': 'web_search_preview'}],
        input=PROMPT,
    )
    result = response.output_text
    elapsed = time.time() - start
    print(f"[Q4] OK: {len(result)} chars in {elapsed:.1f}s", flush=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"[Q4] Saved to {OUT}", flush=True)
except Exception as e:
    elapsed = time.time() - start
    print(f"[Q4] ERROR after {elapsed:.1f}s: {e}", flush=True)
    import traceback
    traceback.print_exc()
