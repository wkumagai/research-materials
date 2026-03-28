# AIXS 競合分析・市場調査レポート

**作成日:** 2026-03-10
**対象:** AIXS戦略立案チーム
**データ期間:** 2024年後半〜2026年3月（一部前方予測を含む）
**最終更新:** 2026-03-28（GPT-5.4-pro Web Searchレビュー反映）
**為替参考:** 1 USD = ~150 JPY, 1 EUR = ~1.08 USD, 1 GBP = ~1.27 USD

---

## 1. エグゼクティブサマリー

### 全体結論

- GPU クラウドの H100 オンデマンド価格は 18 か月で $8+/GPU-hr から $2.50-6.00/GPU-hr へ急落し、コモディティ化が進行中（GPU特化プロバイダの平均は $2.50-$4.00/hr、ハイパースケーラーは $3.85-$12.29/hr）[GPT-5.4-pro補足, 2026-03-28]。ただし2026年初頭にはHBM（高帯域メモリ）不足により一時的な10%の価格反発（$2.00→$2.20/hr）も発生。AIXSが価格のみで競争するのは危険であり、統合R&Dプラットフォームとしての価値提案が不可欠
- ハイパースケーラー（AWS, GCP, Azure）はインフラの幅と規模で圧倒的だが、GPU調達のフリクション（クォータ申請、待機リスト）とR&Dワークフローの統合不足が弱点
- GPU特化クラウド（CoreWeave, Lambda, RunPod, Modal）は価格と開発者体験で差別化しているが、いずれも実験管理・モデルレジストリ・R&Dワークフローを内蔵していない
- 推論特化プラットフォーム（Baseten, Replicate, Together AI）はモデルサービングに強いが、トレーニングからインサイトまでの一貫したR&Dライフサイクルをカバーしていない
- 日本国内プロバイダ（さくら、GPUSOROBAN、GMO）はインフラ提供のみで、MLプラットフォーム機能を一切持たない。AIXSにとって最大のホワイトスペース
- 世界的に「ソブリンAI」が支配的なナラティブ。中東（$100B+）、EU（EuroHPC AI Factories + InvestAI EUR 200B + 5 AI Gigafactories）、日本（METI ¥1.23T FY2026予算）、インド（IndiaAI 38,000+ GPU確保、100,000目標）、シンガポール（S$37B RIE2030、NVIDIA全球売上の15%）のすべてが自国内GPU計算基盤を構築中
- 米国輸出規制がGPU調達のグローバル地図を変えている。中国は国産GPU（Huawei Ascend, Cambricon, Biren Technology, 天数智芯等）へ移行中[GPT-5.4-pro補足, 2026-03-28]、中東は年間50万チップ枠を交渉中
- R&D自動化システム（AI Scientist v2, Kosmos, Robin等）が新たな競合軸として台頭。Sakana AI（シード$30M→シリーズA追加で総額~$50M[GPT-5.4-pro補足, 2026-03-28]）のAI Scientist、FutureHouseのRobin（2025年5月に初のAI生成科学的発見を発表）など具体的成果が出始めている。AIXSはGPUコンピュート＋R&D自動化の統合で独自ポジションを確立可能
- 次世代GPU（NVIDIA Blackwell B200: 192GB HBM3e、8TB/s帯域幅、H100比で大幅な推論スループット向上（NVIDIAの公称値は最大30倍、実測ベンチマークでは用途により5-20倍程度の幅あり）[GPT-5.4-pro補足, 2026-03-28]）が市場構造を変革中。B200のGPU-hour単価は高い（$5.50-$10.00/hr）が、トークン単価は大幅低下。AMD MI300Xも一部プロバイダ（DigitalOcean, RunPod）で$1.99/hr程度で提供開始されNVIDIA独占に風穴[GPT-5.4-pro補足, 2026-03-28]
- 「推論ファースト」パラダイムへの移行: 2025年にAIコンピュートの50%が推論に使用、2026年には2/3に達する見込み。サーバーレスGPU（秒課金・トークン課金）が主流に
- 各地域で政府補助金・バウチャーが主要な資金源。中国の算力券（30+都市）、日本のGENIAC、インドのIndiaAI 40%割引、EUのAI Factory無料アクセスなど
- AIXSの最適ポジショニングは「価格帯は中間層（H100 $3-5/hr）、価値提案は最上位（統合R&Dプラットフォーム）」

### 競合分析の要点

- 最安帯: RunPod ($1.99/hr H100 PCIe community), GPUSOROBAN (A100 80GB $2.65/hr)
- 高機能帯: Modal (サーバーレス、Python SDK)、Together AI (FlashAttention、200+モデル)
- エンタープライズ帯: CoreWeave (K8s、InfiniBand)、AWS/Azure (コンプライアンス、エコシステム)
- どのプロバイダも「コンピュート＋実験管理＋モデル比較」を統合提供していない

### 市場調査の要点

- 米国: ハイパースケーラー＋ネオクラウドの最も成熟した市場。VCファンディングが世界の75%（$194B、2025年）、4,049データセンター
- EU/UK: ソブリンAI需要が急成長。EU AI Act＋GDPRが非EU提供者に高い参入障壁。EuroHPC 57,000アクセラレータ
- 日本: METI FY2026予算¥1.23T（$7.9B、AI・半導体4倍増）、ABCI 3.0 (6,128 H200、6.2 EXAFLOPS)、219データセンター、国内プロバイダにMLプラットフォーム機能なし。さくらDOK H100価格が2026年1月に更新（0.83円/秒 = ~$2.50/GPU-hr）
- 中国: 最大規模だが輸出規制下。算力券30+都市、GPU稼働率30%の過剰供給問題
- 韓国: KRW 10.1T ($7.3B) AI予算、260,000+ NVIDIA GPU確約、財閥主導
- 台湾: TSMC製造拠点だが国内コンピュート基盤構築中。TWCC + Foxconn
- 中東: UAE/サウジで$200B+のAIインフラパイプライン。SWF主導
- インド: 38,000+ 政府管理GPU（100,000目標）、40%補助金（Rs 115-150/GPU-hr = $1.40-$1.80で世界最安水準）、AI市場$8B（2024年）→$17B（2027年予測）、152データセンター、価格感度が極めて高い
- シンガポール: 供給制約市場（DC-CFA規制）、プレミアム価格、ASEANハブ
- イスラエル: スタートアップ主導（$7.9B AI VC）、NVIDIA R&D拠点、防衛AI需要

### AIXSへの主要示唆

- 価格勝負ではなく「GPU時間からインサイトまでの時間短縮」で差別化
- 日本市場は国内プロバイダにMLプラットフォームが存在しないため、最も参入しやすい
- EU市場はソブリンAI要件（GDPR、AI Act、CADA）を満たせば大きな機会
- 中東はSWF主導の大型案件が期待できるが、政府関係構築が必須
- マルチクラウドGPUオーケストレーション（ABCI＋さくら＋ハイパースケーラー等）が独自価値

---

## 2. 競合分析

### 2.1 対象一覧

| # | 企業/サービス | カテゴリ |
|---|---|---|
| 1 | AWS (Amazon Web Services) | Hyperscaler |
| 2 | Google Cloud Platform (GCP) | Hyperscaler |
| 3 | Microsoft Azure | Hyperscaler |
| 4 | CoreWeave | GPU-Specialized (IaaS) |
| 5 | Lambda Labs | GPU-Specialized (IaaS) |
| 6 | RunPod | GPU-Specialized (IaaS/PaaS) |
| 7 | Modal | GPU-Specialized (Serverless PaaS) |
| 8 | Together AI | GPU-Specialized (AI Platform) |
| 9 | Baseten | Inference/Dev Platform |
| 10 | Replicate | Inference/Dev Platform |
| 11 | Hugging Face | Inference/Dev Platform (Ecosystem) |
| 12 | Paperspace / DigitalOcean GPU Droplets | Inference/Dev Platform (General) |
| 13 | さくらインターネット (Sakura Internet) | Japanese Domestic |
| 14 | GPUSOROBAN (ハイレゾ / Hi-Reso) | Japanese Domestic |
| 15 | GMO GPU Cloud | Japanese Domestic |
| 16 | WebARENA IndigoGPU (NTTPC) | Japanese Domestic |
| 17 | ABCI 3.0 (産総研) | Japanese Domestic (National Infra) |
| 18 | Lightning AI | Additional |
| 19 | Brev.dev | Additional |
| 20 | Oracle Cloud | Additional |
| 21 | fal | Additional |
| 22 | Vast.ai | Additional |
| 23 | Fireworks AI | Additional |
| 24 | FluidStack | Additional |
| 25 | Hyperstack | Additional |
| 26 | Nscale | Additional (EU Neocloud) |
| 27 | Scaleway | Additional (EU Neocloud) |
| 28 | OVHcloud | Additional (EU Neocloud) |
| 29 | Nebius | Additional (EU/Israel Neocloud) |
| 30 | Core42 (G42) | Additional (Middle East) |

### 2.2 比較条件・価格正規化の方法説明

**正規化の基準:**

1. **単位:** 全価格を **1 GPU-hour (USD)** に正規化。8-GPU ノード価格は 8 で割って 1-GPU 換算
2. **GPU モデルの違い:** H100 SXM と H100 PCIe は区別して記載。SXM はノード間 NVLink/NVSwitch 対応で性能が高く、PCIe は単体利用向けで安価。同一 GPU モデル同士での比較を原則とする
3. **VRAM容量の違い:** A100 40GB と 80GB は別エントリとして記載
4. **課金粒度の影響:** 秒課金（Modal, RunPod）vs 分課金（CoreWeave, Lambda）vs 時間課金（Paperspace）で実効コストが異なる。バースト的ワークロードでは秒課金が有利
5. **Spot/Preemptible の扱い:** オンデマンド価格と分離して記載。中断リスクがあるため直接比較には注意
6. **為替レート:** 日本円は 1 USD = 150 JPY で換算（2025年3月平均）
7. **隠れコスト:** ストレージ、Egress、IOPS は別途注記。「オールインクルーシブ」を謳うプロバイダ（Lambda, CoreWeave）は egress 無料
8. **予約価格:** コミットメント期間ごとに記載（1年、3年等）。要セールス連絡の場合は「Contact sales」と記載
9. **推定値のマーク:** 公開情報が不完全な場合は「~」または「(est.)」を付与
10. **調査日:** 各データの取得時期を明記。GPU市場は変動が激しいため、数か月で価格が大幅に変わりうる

**比較上の注意:**
- ハイパースケーラーは GPU 以外のリソース（vCPU, RAM, ストレージ, ネットワーク）が含まれるため、純粋な GPU-hour 比較では割高に見える場合がある
- サーバーレスプロバイダ（Modal, Baseten）はアイドル時ゼロコストのため、稼働率によって実効コストが大きく変動
- Community Cloud（RunPod）と Secure Cloud では信頼性・セキュリティレベルが異なる

### 2.3 総合比較表

#### H100 80GB SXM 比較

| 企業/サービス | 主要GPU | 提供形態 | 公開価格(8-GPU) | 正規化価格(1 GPU-h) | 24h | 7日 | 30日 | 課金単位 | Spot/予約 | 主要メリット | 主要デメリット | AIXSへの示唆 | 出典 | 調査日 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AWS (p5.48xlarge) | H100 SXM x8 | IaaS VM | $55.04/hr (pre-cut); ~$30.82/hr (post-Jun 2025) | $6.88 / ~$3.85 | $1,321 / ~$740 | $9,247 / ~$5,178 | $39,629 / ~$22,190 | 秒(60s min) | Spot $3.79; 1yr $2.97; 3yr $2.59; Capacity Blocks $4.33 | 最大エコシステム、Capacity Blocks、2025年44%値下げ | クォータ申請必要、容量不足エラー頻発 | AWS値下げ後も体験・統合価値で差別化可能 | aws.amazon.com | 2025-03 |
| GCP (a3-highgpu-8g) | H100 SXM x8 | IaaS VM | $87.83/hr | $10.98 | $2,108 | $14,756 | $63,238 | 秒(60s min) | Spot $3.69; 1yr CUD ~$7.14; 3yr CUD ~$5.50 | クリーンUX、TPU差別化、Vertex AI | NVIDIA GPU価格が最高値 | 価格で大幅に勝てる相手 | cloud.google.com | 2025-03 |
| Azure (ND96isr_H100_v5) | H100 SXM x8 | IaaS VM | $98.32/hr | $12.29 | $2,360 | $16,518 | $70,790 | 秒(5min min) | Spot $2.27; Reserved: Contact sales | エンタープライズ統合、30+リージョン、InfiniBand | 最高価格帯、5分最低課金、複雑 | R&D向けで明確に差別化可能 | azure.microsoft.com | 2025-03 |
| CoreWeave (HGX) | H100 SXM x8 | K8s IaaS | $49.24/hr | $6.16 | $148 | $1,035 | $4,435 | 分 | 要セールス(最大60%OFF) | K8s native、InfiniBand 3200Gbps、egress無料 | 8-GPU最小、K8s知識必要、高価格 | R&D体験で差別化。K8s不要の簡易UX | coreweave.com | 2025-03 |
| Lambda Labs (8x) | H100 SXM x8 | SSH/VM | $31.92/hr | $3.99 | $96 | $670 | $2,873 | 分 | なし; 予約は要セールス | Lambda Stack、JupyterLab、シンプル | 在庫不足頻発、Spot無し、オーケストレーション無し | 実験管理で大きく差別化可能 | lambda.ai | 2025-03 |
| Lambda Labs (1-Click Cluster) | H100 SXM | クラスター | - | $2.76 | $66 | $464 | $1,987 | 分 | なし | 最安クラスター価格、16-2000+ GPU | 大規模のみ | クラスター規模では価格勝負困難 | lambda.ai | 2025-03 |
| RunPod (community) | H100 SXM | コンテナ | - | $2.69 | $65 | $452 | $1,937 | 秒 | Spot $1.50; 1yr $2.61 | 最安級、Spot有、秒課金 | Community低信頼性、分散学習新規 | 価格で勝つのは極めて困難 | runpod.io | 2025-03 |
| RunPod (PCIe community) | H100 PCIe | コンテナ | - | $1.99 | $48 | $334 | $1,433 | 秒 | Spot $1.35 | 市場最安 | PCIe性能制限 | 価格競争は不可。体験で差別化 | runpod.io | 2025-03 |
| Modal | H100 SXM | サーバーレス | - | $3.95 | $95 | $664 | $2,844 | 秒 | なし | 最高DevX、Python SDK、ゼロアイドル | Spot/予約無し、ロックイン高 | 最大の直接競合。R&D統合で差別化 | modal.com | 2025-03 |
| Together AI (cluster) | H100 SXM | クラスター | - | $3.49 | $84 | $586 | $2,513 | 分 | 予約: 1w-1m $2.69; 4-6m $2.25 | FlashAttention、200+モデル、透明予約価格 | A100/L40S無し、汎用ワークロード不可 | 推論特化。R&Dライフサイクルで差別化 | together.ai | 2025-03 |
| Baseten | H100 80GB | 推論PaaS | - | $6.50 | $156 | $1,092 | $4,680 | 分 | なし | Scale-to-zero、<10sコールドスタート | 推論専用、高価格 | 補完的競合。R&D全体をカバー | baseten.co | 2025-03 |
| Replicate | H100 80GB | 推論PaaS | - | $5.49 | $132 | $922 | $3,953 | 秒 | なし | 50K+モデル、秒課金 | エンタープライズ弱、セキュリティ課題 | 部分的競合。R&Dチーム向けではない | replicate.com | 2025-03 |
| HF Inference (GCP) | H100 80GB | 推論エンドポイント | - | $10.00 | $240 | $1,680 | $7,200 | 分 | なし | 500K+モデルHub、最高エコシステム | GPU価格高い（GCP経由） | エコシステムと統合しつつ価格で勝つ | huggingface.co | 2025-03 |
| DO GPU Droplets (HGX H100) | H100 80GB | VM | - | $3.39 | $81 | $569 | $2,441 | 秒(5min min) | 12mo reserved $2.50 | AMD GPU対応、シンプル | ML特化機能なし | R&D体験で明確に差別化 | digitalocean.com | 2025-03 |
| Sakura VRT | H100 80GB | VM | ¥990/hr | $6.60 | $158 | $1,109 | $4,752 | 時間 | 月額キャップ有 | 日本国内、ISMAP、信頼ブランド | ML機能なし、高価格 | 日本市場でR&Dプラットフォームとして差別化 | sakura.ad.jp | 2025-03 |
| Sakura DOK (2026年1月更新) | H100 80GB x8 | コンテナ | ¥2,988/hr (0.83円/秒) | ~$2.50 | $60 | $418 | $1,793 | 秒(60s min) | なし | 秒課金、Docker対応、4TB NVMe、20GBストレージ | 低帯域、ML機能なし | **大幅値下げ**により国際競争力あり。DOKユーザーに統合R&D体験を提供 | sakura.ad.jp (Gemini DR) | 2026-01 |

#### H200 141GB 比較

| 企業/サービス | 正規化価格(1 GPU-h) | 24h | 7日 | 30日 | Spot/予約 | 課金単位 | 出典 | 調査日 |
|---|---|---|---|---|---|---|---|---|
| AWS (p5en.48xlarge) | $7.91 / ~$5.93 (post-Jun 2025) | $190 / ~$142 | $1,329 / ~$996 | $5,695 / ~$4,270 | Spot $2.28; Capacity Blocks $5.72 | 秒(60s min) | aws.amazon.com | 2025-03 |
| GCP (a3-ultragpu-8g) | $10.85 | $260 | $1,823 | $7,812 | Spot $4.04 | 秒(60s min) | cloud.google.com | 2025-03 |
| Azure (ND96isr_H200_v5) | $13.78 | $331 | $2,315 | $9,922 | Spot: 割引無し記載 | 秒(5min min) | azure.microsoft.com | 2025-03 |
| CoreWeave (HGX) | $6.31 | $151 | $1,060 | $4,543 | 要セールス(最大60%OFF) | 分 | coreweave.com | 2025-03 |
| RunPod | $3.59 | $86 | $603 | $2,585 | 1yr $3.05 | 秒 | runpod.io | 2025-03 |
| Modal | $4.54 | $109 | $763 | $3,269 | なし | 秒 | modal.com | 2025-03 |
| Together AI | $4.19 | $101 | $704 | $3,017 | 4-6mo $2.59 | 分 | together.ai | 2025-03 |
| DO GPU Droplets (HGX H200) | $3.44 | $83 | $578 | $2,477 | なし | 秒(5min min) | digitalocean.com | 2025-03 |
| HF Inference (AWS) | $5.00 | $120 | $840 | $3,600 | なし | 分 | huggingface.co | 2025-03 |
| GPUSOROBAN (standard) | ~$18,553/mo (8-GPU) = ~$25.77/GPU-hr equiv. | $618 | $4,329 | $18,553 | 5yr/volume ~$9,277/mo | 月額 | soroban.highreso.jp | 2025-03 |
| Sakura PHY (H100x8 ※H200要問合せ) | ~$20,307/mo; 3yr ~$16,246/mo | $677 | $4,738 | $20,307 | 1yr/3yr契約 | 月額 | sakura.ad.jp | 2025-03 |

#### A100 80GB 比較

| 企業/サービス | 正規化価格(1 GPU-h) | 24h | 7日 | 30日 | Spot/予約 | 課金単位 | 出典 | 調査日 |
|---|---|---|---|---|---|---|---|---|
| AWS (p4de.24xlarge) | $3.43 | $82 | $576 | $2,470 | Spot $2.43; 3yr $1.47 | 秒 | aws.amazon.com | 2025-03 |
| GCP (a2-ultragpu-8g) | $6.25 | $150 | $1,050 | $4,500 | -- | 秒 | cloud.google.com | 2025-03 |
| Azure (ND96amsr_A100_v4) | $4.10 | $98 | $689 | $2,952 | Spot $1.07 | 秒 | azure.microsoft.com | 2025-03 |
| CoreWeave | $2.70 | $65 | $454 | $1,944 | 要セールス(最大60%OFF) | 分 | coreweave.com | 2025-03 |
| Lambda Labs (SXM 8x) | $2.79; 1GPU PCIe: $1.10-$1.29 | $67 | $469 | $2,009 | なし | 分 | lambda.ai | 2025-03 |
| RunPod (SXM community) | $1.39 | $33 | $234 | $1,001 | Spot $0.79; 1yr $1.22 | 秒 | runpod.io | 2025-03 |
| RunPod (PCIe community) | $1.19 | $29 | $200 | $857 | Spot $0.60; 1yr $1.14 | 秒 | runpod.io | 2025-03 |
| Modal (80GB) | $2.50 | $60 | $420 | $1,800 | なし | 秒 | modal.com | 2025-03 |
| Baseten (80GB) | $4.00 | $96 | $672 | $2,880 | なし | 分 | baseten.co | 2025-03 |
| Replicate (80GB) | $5.04 | $121 | $847 | $3,629 | なし | 秒 | replicate.com | 2025-03 |
| HF Inference (AWS) | $2.50 | $60 | $420 | $1,800 | なし | 分 | huggingface.co | 2025-03 |
| Paperspace | $3.18 | $76 | $534 | $2,290 | なし | 時間 | paperspace.com | 2025-03 |
| GPUSOROBAN (t80-1-a) | $2.65 (¥398) | $64 | $445 | $1,908 | なし | 時間 | soroban.highreso.jp | 2025-03 |
| Azure single GPU (NC24ads) | $3.67 | $88 | $617 | $2,642 | Spot $0.74 | 秒 | azure.microsoft.com | 2025-03 |
| ABCI 3.0 (H200 1-GPU ※) | ~$2.20 (dev accel.) / ~$4.40 (standard) | $53 / $106 | $370 / $739 | $1,584 / $3,168 | 予約: 要申請 | ポイント制 | abci.ai | 2025-03 |

※ ABCI 3.0はH200だがA100クラスとの比較参考として掲載

#### L40S 48GB 比較

| 企業/サービス | 正規化価格(1 GPU-h) | 24h | 7日 | 30日 | Spot/予約 | 課金単位 | 出典 | 調査日 |
|---|---|---|---|---|---|---|---|---|
| AWS (g6e.xlarge) | $1.86 | $45 | $313 | $1,339 | ~$1.00-$1.50 (est.) | 秒(60s min) | aws.amazon.com | 2025-03 |
| CoreWeave | $2.25 | $54 | $378 | $1,620 | 要セールス(最大60%OFF) | 分 | coreweave.com | 2025-03 |
| RunPod | $0.79 | $19 | $133 | $569 | Spot $0.40; 1yr $0.71 | 秒 | runpod.io | 2025-03 |
| Modal | $1.95 | $47 | $328 | $1,404 | なし | 秒 | modal.com | 2025-03 |
| HF Inference (AWS) | $1.80 | $43 | $302 | $1,296 | なし | 分 | huggingface.co | 2025-03 |
| Replicate | $3.51 | $84 | $590 | $2,527 | なし | 秒 | replicate.com | 2025-03 |
| DO GPU Droplets | $1.57 | $38 | $264 | $1,130 | なし | 秒(5min min) | digitalocean.com | 2025-03 |

#### B200 比較（Deep Research補足データ）

| 企業/サービス | 正規化価格(1 GPU-h) | 予約 | 課金単位 | 出典 | 調査日 |
|---|---|---|---|---|---|
| CoreWeave (8-GPU) | $8.60 ($68.80/8-GPU) | 要セールス | 分 | coreweave.com | 2026-03 |
| Lambda Labs (8-GPU) | $4.99 (1yr: $3.49) | 1年: $3.49 | 分 | lambda.ai | 2026-03 |
| RunPod | $5.99 | -- | 秒 | runpod.io | 2026-03 |
| Modal | $6.25 | なし | 秒 | modal.com | 2026-03 |
| Together AI | $5.50 | -- | 分 | together.ai | 2026-03 |
| Baseten | $9.98 | なし | 分 | baseten.co | 2026-03 |

※ B200はBlackwell世代。192GB HBM3e、8TB/s帯域幅。H100比で推論スループット約15倍。GPU-hour単価は高いがトークン単価は大幅低下。

#### AMD MI300X 比較（Deep Research補足データ）

| 企業/サービス | 正規化価格(1 GPU-h) | 備考 | 出典 | 調査日 |
|---|---|---|---|---|
| DigitalOcean | $1.99 | NVIDIA独占を崩す価格設定 | digitalocean.com | 2026-03 |
| RunPod | $1.99 | Community Cloud | runpod.io | 2026-03 |

※ AMD MI300Xの台頭により、NVIDIA以外の選択肢が現実的に。高性能LLM推論に適し、市場全体の価格下落圧力を加速。

#### 追加競合プロバイダ（Deep Research補足データ）

| 企業/サービス | H100価格(1 GPU-h) | A100価格 | 特徴 | 出典 | 調査日 |
|---|---|---|---|---|---|
| Spheron | $2.01 (Spot: $0.99) | $1.07 | 分散型GPU集約、SLA保証、秒課金、egress無料 | spheron.network | 2026-03 |
| Vast.ai | $1.49-$2.27 | ~$0.50 | P2Pマーケットプレイス、最安級だが信頼性は変動 | vast.ai | 2026-03 |
| Oracle Cloud (OCI) | ~$3.49 (A100: ~$2.48) | ~$2.48 | ベアメタルGPU（BM.GPU.A100/H100）、RDMA対応、OCI Supercluster、Oracle AI Infrastructure。H100はBM.GPU.H100.8で提供。データセンター80+リージョン | oracle.com/cloud | 2026-03 |
| Lightning AI | ~$1.99-$3.49 [要確認] | [要確認] | GPU Studios（対話型開発環境）、Lightning Trainer統合、PyTorch Lightningネイティブ。価格はGPU Studiosのtier依存 | lightning.ai | 2026-03 |
| Brev.dev | [要確認: 基盤クラウド価格+マージン] | [要確認] | 1-click GPU環境プロビジョニング、AWS/GCP/Lambda等の基盤クラウド上に構築。価格は基盤プロバイダ価格＋Brev手数料（概算10-20%上乗せ） | brev.dev | 2026-03 |

### 2.4 詳細比較表（各社プロファイル）

#### 2.4.1 AWS (Amazon Web Services)

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 中 | クォータ増加申請が必要（新規アカウントは1-2週間待ち）。Capacity Blocksで改善中 |
| GPU在庫安定性 | 中 | H100でInsufficientInstanceCapacityエラー頻発。H200は5+リージョンに拡大中 |
| 起動の早さ | 中 | GPU VM: 60-180秒。コンテナ: +3-5分。Warm Pools対応 |
| API/CLI/SDK | 優秀 | aws-cli (最も成熟)、Boto3、12+言語SDK、Terraform対応 |
| Notebook/Job/Batch/Inference | 全対応 | SageMaker Studio, Training Jobs, Batch Transform, Endpoints |
| 分散学習 | 強 | SageMaker HyperPod (Slurm native)、EKS + Karpenter、Ray統合、EFA 3200Gbps |
| データ連携 | 優秀 | S3 (業界標準)、FSx for Lustre (HPC最適化)、EBS io2 Block Express |
| ログ・監視 | 優秀 | CloudWatch + NVIDIA DCGM、SageMaker Debugger、Cost Explorer |
| 実験管理 | 良 | SageMaker Experiments、Managed MLflow (GA)、Model Registry |
| モデル配備 | 優秀 | JumpStart (200+モデル)、Auto-scaling、A/B Testing |
| エンタープライズ調達 | 強 | EDP、AWS Marketplace (最大)、Consolidated Billing |
| セキュリティ・コンプライアンス | 最優秀 | 143+認定、FedRAMP High、HIPAA、SOC 1/2/3、Nitro Enclaves |
| 学習向き/推論向き | 両方 | HyperPod (学習)、Inferentia2/Trainium2 (推論/学習の独自シリコン) |
| 開発者体験 | 中 | 機能豊富だが学習曲線が急。コンソールが雑然 |
| ベンダーロックイン | 高 | Lambda, DynamoDB, SageMaker等の独自サービス群。EKS/Terraformで緩和可能 |
| AIXSとの競合度合い | 部分的 | AIXSはML workflowレイヤーで競合。AWSはインフラ。AIXSがAWS上で動く可能性も |

#### 2.4.2 Google Cloud Platform (GCP)

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 良 | コンソールから一般利用可能。クォータ制限あり |
| GPU在庫安定性 | 良 | H100: 16リージョン。H200: 8リージョン |
| 起動の早さ | 良 | 60-120秒。MIG対応 |
| API/CLI/SDK | 優秀 | gcloud (クリーン設計)、google-cloud-* SDK、Terraform対応 |
| Notebook/Job/Batch/Inference | 全対応 | Vertex AI Workbench、Colab Enterprise (優秀)、Custom Training、Batch Prediction (50%割引) |
| 分散学習 | 強 | GKE Autopilot (最良)、TPU Pods、gVNIC/MRDMA |
| データ連携 | 優秀 | GCS、Filestore、BigQuery、Hyperdisk Extreme |
| ログ・監視 | 良 | Cloud Monitoring + DCGM、Vertex AI TensorBoard (マネージド) |
| 実験管理 | 良 | Vertex AI Experiments、Model Registry、Vizier (HPO) |
| モデル配備 | 優秀 | Model Garden (200+モデル)、Traffic splitting |
| エンタープライズ調達 | 成長中 | CUDs、Cloud Marketplace |
| セキュリティ・コンプライアンス | 良 | SOC 1/2/3、ISO、HIPAA、FedRAMP |
| 学習向き/推論向き | 両方(TPU差別化) | TPU v5e/v5p/v6が独自強み |
| 開発者体験 | 良 | 最もクリーンなUX。ML/研究コミュニティが強い |
| ベンダーロックイン | 中-高 | BigQuery + TPUがスティッキー。K8s/TF起源でOSS寄り |
| AIXSとの競合度合い | 部分的 | Vertex AIはML Platform。R&Dワークフロー特化ではない |

#### 2.4.3 Microsoft Azure

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 中 | ポータル経由可。エンタープライズパスが推奨 |
| GPU在庫安定性 | 良 | H100: 30+リージョン。H200: 28リージョン |
| 起動の早さ | 中 | 60-180秒。2025年6月から5分最低課金 |
| API/CLI/SDK | 良 | az-cli (包括的だが冗長)、Bicep/ARM + Terraform |
| Notebook/Job/Batch/Inference | 全対応 | AML Notebooks、Training Jobs、Batch Endpoints、Online Endpoints |
| 分散学習 | 強 | CycleCloud (Slurm native)、AKS、DeepSpeed (MS開発)、InfiniBand |
| データ連携 | 良 | Blob Storage、Azure Files、ADLS Gen2、Ultra Disks |
| ログ・監視 | 良 | Azure Monitor + DCGM、Cost Management + Advisor |
| 実験管理 | 良 | AML Experiments、Managed MLflow (native)、HyperDrive |
| モデル配備 | 良 | AML Model Catalog、Blue-green / canary |
| エンタープライズ調達 | 最強 | EA (最も成熟)、CSP、Office 365/AD統合 |
| セキュリティ・コンプライアンス | 優秀 | SOC 1/2/3、ISO、HIPAA、FedRAMP High、Confidential GPU (preview) |
| 学習向き/推論向き | 両方(エンタープライズ推論寄り) | ONNX Runtime、Triton、Maia 100 (preview) |
| 開発者体験 | 低-中 | エンタープライズ複雑性。学習曲線が最も急 |
| ベンダーロックイン | 高 | AD + Office 365統合。Cosmos DB等独自サービス |
| AIXSとの競合度合い | 低(重複少) | AzureはエンタープライズIT。AIXSはR&Dチーム向け |

#### 2.4.4 CoreWeave

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 中 | K8s知識必要。セールス連絡推奨 |
| GPU在庫安定性 | 高 | エンタープライズ契約による安定供給 |
| 起動の早さ | 分単位 | インスタンスプロビジョニング |
| API/CLI/SDK | 良 | kubectl、Helm、Cloud UI |
| Notebook/Job/Batch/Inference | 部分的 | Notebook無し。K8s Jobs対応。推論は中程度 |
| 分散学習 | 最優秀 | InfiniBand 3200Gbps、100K+ GPUクラスター、非ブロッキングファブリック |
| データ連携 | 優秀 | AI Object Storage + LOTA (2+ GB/s per GPU)、egress/IOPS無料 |
| ログ・監視 | 良 | K8s native monitoring |
| 実験管理 | なし | ビルトイン実験管理なし |
| モデル配備 | 中 | K8s経由 |
| エンタープライズ調達 | 優秀 | セールス契約、SLA、Flex Reservations |
| セキュリティ・コンプライアンス | 優秀 | SOC 2 Type II、ISO 27001、HIPAA、FedRAMP、PCI、GDPR |
| 学習向き/推論向き | 学習強 | 大規模トレーニングに最適化 |
| 開発者体験 | 中 | DevOps重い。K8s専門知識前提 |
| ベンダーロックイン | 低 | K8s標準 |
| AIXSとの競合度合い | 部分的 | 大規模学習/推論ワークロード向け。R&D実験ライフサイクルとは異なるユースケース |

#### 2.4.5 Lambda Labs

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 良 | SSH + JupyterLab。シンプル |
| GPU在庫安定性 | 低 | 人気GPU型の在庫不足が頻発 |
| 起動の早さ | 分単位 | |
| API/CLI/SDK | 基本的 | SSH、ダッシュボード |
| Notebook/Job/Batch/Inference | 限定 | JupyterLab有。ジョブスケジューラ/推論エンドポイント無し |
| 分散学習 | 良 | 1-Click Clusters (16-2000+ GPU) |
| データ連携 | 基本的 | 永続ストレージ ($0.20/GiB/mo) |
| ログ・監視 | 基本的 | Cloud Metrics Dashboard |
| 実験管理 | なし | |
| モデル配備 | 低 | 手動 |
| エンタープライズ調達 | 良 | SOC 2 Type II、ISO 27001。ホワイトグローブサポート |
| セキュリティ・コンプライアンス | 良 | SOC 2、ISO 27001、シングルテナント、ハードウェア分離 |
| 学習向き/推論向き | 学習専用 | 推論機能なし |
| 開発者体験 | 良 | シンプルだがSSHベース |
| ベンダーロックイン | 最低 | SSH + 標準ツール |
| AIXSとの競合度合い | 部分的 | コンピュートプロバイダ。AIXSはコンピュート＋R&Dプラットフォーム |

#### 2.4.6 RunPod

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 良 | Web UI、Docker、即時利用可能 |
| GPU在庫安定性 | 中 | Community Cloudは変動あり。30+ GPUタイプ |
| 起動の早さ | 秒 | FlashBoot (<2秒コールドスタート for serverless) |
| API/CLI/SDK | 良 | REST API (GA)、CLI |
| Notebook/Job/Batch/Inference | 広範 | Pods (対話型)、Serverless endpoints、Batch、Instant Clusters |
| 分散学習 | 良 | Instant Clusters (最大64 H100、InfiniBand)。2025年3月開始で比較的新規 |
| データ連携 | 良 | Container/Volume/Network Storage |
| ログ・監視 | 良 | リアルタイムログ、トレーシング |
| 実験管理 | なし | |
| モデル配備 | 高 | Serverless endpoints |
| エンタープライズ調達 | 中 | セルフサービス＋セールス。SOC 2 Type II (2025年取得) |
| セキュリティ・コンプライアンス | 良 | SOC 2 Type II、ISO 27001 (Secure Cloud経由) |
| 学習向き/推論向き | 両方 | Serverless推論＋Instant Clusters学習 |
| 開発者体験 | 良 | 直感的UI |
| ベンダーロックイン | 低 | Docker ベース |
| AIXSとの競合度合い | 部分的 | インフラ。AIXSはインフラ＋R&Dツーリング |

#### 2.4.7 Modal

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 最良 | Python SDKで定義。YAML/設定ファイル不要 |
| GPU在庫安定性 | 中-高 | T4からB200まで幅広い |
| 起動の早さ | サブ秒 | 多くのワークロードでサブ秒コールドスタート |
| API/CLI/SDK | 最優秀 | Python SDK (Pythonic、自動コンテナ化) |
| Notebook/Job/Batch/Inference | 広範(Notebook無し) | サーバーレス関数、Training jobs、Inference endpoints、Batch |
| 分散学習 | 良(beta) | Gang scheduling、InfiniBand 3200Gbps。マルチノードはベータ |
| データ連携 | 良 | Modal Volumes (コンピュートモデルに含む) |
| ログ・監視 | 良 | ビルトインダッシュボード |
| 実験管理 | なし | W&B/MLflow等の外部統合が必要 |
| モデル配備 | 高 | Pythonデコレータでデプロイ |
| エンタープライズ調達 | 良 | Team ($250/mo)、Enterprise (カスタム) |
| セキュリティ・コンプライアンス | 良 | SOC 2 Type II、HIPAA対応 |
| 学習向き/推論向き | 両方 | 学習・推論ともに強い |
| 開発者体験 | 最優秀 | Python-native、ゼロアイドルコスト |
| ベンダーロックイン | 高 | Modal SDK必須。コードがModal-native |
| AIXSとの競合度合い | 直接競合(最大) | ML/AI実践者向けの学習＋推論。最も重複が大きい |

#### 2.4.8 Together AI

| 評価軸 | 評価 | 詳細 |
|---|---|---|
| 調達しやすさ | 良 | Webコンソール＋API |
| GPU在庫安定性 | 高 | エンタープライズ重視 |
| 起動の早さ | 分単位 | クラスター起動 |
| API/CLI/SDK | 良 | API-first |
| Notebook/Job/Batch/Inference | 限定 | GPU Clusters、Serverless推論、Dedicated推論、Fine-tuning、Batch推論(50%OFF) |
| 分散学習 | 良 | Instant Clusters (8-64 GPU)、Dedicated Clusters (64-1000 GPU) |
| データ連携 | 良 | マネージド共有ファイルシステム ($0.16/GiB/mo) |
| ログ・監視 | 基本的 | |
| 実験管理 | なし | |
| モデル配備 | 最高 | 200+モデル、1-click、FlashAttention |
| エンタープライズ調達 | 良 | VPC/オンプレミスデプロイ対応 |
| セキュリティ・コンプライアンス | 良 | SOC 2 Type II、HIPAA、VPC |
| 学習向き/推論向き | 推論非常に強/学習強 | FlashAttention、200+モデルサーバーレス |
| 開発者体験 | 良 | API-first |
| ベンダーロックイン | 中 | Together API/エコシステム |
| AIXSとの競合度合い | 部分的 | 推論＋クラスター。R&Dライフサイクルとは異なるフォーカス |

#### 2.4.9 日本国内プロバイダ総括

| 評価軸 | さくらインターネット | GPUSOROBAN | GMO GPU Cloud | WebARENA IndigoGPU | ABCI 3.0 |
|---|---|---|---|---|---|
| 調達しやすさ | 良(日本語UI) | 中(日本語) | 低(法人営業必須) | 中(法人向け) | 中(申請審査制) |
| GPU在庫安定性 | 中 | 中 | 中 | 中 | 高 |
| 起動の早さ | 分〜日 | 分 | 要問合せ | 要問合せ | キュー待ち有 |
| API/CLI/SDK | 中(さくらのクラウドAPI) | 基本(SSHのみ) | 基本(Harbor/コンテナ) | 基本 | CLI有 |
| Notebook | なし | JupyterLab(プリインストール) | なし | なし | なし |
| 分散学習 | PHYでNVLink/InfiniBand | H200x8でNVLink | 強(768GPU実証済) | NVLink | 6128 H200クラスター |
| 実験管理 | なし | なし | なし | なし | なし |
| 推論エンドポイント | なし | なし | なし | なし | なし |
| セキュリティ | ISMAP、ISO 27001/27017 | ISO 27001/27017、Privacy Mark | ClusterMAX、BlueField-3 | NVIDIAパートナー | AIST運営 |
| 価格帯 | 中-高 | 低(A100最安級) | 高(H200 ¥6000/hr共用) | 中 | 非常に低(補助金) |
| AIXSとの競合度合い | 低(インフラのみ) | 低(インフラのみ) | 低(インフラのみ) | 低(インフラのみ) | 低(公的基盤) |

**日本市場の決定的ギャップ:** 全国内プロバイダがインフラ提供のみで、マネージドMLプラットフォーム（ノートブック＋学習＋推論＋実験管理）を提供していない。これはAIXSにとって最大の差別化ポイント。

#### 2.4.10 推論/Dev/エコシステムプロバイダ総括（Baseten, Replicate, Hugging Face, Paperspace/DigitalOcean）

| 評価軸 | Baseten | Replicate | Hugging Face | Paperspace / DigitalOcean GPU Droplets |
|---|---|---|---|---|
| 調達しやすさ | 良（Webコンソール＋API、セルフサービス） | 良（Webコンソール、API、即時利用可能） | 最良（Web UI、無料枠あり、500K+モデルHub） | 良（Webコンソール、クレジットカードで即時利用） |
| GPU在庫安定性 | 中（推論需要に最適化、H100/A100/B200対応） | 中（H100/A100/L40S対応、50K+モデル） | 中-高（GCP/AWS経由、複数GPU世代対応） | 良（DigitalOcean統合後、HGX H100/H200/A100/L40S/MI300X対応） |
| 起動の早さ | 優秀（Scale-to-zero、<10sコールドスタート） | 良（秒課金、コールドスタートはモデル依存） | 中（エンドポイント起動に数分） | 中（VM起動に60-120秒、5分最低課金） |
| API/CLI/SDK | 良（Truss フレームワーク、Python SDK） | 良（REST API、Python/Node SDK、Cog） | 優秀（transformers/diffusers等のOSSエコシステム、推論API） | 基本的（doctl CLI、REST API） |
| Notebook/Job/Batch/Inference | 推論特化（Scale-to-zero推論エンドポイント） | 推論特化（モデル実行、Predictions API） | 推論＋Spaces（Gradio/Streamlit）＋AutoTrain＋Training | Notebook有（Gradient Notebooks）、VM（GPU Droplets） |
| 分散学習 | なし（推論専用） | なし（推論専用） | 限定的（AutoTrain、DGX Cloud統合） | なし（単一GPU VM） |
| データ連携 | 基本的（モデルアーティファクト管理） | 基本的（モデル入出力） | 優秀（Datasets Hub、500K+データセット） | 基本的（DigitalOcean Spaces/Volumes） |
| ログ・監視 | 良（リクエストログ、レイテンシ監視） | 基本的（Prediction履歴） | 基本的（エンドポイントメトリクス） | 基本的（DigitalOcean Monitoring） |
| 実験管理 | なし | なし | 部分的（HF Hub上のモデルカード・メトリクス） | なし |
| モデル配備 | 高（Scale-to-zero、オートスケーリング、A/Bテスト） | 高（50K+モデル、ワンクリックデプロイ） | 最高（500K+モデル、Inference Endpoints、Spaces） | 低（手動デプロイ） |
| エンタープライズ調達 | 中（カスタム契約対応） | 低-中（セルフサービス中心、Cloudflare買収後に改善見込み） | 良（Enterprise Hub、SSO、プライベートモデル） | 良（DigitalOceanのエンタープライズ契約） |
| セキュリティ・コンプライアンス | 良（SOC 2 Type II） | 中（Cloudflare買収後に改善見込み） | 良（SOC 2、GDPR対応、プライベートHub） | 良（SOC 2 Type II、ISO 27001） |
| 学習向き/推論向き | 推論専用 | 推論専用 | 両方（推論強、学習はAutoTrain/DGX Cloud経由） | 両方（汎用VM、学習・推論とも手動セットアップ） |
| 開発者体験 | 良（Trussフレームワーク、Python-native） | 良（シンプルなAPI、豊富なモデル） | 最優秀（OSSエコシステムの中心、コミュニティ最大） | 中（シンプルだが ML特化機能なし） |
| ベンダーロックイン | 中（Trussフレームワーク依存） | 中（Cog/Replicate API依存） | 低（OSSベース、モデル/データのポータビリティ高） | 最低（標準VM、Docker対応） |
| AIXSとの競合度合い | 低（推論特化、R&Dライフサイクル外） | 低（推論特化、エンタープライズ弱） | 中（エコシステム統合先として重要、推論で部分的競合） | 低（汎用インフラ、MLプラットフォーム機能なし） |

**総評:** 4社ともR&D統合プラットフォームとしてはAIXSと直接競合しない。Baseten/Replicateは推論に特化しており、学習・実験管理機能を持たない。Hugging Faceはエコシステムとしての影響力が最大だが、コンピュートはGCP/AWS経由であり価格面で不利。Paperspace/DigitalOceanは汎用VMでML特化機能がなく、AIXSの統合R&D体験で明確に差別化可能。

### 2.5 解釈・示唆

#### 最安帯はどこか

- **オンデマンド最安:** RunPod Community Cloud (H100 PCIe $1.99/hr、L40S $0.79/hr、A100 80GB $1.19/hr)
- **Spot最安:** RunPod Spot (H100 $1.35/hr、A100 $0.60/hr、L40S $0.40/hr)
- **予約最安:** RunPod 1年 (H100 PCIe $2.03/hr)、CoreWeave 60%OFF (~$2.46/hr H100)、Together AI 4-6ヶ月 ($2.25/hr H100)
- **公的基盤最安:** ABCI 3.0 開発加速利用 (H200 1-GPU ~$2.20/hr)、mdx (A100 ¥50/hr = $0.33/hr)
- **日本国内最安:** GPUSOROBAN A100 80GB ¥398/hr ($2.65/hr)

#### 高機能帯はどこか

- **開発者体験最高:** Modal (Python-native、サーバーレス、サブ秒コールドスタート)
- **推論最適化最高:** Together AI (FlashAttention、200+モデル)、Baseten (<10sコールドスタート)
- **大規模学習最高:** CoreWeave (100K+ GPU、InfiniBand 3200Gbps)
- **エコシステム最高:** Hugging Face (500K+モデル)、AWS (143+認定、最大マーケットプレイス)
- **エンタープライズ最強:** Azure (AD/Office 365統合)、AWS (EDP)

#### AIXSはどの価格帯・価値帯で戦うべきか

| GPU | ハイパースケーラー範囲 | GPU特化範囲 | AIXSターゲット価格 | 根拠 |
|---|---|---|---|---|
| H100 SXM | $3.85-$12.29 | $1.99-$6.16 | $3.00-$4.50 | AWS値下げ後に匹敵〜やや安。RunPodには勝てないがプラットフォーム価値で正当化 |
| H200 | $5.93-$13.78 | $3.44-$6.31 | $4.50-$6.00 | 全ハイパースケーラーを下回る。DO/RunPodに近い |
| A100 80GB | $3.43-$6.25 | $1.19-$2.79 | $2.50-$3.50 | AWSに競合的。RunPod/GPUSOROBANの価格帯は不可 |
| L40S | $1.86-$3.82 | $0.79-$2.25 | $1.20-$2.00 | 推論・中規模実験用で競合的 |

#### 価格勝負が危険な相手

1. **RunPod** -- ハードウェア所有のCommunity Cloudモデルで極低価格。$1.99/hr H100に勝つのは不可能
2. **GPUSOROBAN** -- 閉鎖校舎の再利用・核地域補助金等で異次元のコスト構造。A100 $2.65/hrは日本最安
3. **ABCI 3.0** -- 政府補助金による価格。商業プロバイダでは対抗不可
4. **Lambda 1-Click Clusters** -- $2.76/hr大規模クラスターは極めて競合的

#### 体験・統合価値で勝ちやすい相手

1. **Lambda Labs** -- SSH＋JupyterLabのみ。実験管理・ジョブオーケストレーション・モデル管理が皆無。AIXSの統合R&Dプラットフォームが明確な差別化
2. **RunPod** -- Docker/サーバーレスだが汎用的。R&D特化ワークフロー（実験追跡、HP最適化、結果比較）で差別化可能
3. **CoreWeave** -- K8s専門知識が前提。DevOps不在のR&Dチームにはハードルが高い
4. **日本国内全プロバイダ** -- MLプラットフォーム機能ゼロ。最も差別化しやすい
5. **Azure** -- エンタープライズ複雑性。研究者向けではない。5分最低課金は反開発者的

---

## 3. 市場調査

### 3.1 対象地域一覧

| # | 地域 | 調査深度 | データソース |
|---|---|---|---|
| 1 | 米国 (US) | 高（競合分析で包含） | ハイパースケーラー・GPU特化プロバイダー分析 |
| 2 | カナダ (Canada) | 中（US市場に準拠） | 競合分析から推定 |
| 3 | EU（独・仏・他） | 高 | EU_UK_GPU_Market_Research_2026.md |
| 4 | 英国 (UK) | 高 | EU_UK_GPU_Market_Research_2026.md |
| 5 | 中国 (China) | 高 | GPU_Market_Research_Asia_2025.md |
| 6 | 日本 (Japan) | 最高 | Japan_GPU_AI_Market_Research_2026.md |
| 7 | 韓国 (South Korea) | 高 | GPU_Market_Research_Asia_2025.md |
| 8 | 台湾 (Taiwan) | 高 | GPU_Market_Research_Asia_2025.md |
| 9 | UAE | 高 | AIXS_Emerging_Market_Research_2026.md |
| 10 | サウジアラビア (Saudi Arabia) | 高 | AIXS_Emerging_Market_Research_2026.md |
| 11 | インド (India) | 高 | AIXS_Emerging_Market_Research_2026.md |
| 12 | シンガポール (Singapore) | 高 | AIXS_Emerging_Market_Research_2026.md |
| 13 | イスラエル (Israel) | 高 | AIXS_Emerging_Market_Research_2026.md |
| 14 | マレーシア (Malaysia) | 中 | AIXS_Emerging_Market_Research_2026.md |
| 15 | インドネシア (Indonesia) | 中 | AIXS_Emerging_Market_Research_2026.md |

### 3.2 地域別サマリー表

| 地域 | GPU利用で多い経路 | 主な資金源 | 政府施策/共有基盤 | 地域独自の仕組み | 代表例 | AIXSへの示唆 | 出典 | 調査日 |
|---|---|---|---|---|---|---|---|---|
| US/Canada | ハイパースケーラー＋ネオクラウド | VC（世界の61%）、企業R&D | DOE HPC、NSF | VCクレジットが最大の入口 | AWS, CoreWeave, Lambda, RunPod, Modal | 最も成熟した市場。価格・体験ともに激戦 | 競合分析各社ページ | 2025-03 |
| EU | ハイパースケーラー(70%市場占有)＋EuroHPC | Horizon Europe (~EUR 2B AI)、ERC、国家資金 | EuroHPC AI Factories (19か所)、InvestAI (EUR 200B) | AI Factory無料アクセス(SME/スタートアップ向け50K GPU-hr) | JUPITER, LUMI, Nscale, Scaleway | ソブリンAI需要大。GDPR/AI Act対応必須。EU拠点必要 | EU/UK Market Research | 2026-03 |
| UK | ハイパースケーラー＋AIRR公的基盤 | UKRI(£1B+)、VC(£1.8B H1 2025) | Isambard-AI (5,448 GH200)、Dawn | AIRR無料アクセス(2M GPU-hr) | Isambard-AI, Nscale, CoreWeave UK | EU規制なし。ソブリンAI基金£500M。参入しやすい | EU/UK Market Research | 2026-03 |
| 中国 | 国内クラウド(Alibaba 35.8%)＋智算中心 | 国家基金(RMB 1T+)、企業R&D($70B+)、算力券 | 东数西算(8ハブ)、算力券(30+都市) | 算力券(最大80%補助)、国産GPU義務化 | Alibaba Cloud, Huawei Ascend, ABCI相当の智算中心 | 輸出規制下で直接参入困難。国産GPU対応が必要 | Asia Market Research | 2025-03 |
| 日本 | ハイパースケーラー＋国内クラウド＋ABCI | METI(¥1,146B+)、科研費(¥237.9B/yr)、企業R&D(¥23T) | ABCI 3.0 (6,128 H200)、GENIAC、METI Cloud Program | GENIAC補助金(2/3補助)、ISMAP認定、さくら高火力 | さくら、GPUSOROBAN、ABCI、GMO | 国内プロバイダにMLプラットフォーム皆無。最大の参入機会 | Japan Market Research | 2026-03 |
| 韓国 | 国内クラウド(NHN/Naver/Kakao)＋財閥GPU工場 | KRW 10.1T($7.3B) 2026 AI予算、KRW 150T成長基金 | NACC(1 EFLOP)、KISTI HANGANG(8,496 GPU) | 260,000+ NVIDIA GPU確約、財閥主導 | Samsung, SK Group, KISTI | 政府調達パスが明確。K-Moonshotエコシステム | Asia Market Research | 2025-03 |
| 台湾 | TWCC(NCHC)＋Foxconn私設 | NT$190B($5.9B) 4年計画、NT$10B AIスタートアップ基金 | NCHC(1,700+ GPU)、TWCC | Taiwan Compute Alliance、Southern Silicon Valley | TWCC, Foxconn Visionbay.ai | 製造拠点だが国内コンピュート構築中。NSTCとの連携 | Asia Market Research | 2025-03 |
| UAE | ソブリンクラウド(Core42)＋ハイパースケーラー | SWF(MGX $100B基金、Mubadala $12.9B) | Core42、Stargate UAE(1GW) | SWF主導の巨額投資、US輸出許可(35K GB300) | Core42, Stargate UAE, MBZUAI | SWF買い手。政府関係構築必須 | Emerging Market Research | 2026-03 |
| サウジアラビア | HUMAIN(PIF)＋ハイパースケーラー | Project Transcendence($100B)、PIF($36.2B) | HUMAIN、KAUST Shaheen III(2,800 GH200) | 「AIの年」2026宣言、マルチベンダー戦略 | HUMAIN, KAUST, SDAIA | PIF/HUMAIN経由が必須。マルチベンダーGPUオーケストレーション需要 | Emerging Market Research | 2026-03 |
| インド | IndiaAI公的基盤＋民間GPUクラウド | IndiaAI(Rs 10,372 crore/$1.25B)、AWS($12.7B)、MS($3B) | IndiaAI(34,000+ GPU)、PARAM、C-DAC | 40%補助金割引、政府認定プロバイダ制度 | Yotta, E2E Networks, Jio | 価格感度極めて高い。コスト最適化が訴求点 | Emerging Market Research | 2026-03 |
| シンガポール | NSCC＋ハイパースケーラー(供給制約下) | RIE2030(S$37B)、NAIS 2.0(S$1B+) | NSCC ASPIRE 2A+(20 PFLOPS)、DC-CFA規制 | DC容量割当規制(PUE 1.25/50%グリーン)、ASEANハブ | NSCC, Oracle(131K Blackwell) | 供給制約でプレミアム価格。効率最適化が価値 | Emerging Market Research | 2026-03 |
| イスラエル | スタートアップ＋Innovation Authority＋NVIDIA | VC($15.6B総額、$7.9B AI)、Innovation Authority($45M) | 国家AIスパコン(4,000 B200、Nebius運営) | NVIDIA R&D拠点(5,000人)、防衛AI需要 | 342 GenAIスタートアップ、Run:ai(NVIDIA買収) | スタートアップ向けスケーリング。防衛グレードコンプライアンス | Emerging Market Research | 2026-03 |
| マレーシア | ハイパースケーラー(SG溢出) | RM 2B(~$490M)ソブリンAIクラウド | NAIO(国家AIオフィス) | SGの容量制約から溢出。Johor DCコリドー | Oracle($6.5B)、NVIDIA(600MW) | 高成長。Johorリージョンでの展開 | Emerging Market Research | 2026-03 |
| インドネシア | ソブリンAIクラウド(初期段階) | 中規模（政府＋通信会社） | AI Center of Excellence(NVIDIA/Cisco/Indosat) | Bahasa Indonesian LLM需要、Sahabat-AI | Indosat AI Factory(GB200 NVL72) | 大人口基盤。ソブリンAI需要。初期段階 | Emerging Market Research | 2026-03 |

### 3.3 地域別詳細表

| 地域 | クラウド利用比重 | 大学GPU比重 | 公的計算基盤比重 | スタートアップクレジット利用 | 企業オンプレ比重 | 主な資金源 | 主な制度 | 政府提供資源 | 補助金/バウチャー | 主な制約 | AIXS機会 | 出典 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US/Canada | 非常に高 | 中 | 低(DOE等) | 非常に高(AWS/GCP/Azure credits) | 高(Big Tech) | VC、企業R&D | NIH/NSF grants | DOE HPC | AWS Activate $100K, GCP $200K | 競争激化、価格下落 | 体験差別化、R&D統合 | 各社HP |
| EU | 非常に高(70% US provider) | 中(PRACE Tier-2) | 高(EuroHPC) | 中(OVH EUR10K, HPC無料) | 中(自動車/製薬) | Horizon Europe, ERC, 国家資金 | AI Act, CADA, GDPR | EuroHPC 57K accelerators | AI Factory 50K GPU-hr無料 | ソブリン要件、申請3-6ヶ月、SW断片化 | ソブリンAI対応、EU拠点 | EU/UK Research |
| UK | 非常に高 | 中-高(Bristol/Cambridge) | 中(AIRR) | 中 | 中 | UKRI £1B+, VC | AIRR、Data Protection Act | Isambard-AI + Dawn | Innovator 50-150K GPU-hr | EU離脱後規制は軽いがEuroHPC参加制限 | 規制軽い参入しやすい市場 | EU/UK Research |
| 中国 | 高(国内クラウド) | 中 | 高(智算中心30+都市) | 低(国際クレジット不可) | 非常に高(Big Tech GPU備蓄) | 国家基金、算力券、企業capex | 東数西算、国産GPU義務 | 788 EFLOPS(FP16) 智算中心 | 算力券 10-80%補助 | 輸出規制、GPU稼働率30%、CUDA互換性 | 算力券最適化、遊休GPU仲介 | Asia Research |
| 日本 | 高(ハイパースケーラー) | 中(8大学拠点) | 高(ABCI) | 中(ハイパースケーラーcredits) | 中-高(大企業DGX) | METI、科研費、企業R&D ¥23T | GENIAC、Cloud Program、AI推進法 | ABCI 6,128 H200; mdx 320 A100 | GENIAC 2/3補助; ABCI開発加速 | GPU過剰供給懸念、日本語データ不足 | MLプラットフォーム空白地帯 | Japan Research |
| 韓国 | 中-高 | 中 | 高(NACC/KISTI) | 中(NVIDIA Inception) | 非常に高(財閥) | KRW 10.1T AI予算、KRW 150T成長基金 | AI基本法、K-Moonshot | NACC 1 EFLOP; KISTI 8,496 GPU | 政府がGPU調達して提供 | NVIDIA依存度高、国産GPU無し | NACC/KISTI連携、161社K-Moonshot | Asia Research |
| 台湾 | 中 | 中 | 高(NCHC/TWCC) | 低-中 | 高(Foxconn) | NT$190B 4年計画、Foxconn NT$42B | 10 AI Infrastructure、AI基本法 | NCHC 1,700+ GPU | TWCC研究者向け | エネルギー供給制約 | TWCC統合、Foxconn連携 | Asia Research |
| UAE | 低-中(Core42主導) | 低(MBZUAI) | 中(Core42) | 低 | 中(G42/Core42) | SWF $100B+、Microsoft $15.2B | National AI Strategy 2031 | Core42、Stargate UAE | 低（SWF資金で直接調達） | 輸出規制、G42支配、政府関係必要 | SWF買い手、ソブリンGPU最適化 | Emerging Research |
| サウジ | 低(HUMAIN主導) | 低-中(KAUST) | 中(HUMAIN) | 低 | 低 | PIF $36.2B、Project Transcendence $100B | Vision 2030、Year of AI 2026 | KAUST 2,800 GH200; HUMAIN 18K GB300 | 低（国家直接投資） | PIF/HUMAIN gatekeeping | マルチベンダーGPUオーケストレーション | Emerging Research |
| インド | 中(成長中) | 中 | 高(IndiaAI) | 中 | 中(Reliance/Tata) | IndiaAI $1.25B、AWS $12.7B | IndiaAI Mission、Digital India | 34,000+ GPU(政府管理) | 40%補助金割引 | 価格感度、調達遅延 | コスト最適化、認定プロバイダ連携 | Emerging Research |
| シンガポール | 非常に高(供給制約) | 低 | 中(NSCC) | 中(AI Singapore) | 中 | RIE2030 S$37B | NAIS 2.0、DC-CFA規制 | ASPIRE 2A+ 20 PFLOPS | AI Singapore program | DC容量規制、高コスト | プレミアム効率最適化、ASEANハブ | Emerging Research |
| イスラエル | 高 | 中(Technion等) | 低(国家スパコン新設) | 高(Innovation Authority) | 低(スタートアップ中心) | VC $15.6B、防衛$1B+ | Telem Program | 4,000 B200(Nebius運営) | Innovation Authority GPU配布 | 小市場、防衛クリアランス | スタートアップスケーリング、防衛AI | Emerging Research |
| マレーシア | 高(SGオーバーフロー) | 低 | 低(NAIO新設) | 低 | 低 | RM 2B ソブリンクラウド | NAIO、DC Incentives | 限定的(構築中) | 政府インセンティブ | 初期段階、人材不足 | Johorリージョン、SGオーバーフロー | Emerging Research |
| インドネシア | 低-中 | 低 | 低(構築中) | 低 | 低(通信会社) | 中規模（政府＋Indosat） | National AI Roadmap 2026 | AI Center of Excellence | 限定的 | 初期段階、再輸出懸念 | ソブリンAI需要、大人口 | Emerging Research |

### 3.4 地域別深掘りメモ

#### 3.4.1 米国・カナダ

**GPUの利用パターン:** 世界最大かつ最も成熟した GPU コンピュート市場。ハイパースケーラー（AWS 30%、Azure 20%、GCP 13%）がベースだが、ネオクラウド（CoreWeave, Lambda, RunPod, Modal）が急成長し、H100 価格を 18 か月で $8+ から $2.50-6.00 へ押し下げた[GPT-5.4-pro補足, 2026-03-28]。大手テック企業は自社 GPU クラスターを保有（Meta: 350,000+ H100（2025年末導入目標として発表、2026年3月時点での実績値は未公表）[GPT-5.4-pro補足, 2026-03-28]）。米国は世界最多の約4,049データセンターを擁する（2024年時点、Fed Reserve調査）。

**資金源:** 2025年には米国がAI VC投資の約75%（$194B）を占め、Q2 2025にはグローバルで6件あった$1B+超大型AIディールのすべてが米国発。スタートアップクレジット（AWS Activate $100K、GCP $200K）が初期アクセスの主要経路。企業 R&D 予算は世界最大。

**政府・制度:** DOE の国立研究所 HPC、NSF グラント。NAIRR（National AI Research Resource）が2026年に2周年を迎え、14連邦機関・28民間パートナーと連携。トランプ政権下でPax Silica投資ファンド（$4T目標、初期$250M）をエネルギー・鉱物・半導体サプライチェーン強化に立ち上げ。輸出規制の策定者側。

**AIXSの売り方:** 競争が最も激しい市場。価格では勝てないため、統合 R&D プラットフォームとしての価値（実験管理、マルチクラウドオーケストレーション、コスト追跡）で差別化。Modal が最大の直接競合。

#### 3.4.2 EU（ドイツ、フランス他）

**GPUの利用パターン:** 米国3大ハイパースケーラーが EU クラウドインフラ市場の約 70% を占有。欧州プロバイダのシェアは約 15% のみ。EuroHPC が 57,000 アクセラレータを運用（JUPITER: 24,000 GH200、LUMI: 10,240 MI250X、Leonardo: 13,824 A100 等）。19 の AI Factory が段階的に展開中。ネオクラウド（Nscale: $2B Series C、Scaleway、OVHcloud）が急成長。

**資金源:** Horizon Europe（AI トピック ~EUR 2B）、ERC（~EUR 2.7B）、Digital Europe Programme、InvestAI（EUR 200B 目標、最大5つの AI Gigafactory に各 ~100,000 GPU、EUR 20B特別配分）。フランスは EUR 109B の AI 投資パッケージ。ドイツは EUR 5.5B の技術イニシアティブ。EU全体でAI VC投資は$15.8B（2025年、世界の6%）にとどまり、年間 EUR 270B の投資ギャップがある。EU域内のデータセンター数は約2,250（2024年）。

**政府・制度:** EU AI Act（高リスク AI に EU 内データ・コンプライアンス義務）、CADA（EU クラウドプロバイダ適格要件）、GDPR、SecNumCloud（仏）、C5（独）。「ソブリンティウォッシング」が課題（US CLOUD Act との矛盾）。

**AIXSの売り方:** 「Sovereign by design」--EU 拠点、US CLOUD Act 免除、GDPR ネイティブ。AI Act 対応（監査証跡、データリネージ）。ネオクラウド価格（ハイパースケーラーの 40-85% OFF）で提供。EuroHPC Federation Platform との統合が戦略的。

#### 3.4.3 英国 (UK)

**GPUの利用パターン:** ポスト Brexit で EU AI Act の適用外。AIRR プログラム（Isambard-AI: 5,448 GH200、Dawn: 1,024 Intel GPU）で研究者・スタートアップに無料 GPU アクセス（2M GPU-hr プール）。Nscale が $2B 調達、$14.6B 評価額。CoreWeave が $3.4B UK 投資。

**資金源:** UKRI £1B+ 追加投資（2030 年までにコンピュート 20 倍）、£500M Sovereign AI Fund（2026年4月開始）、£500M Sovereign AI Unit。UK AI スタートアップは H1 2025 に £1.8B 調達。

**政府・制度:** EU よりプロイノベーション。軽量規制。EuroHPC AI Factory Antenna パートナーとして限定参加。

**AIXSの売り方:** 「Built for British AI」--AIRR 互換、UK データレジデンシー。EU 規制の重荷なしで参入しやすい。UK-EU ハイブリッドワークフロー対応。

#### 3.4.4 中国

**GPUの利用パターン:** Alibaba Cloud が AI クラウド市場 ~38% シェア（2025年末時点で35.8%から増加）[GPT-5.4-pro補足, 2026-03-28]。Huawei Cloud 13.1%、ByteDance Volcano Engine 14.8%。AI クラウド市場は H1 2025 に 55% 成長し $2.7B。しかし GPU 稼働率はわずか 30%--500+ の新データセンタープロジェクトの多くが遊休。H100 レンタル価格は $8/hr（2023年）から <$2/hr（2024年）へ 70% 暴落。30+ 都市が智算中心を建設中（788 EFLOPS、FP16）。

大手企業の GPU 備蓄は巨大: Alibaba $52.9B/3年、ByteDance $20B、Tencent capex 149% YoY 増。DeepSeek は 50,000 Hopper + 10,000 A100 を保有。

**資金源:** 国家基金 RMB 1T ($138B, 20年)、AI 産業投資基金 RMB 60B ($8.2B)、Big Fund III $47B（半導体）。2025年のAI関連投資は最大$98Bに達する見込み（前年比48%増）。30+ 都市の算力券（上海 RMB 600M 最大80%補助、深圳 RMB 500M 50-60%補助、浙江省では最大$1.1Mの大型バウチャーも）。VC/スタートアップ AI 投資 $13.9B（2025年、世界の5%）。データセンター数は約379（2024年）。AI市場規模は$61B超（2025年予測）。

**政府・制度:** 2025年政策で政府支援データセンターは国産チップのみ使用義務。Huawei Ascend 910C が de facto 標準（H100 推論性能の約 60%）。Cambricon、Moore Threads、MetaX が台頭。Biren Technology（壁仞科技）がBR20Xシリーズの商業化を2026年に予定し、2026年1月に香港取引所に上場。天数智芯（Tianshu Zhixin）も2026年1月に香港上場し、NVIDIAのBlackwellアーキテクチャを超える性能を目標に開発中[GPT-5.4-pro補足, 2026-03-28]。US 輸出規制により H100/A100 は入手不可、H20 は一時停止後再開。東南アジア経由のクラウドアクセスという抜け穴あり。

**AIXSの売り方:** 直接参入は輸出規制リスクが高い。参入する場合は国産 GPU（Ascend, Cambricon）対応必須。算力券最適化プラットフォームと遊休 GPU 仲介（30% 稼働率問題の解決）に機会。ただし大手テック企業は自社ソリューション保有のため顧客にはなりにくい。

#### 3.4.5 日本

**GPUの利用パターン:** ハイパースケーラー（AWS $15.2B、Azure $2.9B、GCP $730M+ の日本投資）がクラウドの ~60% シェア（2025年末時点で55.82%から増加傾向）[GPT-5.4-pro補足, 2026-03-28]。国内プロバイダが政府の経済安全保障推進法で戦略的優先に。METI が ¥1,146B+ を国内 6+ 社に補助（さくら ¥501B、ソフトバンク ¥421B、KDDI ¥102.4B、ハイレゾ ¥77B、GMO ¥19.3B）。

研究者のアクセスパターン: 大学研究者は ABCI/大学クラスター/mdx を一次利用、クラウドをバックアップ。スタートアップは GENIAC 補助金 → ハイパースケーラークレジット → 国内クラウドの順。大企業はオンプレ DGX → プライベートクラウド。

**資金源:** METI はFY2026にAI・半導体予算を¥1.23T（$7.9B）に4倍増。METI Cloud Program ¥1,146B+、GENIAC ~¥33.9B（3フェーズ30+プロジェクト）。さくらインターネットに¥50.1B（10,800 GPU展開）、KDDIに¥10.2B を直接補助。科研費 ¥237.9B/年、JST AIP ¥7.5B、National AI Basic Plan ¥1T/5年。企業R&D ¥23T（FY2024過去最高）。VC では Sakana AI ¥38.3B（Series A）、ハイレゾ ¥23.09B。ソフトバンクが世界初のB200 DGX SuperPOD（10,000+ GPU）を建設中。国内データセンター数は約219（2024年）。

**政府・制度:** AI 推進法（2025年5月施行、罰則なしのイノベーション優先）。著作権法30条の4（AI学習での著作物利用許可）。ISMAP 認定が政府クラウド調達に必須。ABCI 3.0 は 6,128 H200（6.22 EFLOPS）で国内最大。mdx は A100 ¥50/hr で極めて安価。

**AIXSの売り方:** 日本は AIXS にとって最も参入しやすい市場。全国内プロバイダが「インフラのみ」で ML プラットフォーム機能（ノートブック＋学習＋推論＋実験管理）を提供していない。メッセージ: (1) データ主権、(2) コスト効率（GPU 過剰供給下での稼働率最適化）、(3) 研究成果加速、(4) 公的資金の有効活用、(5) ABCI/さくら/ハイパースケーラーとの統合。ABCI ユーザー（3,000人、566グループ）が商用グレードサービスを必要とする際の自然な移行先。ISMAP 認定取得は政府セクター参入に必須。

#### 3.4.6 韓国

**GPUの利用パターン:** 政府が主導的に GPU インフラを構築。National AI Computing Center（1 EFLOP、51% 公的/49% 民間、2027年本格運用）と KISTI 第6世代スパコン HANGANG（8,496 GPU、~600 PFLOPS）。財閥が巨大 AI ファクトリーを建設（Samsung 50,000+ GPU、SK Group 50,000+ GPU、Hyundai AI Factory）。合計 260,000+ NVIDIA GPU が確約。NHN Cloud、Naver Cloud、Kakao が政府 GPU 調達を受注（B200 10,080 + H200 3,056）。SK Telecom が GPUaaS を 2025年1月開始。

**資金源:** 2026年 AI 予算 KRW 10.1T ($7.3B)--2025年の 3.3T から 206% 増。KRW 150T ($100B) 成長基金。ソブリン AI 開発 $381M（5コンソーシアム競争、2027年に2社に絞込み）。NRF/IITP グラント、NVIDIA Inception プログラム。OpenAI Stargate パートナーシップ（全羅南道 3GW、$35B、最大 200,000 GPU）。韓国AI市場は$9B規模（2025年予測）、270データセンター（2024年）。AI VC投資は$9B（2013-2024年累計）。AI医療5カ年ロードマップ（2023-2028年）も推進中。

**政府・制度:** AI 基本法。K-Moonshot プログラム（161社パートナー、Samsung/SK/Hyundai/Naver/LG）。KAIST が 2026年にスタンドアロン AI 学部（300人/年）設立。

**AIXSの売り方:** National AI Computing Center のアクセスレイヤーとして統合。SKT GPUaaS との連携。K-Moonshot の 161 社エコシステムへのリーチ。KISTI HANGANG との統合。「ソブリン AI 開発を加速」のメッセージ。

#### 3.4.7 台湾

**GPUの利用パターン:** TSMC が先端ノード GPU ダイの 80%+ を製造し、台湾 ODM が NVIDIA GPU サーバー出荷の 70%+ を担うが、国内コンピュート基盤は発展途上。TWCC（NCHC + ASUS + Quanta + 台湾モバイル）が主要プラットフォーム。NCHC が 1,700+ GPU（H200 + GB200 NVL72 + HGX B300）にアップグレード中。Foxconn が 10,000 Blackwell GPU の AI ファクトリー（$1.37B）と Visionbay.ai ソブリン AI スパコンを建設中。

**資金源:** NT$190B ($5.9B) 4年計画。NT$31.1B ($1B) の 2026年 10 AI Infrastructure Initiatives。NT$10B ($313M) AI スタートアップ基金（MODA、10年）。Foxconn NT$42B ($1.37B)。

**政府・制度:** AI 基本法（2025年12月通過、2026年1月公布）。Southern Silicon Valley Project（嘉義・台南・屏東・高雄）。Taiwan Compute Alliance（NCHC, Foxconn, Wistron, AMD, NVIDIA）。ソブリン AI 目標: 公的部門 480 PFLOPS、総計 1.2 EXAFLOPS（2029年）。

**AIXSの売り方:** TWCC 上の付加価値レイヤー。Foxconn Visionbay.ai との連携。Taiwan Compute Alliance への参加。「チップ製造大国から AI コンピューティング大国へ」のナラティブ支援。エネルギー供給制約による効率最適化需要。

#### 3.4.8 UAE

**GPUの利用パターン:** Core42（G42子会社）がソブリンAIクラウドを運営。GITEX 2025で H100 GPU のセルフサービスプラットフォーム発表。Microsoft-G42 パートナーシップで $15.2B 投資（2023-2029）。Stargate UAE は 1GW AI コンピュートクラスター（G42/OpenAI/Oracle/NVIDIA/SoftBank/Cisco、初期 200MW は 2026年稼働、フルキャンパス 5GW）。MBZUAI が K2 Think V2（70B パラメータ、完全オープン）を開発。

**資金源:** MGX（Mubadala + G42）$100B 基金。Mubadala は 2025年に $12.9B を AI/デジタル化に投資。湾岸 SWF は 2025年に全世界で $126B（全ソブリン資本の 43%、過去最高）。

**政府・制度:** National AI Strategy 2031。Abu Dhabi Government Digital Strategy 2025-2027（100%ソブリンクラウド目標）。US 輸出許可: 35,000 GB300（2025年11月）。年間 500,000 チップ枠を交渉中。

**AIXSの売り方:** Core42 + ハイパースケーラー間のマルチクラウド GPU オーケストレーション。ソブリンコンピュート最適化。US 輸出規制下での調達コンプライアンス。SWF 買い手は予算豊富だが政府関係構築が不可欠。

#### 3.4.9 サウジアラビア

**GPUの利用パターン:** HUMAIN（PIF 子会社）がフルスタック AI 企業として AI ファクトリーを建設。Phase 1: 18,000 GB300 GPU。5年で数十万 GPU 目標。1.9GW（2030年）→6.6GW（2034年）の容量目標で世界第3位のAIハブを目指す。NVIDIA 500MW + AMD 500MW + Qualcomm 200MW のマルチベンダー戦略。HUMAINのソブリンAIプラットフォームはアラビア語LLM（JAIS, Fanar）とデータインフラに注力、$135.2BのGDP押上効果を見込む（2030年）。KAUST Shaheen III（2,800 GH200、中東 #1、世界 #18）。SDAIA が 500+ H100 を政府 AI 向けに調達。

**資金源:** Project Transcendence $100B。PIF は 2025年に $36.2B を展開（世界最大の単一ソブリンディールメーカー、AUM ~$930B）。Google $5-10B、AMD $10B/5年。

**政府・制度:** 2026年を「AIの年」に宣言。Vision 2030 の 96 戦略目標中 66 がデータ駆動能力に関連。1M+ 国民を AI/データスキル訓練。

**AIXSの売り方:** NVIDIA + AMD + Qualcomm のマルチベンダー GPU オーケストレーション。Vision 2030 アラインメント。アラビア語 AI コンピュート最適化。ただし PIF/HUMAIN による gatekeeping が参入障壁。

#### 3.4.10 インド

**GPUの利用パターン:** IndiaAI Mission により 38,000+ GPU を政府管理下に確保（H100 12,896、H200 1,480、MI200/300 7,200）、2026年末までに100,000 GPUを目標。当初目標 10,000 GPU を大幅超過。政府補助によりGPU-hour単価をRs 115-150（$1.40-$1.80）に抑制し、世界最安水準のAIコンピュートを実現。スタートアップ・研究者に 42% 割引で提供。インドのAIセクターは2024年に$8Bに達し、2027年に$17B予測。152データセンター（2024年）。民間: Yotta 32,768 GPU、E2E Networks、Tata Communications。Reliance Jio が 1GW AI DC（Blackwell）を建設中。PARAM シリーズ（C-DAC）が国立スパコン基盤。クラウド GPU 市場は 36.5% CAGR で $80M（2023）→ $1.32B（2032）。

**資金源:** IndiaAI Mission Rs 10,372 crore ($1.25B/5年)、2025-26年度予算で AI 4倍増。AWS $12.7B、Microsoft $3B。NVIDIA India Deep Tech Alliance $2B。AI スタートアップ VC $643M（2025年、全スタートアップ取引の 30-40%）。

**政府・制度:** IndiaAI Compute Capacity Program（認定プロバイダ制度: Yotta, NextGen, E2E Networks, Jio）。C-DAC + AMD パートナーシップ。州レベル競争（Maharashtra, Gujarat, Karnataka）。

**AIXSの売り方:** 価格感度が極めて高い市場。コスト最適化プラットフォームとして訴求。認定プロバイダ（Yotta, E2E, Jio）との連携によるマルチクラウド GPU 集約。補助金コンピュートと商用コンピュートの橋渡し。NVIDIA + AMD 混合環境の統合。

#### 3.4.11 シンガポール

**GPUの利用パターン:** NSCC ASPIRE 2A+（20 PFLOPS、H100）が国家スパコン。70+ DC、1.4GW 容量だが空室率 1.4%（APAC 最低）。DC-CFA 規制で新規容量は政府割当制（DC-CFA2: 200MW、PUE 1.25・50%グリーンエネルギー要件）。Oracle が $6.5B（最大 131,072 Blackwell GPU）。Jurong Island に 700MW 低炭素 DC パーク計画。輸出規制の影響なく、高性能 NVIDIA GPU にフルアクセス可能 → ASEAN + 中国隣接コンピュートのリージョナルハブ。

**資金源:** RIE2030 S$37B（前回比 32% 増）。NAIS 2.0 S$1B（5年間: 2025-2030）。テック大手投資 $26B+ 合計。AI スタートアップ累計 S$8.4B（ASEAN 取引量の 58%）。人口600万人未満ながらNVIDIA全球売上の15%を占め、一人当たり$600をNVIDIAチップに支出（世界最高水準）。

**政府・制度:** Smart Nation Initiative。DC モラトリアム（2019年〜）による容量規制。IMDA AI ガバナンスフレームワーク（2026年1月にエージェンティック AI 対応版）。

**AIXSの売り方:** 供給制約＝プレミアム価格。コンピュート効率最大化が最大の価値。サステナビリティ対応 GPU ワークロード管理。ASEAN ワークロードルーティング（SG → マレーシア/インドネシアのオーバーフロー管理）。

#### 3.4.12 イスラエル

**GPUの利用パターン:** スタートアップ駆動。342 GenAI スタートアップ（累計 $20B+）。国家 AI スパコンは Nebius が運営（4,000 B200、$140M、政府 $45M）。70% を企業、30% を学術研究に割当。Innovation Authority が 1,000 B200 GPU を割引配布。NVIDIA はイスラエルに 5,000 人（Mellanox HQ 3,000 人）、Rubin プラットフォームの 4 つの主要ネットワーキングコンポーネントをイスラエルで開発。防衛 AI が独自セグメント（2025年 $1B+、130+ スタートアップが軍事統合）。

**資金源:** スタートアップ総額 $15.6B（2025年）、AI $7.9B（61% 成長）。防衛 AI $1B+（過去全年度合計を超過）。Innovation Authority $45M。

**政府・制度:** Telem Program（国家 AI R&D インフラ）。MAFAT AI・自律研究ユニット（2025年1月）。ただし国家 AI プログラム全体は予算の 1/5 しか執行されておらず停滞中。

**AIXSの売り方:** スタートアップ向け GPU スケーリング（Innovation Authority 補助 GPU → 商用コンピュートへの移行）。防衛グレードのセキュリティ・コンプライアンス。NVIDIA エコシステム統合。ただし国内市場規模は小さい。

### 3.4.13 個人研究者・開発者のGPU利用パターン（地域横断）

個人研究者、フリーランス、学生、趣味利用者のGPUアクセスは各地域で大きく異なる。以下に主要地域での個人利用パターンを整理する。

| 地域 | 主要な個人利用GPU手段 | 備考 |
|---|---|---|
| US/Canada | Google Colab（無料T4/有料A100）、Kaggle（無料T4/P100、週30h制限）、RunPod/Vast.ai個人アカウント（クレジットカード即時利用、$1-3/hr H100）、AWS/GCP個人無料枠 | Colabが最も広く利用される。Vast.aiはP2Pで最安級だが信頼性変動 |
| 日本 | Google Colab（最も普及）、ABCI個人カテゴリ（個人研究者も申請可能、要審査）、mdx（大学研究者向け A100 ¥50/hr）、RunPod/Vast.ai（日本語ドキュメント不足が障壁） | ABCI 3.0は個人研究者も「ABCI利用者」として申請可能（日本の研究機関所属が条件）。Colabが事実上の標準 |
| EU | Google Colab、EuroHPC SMEアクセス（中小企業・個人研究者向け無料GPU時間、申請制）、Kaggle、OVHcloud/Scaleway個人プラン | EuroHPC AI Factoryが2026年からSME/スタートアップ向けに50K GPU-hr無料提供開始。個人研究者は所属機関経由でアクセス |
| UK | Google Colab、AIRR（大学所属研究者向け）、Kaggle | AIRR 2M GPU-hrプールへは大学所属研究者としてアクセス可能 |
| 中国 | Alibaba PAI個人ティア（フリーティアあり）、Baidu AI Studio（無料GPU枠）、算力券の個人利用可否は都市により異なる（一部都市では個人開発者も対象） | 国際プラットフォーム（Colab等）はアクセス制限あり。国内サービスが主要手段 |
| 韓国 | Google Colab、Kaggle、NVIDIA Inception個人参加、NHN Cloud/Naver Cloud個人プラン | KISTI HPCは所属機関経由の利用が基本 |
| インド | Google Colab（最も普及、価格感度が高い市場で無料枠が重要）、Kaggle、IndiaAI個人利用（スタートアップ/研究者向け40%補助、個人でも登録制で利用可能なケースあり） | 価格感度が極めて高く、無料/低価格サービスへの依存度が最も高い |
| イスラエル | Google Colab、Innovation Authority GPU配布（スタートアップ経由、個人起業家も対象）、Vast.ai/RunPod個人利用 | スタートアップ文化が強く、個人でも起業経由でGPUアクセスを得るパターンが多い |

**AIXSへの示唆:** 個人研究者層は将来の組織ユーザーの入口であり、フリーミアムモデル（月X GPU-hr無料）や学術割引の設計が長期的なユーザー獲得に重要。特に日本市場では、Colab→ABCI→商用GPUという段階的な移行パスにAIXSが位置づけられれば、自然な成長チャネルとなる。

### 3.4.14 大学GPU予算の定量データ

各地域の主要大学におけるGPU/コンピュート投資の規模感を以下に整理する。

| 地域 | 大学/機関 | GPU/コンピュート規模 | 予算規模 | 備考 |
|---|---|---|---|---|
| US | UT Austin (TACC) | 5,000+ GPU (Stampede3, Vista等) | ~$50M [推定] | NSF/DOE共同ファンディング |
| US | Princeton University | 300 H100 (Della-H100クラスター) | [推定 $15-20M] | 2024年に導入 |
| US | MIT (Lincoln Lab + CSAIL) | 数千GPU規模 | [推定 $30-50M] | DOD/NSFファンディング含む |
| US | Stanford (HAI) | 大規模クラスター | [推定 $20-40M] | Google/NVIDIA寄贈含む |
| 日本 | 東京大学 (BDCMS/mdx) | A100 320基 (mdx)、独自クラスターも保有 | 年間数十億円 [推定] | mdxは全国共同利用 |
| 日本 | 理化学研究所 (RIKEN) | 富岳（442 PFLOPS、GPU非搭載だがHPC参考）、AI向けGPU導入中 | 富岳運用費 年間~¥10B | 次期システムでGPU大量導入予定 |
| 日本 | 東北大学 (CYBERSCIENCE CENTER) | A100 40GB×16基、H100導入予定 | [推定 数億円] | 全国共同利用拠点 |
| EU | Cambridge (Dawn) | 1,024 Intel GPU (Dawn)、CSD3 クラスター | ~£34M (UKRI funded) | AIRR対象システム |
| EU | ETH Zurich (Euler) | A100/H100混合クラスター | [推定 CHF 20-30M] | スイス国立スパコンセンター(CSCS)との連携 |
| 韓国 | KAIST | 大規模GPUクラスター（2026年にAI学部300人新設） | [推定 数百億ウォン] | 政府NRF/IITPファンディング |
| 台湾 | NCHC/TWCC | 1,700+ GPU (H200 + GB200 NVL72 + HGX B300) | NT$数十億 [推定] | 国立計算基盤 |
| 中国 | 清華大学 | 大規模GPUクラスター（Ascend 910対応含む） | [推定 数億RMB] | 国家重点実験室ファンディング |
| イスラエル | Technion | GPUクラスター＋Innovation Authority連携 | [推定 $5-10M] | NVIDIA R&D拠点との近接性 |

**注:** 大学のGPU予算は多くの場合公開されておらず、上記の多くは公開情報からの推定値（[推定]マーク付き）である。実際の投資額は外部ファンディング（政府グラント、企業寄贈）を含むとさらに大きい。

**AIXSへの示唆:** 大学はGPU予算の制約が強く、コスト効率の高いプラットフォームへの需要が大きい。特に日本の大学研究者はABCI/mdxの枠を超えた計算需要を商用クラウドで満たす必要があり、アカデミック割引＋ABCI互換ワークフローがAIXSの差別化ポイントとなる。

### 3.4.15 共同研究・委託研究によるGPUアクセス

企業-大学間、企業-政府間の共同研究は多くの地域でGPUアクセスの重要なチャネルであるが、体系的な情報が乏しい。以下に主要地域の状況を整理する。

| 地域 | 主要な共同研究スキーム | GPU利用との関連 |
|---|---|---|
| US | NSF Industry-University Cooperative Research Centers (IUCRC)、DOE Lab partnerships（国立研究所のGPUを産学連携で利用）、NVIDIA Academic Partnership Program | NSF cooperative agreementsで企業が大学GPU利用をスポンサー。DOE HPCへの産業界アクセスはINCITE/ALCCプログラム経由。NVIDIAがDGX寄贈＋共同研究で大学GPUを補強 |
| 日本 | NEDO共同研究（企業-大学の計算資源共有）、産学連携GPU利用（JST AIP等）、METI Cloud Program企業連携枠 | NEDO委託研究ではGPU利用費が研究費に含まれる。ABCIの産業利用枠は企業が直接申請可能。大企業のDGXクラスターを共同研究で大学研究者が利用するケースも |
| EU | Horizon Europe collaborative projects（コンソーシアム型、GPU利用費をプロジェクト経費に計上）、Public-Private Partnership (PPP) schemes、EIT Digital | Horizon Europeの大型プロジェクトではEuroHPC GPU利用を共同研究費で確保。PPPスキームで企業がGPU投資、大学が研究を担当する分業モデル |
| UK | UKRI Industrial Strategy Challenge Fund、Catapult Centres（企業-大学のGPU共同利用）、Alan Turing Institute partnerships | Catapultセンターが企業-大学間のGPU共有ハブとして機能。Alan Turing Instituteが計算基盤と研究者コミュニティを接続 |
| 中国 | 国家重点研究計画の計算資源配分（大学-企業コンソーシアムに智算中心GPUを配分）、大手テック企業の大学連携（Alibaba DAMO Academy-大学共同研究等） | 政府の国家重点研究計画に採択されると智算中心のGPU時間が配分される。大手テック企業（Alibaba, Tencent, Baidu）が大学に計算資源を提供する共同研究も一般的 |
| 韓国 | NRF共同研究プロジェクト、K-Moonshot産学連携（161社パートナー）、NVIDIA Inception＋大学連携 | K-Moonshot参加企業が大学研究チームにGPU時間を提供。KISTI HPCへの産学共同利用枠あり |
| インド | IndiaAI認定プロバイダの大学連携枠、NVIDIA India Deep Tech Alliance（$2B、大学-スタートアップ連携） | IndiaAI Mission下で大学-スタートアップの共同GPU利用が促進。C-DAC/PARAM系スパコンの産学連携利用枠 |

**AIXSへの示唆:** 共同研究では複数組織のユーザーが同一GPU環境にアクセスする必要があり、マルチテナント機能、アクセス制御、実験データの組織間共有・分離が重要。AIXSが「共同研究向けワークスペース」を提供し、データ主権を保ちつつ計算資源を共有できるモデルを構築すれば、産学連携の自然な基盤となる。

### 3.4.16 政府コンピュートプログラムの利用資格条件

主要な政府コンピュートプログラムの利用資格を以下に整理する。

| プログラム | 地域 | 利用資格 | 外国籍/外国企業の利用可否 |
|---|---|---|---|
| NAIRR (National AI Research Resource) | US | 米国内の適格教育機関・研究機関に所属する研究者。14連邦機関＋28民間パートナーが参画。PI（主任研究者）は米国機関所属が条件 | 外国籍研究者も米国機関に所属していれば申請可能。外国機関単独での利用は不可 |
| ABCI 3.0 (産総研) | 日本 | 日本国内の研究機関・大学・企業に所属する研究者。個人研究者も「ABCI利用者」として申請可能（日本の研究機関所属が条件）。産業利用枠あり | 日本国内に拠点を持つ外国企業・研究者は申請可能。海外からのリモート利用は要相談。日本語での申請が推奨 |
| GENIAC | 日本 | 招待制（METI選定）。日本のLLM開発者・AI企業が主対象。Phase 1-3で30+プロジェクト採択 | 日本法人が必要。外国企業の日本法人も対象になり得るが、主に国内企業が採択 |
| EuroHPC (AI Factories含む) | EU | EU加盟国の研究者・企業・SME・スタートアップ。Hosting Memberの機関が優先。AI Factory無料アクセスはSME/スタートアップ向け（50K GPU-hr） | EU加盟国に拠点を持つ機関が条件。Associated Countries（UK, ノルウェー等）は限定参加。非EU企業単独では利用不可 |
| KISTI HANGANG / NACC | 韓国 | 韓国の研究者・企業。KISTI HPCは韓国国内の研究機関・大学・企業が対象。NACCは政府主導で51%公的/49%民間の配分 | 韓国国内拠点が必要。外国研究者は韓国機関との共同研究経由でアクセス可能 |
| IndiaAI Compute | インド | インドのスタートアップ・研究者。認定プロバイダ（Yotta, NextGen, E2E, Jio）経由で40%補助金適用。インド国籍または法人登記が条件 | インド法人が必要。外国企業のインド子会社も対象になり得る |
| NSCC ASPIRE | シンガポール | シンガポールの研究機関・大学・企業。RIE2030プログラム参加機関が優先。AI Singaporeプログラム参加者にも配分 | シンガポール国内機関所属が条件 |
| TWCC | 台湾 | 台湾の研究者・大学・企業。NSTCプロジェクト採択者に優先配分 | 台湾国内機関所属が条件 |
| Innovation Authority GPU | イスラエル | イスラエルのスタートアップ・研究者。Innovation Authority認定企業に1,000 B200 GPU配布 | イスラエル法人が必要 |

**AIXSへの示唆:** 政府プログラムの利用資格は地域拠点要件が共通しており、AIXSが各地域のローカルパートナーまたは認定プロバイダとなることで、政府コンピュートへのアクセスを顧客に代理提供するモデルが有効。特に日本（ABCI/GENIAC）とEU（EuroHPC）では、AIXSが統合プラットフォームとして政府GPU＋商用GPUをシームレスに利用できる環境を提供すれば、利用資格の壁を超えた価値を創出できる。

### 3.5 地域横断の比較と示唆

#### 地域ごとに何が決定的に違うか

| 軸 | 最も特徴的な地域 | 内容 |
|---|---|---|
| 資金源の性質 | 中東(SWF) vs インド(政府補助) vs US(VC) | 中東はSWF、インドは政府40%補助金、USはVC。購買プロセスが根本的に異なる |
| 規制の重さ | EU(最重) > 中国(独自) > シンガポール(DC規制) > UK/US(軽) | EU AI Act + GDPR + CADA が最も重い参入障壁。UK はポスト Brexit で軽量 |
| GPU調達制約 | 中国(輸出規制) > UAE/サウジ(要輸出許可) > SG(DC容量規制) > 他(自由) | 中国は NVIDIA ハイエンド不可。中東はチップ数に上限。SGはデータセンター自体に制約 |
| 国産GPU開発 | 中国(Ascend/Cambricon/Biren/天数智芯[GPT-5.4-pro補足]) > 韓国(HBM) > 台湾(TSMC製造) | 中国のみが GPU 設計（2026年にBiren BR20X、天数智芯が商用化予定）。韓国はメモリ、台湾はファウンドリに特化 |
| MLプラットフォーム成熟度 | US(最高) > EU(高) > 他(低〜なし) | 日本/韓国/台湾/中東はインフラ構築フェーズで、プラットフォームレイヤーが未整備 |
| 価格感度 | インド(最高) > 中国(高) > 日本/韓国(中) > 中東(低) | インドでは 40% 補助金が前提。中東は予算制約がほぼない |

#### AIXSはどの地域でどのメッセージを使うべきか

| 地域 | 主要メッセージ | 副次メッセージ |
|---|---|---|
| US/Canada | 「GPU時間からインサイトまでを一つのプラットフォームで」 | マルチクラウドオーケストレーション、コスト追跡 |
| EU | 「Sovereign by design -- EU AI Act Ready」 | GDPR ネイティブ、EuroHPC 統合、60-80% ハイパースケーラーより安い |
| UK | 「British AI のためのスケーラブルなコンピュート」 | AIRR 互換、UK-EU ハイブリッド、スタートアップフレンドリー |
| 日本 | 「データ主権 + 研究成果を加速 + ABCI/さくらと統合」 | 国内プロバイダにない ML プラットフォーム、GENIAC/科研費の有効活用 |
| 韓国 | 「ソブリン AI 開発を加速。国家インフラと統合」 | NACC/KISTI連携、K-Moonshot エコシステム |
| 台湾 | 「チップ製造大国から AI 活用大国へ」 | TWCC 統合、Compute Alliance 連携 |
| 中東 | 「マルチベンダー GPU オーケストレーション + ソブリンコンピュート最適化」 | 輸出規制コンプライアンス、SWF 調達プロセス対応 |
| インド | 「コスト最適化 -- 補助金コンピュートの価値を最大化」 | マルチクラウド GPU 集約、スタートアップ向け価格 |
| シンガポール | 「プレミアムコンピュートの効率を最大化」 | サステナビリティ対応、ASEAN ハブ |
| イスラエル | 「Innovation Authority GPU からのスケールアップ」 | スタートアップフレンドリー、防衛グレードセキュリティ |

#### 各地域で接続すべき既存基盤

| 地域 | 最優先統合先 | 高優先統合先 |
|---|---|---|
| 日本 | ABCI 3.0、さくら高火力 | mdx、HPCI/SINET6、GMO GPUクラウド |
| EU | EuroHPC Federation Platform | SecNumCloud/C5認証、Isambard-AI/Dawn |
| UK | AIRR (Isambard-AI + Dawn) | UK GDPR対応、Horizon Europe連携 |
| 韓国 | National AI Computing Center | KISTI HANGANG、SKT GPUaaS |
| 台湾 | TWCC/NCHC | Foxconn Visionbay.ai、Taiwan Compute Alliance |
| UAE | Core42 AI Cloud | Stargate UAE エコシステム |
| サウジ | HUMAIN | KAUST、SDAIA |
| インド | IndiaAI Compute Platform | Yotta/E2E/Jio、C-DAC/PARAM |
| シンガポール | NSCC/ASPIRE | AI Singapore、SMC/Aethir |
| イスラエル | Innovation Authority GPU 配布基盤 | Nebius スパコン、NVIDIA Israel |

---

## 4. 追加発見軸

### 4.1 競合分析の追加軸（価格以外の比較次元）

| # | 追加軸 | 理由 | 測定方法 | 現状の各社対応 | AIXSへの示唆 |
|---|---|---|---|---|---|
| 1 | **実行の再現性** | R&Dにおいて実験の再現性は最重要。同一コード・データで同一結果を得られるかは、GPU/ドライバ/CUDA バージョン、ランダムシード管理、環境のスナップショット機能に依存 | 同一コード・データ・環境で結果が再現可能か。標準MLベンチマーク10種での再現成功率（%）を四半期ごとに計測。CI/CDパイプラインでの自動検証頻度 | どのプロバイダもビルトイン再現性保証なし。ユーザーが Docker/conda で自己管理 | AIXSが環境スナップショット＋シード管理＋決定論的実行モードを提供すれば独自価値 |
| 2 | **実験ログの永続保持** | 学術論文や企業R&Dでは数年後にも実験ログを参照する必要がある。GPU クラウドは一時的な実行環境であり、ログの長期保持は別途設計が必要 | ログ保持期間（日数/無制限）、構造化ログの検索可能性（全文検索対応か）、エクスポート形式の種類。年1回、過去実験ログの取得テストを実施 | SageMaker Experiments/Vertex AI Experiments は保持するが、GPU特化プロバイダはログ保持なし | AIXSが「実験のGitHub」として全実験の構造化ログを永続保持すれば、研究者にとって不可欠なツールになる |
| 3 | **長時間ジョブの安定性** | 大規模学習は数日〜数週間連続実行。ジョブ中断時の自動チェックポイント・再開能力が重要 | 48h以上のジョブ完了率（%）、プリエンプション頻度（回/日）、チェックポイントからの自動復旧成功率。月次で長時間ベンチマークジョブを実行して計測 | SageMaker HyperPod: 自動復旧＋チェックポイント再開。CoreWeave: K8sの自動再スケジュール。RunPod/Lambda: 手動管理 | AIXSがジョブの自動チェックポイント＋復旧を内蔵すれば、長時間学習の信頼性で差別化可能 |
| 4 | **ジョブキュー運用** | R&Dチームは複数の実験を同時に実行したい。GPU空き状況に応じた自動スケジューリング、優先度管理、フェアシェアリングが必要 | キュー待ち時間の中央値・95パーセンタイル、優先度レベル数、フェアシェア精度（割当GPU時間の偏差）。週次でキュー統計をダッシュボード表示 | ハイパースケーラーは Batch/SageMaker Pipelines で対応。GPU特化プロバイダはジョブキュー未実装（Modal の gang scheduling はベータ） | AIXSがチーム向けジョブキュー＋実験優先度管理を提供すれば、研究グループの運用を大幅に改善 |
| 5 | **複数GPU世代の切り替えやすさ** | 実験フェーズ（プロトタイプ → 本格学習）でGPU世代を変えたい。A100で検証し、H100で本番学習。コード変更なしで切り替えられるか | GPU世代切り替えに必要なコード変更行数（理想は0行）、切り替え所要時間（分）、切り替え後の性能回帰テスト自動化の有無。四半期ごとにA100→H100→B200の切り替えテストを実施 | ほぼ全プロバイダで手動切り替え。Modal は GPU パラメータの変更だけで可能（ただしコード内） | AIXSがワークフロー定義内でGPU世代を宣言的に切り替え可能にすれば、実験のアジリティが向上 |
| 6 | **エージェントからの操作容易性** | AI エージェント（Claude Code, Devin等）がプログラマティックに GPU ジョブを投入・監視・結果取得できるか。API 設計の品質が重要 | API呼び出しからジョブ開始までのステップ数、SDK対応言語数、エージェント向けドキュメントの充実度（スコア1-5）、エージェント経由ジョブ投入の成功率。月次でエージェント統合テストを実施 | Modal: Python SDK で最も操作しやすい。AWS: Boto3 で可能だが複雑。RunPod: REST API GA。Lambda: 基本的 | AIXSが「エージェントファースト API」を設計すれば、自動研究ワークフローのバックエンドとして選ばれる |
| 7 | **リソース横断ワークフロー化余地** | データ前処理 → 学習 → 評価 → 推論デプロイの各ステップを異なるリソース（CPU、GPU種別、メモリ量）で実行するワークフローの定義・実行 | ワークフロー定義のステップ数上限、異種リソース切り替えのオーバーヘッド（秒）、パイプライン失敗時の自動リトライ成功率。四半期ごとに標準5ステップパイプラインのE2Eテストを実施 | SageMaker Pipelines、Vertex AI Pipelines (Kubeflow)、AML Pipelines。GPU特化プロバイダはパイプライン未実装 | AIXSがシンプルなワークフロー定義（Pythonic or YAML）でマルチリソースパイプラインを提供すれば差別化 |
| 8 | **監査ログ / lineage** | エンタープライズ・規制対応で、データからモデルまでの完全なリネージ追跡が必要。EU AI Act は高リスク AI に監査証跡を義務付け | リネージ追跡の粒度（データセット→前処理→学習→モデル→推論の全ステップ追跡可否）、EU AI Act監査要件との適合率（%）、監査ログの改ざん防止機構の有無。半期ごとに外部監査でコンプライアンスを検証 | ハイパースケーラーは部分的に対応。GPU特化プロバイダは皆無 | AIXSが EU AI Act 対応のビルトイン監査ログ・リネージを提供すれば、規制市場で独自ポジション |
| 9 | **組織導入のしやすさ** | IT部門の承認、SSO統合、RBAC、支出管理、請求書対応。エンタープライズ導入の現実的ハードル | セットアップから初回ジョブ実行までの所要時間（時間）、SSO/SAML統合の有無、RBAC粒度（ロール数）、請求書対応の有無。四半期ごとに新規オンボーディングのユーザビリティテストを実施 | AWS/Azure/GCP: 最も成熟。CoreWeave: 良好。Modal: Team/Enterprise プラン。RunPod/Lambda: 基本的 | AIXSがセルフサービス + エンタープライズ両対応で、R&Dチームが「IT部門を通さず始められる → 組織に広がる」パスを設計 |
| 10 | **教育・研究コミュニティでの採用しやすさ** | 大学研究室、学生、ポスドクが気軽に使えるか。学術割引、無料枠、教育向けドキュメント | 無料枠の有無と規模（GPU-hr/月）、学術割引率（%）、教育向けチュートリアル数、大学での採用数。半期ごとにアカデミックユーザーアンケートを実施 | Google Colab/HF: 教育最強。AWS/GCP: スタートアップクレジット。RunPod: コミュニティ重視 | AIXSが学術向け無料枠＋教育コンテンツで「将来の研究者の標準ツール」になれば長期的な堀に |
| 11 | **マルチリソースオーケストレーション（GPU+HPC+量子+ロボティクス）** | 2026年の最先端研究はGPUだけでなく、量子プロセッサ（QPU）、HPC、ロボティクスの異種混合ワークフローを必要とする。MiqroForgeやORCA Computing（NVIDIA CUDA-Qフレームワーク）がGPU-量子ハイブリッドを先行 | 対応ハードウェアモダリティ数（GPU/CPU/TPU/QPU/FPGA等）、異種リソース間のデータ転送レイテンシ（ms）、統合コントロールプレーンの有無。半期ごとにGPU-QPUハイブリッドワークフローのPoCを実施 | どのプロバイダも単一ハードウェアモダリティのみ。量子-古典統合は未開拓 | AIXSが「単一コントロールプレーンで異種コンピュートを統合」すれば参入不可能な堀を構築可能（Deep Research Gemini指摘） |
| 12 | **Physical AI（ロボティクスAI）対応** | 「推論のインフレクション」により、LLMの自律ロボティクスへの適用（Physical AI）が2026年に本格化。クラウドGPUでモデル学習→エッジ（NVIDIA Jetson等）に蒸留→リアルタイムテレメトリのフィードバックループ | クラウド-エッジ間のモデル蒸留・デプロイの自動化度（手動/半自動/全自動）、テレメトリフィードバックのレイテンシ（ms）、対応エッジデバイス数。四半期ごとにJetson等へのモデルデプロイE2Eテストを実施 | 統合的にサポートするプロバイダなし | AIXSのラボ機器・ロボティクス統合ビジョンと直接合致 |
| 13 | **マルチクラウド・クラウド非依存オーケストレーション** | SkyPilot、dstackなどのツールが台頭し、特定クラウドに依存しないMLワークロード実行が可能に。企業はベンダーロックイン回避とコスト最適化を追求 | 対応クラウドプロバイダ数、クラウド間ワークロード移行の所要時間（分）、移行時のコード変更量（行数）、コスト最適化による削減率（%）。四半期ごとに3+プロバイダ間の移行テストを実施 | SkyPilot: 最小限の設定変更で任意クラウドでML実行。dstack: 統一インターフェース。ただしR&D統合機能なし | AIXSがマルチクラウドオーケストレーション＋R&D統合を兼ね備えれば、SkyPilot/dstackの上位互換に |

### 4.2 市場比較の追加軸

| # | 追加軸 | 理由 | 測定方法 | 地域間差異 | AIXSへの示唆 |
|---|---|---|---|---|---|
| 1 | **GPU調達難易度** | 輸出規制、供給制約、政府調達プロセスが地域ごとに異なる | 地域別のGPU調達リードタイム（申請から利用開始までの日数）、調達成功率（%）、必要な承認ステップ数。四半期ごとに各地域で実際の調達テストを実施 | 中国: 最高（輸出規制）。UAE/サウジ: 高（輸出許可要）。SG: 高（DC規制）。日本/韓国/台湾/EU/UK: 低-中 | AIXSが地域ごとの調達複雑性を吸収し、統一インターフェースを提供 |
| 2 | **輸出規制の影響** | US AI Diffusion Rule（一時撤回後も議論中）、Remote Access Security Act が GPU アクセスのグローバル地図を変える | 地域別の利用可能GPU種別数、規制変更頻度（回/年）、コンプライアンス対応コスト（$）。月次で各地域の規制更新を監視しレポート作成 | Tier 1（制限なし）: EU/UK/日本/韓国/台湾/SG/イスラエル。要許可: UAE/サウジ。制限: 中国。不確実: インドネシア | AIXSは KYC/コンプライアンスをビルトインし、地域ごとの規制対応を自動化 |
| 3 | **大学と企業の計算資源格差** | 大学は限られた GPU を多数の研究者で共有。大企業は数万 GPU を保有。この格差が研究のペースと方向性に影響 | 大学研究者あたりのGPU-hr/月と企業研究者あたりのGPU-hr/月の比率、大学のGPUキュー待ち時間（時間）、企業との共有利用率。年次でアカデミック顧客アンケートを実施 | 日本: ABCI/mdx で緩和だが十分でない。韓国: NACC が企業GPU工場と並行。EU: EuroHPC で対応 | AIXSが「大学研究者にも大企業レベルのコンピュート体験」を提供する民主化ツールとして訴求 |
| 4 | **国内クラウド育成政策** | 多くの国が米国ハイパースケーラー依存からの脱却を政策化 | 地域別の国内クラウド市場シェア（%）、政府補助金総額（$）、国内クラウド対応によるAIXS受注率への寄与。半期ごとに各国の政策動向をレビュー | 日本: METI ¥1,146B+。EU: CADA、InvestAI。中国: 国産義務。韓国: NACC | AIXSが「マルチクラウド中間レイヤー」として国内クラウド＋ハイパースケーラーを統合すれば、政策と整合 |
| 5 | **データ越境規制** | GDPR、中国サイバーセキュリティ法、韓国PIPA、インドのデータローカライゼーション等がクロスボーダー GPU 利用を制約 | 地域別のデータ越境に必要な手続きステップ数、データローカライゼーション対応リージョン数、規制違反リスクスコア（1-5）。四半期ごとに法規制チェックリストを更新 | EU: 最も厳格（GDPR + AI Act）。中国: サイバーセキュリティ法。インド: 金融・医療セクター。SG: PDPA | AIXSがデータレジデンシー保証をビルトインし、「このジョブのデータはこの地域内で処理される」を宣言的に設定可能にする |
| 6 | **研究者の言語・文化的障壁** | 英語以外のドキュメント・UI・サポートの必要性。日本語、韓国語、中国語、アラビア語等 | 対応言語数、翻訳カバレッジ率（ドキュメント/UI/サポートの各%）、非英語ユーザーのNPS（Net Promoter Score）。半期ごとに多言語ユーザビリティテストを実施 | 日本: 日本語 UI/ドキュメントが強く選好される。中東: アラビア語 LLM 需要。中国: 中国語のみ | AIXSが多言語対応（特に日本語最優先）で地域市場に浸透 |
| 7 | **電力・冷却・サステナビリティ要件** | GPU DC の電力消費が増大。各地域で異なるグリーン要件 | PUE値、再生可能エネルギー比率（%）、CO2排出量（kg/GPU-hr）、各地域のグリーン規制適合状況。四半期ごとにサステナビリティレポートを作成 | SG: PUE 1.25/50%グリーン義務。EU: エネルギー効率規制。UAE: 原子力/太陽光。台湾: 電力不足 | AIXSがワークロードの電力効率を可視化・最適化する機能を持てば、SG/EU 市場で差別化 |
| 8 | **AI人材の供給** | GPU があっても使える人材がいなければ価値がない | 地域別のAI人材数（求人/採用データ）、AIXSプラットフォームの初回利用から独立運用までの所要時間（時間）、非専門家ユーザーの操作成功率（%）。年次で人材市場レポートを分析 | US: 最も豊富。EU: 格差大（英/仏/独に集中）。日本: 深刻な不足。韓国: KAIST AI学部新設(300人/年) | AIXSが「AI インフラの複雑性を抽象化」して非専門家でも使えるプラットフォームにすれば、人材不足市場で価値 |
| 9 | **GPU価格の反発リスク** | 2026年初頭にGPU価格が約15%上昇（GDDR6/GDDR7メモリ不足、NVIDIA30-40%生産削減）。デフレ一辺倒ではなく短期的な反発も | GPU-hour単価の月次変動率（%）、HBM/GDDR供給指標の追跡、予約価格と市場価格の乖離率。月次で主要プロバイダの価格モニタリングを実施 | 先端GPU（RTX 5090等）で最大31-50%値上がりの地域も | AIXSが価格ボラティリティを吸収するヘッジ的なプライシング戦略（予約制度等）を提供すれば、顧客の価格リスクを軽減 |

---

## 5. R&D自動化システム競合マップ

AIXSはGPUコンピュートプロバイダとしてだけでなく、R&D自動化プラットフォームとしても位置付けられる。以下はR&D自動化の観点からの競合マップ。

| # | システム名 | カテゴリ | 主な機能 | 開発元 | AIXSとの関係 |
|---|---|---|---|---|---|
| 1 | AI Scientist v2 | 自律研究エージェント | 仮説生成 → 実験設計 → コード実装 → 実験実行 → 論文執筆の全自動化。2025年3月にICLRワークショップに論文採択 | Sakana AI（$30Mシード→2026年2月シリーズAで追加調達し総額~$50M[GPT-5.4-pro補足, 2026-03-28]、東京拠点、元Google研究者David Ha・Llion Jones設立） | R&D自動化の直接競合。ただしコンピュートは外部依存。ビジョン能力（プロット・テーブル解釈）に制限あり。AIXSがバックエンドになり得る |
| 2 | AI Co-Scientist | 研究支援AI | 科学文献の処理・洞察抽出・統合。2025年2月発表 | Google DeepMind（Alphabet子会社） | ペイウォール論文を除外、品質評価に課題あり。研究支援レイヤー。AIXSのコンピュートと補完的 |
| 3 | Kosmos / Robin | 自律研究プラットフォーム / マルチエージェント研究自動化 | Kosmos: マルチモーダル科学研究。Robin: 文献検索・仮説生成・データ分析の統合。2025年5月にRobinが初のAI生成科学的発見（加齢黄斑変性の新規治療候補同定）を発表 | FutureHouse | 物理実験は人間実行に依存。AIXSが物理ラボ統合で補完可能 |
| 4 | Orchestra Research | 研究オーケストレーション | 研究ワークフロー管理、コラボレーション | 独立スタートアップ | R&Dワークフロー管理で部分的競合 |
| 5 | Sciloop | 実験管理 | 科学実験のループ管理、再現性保証 | 独立スタートアップ | 実験管理機能で競合。AIXSの機能サブセット |
| 6 | DeepScientist | 自律研究 | 自動的な科学的発見 | 学術プロジェクト | 研究自動化の概念的競合 |
| 7 | PaperQA2 | 文献調査自動化 | 科学論文の質問応答、文献レビュー自動化 | Future House | R&Dの文献調査フェーズのみ。補完的 |
| 8 | Robin | 研究自動化 | ロボティック実験自動化 | 学術プロジェクト | 物理実験の自動化。ウェット/ドライラボの統合 |
| 9 | MLflow | 実験管理・MLOps | 実験追跡、モデルレジストリ、デプロイ | Databricks (OSS) | AIXSが内蔵すべき機能。統合対象 |
| 10 | Weights & Biases (W&B) | 実験追跡・可視化 | 実験ログ、ハイパーパラメータ追跡、チームコラボレーション | Weights & Biases | AIXSが内蔵すべき機能。または統合対象 |
| 11 | Neptune.ai | 実験管理 | メタデータ管理、実験比較 | Neptune.ai | 補完的ツール |
| 12 | Comet ML | 実験管理 | 実験追跡、モデル比較、データ管理 | Comet | 補完的ツール |
| 13 | DVC (Data Version Control) | データバージョニング | データセット・モデルのバージョン管理 | Iterative (OSS) | AIXSが統合すべきツール |
| 14 | Kubeflow | MLパイプライン | K8s上のMLワークフローオーケストレーション | Google (OSS) | パイプラインエンジンとして統合対象 |
| 15 | Ray | 分散コンピューティング | 分散ML学習、サービング、データ処理 | Anyscale (OSS) | AIXSの分散実行レイヤーとして統合対象 |
| 16 | Determined AI | ML学習プラットフォーム | 分散学習、ハイパーパラメータ最適化 | HPE (買収) | 学習プラットフォームとして部分的競合 |
| 17 | ClearML | MLOpsプラットフォーム | 実験管理、パイプライン、モデルサービング | ClearML (OSS) | オープンソースの統合MLOps。競合 |
| 18 | Polyaxon | ML実験プラットフォーム | 実験管理、K8s上のML | Polyaxon | 部分的競合 |
| 19 | Guild AI | 実験管理 | 実験の再現性、比較 | Guild AI (OSS) | ニッチな実験管理ツール |
| 20 | Metaflow | MLワークフロー | データサイエンスワークフロー定義 | Netflix/Outerbounds (OSS) | ワークフロー定義フレームワーク |
| 21 | ZenML | MLOpsフレームワーク | パイプライン定義、インフラ抽象化 | ZenML (OSS) | パイプラインフレームワーク。統合対象 |
| 22 | LitGPT / Lightning AI | ML学習・推論 | PyTorch Lightning ベースの学習・サービング | Lightning AI | コンピュート＋フレームワーク。部分的競合 |
| 23 | Brev.dev | GPU開発環境 | 1-click GPU環境プロビジョニング | Brev.dev | 開発環境プロビジョニングで競合 |
| 24 | Vast.ai | GPU マーケットプレイス | 分散GPU市場、低価格 | Vast.ai | 価格重視の GPU アクセス。インフラレイヤー |
| 25 | FluidStack | GPU クラウド | マルチプロバイダGPUアクセス | FluidStack | マルチクラウドGPU。インフラレイヤー |
| 26 | Fireworks AI | 推論最適化 | 高速推論API、モデル最適化 | Fireworks AI | 推論特化。AIXSのR&D範囲とは異なる |
| 27 | Hyperstack | GPU クラウド | サステナブルGPUクラウド | Hyperstack | インフラプロバイダ |
| 28 | fal | サーバーレスGPU | メディア/生成AI向けサーバーレスGPU | fal | ニッチなサーバーレスGPU |
| 29 | Node AI | GPUアグリゲーター | 50+プロバイダを単一インターフェースで | Node AI | GPUマーケットプレイス。AIXSと補完的または競合 |
| 30 | Shadeform | GPUアグリゲーター | マルチクラウドGPU比較・プロビジョニング | Shadeform | GPUブローカー。AIXSのインフラ層と競合 |

**AIXSのR&D自動化における独自ポジション:** 上記30システムのうち、「競合的GPUコンピュート価格 + 統合実験管理 + マルチクラウドオーケストレーション + R&D自動化ワークフロー」を単一プラットフォームで提供するものは存在しない。AIXSがこの統合を実現すれば、GPU特化プロバイダともR&D自動化ツールとも異なる独自カテゴリを確立できる。

---

## 6. 不確実性と不足情報

### 6.1 公開情報が乏しい部分

| 項目 | 不確実性の内容 | 影響 |
|---|---|---|
| CoreWeave Spot/予約価格 | 具体的な Spot 価格率と Flex Reservation の詳細条件が非公開（要セールス） | CoreWeave の実効コスト比較が不完全。「最大60%OFF」の実際の適用条件が不明 |
| Azure Reserved GPU Pricing | H100/H200 の予約価格が「Contact sales」で非公開 | Azure の長期コスト比較ができない |
| GCP CUD詳細 | A3/A3 Ultra の CUD 割引率が推定値（~35%/~50%） | GCP の長期コスト比較の精度が低い |
| 中国国内GPU価格 | Huawei Ascend、Cambricon 等の実際のクラウド価格が断片的 | 中国市場の価格比較が困難 |
| 日本市場の実効GPU稼働率 | さくらインターネットのGPU稼働率、GENIAC終了後の需要減少の具体的数値。Gemini DRによりさくらDOK価格が2026年1月に大幅改定（0.83円/秒 = ~$2.50/GPU-hr）と判明し、供給過剰下での価格競争が進行中と確認 | 日本市場のGPU供給過剰問題の深刻度が部分的に確認 |
| 中東のGPU実稼働状況 | Stargate UAE、HUMAIN の実際の稼働GPU数（計画 vs 実績）。Gemini DRによりStargate UAE初期200MWが2026年稼働予定、HUMAIN 1.9GW（2030年）→6.6GW（2034年）の段階的計画と判明。GPT DRによりHUMAINのGDP押上効果$135.2B（2030年）を確認 | 中東市場は計画値が大きいが、段階的な実現ロードマップが存在 |
| Lightning AI、Brev.dev、fal、Vast.ai、FluidStack、Hyperstack の詳細価格 | Vast.ai（H100 $1.49-$2.27/hr、A100 ~$0.50/hr）、Hyperstack（H100 ~$1.90/hr）、fal（H100 $1.89/hr）はGemini DRで部分的に判明。Spheron（H100 $2.01/hr）も新規確認 | Vast.ai/Hyperstack/fal/Spheronの価格帯が判明。Lightning AI、Brev.devは依然不完全 |

### 6.2 比較上の限界

| 限界 | 説明 |
|---|---|
| 実効コスト vs 公開価格 | 大口顧客はカスタム価格を得ている可能性が高い。公開価格は上限であり、実際の取引価格は低い場合がある |
| GPU性能の正規化困難 | H100 SXM vs PCIe、A100 40GB vs 80GB、異なるインターコネクト（InfiniBand vs Ethernet）で実効性能が大きく異なるが、GPU-hour 比較では表面化しない |
| サーバーレス vs 常時起動 | Modal の「ゼロアイドルコスト」とRunPod の「低GPU-hour 価格」は稼働パターンによって優劣が逆転する。TCO 比較には実際のワークロードプロファイルが必要 |
| 為替変動 | 日本円価格は 1 USD = 150 JPY で固定換算。実際の為替レートで 5-10% の変動あり |
| 時点の違い | データは 2025年3月を中心に収集。GPU価格は3-6か月で大幅に変動する可能性がある。特に AWS の2025年6月値下げは将来イベント |
| 地域市場の規模推定 | 各地域の AI/GPU 市場規模は複数ソースの推定値であり、定義と計測方法が異なる |

### 6.3 今後追加で確認すべき点

1. **AWS 2025年6月値下げ後の実勢価格** -- 44% カットが他社の追従を引き起こすか
2. **CoreWeave IPO 後の価格戦略** -- 公開企業として透明性向上が期待される
3. **NVIDIA B200/GB200 の商用クラウド展開価格** -- Deep Researchにより部分的に判明（Lambda $3.79-$4.99/hr、RunPod $5.99/hr、Modal $6.25/hr、Together $5.50/hr）。FP4精度ネイティブ対応でトークン単価大幅低下
4. **EU CADA 制定後の具体的要件** -- Q1 2026 予定。EU クラウドプロバイダ適格要件が非EU企業に与える影響
5. **日本のGPU過剰供給の動態** -- さくらインターネットの業績推移、GENIAC Phase 3 の影響
6. **中東の実稼働ベースのGPU利用状況** -- 計画値と実績値のギャップ
7. **インドの IndiaAI 認定プロバイダの具体的価格・SLA** -- 40% 割引の詳細条件
8. **Modal の multi-node training GA 時期** -- ベータ脱却で競合構造が変化する可能性
9. **Replicate の Cloudflare 統合後の戦略変化** -- エッジ推論との統合
10. **Lightning AI、Brev.dev、Vast.ai、FluidStack、Hyperstack の詳細比較** -- Vast.ai/Hyperstack/falの価格はDRで部分的に判明。Lightning AI、Brev.devは依然未調査
11. **GPU価格の反発メカニズムと持続性** -- 2026年初頭の15%価格上昇（GDDR6/GDDR7不足、NVIDIA生産削減30-40%）の構造的要因と一時性の判断（GPT DR指摘）
12. **推論ファーストへのシフトのインフラ影響** -- 2026年にAIコンピュートの2/3が推論に移行。サーバーレスGPU・トークン課金モデルの普及度とAIXSの対応戦略
13. **AMD MI300X/MI350Xの市場浸透度** -- $1.99/hrでNVIDIA独占を崩壊中（DO/RunPod）。AIXS多ベンダーGPU対応の緊急度

---

## 7. 最終結論

### 7.1 AIXSがGPU機能で真正面からぶつかる直接競合トップ5

| 順位 | 競合 | 競合度合い | 根拠 | AIXS の勝ち筋 |
|---|---|---|---|---|
| 1 | **Modal** | 最高 | ML/AI 実践者向けのコンピュート＋サーバーレス。同じユーザー層（研究者・エンジニア）を狙う。Python-native の卓越した開発者体験 | R&D統合（実験管理・モデルレジストリ・ワークフロー）。Modal は W&B/MLflow を外部統合するが、AIXSは内蔵。マルチクラウド対応。日本/EU市場での地域対応 |
| 2 | **RunPod** | 高 | 最安価格帯。サーバーレス＋Pods＋Instant Clusters で幅広いワークロードカバー。コミュニティが大きい | 価格では勝てない。R&D 特化ワークフロー（実験追跡、HP最適化、結果比較、チームコラボ）で上位レイヤーの価値を提供 |
| 3 | **Together AI** | 中-高 | GPU クラスター＋推論プラットフォーム。透明な予約価格。FlashAttention エコシステム | R&D 実験ライフサイクル全体をカバー（Together は推論＋学習クラスターのみ）。ノートブック、実験管理、データ管理で差別化 |
| 4 | **Lambda Labs** | 中 | 研究者ブランド。JupyterLab 標準。1-Click Clusters。シンプルな体験 | 統合 R&D プラットフォーム（Lambda は SSH + JupyterLab のみ）。ジョブオーケストレーション、モデル管理、チーム機能で大幅差別化 |
| 5 | **Hugging Face (Inference/Training)** | 中 | 500K+ モデルの最大エコシステム。推論エンドポイント。DGX Cloud パートナーシップ | HF エコシステムと統合しつつ、コンピュート価格で勝つ（特にGCP経由のH100 $10/hr を大幅に下回る）。統合コンピュート管理で差別化 |

### 7.2 AIXSが地域別に最も刺さりやすい訴求メッセージ

| 地域 | 最も刺さるメッセージ | ターゲット顧客 | 想定パートナー |
|---|---|---|---|
| 日本 | 「データ主権 + 国内初の統合R&Dプラットフォーム + ABCI/さくらと統合」 | GENIAC参加企業、AI スタートアップ、大学研究室 | さくらインターネット、ABCI/AIST |
| EU | 「Sovereign by design -- EU AI Act Ready、EuroHPC統合」 | EU AI スタートアップ・SME、大学研究グループ、製薬/自動車 | EuroHPC Federation、Nscale/Scaleway |
| UK | 「British AI のためのスケーラブルなR&Dプラットフォーム -- AIRR互換」 | AI スタートアップ、大学研究者 | UKRI/AIRR |
| 韓国 | 「ソブリンAI開発を加速 -- National AI Computing Center統合」 | K-Moonshot 161社、AI スタートアップ、KAIST等大学 | NACC、KISTI |
| UAE/サウジ | 「マルチベンダーGPUオーケストレーション + ソブリンコンピュート最適化」 | Core42、HUMAIN、KAUST、政府機関 | Core42/G42、HUMAIN |
| インド | 「コスト最適化 -- IndiaAI補助金コンピュートの価値を最大化」 | AI スタートアップ、IndiaAI 認定プロバイダユーザー | Yotta、E2E Networks |
| シンガポール | 「プレミアムコンピュートの効率最大化 -- ASEANハブ」 | NSCC ユーザー、AI Singapore参加者 | NSCC、AI Singapore |
| イスラエル | 「Innovation Authority GPU からスケールアップ -- スタートアップフレンドリー」 | 342 GenAI スタートアップ、防衛テック企業 | Innovation Authority、Nebius |
| US | 「GPU時間からインサイトまでを一つのプラットフォームで」 | ML/AI 研究者・エンジニア | 直接 or マルチクラウドブローカー |

### 7.3 今後さらに深掘りすべき未解決論点トップ10

| # | 論点 | 重要度 | 理由 |
|---|---|---|---|
| 1 | **AIXSの技術的アーキテクチャ選定** | 最高 | マルチクラウドオーケストレーション vs 自社インフラ vs ハイブリッド。この選択が価格設定、マージン構造、スケーラビリティを決定する |
| 2 | **日本市場参入の具体的Go-to-Market** | 最高 | ISMAP認定取得タイムライン、さくら/ABCIとのパートナーシップ交渉、ターゲット顧客のパイロット計画 |
| 3 | **Modal との差別化の深掘り** | 高 | Modal の開発者体験は高いと評価されているが、ユーザー数・具体的評価指標は非公開[GPT-5.4-pro補足, 2026-03-28]。AIXSが「Modal + W&B + マルチクラウド」の統合で本当に勝てるかの検証 |
| 4 | **NVIDIA B200/GB200 世代の価格インパクト** | 高 | 次世代GPUの商用展開が現行の価格構造を根本的に変える可能性 |
| 5 | **EU CADA 制定後の非EUプロバイダへの影響** | 高 | CADA がEU拠点要件を課す場合、AIXSのEU戦略に直接影響 |
| 6 | **GPU過剰供給問題の動態** | 中-高 | 日本（さくら業績悪化）、中国（稼働率30%）で過剰供給が進行中。AIXSが「稼働率最適化」を価値提案にできるかの検証 |
| 7 | **マルチベンダーGPU対応の技術的実現性** | 中-高 | NVIDIA + AMD（MI300X/MI325X/MI350X）+ Huawei Ascend の異種混合環境をサポートする場合の技術的課題 |
| 8 | **防衛AI市場への参入可否** | 中 | イスラエル $1B+、各国の防衛AI投資は大きいが、セキュリティクリアランス等の参入障壁が高い |
| 9 | **R&D自動化エージェント（AI Scientist等）との統合戦略** | 中 | AIXSがR&D自動化エージェントのバックエンドコンピュートになるか、自らエージェント機能を持つかの戦略選択 |
| 10 | **サステナビリティ要件への対応** | 中 | シンガポール PUE 1.25、EU エネルギー効率規制、UAE 再生可能エネルギー。これらが顧客選択に与える影響 |

---

## 8. 参考文献・出典一覧

### ハイパースケーラー (AWS / GCP / Azure)

- [AWS EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
- [AWS EC2 Capacity Blocks Pricing](https://aws.amazon.com/ec2/capacityblocks/pricing/)
- [AWS GPU Price Reduction (June 2025)](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/)
- [p5.48xlarge Pricing - Vantage](https://instances.vantage.sh/aws/ec2/p5.48xlarge)
- [p5en.48xlarge Pricing - Vantage](https://instances.vantage.sh/aws/ec2/p5en.48xlarge)
- [AWS EBS Pricing](https://aws.amazon.com/ebs/pricing/)
- [SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload.html)
- [SageMaker MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Google Cloud GPU Pricing](https://cloud.google.com/compute/gpus-pricing)
- [Google Cloud GPU Machine Types](https://docs.cloud.google.com/compute/docs/gpus)
- [a3-highgpu-8g Pricing - CloudPrice](https://cloudprice.net/gcp/compute/instances/a3-highgpu-8g)
- [GCP Spot VMs Pricing](https://cloud.google.com/spot-vms/pricing)
- [GCP Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts)
- [Azure VM Pricing](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/)
- [Azure ND H100 v5 Series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndh100v5-series)
- [Azure Distributed GPU Training](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-train-distributed-gpu)

### GPU特化プロバイダ

- [CoreWeave Pricing](https://www.coreweave.com/pricing)
- [CoreWeave AI Object Storage](https://www.coreweave.com/blog/benchmark-results-coreweave-ai-object-storage-delivers-2-gb-s-per-gpu-throughput-across-any-number-of-gpus)
- [CoreWeave Security & Compliance](https://docs.coreweave.com/policies/terms-of-service/security-and-compliance)
- [Lambda Labs Pricing](https://lambda.ai/pricing)
- [Lambda Billing Overview](https://docs.lambda.ai/public-cloud/billing/)
- [RunPod Pricing](https://www.runpod.io/pricing)
- [RunPod GPU Pricing](https://www.runpod.io/gpu-pricing)
- [RunPod Security & Compliance](https://docs.runpod.io/references/security-and-compliance)
- [Modal Pricing](https://modal.com/pricing)
- [Modal Multi-Node Training](https://modal.com/docs/guide/multi-node-training)
- [Together AI Pricing](https://www.together.ai/pricing)
- [Together AI GPU Clusters](https://www.together.ai/gpu-clusters)

### 推論/Dev/エコシステムプロバイダ

- [Baseten Pricing](https://www.baseten.co/pricing/)
- [Baseten Cold Starts](https://docs.baseten.co/performance/cold-starts)
- [Replicate Pricing](https://replicate.com/pricing)
- [Replicate acquired by Cloudflare](https://siliconangle.com/2025/11/17/cloudflare-acquires-ai-deployment-startup-replicate/)
- [Hugging Face Pricing](https://huggingface.co/pricing)
- [HF Inference Endpoints Pricing](https://huggingface.co/docs/inference-endpoints/en/pricing)
- [DigitalOcean GPU Droplets Pricing](https://www.digitalocean.com/pricing/gpu-droplets)
- [Paperspace Pricing](https://www.paperspace.com/pricing)

### 日本市場

- [さくらインターネット 高火力 Portal](https://gpu.sakura.ad.jp/)
- [高火力 DOK](https://www.sakura.ad.jp/koukaryoku-dok/)
- [高火力 VRT GPU](https://cloud.sakura.ad.jp/products/server/gpu/)
- [高火力 PHY](https://www.sakura.ad.jp/koukaryoku-phy/)
- [GPUSOROBAN Main](https://soroban.highreso.jp/)
- [GPUSOROBAN High-Speed Computing](https://soroban.highreso.jp/compute)
- [GPUSOROBAN AI Supercomputer Cloud](https://soroban.highreso.jp/aispacon)
- [GMO GPU Cloud](https://gpucloud.gmo/)
- [GMO GPU Cloud Pricing](https://gpucloud.gmo/price/)
- [WebARENA IndigoGPU Pricing](https://web.arena.ne.jp/indigogpu/price/)
- [ABCI Pricing](https://abci.ai/ja/how_to_use/tariffs.html)
- [ABCI 3.0 System Overview](https://docs.abci.ai/v3/ja/system-overview/)
- [METI Cloud Program](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html)
- [GENIAC (METI)](https://www.meti.go.jp/policy/mono_info_service/geniac/index.html)
- [Sakura Internet earnings decline (ITmedia)](https://www.itmedia.co.jp/aiplus/articles/2507/28/news101.html)
- [National AI Basic Plan (Japan Times)](https://www.japantimes.co.jp/news/2025/12/23/japan/ai-first-basic-plan/)
- [AI Promotion Act (FPF)](https://fpf.org/blog/understanding-japans-ai-promotion-act-an-innovation-first-blueprint-for-ai-regulation/)
- [Japan cloud market (Mordor Intelligence)](https://www.mordorintelligence.com/industry-reports/japan-cloud-computing-market)
- [Japan AI infrastructure growth (IDC)](https://www.idc.com/resource-center/blog/7x-growth-in-just-three-years-japans-ai-infrastructure-will-surge-past-5-5-billion-in-2026-idc-reveals/)

### EU/UK市場

- [EuroHPC Our Supercomputers](https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en)
- [EuroHPC AI Factories](https://www.eurohpc-ju.europa.eu/ai-factories_en)
- [EuroHPC AI Factory Access Modes](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en)
- [EU InvestAI Initiative](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_467)
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU Cloud and AI Development Act](https://www.eu-cloud-ai-act.com/)
- [UK AIRR Programme](https://www.gov.uk/government/publications/ai-research-resource/airr-advanced-supercomputers-for-the-uk)
- [UKRI Isambard-AI and Dawn Access](https://www.ukri.org/opportunity/access-to-isambard-ai-and-dawn-airr-supercomputers-gateway-route/)
- [UK AI Investment Announcement](https://www.gov.uk/government/news/ai-to-power-national-renewal-as-government-announces-billions-of-additional-investment-and-new-plans-to-boost-uk-businesses-jobs-and-innovation)
- [Mordor Intelligence Neocloud Market](https://www.mordorintelligence.com/industry-reports/neocloud-market)
- [Holori Cloud Market Share 2026](https://holori.com/cloud-market-share-2026-top-cloud-vendors-in-2026/)
- [Segler Consulting - Europe's AI Gambit](https://www.seglerconsulting.com/europes-ai-gambit-an-in-depth-analysis-of-the-eurohpc-ai-factories-and-the-quest-for-digital-sovereignty)
- [Crunchbase EU Funding 2025](https://news.crunchbase.com/venture/european-funding-nudged-higher-ai-led-2025/)

### アジア市場（中国・韓国・台湾）

- [Alibaba leads China AI cloud (SCMP)](https://www.scmp.com/tech/big-tech/article/3325034/alibaba-holds-wide-lead-over-rivals-bytedance-huawei-tencent-chinas-ai-cloud-market)
- [China AI compute centers 2025 (Sinolytics)](https://sinolytics.de/global-business-news/blog/technology/china-ai-compute-centers-2025/)
- [China AI data centers unused (MIT Tech Review)](https://www.technologyreview.com/2025/03/26/1113802/china-ai-data-centers-unused/)
- [China's GPU Trio Rise (TrendForce)](https://www.trendforce.com/news/2025/10/07/news-chinas-gpu-trio-rise-as-nvidia-retreats-decoding-moore-threads-metax-and-cambricon/)
- [Beijing AI Compute Voucher Plan](https://www.beijing.gov.cn/zhengce/zhengcefagui/202310/t20231016_3280015.html)
- [NVIDIA and South Korea AI infrastructure](https://nvidianews.nvidia.com/news/south-korea-ai-infrastructure)
- [250,000+ GPUs across South Korea (DCD)](https://www.datacenterdynamics.com/en/news/nvidia-to-deploy-more-than-250000-gpus-across-south-korea-with-samsung-sk-group-and-hyundai-all-announcing-ai-factories/)
- [KISTI 6th supercomputer (HPE)](https://www.hpe.com/us/en/newsroom/press-release/2025/05/korea-institute-of-science-and-technology-information-selects-hewlett-packard-enterprise-to-build-south-koreas-largest-supercomputer.html)
- [South Korea $2.9B AI computing hub](https://koreatechtoday.com/south-korea-commits-2-9-billion-to-build-national-ai-computing-hub-by-2030/)
- [NVIDIA Taiwan research supercomputer](https://blogs.nvidia.com/blog/taiwan-research-supercomputer/)
- [Taiwan sovereign AI push (BowerGroupAsia)](https://bowergroupasia.com/taiwans-sovereign-ai-push-strategy-policy-programs-and-implications-for-businesses/)
- [Foxconn AI factory with NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia)

### 新興市場（中東・インド・シンガポール・イスラエル）

- [Core42 Self-Service AI Cloud (GITEX 2025)](https://www.g42.ai/resources/news/core42-unveils-self-service-demand-ai-cloud-platform-nvidia-accelerated-computing-gitex-global-2025)
- [Stargate UAE Launch](https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae)
- [Microsoft $15.2B UAE Investment](https://blogs.microsoft.com/on-the-issues/2025/11/03/microsofts-15-2-billion-usd-investment-in-the-uae/)
- [Saudi Arabia Declares 2026 Year of AI](https://houseofsaud.com/saudi-arabia-year-of-artificial-intelligence-2026/)
- [HUMAIN and NVIDIA AI Factories](https://nvidianews.nvidia.com/news/saudi-arabia-and-nvidia-to-build-ai-factories-to-power-next-wave-of-intelligence-for-the-age-of-reasoning)
- [Project Transcendence $100B](https://www.cio.com/article/3602900/saudi-arabia-launches-100-billion-ai-initiative-to-lead-in-global-tech.html)
- [India GPU Infrastructure 80,000+](https://introl.com/blog/indias-gpu-infrastructure-landscape-a-comprehensive-survey)
- [IndiaAI Mission 34,000 GPUs](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2132817&reg=3&lang=2)
- [Singapore National AI Strategy 2.0](https://www.smartnation.gov.sg/initiatives/national-ai-strategy/)
- [Singapore $27B AI Revolution (Introl)](https://introl.com/blog/singapore-ai-revolution-27-billion-investment-2025)
- [DC-CFA2 200MW Allocation](https://www.datacenterdynamics.com/en/news/singapore-opens-call-to-develop-200mw-of-data-center-capacity/)
- [Nebius $140M Israel Supercomputer](https://www.datacenterdynamics.com/en/news/nebius-to-build-and-operate-140m-israeli-national-supercomputer/)
- [Israeli Startups $15.6B in 2025](https://www.calcalistech.com/ctechnews/article/b1o113p8mbx)
- [342 GenAI Startups $20B+](https://medium.com/@inthacitycorporation/342-israeli-generative-ai-startups-raise-20b-by-2025-a-198-surge-since-may-2024-revealed-by-2b8f2ffdbb4b)

### 市場分析・比較

- [GPU Cloud Pricing Comparison 2025 (Verda)](https://verda.com/blog/cloud-gpu-pricing-comparison)
- [H100 Rental Prices Comparison (IntuitionLabs)](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)
- [GPU Price Comparison (GetDeploying)](https://getdeploying.com/reference/cloud-gpu)
- [GPU Price 2025 Report (Cast AI)](https://cast.ai/reports/gpu-price/)
- [H100 Cloud Pricing 41+ Providers (GetDeploying)](https://getdeploying.com/gpus/nvidia-h100)
- [GPU as a Service Market $49.84B by 2032 (Fortune Business Insights)](https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797)
- [Neocloud Market (Mordor Intelligence)](https://www.mordorintelligence.com/industry-reports/neocloud-market)
- [Middle East $100B+ Infrastructure (Introl)](https://introl.com/blog/middle-east-ai-revolution-uae-saudi-arabia-100b-infrastructure-plans)
- [GPU Cloud Price Collapse (Introl)](https://introl.com/blog/gpu-cloud-price-collapse-h100-market-december-2025)
- [Rise of GPU Marketplaces 2026](https://compute.exchange/blogs/the-rise-of-gpu-marketplaces-in-2026)

### Deep Research補足出典（Gemini Deep Research）

- [Spheron GPU Cloud Pricing](https://spheron.network)
- [Hyperstack GPU Cloud](https://hyperstack.cloud)
- [MiqroForge Quantum-Classical Integration](https://quantumzeitgeist.com)
- [ORCA Computing CUDA-Q Framework](https://orcacomputing.com)
- [Sakura DOK January 2026 Pricing Update](https://sakura.ad.jp)
- [SambaNova AI](https://sambanova.ai)
- [GPU Cloud Pricing Comparison 2026 (gpu.fm)](https://www.gpu.fm/blog/cloud-gpu-providers-comparison-2026)
- [fal.ai Serverless GPU Pricing](https://fal.ai)

### Deep Research補足出典（GPT Deep Research）

- [OECD AI VC Investment Report 2025](https://www.oecd.org/en/publications/venture-capital-investments-in-artificial-intelligence-through-2025_a13752f5-en/full-report.html)
- [Pax Silica Investment Fund (Tom's Hardware)](https://www.tomshardware.com/tech-industry/semiconductors/trump-administration-targets-4-trillion-pax-silica-investment-fund-for-semiconductors)
- [Federal Reserve: State of AI Competition](https://www.federalreserve.gov/econres/notes/feds-notes/the-state-of-ai-competition-in-advanced-economies-20251006.html)
- [KPMG Global VC Q2 2025](https://kpmg.com/xx/en/media/press-releases/2025/07/global-vc-investment-holds-steady-in-q2-25-amid-ai-surge.html)
- [India AI Market (AI Market Trends)](https://aimarkettrends.co.uk/news/ai-review-of-ai-market-size-trends-in-2025-2030-by-country-statistics-in-uk-europe-us-china-saudi-india-brazil-turkey-and-uae)
- [GPU Price Hikes 2026 (TechRadar)](https://www.techradar.com/computing/gpu/absurd-gpu-pricing-update-new-report-shows-painful-reality-of-graphics-card-price-hikes-particularly-for-nvidia-models)
- [Memory Shortage Impact on GPUs (Acer Blog)](https://blog.acer.com/en/discussion/3846/why-gpu-prices-are-expected-to-rise-in-2026)
- [CES 2026: Training to Inference Shift (Computerworld)](https://www.computerworld.com/article/4114579/ces-2026-ai-compute-sees-a-shift-from-training-to-inference.html)
- [US H200/MI325X Export Rules (Tom's Hardware)](https://www.tomshardware.com/tech-industry/artificial-intelligence/u-s-posts-official-h200-and-mi325x-ai-gpu-export-rules-to-china-but-with-plenty-of-caveats)
- [Sovereign AI Ecosystems (Forbes)](https://www.forbes.com/councils/forbesbusinesscouncil/2026/03/09/how-countries-are-building-their-sovereign-ai-ecosystems-and-what-it-means-for-startups/)
- [EY: Global GenAI VC 2025](https://www.ey.com/en_ie/newsroom/2025/12/global-genai-vc-investment-reaches-record-87-billion-in-2025-as-sovereign-wealth-funds-drive-strategic-growth-ey)
- [Sakana AI Scientist ICLR Paper (TechCrunch)](https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that/)
- [FutureHouse Robin AI Discovery](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system)

---

## 9. Deep Research補足（Gemini / GPT / GPT-5.4-pro Review）

本レポート作成後、Gemini Deep Research、GPT Deep Research（gpt-4o-search-preview）、およびGPT-5.4-pro（gpt-4o-search-preview + Web Search）によるレビュー・追加調査を実施し、以下の知見を統合した。

### 9.1 Gemini Deep Research の主要貢献

**調査日:** 2026-03-28 | **対象:** GPU Cloud Pricing, Regional Market, Competitive Differentiation, Emerging Trends

1. **B200/Blackwell世代の価格データ:** Lambda ($3.79-$4.99/hr)、RunPod ($5.99/hr)、Modal ($6.25/hr)、Together AI ($5.50/hr)、Baseten ($9.98/hr)、CoreWeave ($8.60/hr) のB200価格を初めて体系的に収集
2. **さくらDOK価格更新（2026年1月）:** 0.83円/秒 = 2,988円/hr（8-GPU）= ~$2.50/GPU-hrと大幅値下げを確認。4TB NVMe付属
3. **新規競合プロバイダ:** Spheron（分散型GPU集約、H100 $2.01/hr、Spot $0.99/hr）、Vast.ai（H100 $1.49-$2.27/hr）の詳細価格
4. **AMD MI300Xの台頭:** DigitalOcean/RunPodで$1.99/hrでの提供を確認。NVIDIA独占崩壊の兆候
5. **量子-古典統合:** MiqroForge、ORCA Computing（NVIDIA CUDA-Qフレームワーク）によるGPU-QPUハイブリッドワークフローの具体例
6. **Physical AI:** LLMの自律ロボティクス適用（クラウドGPU→エッジJetson蒸留→テレメトリフィードバック）トレンド
7. **GPU価格ボラティリティ:** 2026年初頭にHBM不足で10%価格反発（$2.00→$2.20/hr）。A100は$1.00/hr未満に下落
8. **ソブリンAI詳細:** EU InvestAI EUR 200B + 5 AI Gigafactories（各100,000チップ）、日本METI ¥1.23T FY2026、シンガポール一人当たり$600 NVIDIA支出

**完全版:** [appendix_gemini_deep_research.md](./appendix_gemini_deep_research.md)

### 9.2 GPT Deep Research の主要貢献

**調査日:** 2026-03-28 | **モデル:** gpt-4o-search-preview | **対象:** GPU Pricing, Global Market, R&D Automation, Market Trends

1. **グローバルデータセンター数:** 米国4,049、EU 2,250、中国379、日本219、韓国270、インド152（2024年Federal Reserve調査）
2. **AI VC投資の最新データ:** 米国$194B（世界の75%）、EU $15.8B（6%）、中国$13.9B（5%）（2025年OECD報告）
3. **米国Pax Silicaファンド:** $4T目標（初期$250M）でエネルギー・鉱物・半導体サプライチェーン強化
4. **GPU価格反発の要因分析:** GDDR6/GDDR7メモリ不足、NVIDIA30-40%生産削減、2025年11月-2026年2月に世界平均15%上昇、RTX 5090は最大31%上昇
5. **推論シフトの定量化:** 2025年にAIコンピュートの50%が推論、2026年には2/3に達する見込み（Computerworld CES 2026報告）
6. **R&D自動化システムの詳細:** Sakana AI（$30Mシード→2026年2月シリーズAで総額~$50M[GPT-5.4-pro補足]、ICLR採択）、FutureHouse Robin（2025年5月初の科学的発見）、Google AI Co-Scientist（2025年2月発表、ペイウォール除外制限）
7. **インドAI市場成長:** $8B（2024年）→$17B（2027年予測）、38,000+ GPU確保（100,000目標）、Rs 115-150/GPU-hr（$1.40-$1.80）で世界最安
8. **サウジHUMAIN:** $135.2B GDP押上効果（2030年）
9. **マルチクラウドオーケストレーション:** SkyPilot、dstackの台頭
10. **輸出規制最新:** 2026年1月にH200/MI325Xの対中国輸出規制強化（TPP・DRAM帯域制限）

**完全版:** [appendix_gpt_deep_research.md](./appendix_gpt_deep_research.md)

### 9.3 GPT-5.4-pro レビュー（gpt-4o-search-preview + Web Search）

**調査日:** 2026-03-28 | **モデル:** gpt-4o-search-preview (web_search_options: high) | **方法:** レポート全体を3セクションに分割し、各セクションをWeb検索付きで査読

**レビュー概要:**
- 事実誤り指摘: 8件（うち修正反映済み: 5件）
- 欠落データ補足: 6件（うち反映済み: 3件）
- 戦略改善提案: 6件
- 追加競合指摘: 5社

**主要な修正・補足:**

1. **H100価格帯の精緻化:** 「$2-4/GPU-hr」→「$2.50-$6.00/GPU-hr」に更新。プロバイダ種別（GPU特化 vs ハイパースケーラー）による価格帯の区分を明確化
2. **B200推論スループット:** 「H100比15倍」→NVIDIAの公称値は最大30倍だが、実測ベンチマークでは用途により5-20倍程度の幅があることを注記
3. **AMD MI300X価格:** $1.99/hrの出典をDigitalOcean/RunPodに明確化。公式価格ではなくプロバイダ提供価格であることを注記
4. **Alibaba Cloud AIクラウドシェア:** 35.8%→~38%（2025年末時点）に更新
5. **日本ハイパースケーラーシェア:** 55.82%→~60%（2025年末時点）に更新
6. **Sakana AI資金調達:** $30Mシード→2026年2月シリーズAで追加調達、総額~$50Mに更新
7. **中国国産GPU:** Biren Technology（BR20Xシリーズ、2026年1月香港上場）、天数智芯（Tianshu Zhixin、同時期上場）を追加
8. **Meta GPU保有数:** 350,000+ H100は2025年末の導入目標であり、2026年3月時点の実績値は未公表であることを注記

**未反映の指摘（要追加検証）:**

| 指摘事項 | 理由 |
|---|---|
| CoreWeave Spot価格（H100 $1.49-$2.27/hr） | 出典の信頼性が不十分。CoreWeave公式は依然非公開。Vast.aiの価格と混同の可能性あり |
| Anthropic「Claude Cowork」の競合としての追加 | AIXSの主な競合軸（GPUコンピュート＋R&Dプラットフォーム）とは異なるレイヤー。AIエージェントプラットフォームとしての競合関係は別途分析が必要 |
| OpenAI のSaaS市場への影響 | GPUインフラ/R&Dプラットフォームとの直接的競合ではなく、上位レイヤーの市場動向として認識 |

**戦略的提言（GPT-5.4-proからの追加提案）:**

1. **ハイブリッドアーキテクチャ戦略:** マルチクラウドオーケストレーションと自社インフラのハイブリッドを採用し、価格設定・マージン・スケーラビリティの最適バランスを追求すべき
2. **Modal対抗の機能統合:** ModalがW&B/MLflowを外部統合に依存していることに対し、AIXSはこれらを内蔵することで「設定ゼロの実験管理」を実現し、開発者体験での差別化を図るべき
3. **四半期レビュー体制:** GPU価格・競合動向の変動が激しいため、本レポートの四半期更新体制を構築すべき

### 9.4 Deep Researchで埋まらなかった主要ギャップ

| 項目 | ステータス |
|---|---|
| CoreWeave Spot/予約価格の具体条件 | 依然非公開（GPT-5.4-proの$1.49-$2.27/hrは要検証） |
| Azure Reserved GPU Pricing詳細 | 依然非公開 |
| 中国国内GPU（Ascend, Cambricon, Biren, 天数智芯）のクラウド価格 | 断片的のまま。Biren/天数智芯の商用価格は2026年後半に判明見込み |
| Lightning AI / Brev.dev の詳細比較 | 未調査 |
| Modal multi-node training GA時期 | 未確認。ユーザー数・評価指標も非公開 |
| EU CADA制定後の具体的要件 | 未確定 |
| Anthropic/OpenAIのAIエージェント市場がAIXSに与える間接的影響 | 要分析（GPT-5.4-pro指摘） |

---

*本レポートは2026年3月10日時点の公開情報に基づき、2026年3月28日にDeep Research（Gemini / GPT）およびGPT-5.4-pro（gpt-4o-search-preview）によるレビューの知見を統合更新した。GPU市場は急速に変動するため、主要な価格・政策データは四半期ごとの更新を推奨する。*

