#!/usr/bin/env python3
"""Query 3: China GPU usage research via GPT-5.4-pro."""
import os
import time, sys
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
client = OpenAI(api_key=API_KEY, timeout=1800.0)

PROMPT = """中国におけるAI用途のGPU利用実態を調査してください。特に米国輸出規制の影響に注目。Web検索で最新データを使ってください。

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

OUT = '/Users/kumacmini/research-materials/gpu_q3_china.md'

print(f"[Q3] Starting at {time.strftime('%H:%M:%S')}", flush=True)
start = time.time()
try:
    response = client.responses.create(
        model='gpt-5.4-pro',
        tools=[{'type': 'web_search_preview'}],
        input=PROMPT,
    )
    result = response.output_text
    elapsed = time.time() - start
    print(f"[Q3] OK: {len(result)} chars in {elapsed:.1f}s", flush=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"[Q3] Saved to {OUT}", flush=True)
except Exception as e:
    elapsed = time.time() - start
    print(f"[Q3] ERROR after {elapsed:.1f}s: {e}", flush=True)
    import traceback
    traceback.print_exc()
