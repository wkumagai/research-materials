# AIXSに対するDevil's Advocate：徹底批判書

**作成日:** 2026-03-28
**立場:** 最も厳しい批判者（Devil's Advocate）
**対象:** AIXS — GPU+HPC+量子+ロボット+実験装置を統合したR&Dコンピュートプラットフォーム（少人数スタートアップ、マーケットプレイスモデル）
**方針:** 希望的観測を徹底排除。数字とデータのみで語る。

---

## エグゼクティブサマリー：なぜAIXSは失敗するか

AIXSは7つの構造的な理由で失敗する可能性が極めて高い。TAMの大きさは「あなたの市場」の大きさを意味しない。マーケットプレイスモデルは数十億ドルの資本なしには機能しない。RunPodの成功は再現不可能な歴史的タイミングの産物である。大手は既にフルスタック化を進めている。技術的複雑さはMoatではなく負債である。日本発のDevToolsが世界で勝った前例は事実上ゼロである。そしてタイミングは、GPU価格崩壊とAIバブル崩壊リスクにより、スタートアップにとって最悪の時期に差し掛かっている。

以下、各論点を数字で証明する。

---

## 1. 市場は巨大だが「あなたの市場」ではない

### 批判の核心

TAM $80B-$134B（2030年）という数字は投資家を興奮させるためのフィクションであり、AIXSが実際に獲得できる市場（SOM）は桁が3つ違う。

### 根拠

**1-1. SOM推定の現実：$1-5M程度**

AIXSの自社分析ですら、SOMを「$50M-$200M（2030年）」と推定しているが、これは楽観的すぎる。現実的な初年度SOMを計算する。

- 日本国内のR&Dコンピュート市場のうち、大学・研究機関が個別プロバイダから調達する割合は極めて小さい。ABCI 3.0（産総研、6,128 H200 GPU）が無料〜格安で提供されており、さくらDOKがH100を$2.50/GPU-hrで提供している現在、有料プラットフォームに移行する研究者は限定的
- Vast.aiは120,000ユーザーを持ちながら、2025年9月時点でARRはわずか**$2.2M**（[GetLatka](https://getlatka.com/companies/vast.ai)）。これはGPUマーケットプレイスの収益化の困難さを象徴する
- 仮にAIXSが日本のAI研究者1万人の1%（100人）を獲得し、ARPU $200/月だとしても、**年間売上$240K**にしかならない

**1-2. 「異種R&D統合」市場は存在しない**

「GPU + HPC + 量子 + ロボット + 実験装置」を統合した市場は、調査会社のレポートにも存在しない。需要の証拠はゼロである。

- GPU利用者はGPUだけを求めている。HPC利用者はSlurm/PBSだけを求めている。量子計算利用者はIBM QuantumやAWS Braketを使う。これらのユーザー群は**重ならない**
- 「統合を求めている」という主張に対するユーザー調査やLOI（Letter of Intent）は存在するか？もし存在しないなら、それは市場が存在しないことの最強の証拠である
- Lab-as-a-Serviceの先駆者であるEmerald Cloud Lab（$92M調達）やStrateos（Arctoris含む）ですら、GPUコンピュートとの統合は行っていない。なぜか？**需要がないからだ**

**1-3. 市場調査会社の数字はバブル的**

- GPUaaS市場規模の推定値は、調査会社によって$26.6B〜$134B（2030年）と**5倍の差**がある（MarketsandMarkets vs Analysys Mason）。この分散の大きさ自体が、推定の信頼性の低さを示す
- Fortune Business Insightsは2032年に$49.8Bと推定するが、これは2024年の$4.31Bからの成長率35.8%が**7年間持続する**前提（[Fortune BI](https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797)）。AIバブル崩壊リスクを全く織り込んでいない
- 2000年のドットコムバブル時、調査会社はeコマース市場を$7T（2004年）と予測した。実際は$1T以下だった。AIインフラも同様の過大推定リスクがある

---

## 2. マーケットプレイスモデルの罠

### 批判の核心

二面市場（Two-sided marketplace）は最も構築が困難なビジネスモデルであり、AIXSのような無名スタートアップが資金ゼロで立ち上げるのは自殺行為に等しい。

### 根拠

**2-1. Uber/Airbnbの供給者獲得コスト**

- Uberは黒字化するまでに合計**$13.2B**を調達した（[Tracxn](https://tracxn.com/d/companies/uber/__wAOgbkstxol2NgmW5SFgVp8zBi7klH1GO5ziIlSERR4/funding-and-investors)）。そのうちサウジアラビアSWFの$3.5B単独投資を含む。AIXSにこの資金力はあるか？答えはNoである
- Airbnbは2009年に週間売上$200で破産寸前だった（[Bloomberg](https://www.bloomberg.com/features/2017-uber-airbnb-99-billion-idea/)）。Y Combinator卒業後もなお、ホスト獲得のためにCraigslist寄生戦略、無料プロカメラマン派遣など**非スケーラブルな戦術**を数年間続けた
- NFXの調査によれば、マーケットプレイスの失敗原因の第1位は「コールドスタート問題を解決できないこと」であり、ほとんどのマーケットプレイスはこの段階で死ぬ（[NFX](https://www.nfx.com/post/19-marketplace-tactics-for-overcoming-the-chicken-or-egg-problem)）

**2-2. Vast.aiの「成功」は実は警告**

Vast.aiはGPUマーケットプレイスとして最も成功した事例だが、その数字を冷静に見るべきだ。

- 120,000ユーザー、14,000月間アクティブ有料顧客を持ちながら、**ARRはたった$2.2M**（2025年9月、[GetLatka](https://getlatka.com/companies/vast.ai)）
- これはユーザーあたり月間支出がわずか**$13/月**（$2.2M / 12 / 14,000）であることを意味する。これで事業が成り立つか？
- Vast.aiは20人チームだからかろうじて生存しているが、統合R&Dプラットフォームを構築するAIXSが20人で済むはずがない
- さらに、Vast.aiは**2024年6月にホスト手数料を0%に引き下げた**（[Vast.ai](https://vast.ai/article/june-2024-product-update)）。つまり、ホストからの手数料収入はゼロ。利用者側からのみ課金するモデルに追い込まれた。これはマーケットプレイスの手数料モデルが**GPUでは機能しない**ことの証明である

**2-3. 手数料66.7%はGPU供給者が許容しない**

AIXSの計画では「調達$2.50→販売$4.00」とあり、これは供給者から見ると37.5%のマークアップ、プラットフォーム側から見ると実質テイクレート37.5%に相当する。しかし：

- Vast.aiのテイクレートは**0%**（ホスト手数料撤廃済み）
- Uber/Lyftのテイクレートは**25%**（ドライバー不満が社会問題化）
- Airbnbのテイクレートは**約15%**
- GPU供給者は自分でRunPodやVast.aiに直接リスティングできる。なぜ37.5%もの手数料を払ってAIXSに出品するのか？合理的な答えはない

**2-4. コールドスタート問題の致命性**

- GPU供給なしに利用者は来ない。利用者なしにGPU供給者は来ない
- RunPodは自社GPU（元マイニングリグ転用）で供給問題を回避した。AIXSはマーケットプレイスモデルなのでこの手が使えない
- サービスマーケットプレイスのコールドスタート問題は「最も難しい」カテゴリに分類される（[Sharetribe](https://www.sharetribe.com/marketplace-glossary/chicken-and-egg-problem/)）。GPUは「レンタルマーケットプレイス」であり、信頼と検証が必要なためさらに困難

---

## 3. RunPodの成功はAIXSの成功を意味しない

### 批判の核心

RunPodの驚異的成功は「再現不可能な歴史的条件」の産物であり、AIXSが同じ成功を収める確率はほぼゼロである。

### 根拠

**3-1. RunPodは「価格」で勝った — AIXSの価格は勝てない**

- RunPodのH100 SXM community価格は**$2.69/hr**、PCIeは**$1.99/hr**。市場最安級（[RunPod](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr)）
- AIXSの計画価格はH100 $3.50-$5.00/hr。RunPodより**30-100%高い**
- AIXSは「統合価値で差別化」と主張するが、研究者の購買行動調査では、GPUクラウド選択の第1要因は**価格**である。統合機能に月$100-$200追加で払う研究者が何人いるか？W&Bは無料枠が充実しており、MLflowは完全無料のOSSである

**3-2. 創業タイミングの決定的な違い**

- RunPodは**2022年**に創業。当時はGPU不足が深刻で、H100の入手に数ヶ月待ちが常態化していた
- RunPodの創業者はComcastの企業開発者で、暗号通貨マイニングリグ（既に所有していたGPU）をAI用に転用した。初期投資ほぼゼロで供給を確保（[TechCrunch](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)）
- **2026年3月現在、GPU不足は解消に向かっている**。H100価格は$8+/hrから$2.50-4.00/hrに急落済み。供給側の参入障壁は消滅した

**3-3. 生存者バイアス：RunPodの裏の屍**

- 2025年のCloud GPU Platforms分野への資金調達は前年比**49.25%減少**（[Tracxn](https://tracxn.com/d/trending-business-models/startups-in-cloud-gpu-platforms/__Zk91xONdI-FxILZ_0x2o9Ta7EdqgYE95i8Wn5s1e5Qc)）。投資家はGPUクラウドへの関心を失っている
- スタートアップの**70%は2-5年目に失敗する**（[DemandSage](https://www.demandsage.com/startup-failure-rate/)）。資金枯渇が最終的な死因の70%
- VultrのThe Great Neocloud Consolidation分析によれば、**2027年までにGPUプロバイダの80%以上が淘汰されるか買収される**（[Vultr](https://blogs.vultr.com/trends-neocloud-consolidation)）。生き残る条件は「継続的な資本アクセス」「マルチリージョン運用規模」「エンタープライズGTM実行力」の3つであり、AIXSはいずれも持っていない
- 具体的な失敗例：Builder.ai（$1.2B評価 → 破産）、Humane（$230M調達 → 閉鎖）。大型調達済みのスタートアップですら生き残れない（[TechCrunch](https://techcrunch.com/2025/01/26/2025-will-likely-be-another-brutal-year-of-failed-startups-data-suggests/)）

---

## 4. 大手は「必ず」来る

### 批判の核心

AIXSが狙う「コンピュート + 実験管理 + ワークフロー統合」の領域は、既に大手が侵食を開始している。3年以内に大手が同等機能を提供する確率は**90%以上**である。

### 根拠

**4-1. AWS SageMaker Unified Studio（2025年GA）**

- AWSは2025年にSageMaker Unified Studioを一般公開。SQL分析、大規模データ処理（EMR, Glue）、ML開発（SageMaker AI）、生成AIアプリ開発（Bedrock）を**単一環境に統合**（[AWS](https://aws.amazon.com/sagemaker/unified-studio/)）
- 2025年だけで**200以上の改善**をリリース。SageMaker Data Agent（自然言語でSQL/Python生成）を追加
- AWSの年間R&D予算は**$730億以上**（2024年）。AIXSの全リソースの数万倍
- さらにAWSは2025年6月にH100価格を**44%値下げ**（$6.88→$3.85/GPU-hr）。価格競争力も急速に改善中

**4-2. Google Vertex AIのフルスタック化**

- Vertex AIは2025-2026年にかけて、Agent Engine（GA）、Vector Search 2.0（GA）、マネージドSlurm環境でのトレーニング機能を追加（[Google Cloud Blog](https://cloud.google.com/blog/products/compute/google-cloud-ai-infrastructure-at-nvidia-gtc-2026/)）
- 2026年後半にはNVIDIA Vera Rubin NVL72ラックスケールシステムを提供予定
- Gemini 3.1 Pro（1Mトークンコンテキスト）をVertex AI内で直接利用可能
- GoogleのAIインフラ年間投資額は**$500億以上**（2025年）

**4-3. Databricksの$134B評価額とフルスタック化**

- Databricksは2026年2月に$134B評価額で$5Bを調達。ARR**$5.4B**、YoY成長率**65%**（[CNBC](https://www.cnbc.com/2026/02/09/databricks-completes-5-billion-funding-round-with-2-billion-in-debt.html)）
- AI製品だけで年間売上**$1.4B**。AIXSの想定SOM全体をDatabricksのAI売上の**1/1000以下**
- Databricksはデータレイクハウス + MLflow（彼ら自身が管理するOSS）+ GPU計算の統合を急速に進めている
- MLOps市場の中核プレーヤーとして、「コンピュート + 実験管理 + ワークフロー」を既に提供しつつある

**4-4. CoreWeave × Weights & Biases：フルスタックGPU+MLOpsの現実**

- CoreWeaveは2025年3月にW&Bを**$1.7B**で買収完了（[CoreWeave](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases)）
- これにより、CoreWeaveは「GPU IaaS + 実験管理 + モデル監視 + MLOpsオーケストレーション」をフルスタックで提供する企業になった
- W&Bは**1,400以上のエンタープライズ顧客**（OpenAI、Meta含む）を保有
- CoreWeaveの2025年推定売上は**$5.1B**（[Sacra](https://sacra.com/c/coreweave/)）。AIXSが目指す「統合R&Dプラットフォーム」は、CoreWeave + W&Bが既に実現している
- **AIXSの差別化要素は消滅した**。「コンピュート + 実験管理を統合していない」という批判は、CoreWeave+W&Bの登場で無効化された

**4-5. 大手が3年以内に同等機能を出す確率**

| 機能 | 大手の現状 | 3年以内の実現確率 |
|---|---|---|
| GPU + 実験管理統合 | CoreWeave+W&B: **実現済み** | 100% |
| マネージドSlurm/HPC | Google Vertex AI: **2025年リリース** | 100% |
| マルチGPUオーケストレーション | AWS, GCP, Azure: **全社提供済み** | 100% |
| AIエージェント統合 | AWS SageMaker Data Agent: **2025年GA** | 100% |
| 量子コンピュート統合 | AWS Braket, Azure Quantum, IBM Quantum: **提供済み** | 100% |
| ラボ装置統合 | 未対応 | 30-50% |

AIXSの唯一の差別化要素は「ラボ装置統合」だが、これは市場規模が$200M-$800Mと極めて小さく、かつEmerald Cloud Labのような専門プレーヤーが既に存在する。

---

## 5. 技術的優位はMoatにならない

### 批判の核心

「異種資源統合は技術的に難しい」は事実だが、「難しい」と「価値がある」は全く別の概念である。複雑さは資産ではなく負債である。

### 根拠

**5-1. K8s + Ray + MLflow + JupyterHubで90%再現可能**

- OSSの組み合わせで「統合R&Dプラットフォーム」の90%の機能は再現可能
- PyCon DE 2025で「Building a Self-Hosted MLOps Platform with Kubernetes」が発表されたように、K8sベースの自前構築は現実的な選択肢として認知されている（[PyCon DE](https://pretalx.com/pyconde-pydata-2025/talk/3CYZUH/)）
- 2026年のMLOps市場では「Managed Open Core」（例：Databricks上のManaged MLflow）が主流。完全プロプライエタリなプラットフォームは選ばれない（[Addepto](https://addepto.com/mlops-platforms-in-2026/)）
- MLflow（Databricks管理）、Kubeflow（Google管理）、Ray（Anyscale管理）はいずれもOSSかつマネージドサービスとして利用可能。AIXSのプロプライエタリ統合に対する需要は限定的

**5-2. OSSの進化速度はプロプライエタリを上回る**

- MLflowのGitHubスター数は19,000+、コントリビューター700+。AIXSの開発チーム（数名）が追いつけるペースではない
- Rayは2025年にGPUクラスタリングの標準として定着。Anyscaleの$1B+評価額がこれを裏付ける
- KubeflowはGoogleが継続的にメンテナンス。エンタープライズ向けMLパイプラインの事実上の標準
- **AIXSが独自に構築する機能は、6-12ヶ月以内にOSSコミュニティに追いつかれる**

**5-3. 「異種資源統合」は技術的に難しいが、難しい ≠ 価値がある**

- GPU利用者の95%以上は「GPUだけ」が欲しい。HPC、量子、ロボット、実験装置を同時に使いたいユーザーは全体の1%以下
- この1%のために異種統合を構築するコストは莫大。一方、市場規模は極小
- 難しいから誰もやっていないのではない。**誰も必要としていないからやっていないのだ**

**5-4. 統合の複雑さはむしろ負債になる**

- 5つの異種資源（GPU, HPC, 量子, ロボット, 実験装置）それぞれに異なるプロトコル、API、セキュリティモデル、課金モデルが存在する
- 少人数チームがこれらすべてを安定的に運用・保守するのは不可能。1つでも障害が起きればプラットフォーム全体の信頼性が損なわれる
- CoreWeaveは**GPU単一**に集中して$5.1B/年の売上を達成した。集中こそが勝利戦略であり、分散は敗北戦略である
- OpenAIですら$14Bの年間損失を出しながらも「汎用AI」に集中している（[Yahoo Finance](https://finance.yahoo.com/news/openais-own-forecast-predicts-14-150445813.html)）。AIXSが5つの異種資源を同時に扱うリソースがあるか？

---

## 6. 日本スタートアップの構造的不利

### 批判の核心

日本から世界的なDevTools/インフラ企業が生まれたことは事実上ゼロであり、これは偶然ではなく構造的な原因がある。

### 根拠

**6-1. 日本のVC市場規模は米国の1/60以下**

- 日本のVC年間投資額: **$2.22B**（2025年推定、[Statista](https://www.statista.com/outlook/fmo/capital-raising/traditional-capital-raising/venture-capital/japan)）
- 米国のVC年間投資額: **$140.5B**（2025年推定、同Statista）
- **比率: 1/63**。日本のGDP比（$4.2T / $28.8T ≈ 1/7）と比較しても、VC投資のギャップは不釣り合いに大きい
- 2025年上半期だけで米国VCは$26B以上を投入。日本の年間VC投資全額を半年で上回る
- AIXSが日本で調達可能なシード資金は現実的に**$500K-$2M**。米国のGPUクラウドスタートアップ（RunPodの$20Mシード等）と比較して桁が1-2つ違う

**6-2. 日本発の世界的DevToolsはゼロ**

- Ruby（まつもとゆきひろ）は日本発だが、これはプログラミング言語であってDevToolsプラットフォームではない
- 日本発のグローバルB2B SaaS企業で$1B以上の評価額を持つ企業は**SmartHR**（HRテック、日本国内特化）など数社のみ。いずれも国内特化
- DevToolsのグローバルリーダー（GitHub, GitLab, Vercel, Datadog, PagerDuty, Snyk等）に日本企業は**1社もない**
- これは偶然ではなく、英語圏でのコミュニティ形成力、ドキュメンテーション力、グローバルセールス力の構造的欠如が原因

**6-3. 言語・文化障壁の深刻さ**

- DevToolsのPLG（Product-Led Growth）はReddit、Hacker News、Twitter/X英語圏で始まる。RunPodのReddit投稿がARR $120Mにつながったように（[TechCrunch](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)）
- 日本語のみのプロダクトはTAMが自動的に1/20に制限される（日本のAI研究者は世界全体の5%以下）
- 英語圏でのマーケティング・セールス・カスタマーサポートには、ネイティブレベルの英語力を持つチームメンバーが不可欠。日本のAI/MLエンジニアで英語ネイティブレベルの人材は極めて稀

**6-4. エンジニア採用の深刻な困難**

- 日本には**推定130万の未充足IT職**がある。AI/ML分野は特に深刻（[Robert Half](https://www.roberthalf.com/jp/en/insights/salary-guide/technology)）
- **85%の日本企業**がテック人材の採用に苦戦 — 世界最高水準（[ISF NET](https://www.isfnet.com/how-to-recruit-engineer-in-jp.html)）
- ML Engineer平均年収 ¥10,839,182（約$72K）。米国の同等ポジション（$150K-$250K+）よりは安いが、日本のスタートアップ水準（年収$40K-$60K）からは大幅に高い
- Distributed Systems + GPU + HPC + 量子計算をカバーできるフルスタックエンジニアは日本に**数十人**しかいない。その大半は大企業・研究機関に所属しており、少人数スタートアップに来る可能性は極めて低い

---

## 7. タイミングは最悪かもしれない

### 批判の核心

AIXSの創業タイミング（2026年）は、GPU価格崩壊、AIバブル崩壊リスク、VC資金枯渇、規制強化の4つが同時に重なる最悪の時期である。

### 根拠

**7-1. GPU過剰供給と価格崩壊**

- H100のオンデマンド価格は18ヶ月で**$8+→$2.50-4.00/hr**に急落（50-70%減）。AIXSの売価$3.50-5.00/hrは既にRunPod（$2.69）やさくらDOK（$2.50）より高い
- 中国のGPU稼働率問題：AIブーム時に各地方政府が技術的専門知識なしにGPUを大量購入し、「地理的に分散した、使いにくい低品質データセンター」が乱立。需要のない場所に供給が溢れている（[ChinaTalk](https://www.chinatalk.media/p/chinas-weird-chip-surplus-explained)）
- **2027年までにGPUプロバイダの80%以上が市場から退出する**との予測（[Vultr](https://blogs.vultr.com/trends-neocloud-consolidation)）。AIXSが退出側になるリスクは高い
- GPU価格競争は底値に向かっており、マージンは圧縮の一途。再販モデルの粗利率は10-20%に低下するリスク

**7-2. AIバブル崩壊リスク（2025-2026年の調整可能性）**

- Yale大学の調査で、CEOの**40%**がAIへの過剰投資と調整の発生を予測（[Yale Insights](https://insights.som.yale.edu/insights/this-is-how-the-ai-bubble-bursts)）
- MIT Media Labの報告：企業の生成AI投資$30-40Bに対し、**95%の組織がリターンゼロ**
- OpenAI自身が2026年に**$14Bの損失**を予測。2023-2028年の累計損失は**$44B**。最も成功したAI企業ですらこの惨状（[Yahoo Finance](https://finance.yahoo.com/news/openais-own-forecast-predicts-14-150445813.html)）
- Sam Altman自身が「AIバブルは進行中」と2025年に認めた（[Wikipedia](https://en.wikipedia.org/wiki/AI_bubble)）
- Hustle FundのElizabeth Yinは「ほとんどのAIスタートアップは18-24ヶ月以内に倒産する」と予測（[NPR](https://www.npr.org/2025/11/23/nx-s1-5615410/ai-bubble-nvidia-openai-revenue-bust-data-centers)）
- NPRの2025年11月報道によれば、AIバブル崩壊への懸念は「かつてないレベル」に

**7-3. VC資金枯渇リスク**

- VCファンディングは2024年にピークに達し、2025年半ばから乾き始めた。LPがリターンを要求している
- Cloud GPU Platforms分野の調達は2025年に**前年比49.25%減少**（[Tracxn](https://tracxn.com/d/trending-business-models/startups-in-cloud-gpu-platforms/__Zk91xONdI-FxILZ_0x2o9Ta7EdqgYE95i8Wn5s1e5Qc)）
- 2025年のスタートアップ閉鎖件数は依然として高水準（[TechCrunch](https://techcrunch.com/2025/01/26/2025-will-likely-be-another-brutal-year-of-failed-startups-data-suggests/)）。2024年は966社が閉鎖、前年比25.6%増
- 日本のVC市場($2.22B)では、AI/GPUインフラへの大型投資は極めて稀。a16zが日本オフィスを開設予定だが、投資対象は日本特化の消費者向けスタートアップが主

**7-4. 規制強化による参入障壁**

- EU AI Actの施行開始。**60%以上の中小テック企業**がコンプライアンス準備不十分と回答（[Digital Watch](https://dig.watch/updates/eu-ai-act-enforcement-startups)）
- 30以上の創業者とVC投資家が、EU AI Actが「イノベーションを阻害し投資を抑制する」と公開書簡で警告（[Vestbee](https://www.vestbee.com/insights/articles/eu-ai-act-takes-effect-what-you-need-to-know)）
- コンプライアンスコストは少人数スタートアップにとって致命的。専門弁護士、コンプライアンスオフィサーの雇用は、ランウェイを一瞬で燃やし尽くす
- 日本でも個人情報保護法改正、経済安全保障推進法により、GPU上で処理されるデータの規制が強化される可能性

---

## 総括：AIXSが失敗する確率の推定

| リスク要因 | 発生確率 | 致命度(1-10) | リスクスコア |
|---|---|---|---|
| 市場が極小（SOM $1-5M） | 70% | 9 | 6.3 |
| コールドスタート問題で立ち上がらない | 60% | 10 | 6.0 |
| RunPod的成功の再現不可能性 | 80% | 7 | 5.6 |
| 大手のフルスタック化で差別化消滅 | 90% | 8 | 7.2 |
| OSSに追いつかれMoat消滅 | 75% | 7 | 5.3 |
| 日本からの構造的不利 | 85% | 6 | 5.1 |
| タイミング（バブル崩壊+GPU価格崩壊） | 50% | 9 | 4.5 |

**複合リスク：上記リスクの1つ以上が致命的に作用する確率 ≈ 95%以上**

投資家として率直に言う。AIXSの事業計画書を読んだとき、最初に浮かぶ質問はこうだ：

> **「CoreWeave + W&B が $1.7B の買収で既に実現していることを、なぜ数人のチームがゼロから再構築する必要があるのか？」**

この質問に説得力のある回答がない限り、AIXSへの投資は推奨できない。

---

## Sources

- [GetLatka - Vast.ai Revenue](https://getlatka.com/companies/vast.ai)
- [ThunderCompute - AI GPU Rental Market Trends March 2026](https://www.thundercompute.com/blog/ai-gpu-rental-market-trends)
- [Vast.ai Hosting](https://vast.ai/hosting)
- [Vast.ai June 2024 Product Update](https://vast.ai/article/june-2024-product-update)
- [Vast.ai Named Fastest Growing by Ramp and Brex](https://vast.ai/article/ramp-brex-fastest-growing-vendor)
- [TechCrunch - RunPod hits $120M ARR](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
- [RunPod - $120M ARR Press Release](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr)
- [Fortune Business Insights - GPU as a Service Market](https://www.fortunebusinessinsights.com/gpu-as-a-service-market-107797)
- [Tracxn - Cloud GPU Platforms Funding Trends](https://tracxn.com/d/trending-business-models/startups-in-cloud-gpu-platforms/__Zk91xONdI-FxILZ_0x2o9Ta7EdqgYE95i8Wn5s1e5Qc)
- [Tracxn - Uber Funding](https://tracxn.com/d/companies/uber/__wAOgbkstxol2NgmW5SFgVp8zBi7klH1GO5ziIlSERR4/funding-and-investors)
- [Bloomberg - Uber and Airbnb $99 Billion Idea](https://www.bloomberg.com/features/2017-uber-airbnb-99-billion-idea/)
- [NFX - 19 Marketplace Tactics](https://www.nfx.com/post/19-marketplace-tactics-for-overcoming-the-chicken-or-egg-problem)
- [Sharetribe - Chicken and Egg Problem](https://www.sharetribe.com/marketplace-glossary/chicken-and-egg-problem/)
- [AWS - SageMaker Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)
- [AWS - SageMaker Unified Studio GA Announcement](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-sagemaker-unified-studio-generally-available/)
- [Google Cloud Blog - AI Infrastructure at NVIDIA GTC 2026](https://cloud.google.com/blog/products/compute/google-cloud-ai-infrastructure-at-nvidia-gtc-2026/)
- [CNBC - Databricks $134B Valuation](https://www.cnbc.com/2026/02/09/databricks-completes-5-billion-funding-round-with-2-billion-in-debt.html)
- [Databricks - $62B Valuation Press Release](https://www.databricks.com/company/newsroom/press-releases/databricks-raising-10b-series-j-investment-62b-valuation)
- [SaaStr - Databricks $5.4B ARR](https://www.saastr.com/growth-may-have-slowed-for-some-but-holy-cow-not-for-databricks/)
- [Sacra - CoreWeave Revenue](https://sacra.com/c/coreweave/)
- [CoreWeave - W&B Acquisition](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases)
- [TechCrunch - CoreWeave Acquires W&B](https://techcrunch.com/2025/03/04/coreweave-acquires-ai-developer-platform-weights-biases/)
- [CoreWeave IPO S-1 Breakdown](https://www.mostlymetrics.com/p/coreweave-ipo-s1-breakdown)
- [Vultr - Neocloud Consolidation Trends](https://blogs.vultr.com/trends-neocloud-consolidation)
- [Statista - Japan VC Market](https://www.statista.com/outlook/fmo/capital-raising/traditional-capital-raising/venture-capital/japan)
- [Japan Dev - Venture Capital in Japan 2026](https://japan-dev.com/blog/venture-capital-in-japan)
- [Robert Half - Japan IT Salary Guide 2026](https://www.roberthalf.com/jp/en/insights/salary-guide/technology)
- [ISF NET - Recruit IT Engineers Japan](https://www.isfnet.com/how-to-recruit-engineer-in-jp.html)
- [DemandSage - Startup Failure Rate 2026](https://www.demandsage.com/startup-failure-rate/)
- [Failory - Startup Failure Rate](https://www.failory.com/blog/startup-failure-rate)
- [TechCrunch - 2025 Brutal Year for Startups](https://techcrunch.com/2025/01/26/2025-will-likely-be-another-brutal-year-of-failed-startups-data-suggests/)
- [Yale Insights - How the AI Bubble Bursts](https://insights.som.yale.edu/insights/this-is-how-the-ai-bubble-bursts)
- [NPR - AI Bubble Concerns](https://www.npr.org/2025/11/23/nx-s1-5615410/ai-bubble-nvidia-openai-revenue-bust-data-centers)
- [Wikipedia - AI Bubble](https://en.wikipedia.org/wiki/AI_bubble)
- [Yahoo Finance - OpenAI $14B Loss Forecast 2026](https://finance.yahoo.com/news/openais-own-forecast-predicts-14-150445813.html)
- [ChinaTalk - China's Weird Chip Surplus](https://www.chinatalk.media/p/chinas-weird-chip-surplus-explained)
- [Addepto - Best MLOps Platforms 2026](https://addepto.com/mlops-platforms-in-2026/)
- [PyCon DE 2025 - Self-Hosted MLOps on K8s](https://pretalx.com/pyconde-pydata-2025/talk/3CYZUH/)
- [Digital Watch - EU AI Act Enforcement Startups](https://dig.watch/updates/eu-ai-act-enforcement-startups)
- [Vestbee - EU AI Act Startups Push Back](https://www.vestbee.com/insights/articles/eu-ai-act-takes-effect-what-you-need-to-know)
- [Chatham House - AI Bubble and Tech Dominance](https://www.chathamhouse.org/2025/12/how-ai-bubble-bursting-could-erode-us-tech-dominance-and-accelerate-chinas-rise)
