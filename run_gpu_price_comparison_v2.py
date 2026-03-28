#!/usr/bin/env python3
"""
Call GPT-5.4-pro via OpenAI Responses API to create a detailed
researcher-realistic GPU cost comparison across all direct competitors.
Runs 4 queries sequentially. Uses httpx timeout of 600s.
Falls back to o3 after 600s timeout on gpt-5.4-pro.
"""

import os
import sys
import time
import httpx
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY", "")
MODEL = 'gpt-5.4-pro'
OUTPUT_PATH = '/Users/kumacmini/research-materials/gpt54pro_price_comparison.md'

# Set 600s timeout on the HTTP client
custom_httpx = httpx.Client(timeout=httpx.Timeout(600.0, connect=30.0))
client = OpenAI(api_key=API_KEY, http_client=custom_httpx)

def call_with_fallback(query, label):
    """Try gpt-5.4-pro first, fall back to o3 if it times out."""
    start = time.time()
    model_used = MODEL

    try:
        print(f"  Calling {MODEL}...", flush=True)
        response = client.responses.create(
            model=MODEL,
            tools=[{'type': 'web_search_preview'}],
            input=query,
        )
        result = response.output_text
        elapsed = time.time() - start
        print(f"  {MODEL} done in {elapsed:.0f}s. Length: {len(result)} chars", flush=True)
        return result, MODEL
    except Exception as e:
        elapsed = time.time() - start
        print(f"  {MODEL} failed after {elapsed:.0f}s: {e}", flush=True)

        # Fallback to o3
        print(f"  Falling back to o3...", flush=True)
        try:
            start2 = time.time()
            response = client.responses.create(
                model='o3',
                tools=[{'type': 'web_search_preview'}],
                input=query,
            )
            result = response.output_text
            elapsed2 = time.time() - start2
            print(f"  o3 done in {elapsed2:.0f}s. Length: {len(result)} chars", flush=True)
            return result, 'o3'
        except Exception as e2:
            print(f"  o3 also failed: {e2}", flush=True)

            # Last resort: gpt-4.1
            print(f"  Last resort: gpt-4.1...", flush=True)
            try:
                start3 = time.time()
                response = client.responses.create(
                    model='gpt-4.1',
                    tools=[{'type': 'web_search_preview'}],
                    input=query,
                )
                result = response.output_text
                elapsed3 = time.time() - start3
                print(f"  gpt-4.1 done in {elapsed3:.0f}s. Length: {len(result)} chars", flush=True)
                return result, 'gpt-4.1'
            except Exception as e3:
                return f"[ERROR: All models failed. {MODEL}: {e}, o3: {e2}, gpt-4.1: {e3}]", "error"


# ── Query 1: Researcher scenario cost comparison ──
QUERY_1 = """あなたはAI/ML研究者がGPUクラウドを選ぶ際のコスト比較を行うアナリストです。以下の「研究者が実際に使いそうな利用シナリオ」で、各プロバイダーの総コストを比較してください。

必ずWeb検索して2026年3月時点の最新価格を使ってください。

## 対象プロバイダー（直接競合＝研究者がAIXSと比較検討するもの全て）
1. AWS (SageMaker / EC2 p5)
2. Google Cloud (Vertex AI / Compute Engine a3)
3. Microsoft Azure (Azure ML / ND H100 v5)
4. CoreWeave
5. Lambda Labs (Lambda Cloud)
6. RunPod
7. Modal
8. Together AI
9. Vast.ai
10. Paperspace (DigitalOcean GPU Droplets)
11. Lightning AI
12. Google Colab Pro/Pro+
13. Hugging Face (Spaces GPU / Inference Endpoints)
14. さくらインターネット (高火力)
15. GPUSOROBAN (ハイレゾ)
16. ABCI 3.0

## 利用シナリオ（研究者の実利用パターン）

### シナリオA: 論文再現実験（短期集中）
- GPU: H100 SXM 1台
- 期間: 72時間連続
- ストレージ: 500GB
- ネットワーク: 100GB egress
- 用途: 既存モデルの再現実験

### シナリオB: ファインチューニング（中期）
- GPU: H100 SXM 1台
- 期間: 1週間（168時間）
- ストレージ: 1TB
- ネットワーク: 200GB egress
- 用途: LLM LoRAファインチューニング

### シナリオC: 月間研究利用（継続）
- GPU: H100 SXM 1台
- 期間: 月160時間（平日8時間×20日、使わない時間は停止）
- ストレージ: 2TB
- ネットワーク: 500GB egress
- 用途: 日常的な研究開発

### シナリオD: 大規模学習（長期）
- GPU: H100 SXM 8台（1ノード）
- 期間: 30日間連続
- ストレージ: 10TB
- ネットワーク: 1TB egress
- 用途: 7Bモデルの事前学習

各シナリオについて、以下の形式で比較表を作成：

| プロバイダー | GPU単価(/hr) | GPU費用 | ストレージ費用 | egress費用 | その他費用 | 合計コスト | 備考 |

価格が不明な場合は「要問合せ」「N/A」と明記。H100がない場合は最も近いGPU（A100等）で代替し注記。"""

# ── Query 2: Non-price comparison for researchers ──
QUERY_2 = """あなたはAI/ML研究者向けGPUクラウドアナリストです。以下16社のプロバイダーについて、研究者視点での金額以外のメリット・デメリットを詳細に比較してください。Web検索で各社の最新情報を確認してください。

対象プロバイダー:
1. AWS (SageMaker / EC2 p5)
2. Google Cloud (Vertex AI / Compute Engine a3)
3. Microsoft Azure (Azure ML / ND H100 v5)
4. CoreWeave
5. Lambda Labs (Lambda Cloud)
6. RunPod
7. Modal
8. Together AI
9. Vast.ai
10. Paperspace (DigitalOcean GPU Droplets)
11. Lightning AI
12. Google Colab Pro/Pro+
13. Hugging Face (Spaces GPU / Inference Endpoints)
14. さくらインターネット (高火力)
15. GPUSOROBAN (ハイレゾ)
16. ABCI 3.0

以下の軸で各社を評価（◎優秀 ○良い △普通 ×劣る で評価）：

1. 即時利用可能性: サインアップから実際にGPUを使えるまでの時間
2. GPU在庫の安定性: 使いたい時に使えるか
3. Jupyter Notebook対応: ブラウザからすぐ実験できるか
4. CLI/API: コマンドラインやAPIでジョブ投入できるか
5. 分散学習対応: マルチGPU/マルチノード学習のしやすさ
6. データ永続性: セッション終了後もデータが保持されるか
7. プリインストール環境: PyTorch/CUDA等が最初から使えるか
8. 実験管理: W&B/MLflow等との統合
9. チーム機能: 共同利用、権限管理
10. 課金の柔軟性: 秒課金/分課金/時間課金、自動停止
11. 日本語サポート: 日本語ドキュメント、日本円決済
12. 学術割引: アカデミック向け特別価格
13. クレジットカード決済: 個人研究者が使いやすいか
14. コスパ（価格対性能）: 実際のベンチマーク性能と価格の比率
15. ベンダーロックイン: 他に移行しやすいか

出力形式：
| プロバイダー | 即時利用 | 在庫 | Notebook | CLI/API | 分散学習 | データ永続 | 環境 | 実験管理 | チーム | 課金柔軟性 | 日本語 | 学術割引 | カード決済 | コスパ | ロックイン | 総合メリット | 総合デメリット |

さらに各社について2-3行で「研究者にとっての最大のメリット」と「最大のデメリット」を文章で記述。"""

# ── Query 3: Researcher persona cost simulation ──
QUERY_3 = """あなたはAI/ML研究者向けGPUクラウドアナリストです。以下の4つの研究者ペルソナが1年間GPUクラウドを使った場合の年間コストを、主要プロバイダーで比較してください。
Web検索して2026年3月時点の最新価格を使ってください。

対象プロバイダー:
AWS, Google Cloud, Azure, CoreWeave, Lambda Labs, RunPod, Modal, Vast.ai, さくらインターネット, GPUSOROBAN, ABCI

ペルソナ1: 大学院生（博士課程）
- 月間GPU利用: H100 40時間（不定期、夜間中心）
- 予算: 月$200以下（科研費から）
- 必須: Jupyter、PyTorch、データ永続

ペルソナ2: ポスドク/助教
- 月間GPU利用: H100 120時間
- 予算: 月$500-1000（研究費から）
- 必須: CLI/API、分散学習（2-4 GPU）、チーム機能

ペルソナ3: AIスタートアップ創業者（1-3人）
- 月間GPU利用: H100 300時間
- 予算: 月$2000-5000（VC資金から）
- 必須: API、自動スケーリング、推論デプロイ

ペルソナ4: 企業R&D研究者
- 月間GPU利用: H100 8台×720時間（常時稼働）
- 予算: 月$30,000-50,000
- 必須: セキュリティ、SLA、請求書払い

各ペルソナ × 各プロバイダーで年間コストと最適プランを表にしてください。最もコスパが良いプロバイダーを推薦。

| ペルソナ | AWS | GCP | Azure | CoreWeave | Lambda | RunPod | Modal | Vast.ai | さくら | SOROBAN | ABCI | 推薦 |"""

# ── Query 4: Where AIXS can win ──
QUERY_4 = """あなたはAI/ML研究者向けGPUクラウドアナリストです。以下の分析を行ってください。Web検索して各社の最新価格を確認してください。

AIXSはGPUクラウドのマーケットプレイス/プラットフォームとして、研究者向けにGPUリソースを提供しようとしている新規参入プレイヤーです。

主要競合の価格帯（2026年3月時点のH100 SXM 1台/時間）:
- AWS EC2 p5: ~$4.00-4.50/hr (on-demand)
- GCP a3: ~$3.50-4.00/hr
- Azure ND H100 v5: ~$4.00/hr
- CoreWeave: ~$2.50-3.00/hr
- Lambda Labs: ~$2.49/hr
- RunPod: ~$1.99-2.49/hr
- Vast.ai: ~$1.50-2.00/hr (marketplace)
- さくら高火力: ~200-300円/hr

上記を踏まえて分析してください：

1. 価格で勝てるか？
- AIXSがマーケットプレイスモデルで再販する場合、RunPod ($1.99-2.49/hr) やVast.ai ($1.50-2.00/hr) より安くできるか？
- マージンを乗せた場合の現実的な価格帯は？
- 価格で勝てない場合、何で補えるか？

2. 体験で勝てるか？
- 既存プロバイダーの中で「研究者向け体験」が最も弱いのはどこか？
- AIXSが改善できる具体的なペインポイントは？
- 「論文再現ワンクリック」は本当にキラー機能か？

3. 統合で勝てるか？
- 研究者が実際に「GPU + 実験管理 + ワークフロー」を一箇所で欲しいと思っているか？
- それとも各ツールを自由に組み合わせたいか？
- 統合の価値に対するWTP（追加支払い意思額）は？

4. 結論: AIXSの最も現実的なポジショニング
- 価格帯
- ターゲット顧客
- 差別化ポイント
- 避けるべき土俵

全て定量データで論じてください。"""

queries = [
    ("Query 1: 研究者シナリオ別コスト比較", QUERY_1),
    ("Query 2: 非価格メリット・デメリット比較", QUERY_2),
    ("Query 3: 研究者ペルソナ別年間コストシミュレーション", QUERY_3),
    ("Query 4: AIXSが勝てるポイント分析", QUERY_4),
]

section_titles = [
    "## Part 1: 研究者シナリオ別コスト比較（16社×4シナリオ）",
    "## Part 2: 非価格メリット・デメリット比較（16社×15軸）",
    "## Part 3: 研究者ペルソナ別年間コストシミュレーション",
    "## Part 4: AIXSが勝てるポイント分析",
]

results = []
models_used = []

for i, (label, query) in enumerate(queries):
    print(f"\n{'='*60}", flush=True)
    print(f"Running {label}...", flush=True)
    print(f"{'='*60}", flush=True)

    result, model = call_with_fallback(query, label)
    results.append(result)
    models_used.append(model)

# ── Combine all results into final markdown ──
print(f"\n{'='*60}", flush=True)
print("Writing combined output...", flush=True)

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write("# GPT-5.4-pro 研究者視点GPU価格・体験比較\n\n")
    f.write("Model: gpt-5.4-pro (Responses API + web_search_preview)\n")
    f.write("調査日: 2026-03-28\n\n")

    # Note which models were actually used
    for i, (title, model) in enumerate(zip(section_titles, models_used)):
        if model != MODEL:
            f.write(f"- {title}: fallback model `{model}` used\n")
    f.write("\n---\n\n")

    for i, (result, title) in enumerate(zip(results, section_titles)):
        f.write(f"{title}\n\n")
        f.write(result)
        f.write("\n\n---\n\n")

print(f"Saved to: {OUTPUT_PATH}", flush=True)
print(f"Models used: {models_used}", flush=True)
print("All done.", flush=True)
