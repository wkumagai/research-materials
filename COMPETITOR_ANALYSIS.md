# 競合分析：GPU クラウドプロバイダー比較

調査日: 2026-03-28〜29
データ出典: GPT-5.4-pro Web Search, Gemini Deep Research, 各社公式サイト
為替参考: 1 USD = 150 JPY

---

## 1. 対象企業一覧

直接競合 = ユーザーがGPUクラウドを使いたいときに候補に挙がるサービス

| # | 企業/サービス | カテゴリ | URL |
|---|---|---|---|
| 1 | AWS (Amazon Web Services) | ハイパースケーラー | aws.amazon.com |
| 2 | Google Cloud Platform (GCP) | ハイパースケーラー | cloud.google.com |
| 3 | Microsoft Azure | ハイパースケーラー | azure.microsoft.com |
| 4 | Oracle Cloud (OCI) | ハイパースケーラー | oracle.com/cloud |
| 5 | CoreWeave | GPU特化 (IaaS) | coreweave.com |
| 6 | Lambda Labs | GPU特化 (IaaS) | lambda.ai |
| 7 | RunPod | GPU特化 (IaaS/PaaS) | runpod.io |
| 8 | Modal | GPU特化 (サーバーレス PaaS) | modal.com |
| 9 | Together AI | GPU特化 (AI Platform) | together.ai |
| 10 | Vast.ai | マーケットプレイス (P2P) | vast.ai |
| 11 | Baseten | 推論・サーバーレス | baseten.co |
| 12 | Replicate | 推論・サーバーレス | replicate.com |
| 13 | Hugging Face | 推論・エコシステム | huggingface.co |
| 14 | Paperspace / DigitalOcean GPU Droplets | 推論・汎用 | digitalocean.com |
| 15 | Lightning AI | GPU特化 (開発環境) | lightning.ai |
| 16 | Spheron | GPU特化 (分散型) | spheron.network |
| 17 | FluidStack | GPU特化 | fluidstack.io |
| 18 | Hyperstack | GPU特化 | hyperstack.cloud |
| 19 | Brev.dev | GPU特化 (プロビジョニング) | brev.dev |
| 20 | さくらインターネット | 国内 | sakura.ad.jp |
| 21 | GPUSOROBAN (ハイレゾ) | 国内 | soroban.highreso.jp |
| 22 | GMO GPU Cloud | 国内 | gmo.jp |
| 23 | WebARENA IndigoGPU (NTTPC) | 国内 | arena.nttpc.co.jp |
| 24 | ABCI 3.0 (産総研) | 国内 (公的基盤) | abci.ai |
| 25 | Nscale | EU ネオクラウド | nscale.com |
| 26 | Scaleway | EU ネオクラウド | scaleway.com |
| 27 | OVHcloud | EU ネオクラウド | ovhcloud.com |
| 28 | Nebius | EU/イスラエル ネオクラウド | nebius.com |
| 29 | Core42 (G42) | 中東 | core42.ai |
| 30 | Crusoe | GPU特化 (AI Factory) | crusoe.ai |

---

## 2. 価格比較（同一条件）

### 2.1 H100 SXM 80GB 1台・1時間あたり（オンデマンド）

| プロバイダー | 価格(/hr) | 課金単位 | Spot価格 | 予約価格 | 出典 |
|---|---|---|---|---|---|
| AWS (p5.48xlarge, 1GPU換算) | $6.88 (値下げ後 ~$3.85) | 秒(60s min) | $3.79 | 1yr $2.97; 3yr $2.59; Capacity Blocks $4.33 | aws.amazon.com (2025-03) |
| GCP (a3-highgpu-8g, 1GPU換算) | $10.98 | 秒(60s min) | $3.69 | 1yr CUD ~$7.14; 3yr CUD ~$5.50 | cloud.google.com (2025-03) |
| Azure (ND96isr_H100_v5, 1GPU換算) | $12.29 | 秒(5min min) | $2.27 | Contact sales | azure.microsoft.com (2025-03) |
| CoreWeave (HGX, 1GPU換算) | $6.16 | 分 | 非公開 | 要セールス(最大60%OFF) | coreweave.com (2025-03) |
| Lambda Labs (8x, 1GPU換算) | $3.99 | 分 | なし | 要セールス | lambda.ai (2025-03) |
| Lambda Labs (1-Click Cluster) | $2.76 | 分 | なし | 要セールス | lambda.ai (2025-03) |
| RunPod (SXM community) | $2.69 | 秒 | $1.50 | 1yr $2.61 | runpod.io (2025-03) |
| RunPod (PCIe community) | $1.99 | 秒 | $1.35 | 1yr $2.03 | runpod.io (2025-03) |
| Modal | $3.95 | 秒 | なし | なし | modal.com (2025-03) |
| Together AI (cluster) | $3.49 | 分 | 非公開 | 1w-1m $2.69; 4-6m $2.25 | together.ai (2025-03) |
| Vast.ai (マーケットプレイス中央値) | $1.55〜$2.27 | 秒 | 変動制 | なし | vast.ai (2025-03) |
| Baseten | $6.50 | 分 | なし | なし | baseten.co (2025-03) |
| Replicate | $5.49 | 秒 | なし | なし | replicate.com (2025-03) |
| HF Inference (GCP経由) | $10.00 | 分 | なし | なし | huggingface.co (2025-03) |
| HF Inference (AWS経由) | $4.50 | 分 | なし | なし | huggingface.co (2025-03) |
| DigitalOcean GPU Droplets (HGX H100) | $3.39 | 秒(5min min) | 非公開 | 12mo $2.50 | digitalocean.com (2025-03) |
| Paperspace | $2.24 | 時間 | なし | なし | paperspace.com (2025-03) |
| Spheron | $2.01 | 秒 | $0.99 | 非公開 | spheron.network (2026-03) |
| Hyperstack (SXM) | $2.40 | 非公開 | 非公開 | 非公開 | hyperstack.cloud (2026-03) |
| Oracle Cloud (BM.GPU.H100.8換算) | ~$3.49 | 非公開 | 非公開 | 非公開 | oracle.com (2026-03) |
| さくら VRT | $6.60 (¥990/hr) | 時間 | なし | 月額キャップ有 | sakura.ad.jp (2025-03) |
| さくら DOK (2026年1月更新) | ~$2.50 (0.83円/秒) | 秒(60s min) | なし | なし | sakura.ad.jp (2026-01) |
| GPUSOROBAN | 非公開 (H100) | 非公開 | 非公開 | 非公開 | soroban.highreso.jp (2025-03) |
| ABCI 3.0 (H200, 参考) | ~$4.40 (standard) / ~$2.20 (dev accel.) | ポイント制 | なし | 要申請 | abci.ai (2025-03) |

### 2.2 研究者の実利用シナリオ別コスト

出典: o3 (Responses API + web_search_preview), 2026-03-28
条件: H100 1台利用、ストレージ500GB、egress 100GB前提。為替 1 USD = 150 JPY。

#### シナリオA: 論文再現実験（H100 1台 x 72時間）

| プロバイダー | GPU単価(/hr) | GPU費用 | ストレージ | egress | 合計 | 備考 |
|---|---|---|---|---|---|---|
| AWS EC2 p5 | $6.88 | $495 | $3.95 | $9.00 | **$508** | gp3 $0.08/GB-mo, egress $0.09/GB |
| GCP a3 | $11.27 | $811 | $1.97 | $8.50 | **$821** | |
| Azure ND H100 v5 | $6.98 | $503 | $1.13 | $0 | **$504** | egress 100GB無料 |
| CoreWeave | $6.42 | $462 | $1.48 | $0 | **$464** | egress無料 |
| Lambda Cloud | $2.99 | $215 | $9.86 | $0 | **$225** | ストレージ $0.20/GB-mo |
| RunPod | $2.99 | $215 | $3.46 | $0 | **$219** | ストレージ $0.07/GB-mo |
| Modal | $3.95 | $284 | $0 | $0 | **$284** | ストレージ無料 |
| Together AI | $3.49 | $251 | $7.89 | $0 | **$259** | ストレージ $0.16/GB-mo |
| Vast.ai | $1.80 | $130 | $1.48 | $0.10 | **$131** | Verified DCホスト中間値 |
| Paperspace | $2.24 | $161 | $14.3 | $9.0 | **$185** | ストレージ $0.29/GB-mo |
| HF Endpoints | $4.50 | $324 | $3.95 | $9.0 | **$337** | AWS上H100 |
| ABCI 3.0 | $4.40 | $317 | $1.0 | $0 | **$318** | H200, 3pt/h x ¥220 |

#### シナリオB: ファインチューニング（H100 1台 x 1週間=168時間）

| プロバイダー | 合計 | 備考 |
|---|---|---|
| AWS | **$1,192** | |
| GCP | **$1,919** | |
| Azure | **$1,184** | |
| CoreWeave | **$1,086** | |
| Lambda Cloud | **$548** | |
| RunPod | **$518** | |
| Modal | **$664** | |
| Together AI | **$623** | |
| Vast.ai | **$310** | |
| Paperspace | **$461** | |
| HF Endpoints | **$792** | |
| ABCI 3.0 | **$744** | |

#### シナリオC: 月間研究利用（H100 1台 x 月160時間）

| プロバイダー | 合計 | 備考 |
|---|---|---|
| AWS | **$1,181** | |
| GCP | **$1,863** | |
| Azure | **$1,147** | |
| CoreWeave | **$1,040** | |
| Lambda Cloud | **$566** | |
| RunPod | **$509** | |
| Modal | **$632** | |
| Together AI | **$629** | |
| Vast.ai | **$302** | |
| Paperspace | **$530** | |
| HF Endpoints | **$800** | |
| ABCI 3.0 | **$713** | |

#### シナリオD: 大規模学習（H100 8台 x 30日=720時間/台）

| プロバイダー | 合計 | 備考 |
|---|---|---|
| AWS | **$40,508** | |
| GCP | **$64,971** | |
| Azure | **$40,477** | |
| CoreWeave | **$37,275** | |
| Lambda Cloud | **$19,194** | |
| RunPod | **$17,913** | |
| Modal | **$22,752** | |
| Together AI | **$21,680** | |
| Vast.ai | **$10,665** | |
| Paperspace | **$15,852** | |
| HF Endpoints | **$26,799** | |
| ABCI 3.0 | **$25,541** | |

### 2.3 その他GPU価格

#### H200 141GB（1GPU-hour, オンデマンド）

| プロバイダー | 価格(/hr) | Spot/予約 | 出典 |
|---|---|---|---|
| AWS (p5en.48xlarge) | $7.91 (値下げ後 ~$5.93) | Spot $2.28; Capacity Blocks $5.72 | aws.amazon.com (2025-03) |
| GCP (a3-ultragpu-8g) | $10.85 | Spot $4.04 | cloud.google.com (2025-03) |
| Azure (ND96isr_H200_v5) | $13.78 | Spot: 割引なし記載 | azure.microsoft.com (2025-03) |
| CoreWeave (HGX) | $6.31 | 要セールス(最大60%OFF) | coreweave.com (2025-03) |
| RunPod | $3.59 | 1yr $3.05 | runpod.io (2025-03) |
| Modal | $4.54 | なし | modal.com (2025-03) |
| Together AI | $4.19 | 4-6mo $2.59 | together.ai (2025-03) |
| DigitalOcean (HGX H200) | $3.44 | なし | digitalocean.com (2025-03) |
| HF Inference (AWS) | $5.00 | なし | huggingface.co (2025-03) |

#### A100 80GB（1GPU-hour, オンデマンド）

| プロバイダー | 価格(/hr) | Spot/予約 | 出典 |
|---|---|---|---|
| AWS (p4de.24xlarge) | $3.43 | Spot $2.43; 3yr $1.47 | aws.amazon.com (2025-03) |
| GCP (a2-ultragpu-8g) | $6.25 | 非公開 | cloud.google.com (2025-03) |
| Azure (ND96amsr_A100_v4) | $4.10 | Spot $1.07 | azure.microsoft.com (2025-03) |
| CoreWeave | $2.70 | 要セールス(最大60%OFF) | coreweave.com (2025-03) |
| Lambda Labs (SXM 8x) | $2.79 | なし | lambda.ai (2025-03) |
| Lambda Labs (PCIe 1x) | $1.10〜$1.29 | なし | lambda.ai (2025-03) |
| RunPod (SXM community) | $1.39 | Spot $0.79; 1yr $1.22 | runpod.io (2025-03) |
| RunPod (PCIe community) | $1.19 | Spot $0.60; 1yr $1.14 | runpod.io (2025-03) |
| Modal (80GB) | $2.50 | なし | modal.com (2025-03) |
| Baseten (80GB) | $4.00 | なし | baseten.co (2025-03) |
| Replicate (80GB) | $5.04 | なし | replicate.com (2025-03) |
| HF Inference (AWS) | $2.50 | なし | huggingface.co (2025-03) |
| Paperspace | $3.18 | なし | paperspace.com (2025-03) |
| GPUSOROBAN (t80-1-a) | $2.65 (¥398/hr) | なし | soroban.highreso.jp (2025-03) |
| ABCI 3.0 (H200参考) | ~$2.20 (dev) / ~$4.40 (standard) | 要申請 | abci.ai (2025-03) |

#### L40S 48GB（1GPU-hour, オンデマンド）

| プロバイダー | 価格(/hr) | Spot/予約 | 出典 |
|---|---|---|---|
| AWS (g6e.xlarge) | $1.86 | ~$1.00-$1.50 (est.) | aws.amazon.com (2025-03) |
| CoreWeave | $2.25 | 要セールス(最大60%OFF) | coreweave.com (2025-03) |
| RunPod | $0.79 | Spot $0.40; 1yr $0.71 | runpod.io (2025-03) |
| Modal | $1.95 | なし | modal.com (2025-03) |
| HF Inference (AWS) | $1.80 | なし | huggingface.co (2025-03) |
| Replicate | $3.51 | なし | replicate.com (2025-03) |
| DigitalOcean GPU Droplets | $1.57 | なし | digitalocean.com (2025-03) |

#### B200（1GPU-hour, オンデマンド）

| プロバイダー | 価格(/hr) | 予約 | 出典 |
|---|---|---|---|
| CoreWeave (8-GPU) | $8.60 ($68.80/8-GPU) | 要セールス | coreweave.com (2026-03) |
| Lambda Labs (8-GPU) | $4.99 | 1yr $3.49 | lambda.ai (2026-03) |
| RunPod | $5.99 | 非公開 | runpod.io (2026-03) |
| Modal | $6.25 | なし | modal.com (2026-03) |
| Together AI | $5.50 | 非公開 | together.ai (2026-03) |
| Baseten | $9.98 | なし | baseten.co (2026-03) |

B200仕様: 192GB HBM3e、8TB/s帯域幅。H100比で推論スループット向上（NVIDIA公称最大30倍、実測ベンチマーク5-20倍の幅）。

#### AMD MI300X（1GPU-hour, オンデマンド）

| プロバイダー | 価格(/hr) | 備考 | 出典 |
|---|---|---|---|
| DigitalOcean | $1.99 | NVIDIA以外の選択肢 | digitalocean.com (2026-03) |
| RunPod | $1.99 | Community Cloud | runpod.io (2026-03) |

---

## 3. 金額以外のメリット・デメリット

### 3.1 比較マトリクス

出典: o3 (web_search_preview), 各社公式ドキュメント, 2026-03-28

評価凡例: ◎=優秀 ○=良好 △=制限あり/課題あり ×=未対応/非対応

| プロバイダー | 即時利用 | GPU在庫 | Notebook | CLI/API | 分散学習 | データ永続 | 環境構築 | 実験管理 | チーム | 課金柔軟性 | 日本語 | 学術割引 | カード決済 | ロックイン |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AWS | ○ | ○ | ◎ | ◎ | ◎ | ◎ | ◎ | ○ | ◎ | ◎ | ◎ | ○ | ◎ | × (高) |
| GCP | ○ | ○ | ○ | ◎ | ◎ | ◎ | ◎ | ○ | ◎ | ◎ | ◎ | ○ | ◎ | △ (中-高) |
| Azure | ○ | ○ | ○ | ◎ | ◎ | ◎ | ◎ | ○ | ◎ | ◎ | ◎ | ○ | ◎ | △ (高) |
| CoreWeave | ○ | ○ | △ | ◎ | ◎ | ○ | ○ | △ | ○ | ○ | △ | △ | ○ | ○ (低) |
| Lambda Labs | ◎ | ○ | ○ | ◎ | ◎ | ○ | ◎ | △ | ○ | ◎ | △ | ○ | ◎ | ○ (低) |
| RunPod | ◎ | △ | ○ | ◎ | △ | ○ | ○ | △ | △ | ◎ | △ | △ | ◎ | ○ (低) |
| Modal | ◎ | ○ | ◎ | ◎ | ○ | △ | ◎ | ○ | ○ | ◎ | △ | △ | ◎ | ○ (高) |
| Together AI | ○ | ○ | △ | ◎ | ◎ | ○ | ○ | △ | ○ | ○ | △ | ○ | ◎ | ○ (中) |
| Vast.ai | ◎ | △ | ○ | ◎ | △ | △ | △ | △ | △ | ◎ | △ | △ | ◎ | ○ (低) |
| Paperspace/DO | ◎ | ○ | ◎ | ◎ | ○ | ○ | ◎ | ○ | ○ | ◎ | △ | ○ | ◎ | ○ (低) |
| Lightning AI | ◎ | ○ | ◎ | ○ | ○ | △ | ◎ | ◎ | ◎ | ○ | △ | ○ | ◎ | ○ (中) |
| HF Inference | ◎ | ○ | ◎ | ◎ | △ | △ | ◎ | ◎ | ◎ | ○ | △ | ○ | ◎ | ◎ (低) |
| Baseten | ○ | ○ | △ | ◎ | × | ○ | ○ | △ | ○ | ○ | △ | △ | ◎ | ○ (中) |
| Replicate | ○ | ○ | △ | ◎ | × | △ | ○ | △ | △ | ○ | △ | △ | ◎ | ○ (中) |
| Colab Pro/Pro+ | ◎ | △ | ◎ | △ | △ | × | ◎ | △ | △ | ◎ | ◎ | ◎ | ◎ | ◎ (低) |
| さくら | ○ | ○ | △ | ○ | ○ | ○ | △ | △ | ○ | ○ | ◎ | ○ | ◎ | △ |
| GPUSOROBAN | ○ | ○ | △ | △ | △ | △ | △ | × | △ | ○ | ◎ | ○ | ◎ | ○ |
| ABCI 3.0 | △ | ◎ | △ | △ | ◎ | ◎ | △ | △ | ○ | △ | ◎ | ◎ | × | △ |

### 3.2 各社の特徴（メリット・デメリット）

#### ハイパースケーラー

**AWS (SageMaker / EC2 p5)**
- 強み: SageMakerで分散学習・追跡・デプロイがシームレス。143+認定、最大エコシステム。2025年6月にH100を44%値下げ。EFA 3200Gbps。
- 弱み: H100時間単価が競合の2-3倍。クォータ申請必要、容量不足エラー頻発。サービス間ロックインが大きい。
- 特記: AWS Capacity Blocksで在庫問題を一部改善中。設備投資$2,000億(2026年見込み)。

**Google Cloud (Vertex AI / a3)**
- 強み: 最もクリーンなUX。Colab Enterprise。TPU v5e/v5p/v6が独自強み。Batch Prediction 50%割引。
- 弱み: NVIDIA GPUのオンデマンド価格が最高値帯。人気リージョンで割当不足が起きやすい。
- 特記: Google Cloud Q4'25前年比48%増の$177億。AI co-scientistをGemini 2.0ベースで公開中。

**Microsoft Azure (Azure ML / ND H100 v5)**
- 強み: ND H100 v5 + Quantum-2 InfiniBandで大規模分散が容易。エンタープライズ統合最強(EA、AD/Office 365)。30+リージョン。
- 弱み: 最高価格帯。5分最低課金(2025年6月〜)。サービス階層が複雑で学習コストが高い。
- 特記: FY26 Q2売上$813億、Azure 39%成長。AI Foundry + GitHub Copilot + Azure Quantum + Discoveryの統合が進行中。

#### GPU特化クラウド

**CoreWeave**
- 強み: K8s native。InfiniBand 3200Gbps。100K+ GPUクラスター。egress/IOPS無料。AI Object Storage + LOTA (2+ GB/s per GPU)。SOC 2 Type II、ISO 27001、HIPAA、FedRAMP対応。
- 弱み: 8-GPU最小。K8s知識が前提。日本語情報が乏しく学割なし。
- 特記: 2025年5月にW&B(Weights & Biases)を約$1.4B〜$1.7Bで買収完了。Marimo、OpenPipe、Monolith AIも取り込み、AI開発フルスタックを拡張中。FY2025売上$5.131B。GAAP営業利益率-1%、Adjusted 13%。

**Lambda Labs**
- 強み: JupyterLabプリインストール、SSH即利用。1-Click Clusters (16-2000+ GPU)。egress無料。シンプルな開発者体験。
- 弱み: 在庫不足が頻発。Spot/予約なし。ジョブスケジューラ・推論エンドポイントなし。東京リージョンなし。
- 特記: 推定ARR $500M+、従業員約750人 (Sacra推定, 2025-05)。NVL72導入でメモリ拡大中。2026年4月から1x H100 PCIe $3.29/hr、SXM $4.29/hrに価格改定。

**RunPod**
- 強み: 市場最安級(H100 PCIe $1.99/hr)。秒課金。FlashBoot (<2秒コールドスタート)。Serverless endpoints。Instant Clusters (最大64 H100、InfiniBand)。
- 弱み: Community Cloudは信頼性にばらつき。2026年3月時点でGPU枯渇報告が頻発。分散学習は2025年3月開始で比較的新規。
- 特記: ARR $120M+ (2026-01公式)。+90% YoY。50万人超のdeveloper。従業員約90人。$20M seed調達(Intel Capital / Dell Technologies Capital, 2024-05)。

**Modal**
- 強み: Python-native SDK (最高の開発者体験)。サブ秒コールドスタート。ゼロアイドルコスト。InfiniBand 3200Gbps (beta)。
- 弱み: Spot/予約なし。セッション終了でボリューム削除。マルチノード学習はベータ。Modal SDKへのロックイン。
- 特記: Series B $87M / $1.1B post-money (2025-09)。$2.5B valuation報道あり(2026-02、未確定)。推定ARR ~$50M。従業員約112人。

**Together AI**
- 強み: FlashAttention、200+モデルの1-clickサーバーレス推論。Instant Clusters (8-64 GPU)、Dedicated Clusters (64-1000 GPU)。透明な予約価格体系。
- 弱み: Web UI中心でNotebookはβ。A100/L40Sの直接提供なし。日本語サポートなし。
- 特記: Series B $305M (2025-02)。研究〜推論まで同一GPUクラスターで一貫運用。

#### マーケットプレイス

**Vast.ai**
- 強み: P2Pマーケットプレイスで最安H100を秒課金で確保可能。Jupyter一発起動。Verified DCホスト対応。
- 弱み: ホスト品質と在庫が不安定。データ永続は自己管理。安定運用が難しい。
- 特記: 月間売上が初めて$1M超(2026-03公式)。推定ARR $12M+。14,000+月間有料顧客。手数料率25%(ホスト75%、Vast.ai 25%)。

#### 推論・サーバーレス

**Baseten**
- 強み: Scale-to-zero推論。<10秒コールドスタート。Trussフレームワーク(Python-native)。B200対応。
- 弱み: 推論専用(学習機能なし)。高価格帯(H100 $6.50/hr)。
- 特記: Series C $75M (2025-02)、Series E $300M (2026-02)。

**Replicate**
- 強み: 50K+モデル。秒課金。シンプルなAPI。
- 弱み: エンタープライズ弱。セキュリティ課題。
- 特記: Cloudflare買収後に改善見込み。

**Hugging Face**
- 強み: 500K+モデルHub。最大のOSSエコシステム。Spaces + Endpoints。自動スケール0→N。
- 弱み: GPU価格が高い(GCP/AWS経由)。分散学習や長時間訓練は非想定。
- 特記: OSSエコシステムの事実上の標準。

#### 開発環境・その他

**Lightning AI**
- 強み: Studioで80 GPU時間無料。W&B/MLflow連携。PyTorch Lightningネイティブ。
- 弱み: 6 GPUまでの制限。永続Volumeは有料オプション。
- 特記: 推定H100価格 ~$1.99-$3.49 (要確認)。

**Paperspace / DigitalOcean GPU Droplets**
- 強み: GPU Dropletを秒課金。Gradient NotebookでGUI/CLI両方。AMD MI300X対応($1.99/hr)。12ヶ月予約H100 $2.50/hr。
- 弱み: H100は北米のみ。InfiniBand無し。ML特化機能は限定的。
- 特記: DigitalOcean統合後にHGX H100/H200/A100/L40S/MI300Xまで対応拡大。

#### 日本国内プロバイダ

**さくらインターネット (高火力)**
- 強み: 国内H100/H200の物理・VM両プラン。日本円決済。ISMAP認定。信頼ブランド。秒課金DOK対応。PHYでNVLink/InfiniBand。
- 弱み: ML機能なし。Notebook環境は自力構築。VRTは時間課金で高い(¥990/hr)。
- 特記: DOKが2026年1月に大幅値下げ(0.83円/秒、~$2.50/GPU-hr)で国際競争力を獲得。METI補助金¥501B。

**GPUSOROBAN (ハイレゾ)**
- 強み: 国内最安級A100 80GB ¥398/hr ($2.65/hr)。日本語サポート充実。
- 弱み: APIや実験管理が未整備。分散学習は自己構築。H100公開単価なし。
- 特記: METI補助金¥77B。H200x8でNVLink対応。

**ABCI 3.0 (産総研)**
- 強み: 6,128 H200 GPUで国内最大規模(6.22 EFLOPS)。学術価格。200 Gb/s InfiniBand。
- 弱み: 事前審査とキュー待ちで即時利用不可。カード払い不可。Notebook環境なし。
- 特記: ユーザー約3,000人、566グループ。ポイント単価¥220、3pt/h (standard)。開発加速利用で半額。

**GMO GPU Cloud**
- 強み: 768GPU実証済みの大規模分散学習対応。ClusterMAX、BlueField-3。
- 弱み: 法人営業必須。ML機能なし。価格高い(H200共用 ¥6,000/hr)。
- 特記: METI補助金¥19.3B。

**共通特徴:** 全国内プロバイダがインフラ提供のみで、マネージドMLプラットフォーム（ノートブック+学習+推論+実験管理の統合）を提供していない。

---

## 4. 主要競合の財務データ

公開情報および推定値。出典はGPT-5.4-pro Web Search (2026-03-28)。

| 企業 | 売上/ARR | 成長率 | 従業員 | 調達額/評価額 | 粗利率 | ユーザー数 | 出典 |
|---|---|---|---|---|---|---|---|
| CoreWeave | FY2025売上 $5.131B | 非公開 | 非公開 | IPO済 | GAAP 71.7% (原価定義次第で14.6%) | 非公開 | investors.coreweave.com |
| Lambda Labs | 推定ARR $500M+ | 非公開 | ~750人 | Series D $480M (2025-02) | 推定20-30% | 非公開 | sacra.com推定 |
| RunPod | ARR $120M+ (公式) | +90% YoY (公式) | ~90人 | $20M seed (2024-05) | 推定15-25% | 500K+ developers | runpod.io公式 |
| Modal | 推定ARR ~$50M | 非公開 | ~112人 | Series B $87M / $1.1B (2025-09) | 推定30-40% | 非公開 | TechCrunch推定 |
| Vast.ai | $12M+ run-rate (公式) | 非公開 | 非公開 | 非公開 | 手数料25% | 14K+ 月間有料顧客 | vast.ai公式 |
| Together AI | 非公開 | 非公開 | 非公開 | Series B $305M (2025-02) | 非公開 | 非公開 | together.ai |
| Baseten | 非公開 | 非公開 | 非公開 | Series E $300M (2026-02) | 非公開 | 非公開 | businesswire.com |
| Nscale | 非公開 | 非公開 | 非公開 | Series C $2B / $14.6B (2026-03) | 非公開 | 非公開 | nscale.com |
| Crusoe | 非公開 | 非公開 | 非公開 | Series E $1.375B (2025-10) | 非公開 | 非公開 | crusoe.ai |

### H100 1台のユニットエコノミクス（推定）

出典: GPT-5.4-pro, Epoch AI, NVIDIA, CBRE, EIA (2026-03-28)

| 項目 | 金額 |
|---|---|
| GPU市場価格 (2025年) | $22K-$30K (幾何平均 $25.6K) |
| サーバ込み1GPUあたりCAPEX | ~$35.3K ($25.6K x 1.38 premium) |
| 減価償却 (3年直線) | $11,776/年 |
| 電力 (1.275kW/GPU, 70%稼働, 8.62c/kWh) | $674/年 |
| コロケーション ($196.25/kW/month) | $3,003/年 |
| **年間コスト合計** | **$15,453/年** |
| $2.50/hr x 70%稼働の年間収益 | $15,330/年 |
| **粗利** | **-$123/年 (-0.8%)** |
| **ブレークイーブン価格** | **~$2.52/hr (70%稼働時)** |

感度分析:
- 低CAPEX ($22K GPU): 粗利率 +10.0%
- 高CAPEX ($30K GPU): 粗利率 -14.0%

---

## 5. 出典

### 主要出典URL

| 区分 | URL |
|---|---|
| AWS | aws.amazon.com, calculator.holori.com |
| GCP | cloud.google.com |
| Azure | azure.microsoft.com, instances.vantage.sh |
| CoreWeave | coreweave.com, investors.coreweave.com, techcrunch.com |
| Lambda Labs | lambda.ai, sacra.com |
| RunPod | runpod.io, gpucost.org |
| Modal | modal.com, techcrunch.com |
| Together AI | together.ai |
| Vast.ai | vast.ai, computeprices.com |
| Baseten | baseten.co, businesswire.com |
| Replicate | replicate.com |
| Hugging Face | huggingface.co |
| DigitalOcean / Paperspace | digitalocean.com, paperspace.com |
| Lightning AI | lightning.ai |
| Spheron | spheron.network |
| Hyperstack | hyperstack.cloud |
| Oracle Cloud | oracle.com |
| さくらインターネット | sakura.ad.jp, cloud.sakura.ad.jp |
| GPUSOROBAN | soroban.highreso.jp |
| ABCI | abci.ai, docs.abci.ai |
| GMO GPU Cloud | gmo.jp |
| Nscale | nscale.com, itpro.com |
| GPU原価データ | epoch.ai (AI chip sales documentation) |
| 電力単価 | eia.gov (US industrial average 2025) |
| コロケーション | cbre.com (North America DC trends H2 2025) |
| NVIDIA DGX H100スペック | nvidia.com (DGX H100 datasheet) |
| SaaS/開発ツール ベンチマーク | openviewpartners.com, lightercapital.com, revmine.ai, proven-saas.com |
| 研究利用パターン | arxiv.org (NotebookOS 2503.20591) |

### データ取得モデル・時期

| データソース | モデル | 取得日 |
|---|---|---|
| AIXS_Competitive_Analysis_Market_Research.md | Gemini Deep Research + GPT-5.4-pro補足 | 2026-03-10〜28 |
| gpt54pro_price_comparison.md | o3 (Responses API + web_search_preview) | 2026-03-28 |
| gpt54pro_comprehensive_analysis.md | gpt-5.4-pro (Responses API + web_search_preview) | 2026-03-29 |
| gpt54pro_financial_critique.md | gpt-5.4-pro | 2026-03-28 |
