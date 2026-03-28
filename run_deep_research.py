"""
Gemini Deep Research API call for AIXS strategic analysis.
Uses the Interactions API with deep-research-pro-preview-12-2025.
"""

from google import genai
from google.genai._interactions.types.tool_param import GoogleSearch
import os
import time
import sys

API_KEY = os.environ.get("GOOGLE_API_KEY", "")
MODEL = 'deep-research-pro-preview-12-2025'
OUTPUT_PATH = '/Users/kumacmini/research-materials/deep_research_gemini_strategy.md'
TIMEOUT_SECONDS = 15 * 60  # 15 minutes
POLL_INTERVAL = 15  # seconds

QUERY = """
AIXSのような「GPU+HPC+量子+ロボット+実験装置を統合したR&D compute platform」について、以下を徹底調査してください。

1. GPU-as-a-Service市場の規模と成長率（2024-2030年、TAM/SAM/SOM）
   - 特にAI研究者・開発者向けセグメントの規模
   - 個人・小規模チーム向け（ToC）の市場規模

2. GPUクラウドスタートアップのユニットエコノミクス
   - GPU調達コスト vs 販売価格の粗利構造
   - H100/H200のOEMまたはリセール価格
   - データセンター設備費用
   - 1台のH100の月間稼働率と想定売上
   - 代表的なGPUクラウドスタートアップの粗利率

3. 成功したGPUクラウドスタートアップの成長戦略
   - Modal, RunPod, CoreWeave, Lambda Labsの初期戦略
   - 資金調達履歴と評価額推移
   - 初期のGo-to-Market戦略
   - Product-Led Growthの具体的施策
   - ARR成長速度

4. 失敗したGPUクラウドスタートアップの事例と教訓
   - FloydHub, Paperspace, Gradientなど
   - 失敗の原因分析

5. AI研究者のGPU利用パターンと支払意欲
   - 研究者の月間GPU利用時間の中央値
   - GPU compute に対するWTP（Willingness to Pay）
   - 無料枠から有料への転換率ベンチマーク
   - 研究者向けSaaS/PaaSのARPU相場

6. 「異種R&D資源統合」という概念の市場的可能性
   - GPU以外のR&D資源（HPC、量子、ロボット、実験装置）をクラウド化した事例
   - Lab-as-a-Service市場の動向
   - 研究ワークフロー自動化ツールの市場規模

具体的な数字、調査会社レポートの引用、出典URLを含めてください。
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
            # Try to dump whatever info is available
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
            # Look for TextContent
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
