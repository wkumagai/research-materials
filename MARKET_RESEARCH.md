# 市場調査：地域別GPU利用実態

調査日: 2026-03-28〜29
データ期間: 2024年後半〜2026年3月
為替参考: 1 USD ≈ 150 JPY, 1 EUR ≈ 1.08 USD, 1 GBP ≈ 1.27 USD

---

## 1. 対象地域

アメリカ、EU、UK、中国、日本、カナダ、韓国、インド、UAE、サウジアラビア、シンガポール、イスラエル、台湾

---

## 2. 地域別サマリー表

| 地域 | 主なGPU利用経路 | 主な資金源 | 政府の計算資源施策 | 独自の取り組み | 出典 |
|---|---|---|---|---|---|
| アメリカ | ハイパースケーラー（AWS 28%/Azure 21%/GCP 14%）＋ネオクラウド（CoreWeave, Lambda, RunPod等） | VC（世界の75%、$194B）、企業R&D（$330B+ capex）、NSF/NIH/DOE | NAIRR（600+プロジェクト）、ACCESS（7,022ユーザー）、DOE HPC | VCクレジットが主要な初期アクセス経路、CalCompute設計中 | srgresearch.com, nsf.gov |
| EU | ハイパースケーラー（市場の70%）＋EuroHPC＋欧州ネオクラウド | Horizon Europe（AI ~€2B）、InvestAI（€200B目標）、国家資金 | EuroHPC AI Factories（19拠点）、57,000アクセラレータ | AI Factory SME/スタートアップ無料アクセス（最大50K GPU-hr）、GDPR/AI Act対応 | eurohpc-ju.europa.eu, srgresearch.com |
| UK | ハイパースケーラー＋AIRR公的基盤 | UKRI（£1B+）、VC（£1.8B、H1 2025）、Sovereign AI Fund £500M | Isambard-AI（5,448 GH200）、Dawn（1,024 Intel GPU） | AIRR無料アクセス（2M GPU-hrプール）、EU AI Act適用外 | gov.uk, nscale.com |
| 中国 | 国内クラウド（Alibaba 35.8%）＋智算中心（30+都市）＋企業備蓄 | 国家基金（RMB 1T+）、企業R&D（$70B+）、算力券（30+都市） | 东数西算（8ハブ）、智算中心（788 EFLOPS→1,037 EFLOPS予測） | 算力券（最大80%補助）、国産GPU義務化（政府支援DC）、GPU稼働率30%問題 | scmp.com, gov.cn |
| 日本 | ハイパースケーラー（~60%）＋国内クラウド＋ABCI | METI（¥1,146B+）、科研費（¥237.9B/年）、企業R&D（¥23T） | ABCI 3.0（6,128 H200）、GENIAC（~¥33.9B）、METI Cloud Program | GENIAC補助金（2/3補助）、国内プロバイダにMLプラットフォーム機能なし | meti.go.jp, abci.ai |
| カナダ | ハイパースケーラー＋大学クラスター | Compute Canada配分、NSERC | Compute Canada/Digital Research Alliance | 米国市場に準拠した利用パターン | alliancecan.ca |
| 韓国 | 国内クラウド（NHN/Naver/Kakao）＋財閥GPU工場 | KRW 10.1T（$7.3B）2026年AI予算、KRW 150T成長基金 | NACC（1 EFLOP）、KISTI HANGANG（8,496 GPU） | 260,000+ NVIDIA GPU確約、財閥主導、K-Moonshot（161社） | nvidia.com, koreatechtoday.com |
| インド | IndiaAI公的基盤＋民間GPUクラウド | IndiaAI（$1.25B/5年）、AWS $12.7B、Microsoft $3B | IndiaAI（38,000+ GPU、100,000目標） | 40%補助金割引（Rs 115-150/GPU-hr）、世界最安水準 | indiaai.gov.in |
| UAE | Core42ソブリンクラウド＋ハイパースケーラー | SWF（MGX $100B基金、Mubadala $12.9B） | Core42、Stargate UAE（1GW） | SWF主導巨額投資、US輸出許可（35K GB300）、年間500Kチップ枠交渉中 | g42.ai |
| サウジアラビア | HUMAIN（PIF）＋ハイパースケーラー | Project Transcendence $100B、PIF $36.2B | HUMAIN、KAUST Shaheen III（2,800 GH200） | 「AIの年」2026宣言、マルチベンダー戦略（NVIDIA+AMD+Qualcomm） | humain.com |
| シンガポール | NSCC＋ハイパースケーラー（供給制約下） | RIE2030（S$37B）、NAIS 2.0（S$1B+） | NSCC ASPIRE 2A+（20 PFLOPS） | DC-CFA規制（容量割当制）、NVIDIA全球売上の15%を占有 | nscc.sg |
| イスラエル | スタートアップ＋Innovation Authority＋NVIDIA | VC（$15.6B総額、$7.9B AI）、Innovation Authority $45M | 国家AIスパコン（4,000 B200、Nebius運営） | NVIDIA R&D拠点（5,000人）、防衛AI需要（$1B+） | innovationisrael.org.il |
| 台湾 | TWCC（NCHC）＋Foxconn私設 | NT$190B（$5.9B）4年計画、NT$10B AIスタートアップ基金 | NCHC（1,700+ GPU）、TWCC | Taiwan Compute Alliance、TSMC製造拠点だが国内計算基盤構築中 | nchc.org.tw |

---

## 3. 地域別詳細

### 3.1 アメリカ

#### GPUの利用経路

**ハイパースケーラー（AWS/GCP/Azure）**
- 2025年Q4のクラウド基盤市場シェア: AWS 28%、Azure 21%、GCP 14%、上位3社合計68% [srgresearch.com, 2025-Q4]
- AWS Bedrock: 10万超の組織が利用 [srgresearch.com]
- Azure AI Foundry: 8万社 [microsoft.com]
- Google: 8.5万超企業がGeminiで構築、700万人超の開発者がGeminiで開発、Vertex AI利用40倍 [blog.google, Google I/O 2025]

**GPU特化クラウド（ネオクラウド）**
- ネオクラウド全体: 2025年通年売上$23B超見込み、前年比205%成長 [srgresearch.com]
- CoreWeave: 2025年売上$5.131B、売上バックログ$66.8B、43 DC/850MW超 [investors.coreweave.com]
- Lambda: 15万人超のCloud users、5,000超のハードウェア/プライベートクラウド顧客 [lambda.ai]
- RunPod: 50万人超の開発者、$120M ARR、+90% YoY [runpod.io, 2026-01]
- Vast.ai: 10万人超ユーザー、月次課金顧客1.4万人超、GPU供給約2万基 [vast.ai]

**大学GPUクラスター**
- UT Austin (TACC): 5,000超の先端NVIDIA GPU [news.utexas.edu]
- MIT: 少なくとも1,542基超（ORCD 308基 + Engaging 384基 + SuperCloud 850基超） [orgchart.mit.edu]
- Stanford: 少なくとも440基（Sherlock 192基 + Marlowe 248 H100） [sherlock.stanford.edu]
- CMU: 296 H100 [cmu.edu]

**国のスーパーコンピュータ・研究用公共経路**
- NAIRR: 600超の研究/教育プロジェクト、6,000人の学生、全50州+DC+Puerto Rico、累計14.2M GPU-hours配分（2025年9月時点） [nsf.gov]
- ACCESS: 7,022 users / 3,260 projects / 20 resources（最新月次）、Maximize回で90プロジェクトに4M超GPU-hours [allocations.access-ci.org]
- DOE OLCF / Frontier: 37,000超のAMD MI250X GPU、2,072 users / 639 projects [olcf.ornl.gov]
- DOE ALCF / Aurora: 63,744 GPU、2,013 users / 565 active projects [alcf.anl.gov]
- NERSC / Perlmutter: 7,168 A100 GPU、11,000超の科学者 / 800超機関 [nersc.gov]

**企業オンプレ**
- Meta: 350,000 H100目標（2024年末、Zuckerberg発表）、他GPU込みで約600,000 H100-equivalent。2025年capex $66-72B [facebook.com]
- Microsoft: GPU台数未公表。FY2025 AI DC投資約$80B、FY2026でAI capacity 80%以上増強計画 [microsoft.com]
- Google/Alphabet: GPU台数未公表（TPU依存大）。2025年capex $85B [blog.google]
- AWS/Amazon: 2025年投資$100B超見込み [blogs.microsoft.com参考]
- 米国データセンター数: 約4,049（2024年） [Fed Reserve調査]

**スタートアップ向けクレジット**
- AWS Activate: 最大$100,000/社、2013年以降の累計提供額$7B [aws.amazon.com]
- Google for Startups Cloud Program: 通常最大$200,000、AI-firstなら最大$350,000 [startup.google.com]
- NVIDIA Inception: 22,000超のスタートアップ支援（米国内10,000社） [investor.nvidia.com]

**個人利用**
- Google Colab: 1,000万超MAU。2025年に高等教育向け無料Colab Pro提供開始 [blog.google]
- Kaggle: 2,500万登録ユーザー、150万 public notebooks [kaggle.com]

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| VC/AI投資 | 2025年米国AI VC約$194B（世界の75%）。Q2 2025にグローバル$1B+超大型AIディール6件すべてが米国発 | oecd.org |
| 企業R&D/capex | Microsoft $80B、Meta $66-72B、Alphabet $85B、Amazon $100B+。4社合計$330B超 | 各社IR |
| NSF/NIH/DOE公的研究費 | CloudBank 2.0: $20M/5年/年500プロジェクト。NAIRR累計14.2M GPU-hours。AI向け公的compute年率$30M-$50M以上（推定下限） | nsf.gov |
| 大学予算（内部資金） | Stanford Marlowe $30M、MIT ORCD $6.5Mで276 GPU発注、UT Austin Texas Legislature $20M | 各大学プレスリリース |
| スタートアップクレジット | AWS Activate累計$7B（年平均約$538M、世界）。Googleも合わせると年数億ドル規模（推定） | aws.amazon.com |

#### 政府施策・独自の取り組み

| 施策 | 詳細 | 出典 |
|---|---|---|
| NAIRR | 14連邦機関・28民間パートナー。600+プロジェクト、6,000学生。恒久的国家基盤への移行方針 | nsf.gov |
| ACCESS | 無料。7,022 users / 3,260 projects。申請は多くが24-48時間で承認 | allocations.access-ci.org |
| DOE Genesis Mission | 2025年11月開始。$320M超投資（American Science Cloud、Transformational AI Models Consortium等） | energy.gov |
| CHIPS Act | R&D Office $11B管理。$825M EUV Accelerator、SK hynix $3.87B AI向け先端パッケージ工場等 | nist.gov |
| CalCompute | California SB 53（2025年9月成立）。14 member consortium。2027年1月までに設計報告。まだ稼働前 | leginfo.legislature.ca.gov |
| NSF AI Institutes | 2025年に$100M投入 | nsf.gov |
| NSF CloudBank 2.0 | $20M grant / 5年 / 年500プロジェクト | nsf.gov |
| 輸出規制 | 2025年1月AI Diffusion Rule発出→5月撤回。対中高性能AI chip締め付けは維持・強化 | bis.doc.gov |

---

### 3.2 EU

#### GPUの利用経路

**ハイパースケーラー**
- 欧州クラウド市場規模: €61B（2024年）、€36B（2025年上期） [srgresearch.com]
- AWS/Azure/GCPの欧州合算シェア: 70% [srgresearch.com]
- 欧州事業者の合算シェア: 15%（SAP 2%、Deutsche Telekom 2%等） [srgresearch.com]
- GenAI専用GPUaaS/PaaS: 140-160%成長 [srgresearch.com]

**データ主権対応**
- Microsoft: 2025年2月にEU Data Boundary完了 [blogs.microsoft.com]
- AWS: 2026年1月にEuropean Sovereign Cloud一般提供（最初はドイツ・ブランデンブルク） [aws.amazon.com]
- Google Cloud: Frankfurt, Paris, Eemshaven等でSovereign Controls提供 [cloud.google.com]

**欧州ネオクラウド**
- Nscale: 2027年までに欧州へ10万超GPU。UK Loughtonは23,040 GB300 GPU（Q1 2027予定）。5,000超ユーザー [nscale.com]
- Nebius: 2025年3月末で約30,000 GPU（主にH200）。DC: フィンランド・フランス・アイスランド [sec.gov]
- OVHcloud: 500,000超サーバー、46 DC、1.6M customers。H100 $2.99/hから [corporate.ovhcloud.com]
- Scaleway: カスタムAIクラスタ最大1,016 H100 [scaleway.com]
- Fluidstack: 100,000超GPU under management。Mistral向けフランス拠点は18,000 GPU超へ拡張設計 [businesswire.com]

**EuroHPC主要GPUシステム**

| システム | GPU数 | AI利用実績 | 出典 |
|---|---|---|---|
| LUMI（フィンランド） | 11,912 MI250Xモジュール | 利用資源の過半がAI関連、約7,000 users、1.4億GPU時間、3,000超プロジェクト | docs.lumi-supercomputer.eu |
| Leonardo Booster（イタリア） | 13,824 A100 | CINECA全体で6,925 active users、AI/MLが15%のユーザー・14.2%の配分資源 | leonardo-supercomputer.cineca.eu |
| MareNostrum 5 ACC（スペイン） | 4,480 H100 | AI利用率未公表。容量の20%を産業向けに充当予定 | bsc.es |
| JUPITER Booster（ドイツ） | 約24,000 GH200 | AI学習向け40+ exaFLOPS（8-bit）見込み | fz-juelich.de |

**大学・国立クラスター**
- JUWELS（ドイツ）: 3,968 GPU（A100 3,744 + V100 224） [apps.fz-juelich.de]
- Jean Zay（フランス）: 3,700+ NVIDIA GPU（H100 1,456、A100 416、V100 1,832）、125.9 PF。2025年通常配分の40%、ダイナミック配分の75%がAI手法 [cnrs.fr]
- Snellius（オランダ）: 2024年に352 H100（88 nodes）追加、理論性能15→38 PF [surf.nl]
- Alvis（スウェーデン）: 884 GPU（AI/ML専用national resource） [naiss.se]

**企業オンプレ/専用**
- Deutsche Telekom + NVIDIA: 10,000 Blackwell GPU、0.5 ExaFLOPS、€1B超パートナーシップ [telekom.com]
- Mistral AI + Fluidstack: Essonne専用クラスタ18,000 GPU超へ拡張設計、40MW→100MW+ [businesswire.com]
- Stargate Norway（Nscale/Aker/OpenAI）: 100,000 NVIDIA GPU by end-2026、230MW [nscale.com]

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| Horizon Europe | 総額€93.5B（2021-2027）。AI R&D: €2.6B（2021-2022）、約€1.6B（2025年）、€2.023B（2026-2027） | digital-strategy.ec.europa.eu |
| InvestAI | €200B動員目標、うち€20BがAI gigafactories向け | digital-strategy.ec.europa.eu |
| GenAI4EU | 約€700M | digital-strategy.ec.europa.eu |
| AI Innovation Package | 2027年までに公私あわせて約€4B | digital-strategy.ec.europa.eu |
| EuroHPC全体 | 2021-2027で€10B | digital-strategy.ec.europa.eu |
| Digital Europe | AIに2021-2024で€1B超 | digital-strategy.ec.europa.eu |
| EU AI VC投資 | $15.8B（2025年、世界の6%）。年間€270B投資ギャップ | oecd.org |
| フランスAI投資パッケージ | €109B | 不明 |
| ドイツ技術イニシアティブ | €5.5B | 不明 |

**ERC研究助成（GPU調達関連ルール）**
- ERC Starting Grant: €1.5M/5年＋追加€1M。major equipment/large facilities accessに充当可 [erc.europa.eu]
- DFG（ドイツ）: €50K以上をmajor instrumentationと定義。Major Research Instrumentation Programmeで投資額の50%負担 [dfg.de]
- ANR（フランス）: service costsカテゴリ上限50% [anr.fr]

#### 政府施策・独自の取り組み

| 施策 | 詳細 | 出典 |
|---|---|---|
| EuroHPC AI Factories | 19拠点＋13 Antennas。SME/スタートアップ無料。Playground（2営業日）、Fast Lane（4営業日、最大50,000 GPUh）、Large Scale（10営業日、50,000 GPUh超） | eurohpc-ju.europa.eu |
| EU AI Act | GPAI obligations 2025年8月適用開始。10^25 FLOP超モデルはsystemic risk推定。研究exemptionあり。全面適用2026年8月 | digital-strategy.ec.europa.eu |
| GDPR/データ越境 | 第三国移転にChapter V＋essentially equivalent protection必要。医療・公共・防衛・金融でGPU調達先にデータ所在地要件 | edpb.europa.eu |
| GAIA-X | federated system/rules/verification framework（クラウド事業者ではない）。欧州委員会が€180M tenderでCloud Sovereignty Framework推進 | gaia-x.eu, commission.europa.eu |

**EuroHPC既存枠（即時利用可能）**
- 1 cut-offあたり合計約1,065,918 node-hours。固定枠: LUMI-G 35,000、Leonardo Booster 50,000、MareNostrum 5 ACC 32,000、MeluXina GPU 25,000、Karolina GPU 7,500、Vega GPU 7,100 [eurohpc-ju.europa.eu]
- EU域内データセンター数: 約2,250（2024年）

---

### 3.3 UK

#### GPUの利用経路

**ハイパースケーラー**
- 2024年UK cloud spend: £10.5B。AWSとMicrosoftが各30-40% [assets.publishing.service.gov.uk CMA調査]

**AIRR（AI Research Resource）**
- Isambard-AI: 5,448 GH200 [gov.uk]
- Dawn: 1,024 Intel Data Center GPU Max 1550 [hpc.cam.ac.uk]
- AIRR無償枠: Rapid 20,000 GPUh/3か月、Gateway 10,000 GPUh/3か月、Innovator 50,000-150,000 GPUh/6か月。Rapidのtime-to-access: 最大2か月 [gov.uk]

**ネオクラウド**
- Nscale: UK AI campus 23,040 GB300 GPU（Q1 2027）、50MW→90MW拡張可能。$2B調達、$14.6B評価額 [nscale.com]
- CoreWeave: £3.4B UK投資 [不明]

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| UKRI | £1B+追加投資（2030年までにコンピュート20倍） | gov.uk |
| Sovereign AI Fund | £500M（2026年4月開始） | assets.publishing.service.gov.uk |
| Sovereign AI Unit | up to £500M（British Business Bank連携） | assets.publishing.service.gov.uk |
| Spending Review 2025 | AI Opportunities Action Plan実装に£2B超（20倍AIRR、Sovereign AI Unit £500M、AISI £240M含む） | assets.publishing.service.gov.uk |
| UK AI VC | £1.8B（H1 2025） | 不明 |
| AIRR投資 | £350M超 by 2030 | dera.ioe.ac.uk |
| UKRI GPU調達ルール | 80% FEC。£25K超のequipment、specialist computer costsが対象 | ukri.org |

#### 政府施策

- EU AI Act適用外（ポストBrexit）。プロイノベーション・軽量規制
- EuroHPC AI Factory Antennaパートナーとして限定参加
- Data Protection Act 2018準拠

---

### 3.4 中国

#### GPUの利用経路

**国内クラウド**
- AI public cloud services（IDC 2024年）: Baidu AI CloudとAlibaba Cloudが各約25%で首位 [scmp.com]
- AI Cloud Market IaaS+PaaS+MaaS（Omdia 1H25）: Alibaba 35.8%、Volcano Engine 14.8%、Huawei 13.1%、Tencent 7.0%、Baidu 6.1% [asiatechwire.com]
- 国産GPUクラウド（Frost & Sullivan 1H25）: Baidu 40.4%、Huawei 30.1%、両社合計70%超 [datacenterdynamics.com]
- AI クラウド市場: H1 2025に55%成長し$2.7B [scmp.com]

**国際ハイパースケーラー**
- 法的にグレーな経路。中国の大学（四川大学、深圳大学等）がAWS/Azure経由でアクセス。50+公開入札文書で11+団体が制限技術を追求 [tomshardware.com]
- 2026年にUS House Remote Access Security Actを通過（抜け穴封鎖） [tomshardware.com]

**智算中心（インテリジェント・コンピューティング・センター）**
- 788 EFLOPS（FP16、2025年6月）、2025年末に1,037 EFLOPS予測 [sinolytics.de]
- 30+都市が建設中。500+新DCプロジェクト（2023-2024年） [trendforce.com]

**企業GPU備蓄**

| 企業 | 投資/GPU規模 | 出典 |
|---|---|---|
| Alibaba | $52.9B/3年 | scmp.com |
| ByteDance | $20B | 不明 |
| Tencent | capex 149% YoY増、$2.5B/四半期 | 不明 |
| DeepSeek | 50,000 Hopper + 10,000 A100（Fire-Flyer 2クラスター） | 不明 |

**GPU稼働率問題**
- GPU稼働率: 約30%。多くのDCが遊休 [trendforce.com, MIT Technology Review]
- H100レンタル価格: $8/hr（2023年）→ <$2/hr（2024年）、70%暴落 [panewslab.com]

**海外GPU租借（抜け穴）**
- 中国企業（Alibaba、ByteDance等）がシンガポール、マレーシア、インドネシアのDCからGPUリース [tomshardware.com]
- INF Techがジャカルタ経由で2,300 Blackwell GPUにアクセス [tomshardware.com]

#### 国産GPU

| メーカー | フラッグシップ | H100比性能 | 生産 | 備考 | 出典 |
|---|---|---|---|---|---|
| Huawei Ascend | 910C（dual-chiplet） | 推論約60%（H100 dense比、推定） | 7nm（SMIC、EUV無し） | 200K-300K chips/年推定。de facto国内標準。Atlas 900超節点384カードで300 PFLOPS | huawei.com |
| Cambricon | Siyuan 590 | 345 TFLOPS FP16。一部シナリオでH20相当と主張 | 7nm | 2024年に初の黒字 | cambricon.com |
| Moore Threads | S4000（第4世代） | FP16 100 TFLOPS（H100の約1割） | 不明 | 千卡級KUAEクラスタ、万卡級対応。IPO初日+400% | docs.mthreads.com |
| MetaX | 複数製品 | 不明 | 不明 | 2025年12月IPO ~$600M | cnbc.com |
| Biren | BR100 | BF16 1,024 TFLOPS（理論値H100 dense相当級） | 不明 | 大規模商用導入台数は未確認 | hc34.hotchips.org |
| Baidu Kunlun | P800 | 不明 | 不明 | 3万-3.2万卡規模集群を実運用。2024年出荷約7万枚（IDC） | cloud.baidu.com |

**2025年政策**: 政府支援データセンターは国産チップのみ使用義務。省政府は国産チップ使用施設に最大50%電力補助 [各種報道]

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| NSFC（自然科学基金） | AI special programs RMB 35M。10-15プロジェクト×RMB 2-3M | 不明 |
| MOST / 次世代AI Megaproject | ~RMB 50B（$7B）総額 | 不明 |
| 教育部＋CAS | RMB 2.4B（$327M）ICT関連state key labs | 不明 |
| 企業R&D | $70B+（2025年、トップインターネット企業） | goldmansachs.com |
| 算力券 | 30+都市（後述の都市別表参照） | scmp.com |
| VC/スタートアップAI投資 | RMB 287B（AIスタートアップ、2025年）。中国AI投資総額RMB 890B（$125B、18% YoY、世界の38%） | secondtalent.com |
| 国家基金 | RMB 1T（$138B）20年ガイダンスファンド（2025年）。AI産業投資基金 RMB 60B（$8.2B）。Big Fund III $47B（半導体） | thequantuminsider.com |
| 省/市基金 | 东数西算8ハブで総投資RMB 200B超 | gov.cn |

#### 算力券（Compute Vouchers）都市別

| 都市/省 | 年間予算 | 補助率 | 企業あたり上限 | 出典 |
|---|---|---|---|---|
| 上海 | RMB 600M（$84M） | 最大80% | 不明 | scmp.com |
| 深圳 | RMB 500M（$68M） | 50%（スタートアップ60%） | 不明 | scmp.com |
| 北京 | 非公開 | 最大20% | RMB 2M/年 | beijing.gov.cn |
| 成都 | 非公開 | 50% | RMB 1M/年（最低RMB 10K） | 不明 |
| 無錫 | RMB 50M | 不明 | 不明 | 不明 |
| 青陽 | 最大RMB 100M | 不明 | 不明 | 不明 |
| 武漢 | RMB 10M超/年 | 不明 | SME重点 | 不明 |
| 浙江省 | プログラム稼働中 | 不明 | 不明 | 不明 |

#### 政府施策

| 施策 | 詳細 | 出典 |
|---|---|---|
| 东数西算 | 2022年2月開始。8国家計算ハブ、10 DCクラスター。直接投資RMB 43.5B（$6.1B、2024年6月）、総駆動投資RMB 200B超。DCラック1.95M超 | gov.cn, sciencedirect.com |
| 2017 NAIDP | 2030年までにグローバルAIリーダー。国内AI産業RMB 1T＋関連産業RMB 10T目標 | 不明 |
| 2025年「AI+」イニシアティブ | 6重要領域でAI統合、2027年に70%超、2030年に90%超目標 | 不明 |
| 国家一体化計算ネットワーク | 民間・公共クラウドを全国統一プラットフォームに統合 | 不明 |
| 米国輸出規制 | 2022年10月: A100/H100輸出停止。2023年10月: 性能密度閾値で強化。2025年4月: H20停止。2025年7月: H20とAMD MI308販売再開。密輸ネットワーク8+件、各$100M超 | rand.org, tomshardware.com |

---

### 3.5 日本

#### GPUの利用経路

**ハイパースケーラー**
- クラウドサービスプロバイダーのAI最適化DC市場シェア: 55.82%（2024年） [mordorintelligence.com]
- 日本クラウド市場: $31.44B（2025年）→$80.85B（2031年）、17.05% CAGR [mordorintelligence.com]
- ハイパースケーラーの日本投資:

| プロバイダー | 日本投資額 | 詳細 | 出典 |
|---|---|---|---|
| AWS | $15.2B（¥2.26T）by 2027 | 東京4 AZ、大阪3 AZ。GENIAC Phase 2選定（EC2 P5 H100） | siliconangle.com, amazon.com |
| Microsoft Azure | $2.9B（2024-2026） | Japan East/West AI半導体アップグレード。MS Research Asia初の東京ラボ | itpro.com |
| Google Cloud | $730M+（2024年） | 千葉県印西市に初の自社DC。A3 GPU（H100）でGENIAC Phase 1選定（¥8.4B、7組織） | cloud.google.com |

**国内GPUクラウド（METI Cloud Program補助付き）**

| 企業 | 最大補助額 | 総投資 | GPU計画 | 出典 |
|---|---|---|---|---|
| さくらインターネット | ¥501B | ¥1,000B+ | 2,800+ H100（Phase 1）、8,000+ GPU含むB200（Phase 2、2027年） | meti.go.jp |
| ソフトバンク | ¥421B | ¥1,500B | ~4,000 Hopper GPU。GB200 NVL72（2025年12月運用開始）。目標25 EFLOPS | publickey1.jp |
| KDDI | ¥102.4B | ¥1,000B（4年） | スタートアップ・企業向けGPU compute | publickey1.jp |
| ハイレゾ（Highreso） | ¥77B | ~¥200B | 408 HGX H200（高松）。2nd DC（綾川）2026年開業。1,600 GPU総計画 | prtimes.jp |
| GMOインターネット | ¥19.3B | ~¥100B | H200 + Spectrum-X。TOP500 #37（世界）、Green500 #34（世界）/ #1（国内商用） | internet.gmo |
| RUTILEA | ¥25.6B | 不明 | AIコンピュートインフラ | meti.go.jp |

- さくらインターネット高火力 VRT: ¥990/hr（$6.60/hr）per H100 GPU [sakura.ad.jp]
- さくらDOK（2026年1月更新）: ¥2,988/hr（0.83円/秒）H100x8 = ~$2.50/GPU-hr [sakura.ad.jp]
- GPUSOROBAN: A100 80GB ¥398/hr（$2.65/hr）[soroban.highreso.jp]
- GMO GPUクラウド: 2024年11月開始、768 GPU実証済 [internet.gmo]

- 日本国内全プロバイダの特徴: インフラ提供のみ。マネージドMLプラットフォーム（ノートブック＋学習＋推論＋実験管理）を提供している事業者は存在しない [2026年3月時点の競合分析]

**大学共有GPUクラスター**
- 学際大規模情報基盤共同利用・共同研究拠点: 8中核機関（北海道大、東北大、東京大、東京科学大、名古屋大、京都大、大阪大、九州大） [jhpcn-kyoten.itc.u-tokyo.ac.jp]
- Miyabi（東京大学＋筑波大学 JCAHPC）: GH200（日本初）、TOP500 #28、2025年1月運用開始 [nikkei.com]
- 北海道大学ILCS: 96x H100（24ノード×4 GPU）＋~200 AI4S GPU。2025年4月アップグレード [不明]
- mdx: 320x A100 GPU、2サイト（東大柏＋阪大吹田）。¥50/hr（A100 spot VM）。9大学＋2研究所共同運営 [utelecon.adm.u-tokyo.ac.jp]

**国のスーパーコンピュータ**

| システム | 運営 | スペック | 出典 |
|---|---|---|---|
| ABCI 3.0 | AIST/AISol | 6,128x H200（766ノード）、6.22 EFLOPS（FP16）、2025年1月運用開始 | abci.ai |
| 富岳（Fugaku） | 理研 R-CCS | ARM A64FX（GPU非搭載）。元世界#1 | riken.jp |
| 富岳NEXT | 理研＋富士通＋NVIDIA | FUJITSU-MONAKA-X CPU + NVIDIA GPU hybrid。2029-2030年目標。FY2025予算¥73B | riken.jp |
| mdx | 9大学＋2研究所 | 320x A100。¥50/hr | utelecon.adm.u-tokyo.ac.jp |
| HPCI | 多機関ネットワーク | 富岳＋大学システムをSINET6で接続。2025年4月に国際帯域400Gbpsへアップグレード | nii.ac.jp |

**ABCI 3.0 料金（FY2025）**
- ポイント単価: ¥220（税込）
- 最低購入: 1,000ポイント（¥220,000）
- 8-GPUノード（rt_HF）: 16ポイント/時間 = ¥3,520/hr
- 1-GPUパーティション: 1.5ポイント/時間 = ¥330/hr（~$2.20）
- ユーザー数: ~3,000人、566グループ（~87%がAIST外部）
- [abci.ai]

**企業オンプレ**
- NTT Data: DGX B200 SuperPODベース「GPU as a Service」（2025年10月開始） [nttdata.com]
- Preferred Networks: 自社GPUクラスター（MN-3等）。GENIAC主要参加者 [不明]
- ソフトバンク: B200 DGX SuperPOD（10,000+ GPU）建設中 [不明]
- 大手製造業（トヨタ、ソニー等）: 内部GPUクラスター [不明]
- セキュリティ重視の日本企業はオンプレ/プライベートクラウドを選好 [nttpc.co.jp]

**個人・小規模チーム利用**
- Google Colab: 最も普及した個人利用手段 [不明]
- ABCI: 個人研究者も申請可能（日本の研究機関所属が条件） [abci.ai]
- mdx: ¥50/hr（大学研究者向け） [utelecon.adm.u-tokyo.ac.jp]
- さくら高火力: 100時間無料トライアル（法人ユーザー） [sakura.ad.jp]
- 日本国内データセンター数: 約219（2024年） [不明]

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| METI FY2026 AI・半導体予算 | ¥1.23T（$7.9B）、前年比4倍増 | 不明 |
| METI Cloud Program | ¥1,146B+（6+社への補助） | meti.go.jp |
| GENIAC | ~¥33.9B累計（3フェーズ、30+プロジェクト）。補助率: 最大2/3 | meti.go.jp |
| GENIAC-PRIZE | ~¥800M（AIエージェント開発、2025年5月） | meti.go.jp |
| 科研費（KAKENHI） | ¥237.9B/年（~$1.6B）。個別¥5M（若手）〜¥200M+（特別推進） | jsps.go.jp |
| JST AIP | ¥7.5B（FY2025）。AIP Center ¥3.0B | jst.go.jp |
| 国家AI基本計画 | ¥1T/5年（2025年12月閣議決定） | japantimes.co.jp |
| 半導体戦略 | ¥10T+（FY2030まで）。Rapidus ¥920B政府支援（2nm、2027年目標） | 不明 |
| 企業R&D | ¥23T（FY2024、過去最高） | nikkei.com |
| VC（スタートアップ） | 2024年総額¥779.3B。Sakana AI ¥38.3B（Series A、NVIDIA出資）、ハイレゾ ¥23.09B | startup-db.com, initial.inc |
| 大学予算 | 国立大学運営費交付金（MEXT）。Miyabi（東大＋筑波大）: 大学予算共同調達 | 不明 |

#### 政府施策

| 施策 | 詳細 | 出典 |
|---|---|---|
| ABCI 3.0 | 国内最大の政府AI計算基盤。LLM開発支援、大規模生成AI開発支援、Grand Challengeの各プログラム | abci.ai |
| GENIAC | 2024年2月開始。Phase 1: 10プロジェクト（Google Cloud A3 H100）。Phase 2: 20プロジェクト（AWS EC2 P5 H100）。Phase 3: 24プロジェクト。日本語学習データ不足が#1ボトルネック | meti.go.jp |
| AI推進法 | 2025年5月施行。罰則なしのイノベーション優先。著作権法30条の4（AI学習での著作物利用許可） | fpf.org |
| 国家AI基本計画 | 2025年12月閣議決定。¥1T/5年。公民AI企業（ソフトバンク+PFN+~10社、~100エンジニア）。1兆パラメータ国内基盤モデル目標 | japantimes.co.jp |
| METI Cloud Program | 経済安全保障推進法。クラウドを特定重要物資に分類。¥1,146B+補助 | meti.go.jp |
| 富岳NEXT | 日本初のGPU搭載フラッグシップスパコン。2029-2030年。¥73B FY2025。ゼッタスケールAI性能の可能性 | riken.jp |
| HPCI/SINET6 | 富岳＋8大学センターの連邦ネットワーク。国際帯域400Gbps（2025年4月） | nii.ac.jp |
| ISMAP | 政府クラウド調達に必須の認定制度 | 不明 |

**研究者の典型的なGPU利用パターン**

| ユーザー種別 | 一次GPU源 | バックアップ | 資金源 |
|---|---|---|---|
| 大学研究者 | ABCI / 大学クラスター / mdx | クラウド（AWS/GCPクレジット） | 科研費 / JST / 大学予算 |
| 国立研究所 | ABCI / 所内インフラ | HPCI | 機関予算 |
| AIスタートアップ | GENIAC補助金 / 国内クラウド | ハイパースケーラークレジット | VC / NEDO grants |
| 大企業 | オンプレDGX / プライベートクラウド | 国内GPUクラウド | 企業R&D予算 |
| 個人/学生 | Google Colab / 消費者GPU | mdx（¥50/hr） | 自費 / 奨学金 |

---

### 3.6 カナダ

#### GPUの利用経路
- Digital Research Alliance of Canada（旧Compute Canada）が全国共有計算基盤を運営
- 主要クラスター: Narval（Université de Montréal/Calcul Québec）、Cedar（Simon Fraser University）、Graham（University of Waterloo）、Niagara（University of Toronto）
- ハイパースケーラー（AWS/GCP/Azure）: 米国市場に準拠、制限なし利用可能
- Mila（モントリオールAI研究所）: 独自のGPUクラスター保有、カナダAI研究の中核 [mila.quebec]

#### 資金源
- NSERC（Natural Sciences and Engineering Research Council）: カナダの主要研究助成機関
- Canadian Foundation for Innovation（CFI）: 研究インフラ投資
- Pan-Canadian AI Strategy: 2017年開始、$443M（Phase 1）＋$2.4B追加（2024年Budget発表） [不明]
- Digital Research Alliance: 年間予算で全国研究者に無料compute配分

#### 政府施策
- Pan-Canadian AI Strategy（世界初の国家AI戦略、2017年）
- Canada's AI Compute Access Fund: 研究者向けGPUアクセス支援
- CIFAR（Canadian Institute for Advanced Research）: AI研究ネットワーク支援
- 米国市場と緊密に連動した利用パターン

---

### 3.7 韓国

#### GPUの利用経路

**国内クラウド**
- 政府が13,000+ NVIDIA GPUを調達（NHN Cloud: B200 7,656台、Kakao: B200 2,040台、Naver Cloud: H200 3,056台） [nvidia.com]
- SK Telecom: GPUaaS 2025年1月開始（H100/H200、加山/ソウル） [不明]

**財閥GPU工場**

| 企業 | GPU規模 | 用途 | 出典 |
|---|---|---|---|
| Samsung | 50,000+ GPU | 半導体AIファクトリー | nvidia.com |
| SK Group | 50,000+ GPU | アジア初の産業AIクラウド | nvidia.com |
| Hyundai | AIファクトリー | 自動運転＋ロボティクス | nvidia.com |

- 韓国全体: 260,000+ NVIDIA GPU確約 [datacenterdynamics.com]

**国家スーパーコンピュータ**
- KISTI HANGANG（第6世代）: 8,496 NVIDIA GPU（GH200）、~600 PFLOPS、HPE Cray EX4000。H1 2026完成。NVIDIA Center of Excellence（量子-GPUハイブリッド） [hpe.com]

**大学・研究**
- KAIST: 2026年にスタンドアロンAI学部新設（300人/年） [koreaherald.com]
- NRF/IITPグラント経由でcompute配分

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| 2026年AI予算 | KRW 10.1T（$7.3B）。2025年の3.3Tから206%増 | koreatimes.co.kr |
| 成長基金 | KRW 150T（$100B）。AI・半導体・バッテリー | 不明 |
| ソブリンAI開発 | $381M（2025年8月）。5コンソーシアム（Naver, SK Telecom, LG, NCSoft, Upstage）→2027年に2社に絞込み | 不明 |
| GPU調達 | KRW 1.634T。2025年末までに10,000 先端GPU＋民間3,000リース | 不明 |
| 企業投資 | $65B超合計（Samsung + SK） | introl.com |
| NACC | KRW 4T（$2.9B）by 2030 | koreatechtoday.com |
| NRF/IITPグラント | プロジェクトあたり最大KRW 360M。若手AI研究者にKRW 60B。戦略技術院生にKRW 599B | 不明 |
| MSIT R&D予算 | KRW 4.32T（2025年、44%が先駆的R&D） | 不明 |

#### 政府施策

| 施策 | 詳細 | 出典 |
|---|---|---|
| National AI Computing Center | 1 EFLOP。51%公的/49%民間。初期サービス2025年11月、本格運用2027年 | koreatechtoday.com |
| AI基本法 | AIガバナンスフレームワーク | 不明 |
| K-Moonshot | 161社パートナー（Samsung, SK, Hyundai, Naver, LG）。MSITがNRF/IITP連携で管理 | kmoonshot.com |
| OpenAI Stargate | MSIT MoU。Samsung/SK HynixがStargate参加。全羅南道3GW施設、$35B、最大200,000 GPU（2028年目標） | openai.com |

- データセンター数: 約270（2024年）
- 国産GPU製造なし（HBMメモリに特化: Samsung/SK Hynix）
- AI市場規模: $9B（2025年推定）

---

### 3.8 インド

#### GPUの利用経路
- IndiaAI Mission: 38,000+ GPU政府管理下（H100 12,896台、H200 1,480台、MI200/300 7,200台）。2026年末までに100,000 GPU目標 [不明]
- 民間: Yotta 32,768 GPU、E2E Networks、Tata Communications [不明]
- Reliance Jio: 1GW AI DC（Blackwell）建設中 [不明]
- PARAM シリーズ（C-DAC）: 国立スパコン基盤 [不明]
- 補助金付GPU-hour: Rs 115-150（$1.40-$1.80）で世界最安水準 [不明]
- クラウドGPU市場: 36.5% CAGRで$80M（2023年）→$1.32B（2032年） [不明]
- データセンター数: 152（2024年）

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| IndiaAI Mission | Rs 10,372 crore（$1.25B/5年）。2025-26年度予算でAI 4倍増 | 不明 |
| AWS | $12.7B投資 | 不明 |
| Microsoft | $3B投資 | 不明 |
| NVIDIA India Deep Tech Alliance | $2B | 不明 |
| AI VC | $643M（2025年、全スタートアップ取引の30-40%） | 不明 |

#### 政府施策
- IndiaAI Compute Capacity Program: 認定プロバイダ制度（Yotta, NextGen, E2E Networks, Jio）
- 42%割引（スタートアップ・研究者向け）で40%補助金提供
- C-DAC + AMDパートナーシップ
- 州レベル競争: Maharashtra, Gujarat, Karnataka
- AI市場: $8B（2024年）→$17B（2027年予測）

---

### 3.9 UAE・サウジアラビア

#### UAE

**GPUの利用経路**
- Core42（G42子会社）: ソブリンAIクラウド運営。GITEX 2025でH100セルフサービスプラットフォーム発表
- Microsoft-G42パートナーシップ: $15.2B投資（2023-2029）
- Stargate UAE: 1GW AIコンピュートクラスター（G42/OpenAI/Oracle/NVIDIA/SoftBank/Cisco）。初期200MW 2026年稼働、フルキャンパス5GW
- MBZUAI: K2 Think V2（70Bパラメータ、完全オープン）開発

**資金源**
- MGX（Mubadala + G42）: $100B基金
- Mubadala: 2025年に$12.9BをAI/デジタル化に投資
- 湾岸SWF: 2025年に全世界で$126B（全ソブリン資本の43%、過去最高）

**政府施策**
- National AI Strategy 2031
- Abu Dhabi Government Digital Strategy 2025-2027（100%ソブリンクラウド目標）
- US輸出許可: 35,000 GB300（2025年11月）。年間500,000チップ枠を交渉中

#### サウジアラビア

**GPUの利用経路**
- HUMAIN（PIF子会社）: フルスタックAI企業。Phase 1: 18,000 GB300 GPU。5年で数十万GPU目標。1.9GW（2030年）→6.6GW（2034年）
- マルチベンダー戦略: NVIDIA 500MW + AMD 500MW + Qualcomm 200MW
- KAUST Shaheen III: 2,800 GH200（中東#1、世界#18）
- SDAIA: 500+ H100（政府AI向け）
- $135.2BのGDP押上効果見込み（2030年）

**資金源**
- Project Transcendence: $100B
- PIF: 2025年に$36.2B展開（世界最大の単一ソブリンディールメーカー、AUM ~$930B）
- Google: $5-10B
- AMD: $10B/5年

**政府施策**
- 2026年を「AIの年」に宣言
- Vision 2030の96戦略目標中66がデータ駆動能力に関連
- 1M+国民をAI/データスキル訓練目標

---

### 3.10 シンガポール

#### GPUの利用経路
- NSCC ASPIRE 2A+: 20 PFLOPS（H100）
- 70+ DC、1.4GW容量、空室率1.4%（APAC最低）
- DC-CFA規制: 新規容量は政府割当制（DC-CFA2: 200MW、PUE 1.25・50%グリーンエネルギー要件）
- Oracle: $6.5B（最大131,072 Blackwell GPU）
- Jurong Island: 700MW低炭素DCパーク計画
- 人口600万人未満ながらNVIDIA全球売上の15%を占有（一人当たり$600をNVIDIAチップに支出、世界最高水準）

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| RIE2030 | S$37B（前回比32%増） | 不明 |
| NAIS 2.0 | S$1B（5年間、2025-2030） | 不明 |
| テック大手投資 | $26B+合計 | 不明 |
| AIスタートアップ累計 | S$8.4B（ASEAN取引量の58%） | 不明 |

#### 政府施策
- Smart Nation Initiative
- DCモラトリアム（2019年〜）による容量規制
- IMDA AIガバナンスフレームワーク（2026年1月にエージェンティックAI対応版）
- 輸出規制の影響なし（高性能NVIDIA GPUにフルアクセス可能）→ASEANリージョナルハブとして機能

---

### 3.11 イスラエル

#### GPUの利用経路
- 342 GenAIスタートアップ（累計$20B+）
- 国家AIスパコン: Nebius運営、4,000 B200、$140M（政府$45M）。70%企業、30%学術研究に割当
- Innovation Authority: 1,000 B200 GPUを割引配布
- NVIDIA: イスラエルに5,000人（Mellanox HQ 3,000人）。Rubinプラットフォームの4つの主要ネットワーキングコンポーネントをイスラエルで開発
- 防衛AI: 2025年$1B+、130+スタートアップが軍事統合

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| スタートアップ総額 | $15.6B（2025年） | 不明 |
| AI VC | $7.9B（61%成長） | 不明 |
| 防衛AI | $1B+（過去全年度合計を超過） | 不明 |
| Innovation Authority | $45M | 不明 |

#### 政府施策
- Telem Program（国家AI R&Dインフラ）
- MAFAT AI・自律研究ユニット（2025年1月）
- 国家AIプログラムは予算の1/5しか執行されておらず停滞中

---

### 3.12 台湾

#### GPUの利用経路
- TWCC（Taiwan Computing Cloud）: NCHC+ASUS+Quanta+台湾モバイル。元2,016 V100 GPU。H200+GB200+B300にアップグレード中 [nvidia.com]
- NCHC: 1,700+ GPU（H200 + GB200 NVL72 + HGX B300）、8x Taiwania 2性能、100-200 PFLOPS目標 [taiwannews.com.tw]
- Foxconn: 10,000 Blackwell GPU AIファクトリー（$1.37B投資）。Visionbay.aiソブリンAIスパコンセンター（H1 2026） [cnbc.com, nvidia.com]
- 台湾ODM: NVIDIA GPU サーバー出荷の70%超（Foxconn 24%、Inventec 22%、Quanta 15%）
- TSMC: 先端ノードGPUダイの80%超を製造（NVIDIA, AMD, Apple, Qualcomm）
- Tainan National Cloud Computing Center: 15MW、Nano 4 AIスパコン。新9.6MW AI DCで23MWへ拡張

#### 資金源

| 資金源 | 規模 | 出典 |
|---|---|---|
| 4年計画 | NT$190B（$5.9B） | techsoda.substack.com |
| 10 AI Infrastructure Initiatives（2026年） | NT$31.1B（$1B） | abtaiwan.org |
| AI Startup Fund（MODA） | NT$10B（$313M）/10年 | taiwannews.com.tw |
| Foxconn投資 | NT$42B（$1.37B）2025-2026 | cnbc.com |
| NSTC研究グラント | NT$5M/年/プロジェクト（国際共同研究） | 不明 |

#### 政府施策

| 施策 | 詳細 | 出典 |
|---|---|---|
| 10 AI Infrastructure Initiatives | Executive Yuan。2026年NT$31.1B。2040年までにNT$15T産出＋50万AI雇用目標 | abtaiwan.org |
| ソブリンAI目標 | 公的部門480 PFLOPS by 2029。総計1.2 EXAFLOPS by 2029 | bowergroupasia.com |
| AI基本法 | 2025年12月立法院通過、2026年1月公布。台湾初の包括的AIガバナンス法 | techpolicy.press |
| Southern Silicon Valley Project | 2025年1月行政院承認。嘉義・台南・屏東・高雄 | taipeitimes.com |
| Taiwan Compute Alliance | NSTC主導。NCHC, Foxconn, Wistron, AMD, NVIDIA等が参加 | 不明 |

- エネルギー供給制約がAI拡張の主要リスク
- 国産GPU設計なし（製造に特化）

---

## 4. 地域横断比較表

| 地域 | クラウド利用 | 大学GPU | 公的基盤 | スタートアップクレジット | オンプレ | 主な資金源 | 政府施策規模 | 補助金/バウチャー |
|---|---|---|---|---|---|---|---|---|
| アメリカ | 非常に高（AWS/Azure/GCPで68%＋ネオクラウド急成長） | 中（数百〜5,000 GPU/校） | 中（NAIRR/ACCESS/DOE HPC） | 非常に高（AWS $100K、GCP $350K） | 非常に高（Meta 350K+ H100等） | VC $194B、企業capex $330B+ | NAIRR＋ACCESS＋DOE $320M | AWS/GCP/NVIDIAクレジット |
| EU | 非常に高（米3社で70%）＋欧州ネオクラウド成長中 | 中（JUWELS 3,968、Jean Zay 3,700+） | 高（EuroHPC 57,000アクセラレータ） | 中（AI Factory 50K GPUh無料、OVH €10K） | 中（DT 10K Blackwell、Mistral 18K+） | Horizon €2B AI、InvestAI €200B目標 | EuroHPC €10B（2021-2027） | AI Factory SME無料、ERC最大€2.5M |
| UK | 非常に高（AWS/MS各30-40%） | 中-高（Isambard/Dawn） | 中（AIRR 2M GPUh） | 中 | 中（Nscale 23K GB300） | UKRI £1B+、VC £1.8B | Spending Review £2B+ | AIRR Innovator 50-150K GPUh |
| 中国 | 高（国内クラウド中心） | 中（清華/北京大等） | 高（智算中心788 EFLOPS） | 低（国際クレジット不可） | 非常に高（Alibaba $52.9B、DeepSeek 60K GPU） | 国家基金RMB 1T+、企業$70B+、算力券 | 东数西算RMB 200B+駆動投資 | 算力券（30+都市、最大80%） |
| 日本 | 高（ハイパースケーラー~60%） | 中（8大学拠点、Miyabi GH200） | 高（ABCI 6,128 H200） | 中（ハイパースケーラーcredits） | 中-高（大企業DGX） | METI ¥1,146B+、科研費¥237.9B/年 | METI Cloud Program ¥1,146B+ | GENIAC 2/3補助、ABCI開発加速 |
| カナダ | 高（米国準拠） | 中（Mila等） | 中（Digital Research Alliance） | 中 | 低-中 | Pan-Canadian AI Strategy $2.4B+$443M | Pan-Canadian AI Strategy | Alliance配分（無料） |
| 韓国 | 中-高（NHN/Naver/Kakao） | 中（KAIST等） | 高（NACC 1 EFLOP、KISTI 8,496 GPU） | 中（NVIDIA Inception） | 非常に高（Samsung/SK各50K+ GPU） | KRW 10.1T AI予算、KRW 150T成長基金 | NACC KRW 4T by 2030 | 政府がGPU調達して提供 |
| インド | 中（成長中） | 中 | 高（IndiaAI 38,000+ GPU） | 中 | 中（Reliance/Tata） | IndiaAI $1.25B、AWS $12.7B | IndiaAI Mission Rs 10,372 crore | 40-42%補助金（世界最安GPU-hr） |
| UAE | 低-中（Core42主導） | 低（MBZUAI） | 中（Core42、Stargate UAE 1GW） | 低 | 中 | SWF $100B+基金 | National AI Strategy 2031 | 低（SWF直接調達） |
| サウジアラビア | 低（HUMAIN主導） | 低-中（KAUST） | 中（HUMAIN 18K GB300、KAUST 2,800 GH200） | 低 | 低 | PIF $36.2B、Project Transcendence $100B | Year of AI 2026 | 低（国家直接投資） |
| シンガポール | 非常に高（供給制約下） | 低 | 中（NSCC 20 PFLOPS） | 中（AI Singapore） | 中 | RIE2030 S$37B | NAIS 2.0 S$1B | AI Singapore program |
| イスラエル | 高 | 中（Technion等） | 低（国家スパコン4,000 B200新設） | 高（Innovation Authority） | 低（スタートアップ中心） | VC $15.6B（AI $7.9B）、防衛$1B+ | Telem Program | Innovation Authority GPU配布 |
| 台湾 | 中（TWCC中心） | 中（NCHC経由） | 高（NCHC 1,700+ GPU） | 低-中（NT$10B基金） | 高（Foxconn 10K GPU） | NT$190B 4年計画 | 10 AI Infrastructure NT$31.1B | TWCC研究者向けアクセス |

---

## 5. 出典

### 米国
- srgresearch.com -- クラウド市場シェア・ネオクラウド成長データ
- nsf.gov -- NAIRR、ACCESS、CloudBank、NSF AI Institutes
- allocations.access-ci.org -- ACCESS利用統計
- energy.gov -- DOE Genesis Mission
- olcf.ornl.gov -- Frontier/OLCF利用統計
- alcf.anl.gov -- Aurora/ALCF利用統計
- nersc.gov -- Perlmutter/NERSC利用統計
- news.utexas.edu -- UT Austin GPU規模
- aws.amazon.com -- AWS Activate、EC2価格
- startup.google.com -- Google for Startups
- investor.nvidia.com -- NVIDIA Inception
- investors.coreweave.com -- CoreWeave財務
- lambda.ai -- Lambda Labs
- runpod.io -- RunPod
- vast.ai -- Vast.ai
- blog.google -- Google/Colab/Vertex AI
- microsoft.com -- Azure/Microsoft AI投資
- leginfo.legislature.ca.gov -- CalCompute (SB 53)
- nist.gov -- CHIPS Act
- bis.doc.gov -- 輸出規制

### EU・UK
- eurohpc-ju.europa.eu -- EuroHPC AI Factories、アクセスモード、システム仕様
- srgresearch.com -- 欧州クラウド市場シェア
- digital-strategy.ec.europa.eu -- Horizon Europe、InvestAI、GenAI4EU、AI Act
- blogs.microsoft.com -- EU Data Boundary
- aws.amazon.com -- European Sovereign Cloud
- cloud.google.com -- Sovereign Controls
- nscale.com -- Nscale GPU規模・UK campus・Stargate Norway
- sec.gov -- Nebius GPU規模
- corporate.ovhcloud.com -- OVHcloud
- scaleway.com -- Scaleway
- businesswire.com -- Fluidstack/Mistral
- docs.lumi-supercomputer.eu -- LUMI
- leonardo-supercomputer.cineca.eu -- Leonardo
- bsc.es -- MareNostrum 5
- fz-juelich.de -- JUPITER
- apps.fz-juelich.de -- JUWELS
- cnrs.fr -- Jean Zay
- surf.nl -- Snellius
- naiss.se -- Alvis/Arrhenius
- telekom.com -- Deutsche Telekom AI factory
- erc.europa.eu -- ERC助成ルール
- dfg.de -- DFG助成ルール
- anr.fr -- ANR助成ルール
- ukri.org -- UKRI助成ルール
- gov.uk -- AIRR
- assets.publishing.service.gov.uk -- UK Spending Review、CMA調査、Compute Roadmap
- dera.ioe.ac.uk -- AIRR投資
- edpb.europa.eu -- GDPR/データ越境
- gaia-x.eu -- GAIA-X
- commission.europa.eu -- Cloud Sovereignty Framework

### 中国
- scmp.com -- AI クラウド市場、算力券
- asiatechwire.com -- Alibaba AI Cloud シェア
- datacenterdynamics.com -- Baidu/Huawei 国産GPUクラウド、韓国GPU配備
- sinolytics.de -- 智算中心EFLOPS
- trendforce.com -- 国産GPU、遊休DC
- gov.cn -- 东数西算投資額
- sciencedirect.com -- 东数西算分析
- tomshardware.com -- 算力券、輸出規制抜け穴、Remote Access Security Act
- huawei.com -- Ascend 910C
- cambricon.com -- MLU370-X8
- docs.mthreads.com -- S4000
- hc34.hotchips.org -- Biren BR100
- cloud.baidu.com -- Kunlun
- thequantuminsider.com -- 国家ガイダンスファンド
- secondtalent.com -- 中国AI投資統計
- rand.org -- 輸出規制分析
- panewslab.com -- GPUレンタル価格下落
- goldmansachs.com -- 中国DC投資

### 日本
- meti.go.jp -- GENIAC、Cloud Program、10 AI Infrastructure
- abci.ai -- ABCI 3.0仕様・料金・利用統計
- sakura.ad.jp -- さくらインターネット価格
- soroban.highreso.jp -- GPUSOROBAN価格
- internet.gmo -- GMO GPU Cloud
- nttdata.com -- NTT Data GPU service
- publickey1.jp -- GPU投資概観
- prtimes.jp -- ハイレゾDC
- itmedia.co.jp -- さくらインターネット業績
- nikkei.com -- Miyabi、企業R&D統計
- jcahpc.jp -- JCAHPC
- jhpcn-kyoten.itc.u-tokyo.ac.jp -- 学際大規模情報基盤
- utelecon.adm.u-tokyo.ac.jp -- mdx
- riken.jp -- 富岳NEXT
- nii.ac.jp -- SINET6
- jsps.go.jp -- 科研費データ
- jst.go.jp -- JST CREST/PRESTO
- japantimes.co.jp -- 国家AI基本計画
- startup-db.com, initial.inc -- スタートアップ資金データ
- mordorintelligence.com -- 日本クラウド市場
- siliconangle.com, press.aboutamazon.com -- AWS日本投資
- fpf.org -- AI推進法分析

### 韓国
- nvidia.com -- 韓国GPU配備
- koreatechtoday.com -- NACC
- introl.com -- 韓国AI投資
- koreatimes.co.kr -- AI予算
- hpe.com -- KISTI HANGANG
- kisti.re.kr -- NVIDIA Center of Excellence
- kmoonshot.com -- K-Moonshot
- openai.com -- Stargate韓国
- koreaherald.com -- KAIST AI学部

### 台湾
- blogs.nvidia.com -- 台湾スパコン
- taiwannews.com.tw -- Taiwania 2後継、AI Startup Fund
- cnbc.com -- Foxconn AI投資
- bowergroupasia.com -- 台湾ソブリンAI
- nvidia.com -- Foxconn AIファクトリー
- nchc.org.tw -- TWCC
- techsoda.substack.com -- NT$200B計画
- techpolicy.press -- AI基本法
- taipeitimes.com -- Southern Silicon Valley
- abtaiwan.org -- 10 AI Infrastructure Projects
- asianintelligence.ai -- Tainan Cloud Centre

### インド・中東・シンガポール・イスラエル
- 出典の多くは統合市場調査レポートに基づく（個別URLは各ソースファイル参照）

### 市場全体
- oecd.org -- 世界AI VC投資統計
- precedenceresearch.com -- GPU as a Service市場
- businessmarketinsights.com -- アジア太平洋GPU市場
- epoch.ai -- 国別GPUクラスター性能シェア
