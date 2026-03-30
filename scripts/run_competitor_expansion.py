"""
Gemini Deep Research: How major tech companies and GPU cloud competitors
will expand into AIXS's territory.
Uses the Interactions API with deep-research-pro-preview-12-2025.
"""

from google import genai
from google.genai._interactions.types.tool_param import GoogleSearch
import os
import time
import sys

API_KEY = os.environ.get("GOOGLE_API_KEY", "")
MODEL = 'deep-research-pro-preview-12-2025'
OUTPUT_PATH = '/Users/kumacmini/research-materials/deep_research_competitor_expansion.md'
TIMEOUT_SECONDS = 15 * 60  # 15 minutes
POLL_INTERVAL = 15  # seconds

QUERY = """
以下について徹底的に調査してください。AIXSは「GPU+HPC+量子+ロボット+実験装置を統合したR&D compute platform」です。

## 1. 大手テック企業のR&D統合プラットフォーム参入リスク

### AWS
- AWS SageMakerの進化ロードマップ（2025-2027）
- AWS Braket（量子）とSageMaker統合の計画
- AWS RoboMaker（ロボット）との統合
- AWSがR&D統合を目指す可能性と証拠

### Google Cloud
- Vertex AIの進化方向
- Google Quantum AI (Willow)とクラウドの統合
- Google DeepMind AI Co-Scientistの商用化計画
- GoogleがR&D自動化プラットフォームを出す可能性

### Microsoft Azure
- Azure Machine Learningの拡張計画
- Azure Quantum + ML統合
- GitHub Copilot → 研究自動化への発展
- Microsoft Researchとの統合

### NVIDIA
- NVIDIA DGX Cloudの戦略
- NVIDIA Omniverse (デジタルツイン) のR&D応用
- NVIDIA CUDA量子コンピューティング
- NVIDIAがプラットフォームレイヤーに垂直統合する可能性

### CoreWeave
- CoreWeaveのIPO後の戦略
- CoreWeaveが推論→ML platformに拡張する可能性
- CoreWeave Kubernetes Serviceの進化

### Modal
- Modalの最新機能と拡張方向
- Modalがサーバレス → R&Dプラットフォームに進化する可能性

### HuggingFace
- HuggingFace compute拡張の計画
- HuggingFace Spacesの進化
- HuggingFaceがフルR&Dプラットフォームになる可能性

## 2. 隣接分野からの参入リスク

### 実験管理ツールからの下方統合
- Weights & Biases: GPU compute提供の可能性
- MLflow/Databricks: フルスタック化
- Neptune.ai, Comet ML

### Lab-as-a-Service企業の上方統合
- Emerald Cloud Lab: クラウドラボ → 計算統合
- Strateos (Arctoris): ロボットラボ → AI compute
- Benchling: バイオR&D → compute

### AI研究自動化システムからの参入
- FutureHouse (Kosmos, Robin, PaperQA2): 研究自動化 → compute
- Sakana AI (AI Scientist): AIサイエンティスト → 実行環境
- Sciloop: ML研究自動化 → compute

### 量子コンピューティング企業からの参入
- IBM Quantum: 量子 → GPU統合
- Amazon Braket独立化の可能性
- IonQ, Rigetti: 量子 → ハイブリッド計算

### クラウドオーケストレーション企業
- SkyPilot: マルチクラウド → プラットフォーム化
- dstack: GPU orchestration → R&D統合
- Anyscale/Ray: 分散計算 → R&D基盤

## 3. 各参入リスクの評価
- 各社が参入する確率（1-5年以内）
- 参入した場合のAIXSへの影響度
- AIXSが取るべき対策

具体的な数字、発表内容、ロードマップ、資金調達情報を引用してください。
""".strip()


def main():
    print(f"[INFO] Initializing Gemini client...")
    client = genai.Client(api_key=API_KEY)

    print(f"[INFO] Submitting deep research query to {MODEL}...")
    print(f"[INFO] Query length: {len(QUERY)} chars")
    print(f"[INFO] Timeout: {TIMEOUT_SECONDS}s ({TIMEOUT_SECONDS // 60} min)")
    print()

    try:
        response = client.interactions.create(
            agent=MODEL,
            background=True,
            input=QUERY,
            tools=[GoogleSearch(type="google_search")],
        )
    except Exception as e:
        print(f"[ERROR] Failed to create interaction: {type(e).__name__}: {e}")
        sys.exit(1)

    interaction_id = response.id
    print(f"[INFO] Interaction created: {interaction_id}")
    print(f"[INFO] Initial status: {response.status}")
    print(f"[INFO] Polling every {POLL_INTERVAL}s...")
    print()

    start_time = time.time()
    poll_count = 0

    while True:
        elapsed = time.time() - start_time
        if elapsed > TIMEOUT_SECONDS:
            print(f"[ERROR] Timeout after {elapsed:.0f}s. Interaction may still be running.")
            print(f"[INFO] Interaction ID for manual retrieval: {interaction_id}")
            sys.exit(1)

        poll_count += 1
        try:
            status = client.interactions.get(interaction_id)
        except Exception as e:
            print(f"[WARN] Poll #{poll_count} failed ({type(e).__name__}): {e}")
            time.sleep(POLL_INTERVAL)
            continue

        current_status = status.status
        elapsed_min = elapsed / 60
        print(f"[POLL #{poll_count}] Status: {current_status} | Elapsed: {elapsed_min:.1f} min")

        if current_status == 'completed':
            print(f"\n[INFO] Research completed after {elapsed_min:.1f} min ({poll_count} polls)")
            break
        elif current_status in ('failed', 'cancelled'):
            print(f"[ERROR] Interaction ended with status: {current_status}")
            try:
                print(f"[INFO] Outputs: {status.outputs}")
            except Exception:
                pass
            sys.exit(1)

        time.sleep(POLL_INTERVAL)

    # Extract result text from outputs
    result_text = None
    if status.outputs:
        for output in status.outputs:
            if hasattr(output, 'text') and output.text:
                result_text = output.text
                break

    if not result_text:
        print(f"[ERROR] No text content found in outputs")
        print(f"[INFO] Outputs: {status.outputs}")
        sys.exit(1)

    print(f"[INFO] Result length: {len(result_text)} chars")

    # Save
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(result_text)

    print(f"[INFO] Saved to: {OUTPUT_PATH}")
    print(f"\n--- First 500 chars of result ---")
    print(result_text[:500])
    print("...")


if __name__ == '__main__':
    main()
