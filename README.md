# GPU クラウド競合分析・市場調査

調査日: 2026-03-28〜29
データ期間: 2024年後半〜2026年3月
為替参考: 1 USD = 150 JPY, 1 EUR = 1.08 USD

---

## 1. 競合分析

### 対象企業（30社）

**ハイパースケーラー（4社）**
AWS, Google Cloud (GCP), Microsoft Azure, Oracle Cloud (OCI)

**GPU特化クラウド（11社）**
CoreWeave, Lambda Labs, RunPod, Modal, Together AI, Crusoe, FluidStack, Hyperstack, Lightning AI, Brev.dev, Spheron

**マーケットプレイス（1社）**
Vast.ai

**推論・サーバーレス・エコシステム（4社）**
Baseten, Replicate, Hugging Face, Paperspace / DigitalOcean GPU Droplets

**欧州ネオクラウド（4社）**
Nscale, Scaleway, OVHcloud, Nebius

**日本国内（5社）**
さくらインターネット, GPUSOROBAN (ハイレゾ), GMO GPU Cloud, WebARENA IndigoGPU (NTTPC), ABCI 3.0 (産総研)

**中東（1社）**
Core42 (G42)

### H100 価格比較（1GPU・1時間あたり、オンデマンド）

| プロバイダー | 価格(/hr) | Spot価格 | 予約価格 | 課金単位 |
|---|---|---|---|---|
| Vast.ai (Verified DC中央値) | $1.55〜$2.27 | 変動制 | なし | 秒 |
| RunPod (PCIe community) | $1.99 | $1.35 | 1yr $2.03 | 秒 |
| Spheron | $2.01 | $0.99 | 非公開 | 秒 |
| Paperspace | $2.24 | なし | なし | 時間 |
| Hyperstack (SXM) | $2.40 | 非公開 | 非公開 | 非公開 |
| さくら DOK (2026年1月更新) | ~$2.50 | なし | なし | 秒(60s min) |
| RunPod (SXM community) | $2.69 | $1.50 | 1yr $2.61 | 秒 |
| Lambda Labs (1-Click Cluster) | $2.76 | なし | 要セールス | 分 |
| DigitalOcean GPU Droplets (HGX) | $3.39 | 非公開 | 12mo $2.50 | 秒(5min min) |
| Together AI (cluster) | $3.49 | 非公開 | 4-6m $2.25 | 分 |
| Oracle Cloud (BM.GPU.H100.8換算) | ~$3.49 | 非公開 | 非公開 | 非公開 |
| AWS (p5.48xlarge, 1GPU換算) | ~$3.85 (値下げ後) | $3.79 | 3yr $2.59 | 秒(60s min) |
| Modal | $3.95 | なし | なし | 秒 |
| Lambda Labs (8x) | $3.99 | なし | 要セールス | 分 |
| ABCI 3.0 (H200, 参考) | ~$4.40 | なし | 要申請 | ポイント制 |
| CoreWeave (HGX, 1GPU換算) | $6.16 | 非公開 | 要セールス(最大60%OFF) | 分 |
| Baseten | $6.50 | なし | なし | 分 |
| さくら VRT | $6.60 (¥990/hr) | なし | 月額キャップ有 | 時間 |
| AWS (値下げ前) | $6.88 | $3.79 | 1yr $2.97 | 秒(60s min) |
| Replicate | $5.49 | なし | なし | 秒 |
| GCP (a3-highgpu-8g, 1GPU換算) | $10.98 | $3.69 | 1yr CUD ~$7.14 | 秒(60s min) |
| HF Inference (GCP経由) | $10.00 | なし | なし | 分 |
| Azure (ND96isr_H100_v5, 1GPU換算) | $12.29 | $2.27 | 要セールス | 秒(5min min) |

出典: 各社公式サイト (2025-03〜2026-03)。詳細は [COMPETITOR_ANALYSIS.md](./reports/COMPETITOR_ANALYSIS.md) Section 2.1

### 研究者の実利用シナリオ別コスト

条件: H100 1台、ストレージ500GB、egress 100GB。出典: [COMPETITOR_ANALYSIS.md](./reports/COMPETITOR_ANALYSIS.md) Section 2.2

| プロバイダー | 72時間 (論文再現) | 1週間 (ファインチューニング) | 月160時間 (月間研究) | 8GPU x 30日 (大規模学習) |
|---|---|---|---|---|
| Vast.ai | $131 | $310 | $302 | $10,665 |
| RunPod | $219 | $518 | $509 | $17,913 |
| Paperspace | $185 | $461 | $530 | $15,852 |
| Lambda Cloud | $225 | $548 | $566 | $19,194 |
| Together AI | $259 | $623 | $629 | $21,680 |
| Modal | $284 | $664 | $632 | $22,752 |
| ABCI 3.0 | $318 | $744 | $713 | $25,541 |
| HF Endpoints | $337 | $792 | $800 | $26,799 |
| CoreWeave | $464 | $1,086 | $1,040 | $37,275 |
| Azure | $504 | $1,184 | $1,147 | $40,477 |
| AWS | $508 | $1,192 | $1,181 | $40,508 |
| GCP | $821 | $1,919 | $1,863 | $64,971 |

### 金額以外のメリット・デメリット

評価凡例: ◎=優秀 ○=良好 △=制限あり ×=未対応。出典: [COMPETITOR_ANALYSIS.md](./reports/COMPETITOR_ANALYSIS.md) Section 3.1

| プロバイダー | 即時利用 | GPU在庫 | Notebook | CLI/API | 分散学習 | 課金柔軟性 | 日本語 | ロックイン |
|---|---|---|---|---|---|---|---|---|
| AWS | ○ | ○ | ◎ | ◎ | ◎ | ◎ | ◎ | × (高) |
| GCP | ○ | ○ | ○ | ◎ | ◎ | ◎ | ◎ | △ (中-高) |
| Azure | ○ | ○ | ○ | ◎ | ◎ | ◎ | ◎ | △ (高) |
| CoreWeave | ○ | ○ | △ | ◎ | ◎ | ○ | △ | ○ (低) |
| Lambda Labs | ◎ | ○ | ○ | ◎ | ◎ | ◎ | △ | ○ (低) |
| RunPod | ◎ | △ | ○ | ◎ | △ | ◎ | △ | ○ (低) |
| Modal | ◎ | ○ | ◎ | ◎ | ○ | ◎ | △ | ○ (高) |
| Together AI | ○ | ○ | △ | ◎ | ◎ | ○ | △ | ○ (中) |
| Vast.ai | ◎ | △ | ○ | ◎ | △ | ◎ | △ | ○ (低) |
| Paperspace/DO | ◎ | ○ | ◎ | ◎ | ○ | ◎ | △ | ○ (低) |
| Lightning AI | ◎ | ○ | ◎ | ○ | ○ | ○ | △ | ○ (中) |
| HF Inference | ◎ | ○ | ◎ | ◎ | △ | ○ | △ | ◎ (低) |
| さくら | ○ | ○ | △ | ○ | ○ | ○ | ◎ | △ |
| GPUSOROBAN | ○ | ○ | △ | △ | △ | ○ | ◎ | ○ |
| ABCI 3.0 | △ | ◎ | △ | △ | ◎ | △ | ◎ | △ |

### 各社の主な特徴

**AWS** -- SageMakerで学習・追跡・デプロイが統合。143+認定。2025年6月にH100を44%値下げ。ただしオンデマンド価格はGPU特化勢の2-3倍。クォータ申請が必要で容量不足エラーが頻発。サービス間ロックインが大きい。

**GCP** -- Colab Enterprise連携。TPU v5e/v5p/v6が独自の強み。NVIDIA GPUのオンデマンド価格は最高値帯。

**Azure** -- ND H100 v5 + InfiniBandで大規模分散が容易。エンタープライズ統合 (EA, AD, Office 365)。5分最低課金。サービス階層が複雑。

**CoreWeave** -- K8s native。InfiniBand 3200Gbps。egress/IOPS無料。SOC 2 Type II, ISO 27001, HIPAA対応。2025年にW&Bを~$1.7Bで買収。8-GPU最小、K8s知識が前提。FY2025売上$5.131B。

**Lambda Labs** -- JupyterLabプリインストール、SSH即利用。1-Click Clusters (16-2000+ GPU)。egress無料。在庫不足が頻発。Spot/予約なし。東京リージョンなし。推定ARR $500M+。

**RunPod** -- H100 PCIe $1.99/hrで市場最安級。秒課金。FlashBoot (<2秒コールドスタート)。Community Cloudは信頼性にばらつき。GPU枯渇報告あり。ARR $120M+、50万人超の開発者。

**Modal** -- Python-native SDKでサブ秒コールドスタート。ゼロアイドルコスト。InfiniBand 3200Gbps (beta)。Spot/予約なし。セッション終了でボリューム削除。Modal SDKへのロックインあり。Series B $87M / $1.1B評価。

**Together AI** -- FlashAttention、200+モデル。Instant Clusters (8-64 GPU)。Web UI中心でNotebookはベータ。A100/L40S直接提供なし。Series B $305M。

**Vast.ai** -- P2Pマーケットプレイスで秒課金。ホスト品質と在庫が不安定。月間売上初$1M超 (2026-03)。手数料率25%。

**さくらインターネット** -- H100/H200の物理・VM両プラン。ISMAP認定。DOKが~$2.50/GPU-hrに値下げで国際競争力あり。ML機能なし。VRTは¥990/hr。METI補助金¥501B。

**GPUSOROBAN** -- 国内最安級A100 80GB ¥398/hr ($2.65/hr)。日本語サポート充実。API・実験管理が未整備。

**ABCI 3.0** -- 6,128 H200で国内最大規模 (6.22 EFLOPS)。学術価格。事前審査とキュー待ちで即時利用不可。カード払い不可。約3,000ユーザー。

**日本国内プロバイダの共通特徴:** 全社がインフラ提供のみ。マネージドMLプラットフォーム（ノートブック+学習+推論+実験管理の統合）を提供する事業者は2026年3月時点で存在しない。

--> 詳細: [COMPETITOR_ANALYSIS.md](./reports/COMPETITOR_ANALYSIS.md)

---

## 2. 市場調査

### 対象地域

アメリカ、EU、UK、中国、日本、カナダ、韓国、インド、UAE、サウジアラビア、シンガポール、イスラエル、台湾

### 地域別サマリー

| 地域 | 主なGPU利用経路 | 主な資金源 | 政府施策 | 独自の取り組み |
|---|---|---|---|---|
| アメリカ | ハイパースケーラー (AWS 28%/Azure 21%/GCP 14%) + ネオクラウド (CoreWeave, Lambda, RunPod等) | VC $194B (世界の75%)、企業capex $330B+、NSF/NIH/DOE | NAIRR (600+プロジェクト)、ACCESS (7,022ユーザー)、DOE HPC | VCクレジットが主要な初期アクセス経路。CalCompute設計中 |
| EU | ハイパースケーラー (市場の70%) + EuroHPC + 欧州ネオクラウド | Horizon Europe AI ~EUR 2B、InvestAI EUR 200B目標、国家資金 | EuroHPC AI Factories (19拠点)、57,000アクセラレータ | AI Factory SME/スタートアップ無料アクセス (最大50K GPU-hr)。GDPR/AI Act対応 |
| UK | ハイパースケーラー + AIRR公的基盤 | UKRI GBP 1B+、VC GBP 1.8B、Sovereign AI Fund GBP 500M | Isambard-AI (5,448 GH200)、Dawn (1,024 Intel GPU) | AIRR無料アクセス (2M GPU-hrプール)。EU AI Act適用外 |
| 中国 | 国内クラウド (Alibaba 35.8%) + 智算中心 (30+都市) + 企業備蓄 | 国家基金 RMB 1T+、企業R&D $70B+、算力券 | 东数西算 (8ハブ)、智算中心 (788 EFLOPS) | 算力券 (最大80%補助)。国産GPU義務化 (政府支援DC)。GPU稼働率30%問題 |
| 日本 | ハイパースケーラー (~60%) + 国内クラウド + ABCI | METI ¥1,146B+、科研費 ¥237.9B/年、企業R&D ¥23T | ABCI 3.0 (6,128 H200)、GENIAC (~¥33.9B)、METI Cloud Program | GENIAC補助金 (2/3補助)。国内にMLプラットフォーム機能を持つプロバイダなし |
| カナダ | ハイパースケーラー + 大学クラスター (Digital Research Alliance) | NSERC、Pan-Canadian AI Strategy $2.4B+$443M | Digital Research Alliance (旧Compute Canada) | 米国市場に準拠した利用パターン |
| 韓国 | 国内クラウド (NHN/Naver/Kakao) + 財閥GPU工場 | KRW 10.1T ($7.3B) AI予算、KRW 150T成長基金 | NACC (1 EFLOP)、KISTI HANGANG (8,496 GPU) | 260,000+ NVIDIA GPU確約。財閥主導。K-Moonshot (161社) |
| インド | IndiaAI公的基盤 + 民間GPUクラウド | IndiaAI $1.25B/5年、AWS $12.7B、Microsoft $3B | IndiaAI (38,000+ GPU、100,000目標) | 40%補助金割引 (Rs 115-150/GPU-hr)。世界最安水準 |
| UAE | Core42ソブリンクラウド + ハイパースケーラー | SWF (MGX $100B基金、Mubadala $12.9B) | Core42、Stargate UAE (1GW) | SWF主導巨額投資。US輸出許可 (35K GB300) |
| サウジアラビア | HUMAIN (PIF) + ハイパースケーラー | Project Transcendence $100B、PIF $36.2B | HUMAIN、KAUST Shaheen III (2,800 GH200) | 「AIの年」2026宣言。マルチベンダー戦略 (NVIDIA+AMD+Qualcomm) |
| シンガポール | NSCC + ハイパースケーラー (供給制約下) | RIE2030 S$37B、NAIS 2.0 S$1B+ | NSCC ASPIRE 2A+ (20 PFLOPS) | DC-CFA規制 (容量割当制)。NVIDIA全球売上の15%を占有 |
| イスラエル | スタートアップ + Innovation Authority + NVIDIA | VC $15.6B (AI $7.9B)、Innovation Authority $45M | 国家AIスパコン (4,000 B200、Nebius運営) | NVIDIA R&D拠点 (5,000人)。防衛AI需要 ($1B+) |
| 台湾 | TWCC (NCHC) + Foxconn私設 | NT$190B ($5.9B) 4年計画、NT$10B AIスタートアップ基金 | NCHC (1,700+ GPU)、TWCC | Taiwan Compute Alliance。TSMC製造拠点だが国内計算基盤を構築中 |

### 地域別詳細

#### アメリカ

**GPU利用経路**
- ハイパースケーラー: AWS 28%、Azure 21%、GCP 14%で上位3社合計68%。AWS Bedrock 10万超組織、Azure AI Foundry 8万社
- ネオクラウド: 全体で2025年売上$23B超 (前年比205%成長)。CoreWeave $5.131B、RunPod ARR $120M+、Lambda 15万Cloud users
- 大学クラスター: UT Austin 5,000+ GPU、MIT 1,542+基、Stanford 440+基、CMU 296 H100
- 公的基盤: NAIRR 累計14.2M GPU-hours、ACCESS 7,022ユーザー、DOE Frontier 37,000+ MI250X
- 個人: Google Colab 1,000万超MAU、Kaggle 2,500万登録ユーザー

**資金源**
- VC: 2025年米国AI VC約$194B (世界の75%)
- 企業capex: Microsoft $80B、Meta $66-72B、Alphabet $85B、Amazon $100B+の4社合計$330B+
- 公的研究費: CloudBank 2.0 $20M/5年、NAIRR累計14.2M GPU-hours
- 大学予算: Stanford Marlowe $30M、MIT ORCD $6.5M、UT Austin $20M
- スタートアップクレジット: AWS Activate累計$7B、Google最大$350K/社

**政府施策**
- NAIRR: 14連邦機関・28民間パートナー。600+プロジェクト、6,000学生
- ACCESS: 無料。申請は多くが24-48時間で承認
- DOE Genesis Mission: $320M超投資 (2025年11月開始)
- CHIPS Act: R&D Office $11B管理
- CalCompute: SB 53 (2025年9月成立)、14コンソーシアム。2027年1月までに設計報告

#### EU

**GPU利用経路**
- ハイパースケーラー: 欧州市場の70%。欧州事業者合算15% (SAP 2%、Deutsche Telekom 2%等)
- EuroHPC: LUMI 11,912 MI250X、Leonardo 13,824 A100、MareNostrum 5 ACC 4,480 H100、JUPITER ~24,000 GH200
- 欧州ネオクラウド: Nscale (2027年に10万超GPU)、Nebius (~30,000 GPU)、OVHcloud (50万超サーバー)、Scaleway (最大1,016 H100)
- データ主権対応: Microsoft EU Data Boundary完了、AWS European Sovereign Cloud (2026年1月GA)

**資金源**
- Horizon Europe: 総額EUR 93.5B (2021-2027)、AI R&D約EUR 2B
- InvestAI: EUR 200B動員目標
- EuroHPC全体: 2021-2027でEUR 10B
- EU AI VC投資: $15.8B (2025年、世界の6%)
- フランスAI投資: EUR 109B。ドイツ技術イニシアティブ: EUR 5.5B

**政府施策**
- EuroHPC AI Factories: 19拠点+13 Antennas。SME/スタートアップ無料 (Playground 2営業日、Fast Lane最大50,000 GPUh)
- EU AI Act: GPAI obligations 2025年8月適用開始。10^25 FLOP超モデルはsystemic risk推定。研究exemptionあり
- GDPR/データ越境: 医療・公共・防衛・金融でGPU調達先にデータ所在地要件
- GAIA-X: federated system/verification framework。欧州委員会EUR 180M Cloud Sovereignty Framework

#### 中国

**GPU利用経路**
- 国内クラウド: Alibaba 35.8%、Volcano Engine 14.8%、Huawei 13.1%、Tencent 7.0%、Baidu 6.1% (IaaS+PaaS+MaaS)
- 智算中心: 788 EFLOPS (2025年6月)、2025年末に1,037 EFLOPS予測。30+都市が建設中
- 企業備蓄: Alibaba $52.9B/3年、ByteDance $20B、DeepSeek 50,000 Hopper + 10,000 A100
- 国産GPU: Huawei Ascend 910C (推論約60% H100比)、Cambricon Siyuan 590、Baidu Kunlun P800
- GPU稼働率問題: 約30%。H100レンタル価格$8/hr (2023年) --> <$2/hr (2024年)、70%暴落

**資金源**
- 国家基金: RMB 1T ($138B) 20年ガイダンスファンド、AI産業投資基金RMB 60B、Big Fund III $47B (半導体)
- 企業R&D: $70B+ (2025年、トップインターネット企業)
- 算力券: 30+都市。上海RMB 600M (最大80%補助)、深圳RMB 500M (50%)、北京 (最大20%)
- AI VC: RMB 287B (AIスタートアップ、2025年)。中国AI投資総額RMB 890B ($125B、世界の38%)

**政府施策**
- 东数西算: 8国家計算ハブ、10 DCクラスター。総駆動投資RMB 200B超
- 2025年「AI+」イニシアティブ: 6重要領域でAI統合、2030年に90%超目標
- 国産GPU義務化: 政府支援データセンターは国産チップのみ使用義務。省政府は最大50%電力補助
- 米国輸出規制下: 2022年10月A100/H100停止、2025年4月H20停止。海外GPU租借 (SG/MY/ID経由) が抜け穴として存在

#### 日本

**GPU利用経路**
- ハイパースケーラー (~60%): AWS $15.2B日本投資 (by 2027)、Azure $2.9B、GCP $730M+
- 国内クラウド: さくらDOK ~$2.50/GPU-hr、GPUSOROBAN A100 ¥398/hr、GMO H200共用 ¥6,000/hr
- ABCI 3.0: 6,128 H200 (6.22 EFLOPS)、約3,000ユーザー
- 大学: 8中核機関 (北海道大〜九州大)、Miyabi (東大+筑波大、GH200)、mdx 320x A100 (¥50/hr)
- 個人・学生: Google Colab、mdx ¥50/hr、ABCI (研究機関所属が条件)

**資金源**
- METI FY2026 AI・半導体予算: ¥1.23T ($7.9B)、前年比4倍増
- METI Cloud Program: ¥1,146B+の補助 (さくら¥501B、ソフトバンク¥421B、KDDI ¥102.4B等)
- 科研費 (KAKENHI): ¥237.9B/年。個別¥5M (若手) 〜¥200M+ (特別推進)
- GENIAC: ~¥33.9B累計 (30+プロジェクト)。補助率最大2/3
- 企業R&D: ¥23T (FY2024、過去最高)
- VC: 2024年総額¥779.3B

**政府施策**
- ABCI 3.0: 国内最大の政府AI計算基盤。LLM開発支援、大規模生成AI開発支援プログラム
- GENIAC: 2024年2月開始。Phase 1-3で30+プロジェクト
- METI Cloud Program: 経済安全保障推進法でクラウドを特定重要物資に分類。¥1,146B+補助
- 国家AI基本計画: 2025年12月閣議決定。¥1T/5年。1兆パラメータ国内基盤モデル目標
- 富岳NEXT: 日本初のGPU搭載フラッグシップスパコン (2029-2030年)。¥73B FY2025予算

**研究者の典型的なGPU利用パターン**

| ユーザー種別 | 一次GPU源 | バックアップ | 資金源 |
|---|---|---|---|
| 大学研究者 | ABCI / 大学クラスター / mdx | クラウド (AWS/GCPクレジット) | 科研費 / JST / 大学予算 |
| 国立研究所 | ABCI / 所内インフラ | HPCI | 機関予算 |
| AIスタートアップ | GENIAC補助金 / 国内クラウド | ハイパースケーラークレジット | VC / NEDO grants |
| 大企業 | オンプレDGX / プライベートクラウド | 国内GPUクラウド | 企業R&D予算 |
| 個人/学生 | Google Colab / 消費者GPU | mdx (¥50/hr) | 自費 / 奨学金 |

#### その他の地域

**カナダ** -- Digital Research Alliance (旧Compute Canada) が全国共有計算基盤を運営。Pan-Canadian AI Strategy $2.4B+$443M。Mila (モントリオール) が研究の中核。米国市場に準拠した利用パターン。

**韓国** -- 2026年AI予算KRW 10.1T ($7.3B、前年比206%増)。260,000+ NVIDIA GPU確約。Samsung/SK各50,000+ GPU。NACC 1 EFLOP (2027年本格運用)。KISTI HANGANG 8,496 GPU。OpenAI Stargateの全羅南道3GW施設 ($35B)。

**インド** -- IndiaAI Mission Rs 10,372 crore ($1.25B/5年)。38,000+ GPU政府管理下、2026年末100,000目標。補助金付GPU-hr Rs 115-150 ($1.40-$1.80) で世界最安水準。Reliance Jio 1GW AI DC建設中。

**UAE** -- Core42ソブリンAIクラウド。Stargate UAE 1GW (G42/OpenAI/Oracle/NVIDIA等)。MGX $100B基金。US輸出許可35,000 GB300。年間500,000チップ枠を交渉中。

**サウジアラビア** -- HUMAIN (PIF子会社) Phase 1: 18,000 GB300。Project Transcendence $100B。KAUST Shaheen III 2,800 GH200 (中東#1)。マルチベンダー戦略。「AIの年」2026宣言。

**シンガポール** -- NSCC ASPIRE 2A+ 20 PFLOPS。DC-CFA規制で新規容量は政府割当制。NVIDIA全球売上の15%を占有。RIE2030 S$37B。輸出規制なしでASEANハブとして機能。

**イスラエル** -- 342 GenAIスタートアップ (累計$20B+)。VC $15.6B (うちAI $7.9B)。国家AIスパコン4,000 B200 (Nebius運営)。NVIDIA R&D拠点5,000人。防衛AI $1B+。

**台湾** -- NCHC 1,700+ GPU (H200+GB200+B300)。Foxconn 10,000 Blackwell GPU ($1.37B)。NT$190B 4年計画。TSMC製造拠点 (先端GPU ダイの80%超) だが国内計算基盤を構築中。エネルギー供給制約がリスク。

--> 詳細: [MARKET_RESEARCH.md](./reports/MARKET_RESEARCH.md)

---

## 関連ファイル

| ファイル | 内容 |
|---|---|
| [COMPETITOR_ANALYSIS.md](./reports/COMPETITOR_ANALYSIS.md) | 30社の価格・機能・財務データ比較。H100/H200/A100/L40S/B200/MI300X全GPU価格表、メリット・デメリット詳細 |
| [MARKET_RESEARCH.md](./reports/MARKET_RESEARCH.md) | 13地域のGPU利用実態。利用経路、資金源、政府施策、出典URL一覧 |
| [gpt54pro_price_comparison.md](./gpt54pro/gpt54pro_price_comparison.md) | 16社x4シナリオのGPU価格比較、研究者ペルソナ別年間コスト |
| [gpt54pro_regional_gpu_usage.md](./gpt54pro/gpt54pro_regional_gpu_usage.md) | 地域別GPU利用実態の補足調査 (GPT-5.4-pro) |
| [gpt54pro_comprehensive_analysis.md](./gpt54pro/gpt54pro_comprehensive_analysis.md) | Big Tech統合動向分析 (AWS/Google/Microsoft/NVIDIA) |
| [citation_verification.md](./review/citation_verification.md) | 主要30クレームの出典URL検証、矛盾データ5件の原因分析 |

## 調査手法

- Claude Opus 4.6 サブエージェント
- GPT-5.4-pro (Responses API + web_search_preview)
- Gemini Deep Research API
- 出典数: 500+
- 価格データ: 2025年3月〜2026年3月時点のスナップショット。GPU価格は3-6ヶ月で大幅に変動する
