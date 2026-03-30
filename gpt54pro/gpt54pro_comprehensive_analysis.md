# AIXS Comprehensive Competitive Analysis & Market Research

**Generated**: 2026-03-29 05:51:47
**Model**: gpt-5.4-pro (Responses API with web_search_preview)
**Queries**: 7 sequential searches
**Total tokens used**: 1,669,149
**Total API time**: 7634.0s

> This analysis upgrades the previous gpt-4o-search-preview runs with gpt-5.4-pro for higher quality reasoning and more comprehensive web search results.

---

# Query 1: Big Tech Convergence Threat (大手テック企業の統合プラットフォーム脅威)

前提を1つ置きます。**AIXS**の定義が提示されていないため、ここでは **「AIエージェント、研究ワークフロー、シミュレーション、量子、開発者体験を束ねるAI-native R&Dプラットフォーム」** と仮定して脅威度を評価します。したがって点数はこの前提に対するもので、AIXSの実像がより狭い/広い場合は±1〜2点ぶれる可能性があります。

## 結論サマリー

| 企業 | 2025-2026の総評 | R&D統合の実在度 | AIXS脅威度 | 直接参入タイムライン推定 |
|---|---|---:|---:|---|
| **AWS** | SageMakerは急速に強化、Braketも前進しているが、**RoboMaker終了で三位一体の統合はむしろ後退**。現状は「AI/データ統合は強い、量子は隣接、ロボは解体」。 ([aws.amazon.com](https://aws.amazon.com/sagemaker/unified-studio/)) | 弱〜中 | **5/10** | **18-36か月** |
| **Google** | Vertex AIを中核に、DeepMind/Research成果をCloudへ流し込む構図が最も鮮明。**AI co-scientistとDeep ThinkでAI-for-Scienceの商用化前夜**。ただしQuantum AIはまだVertexネイティブ商用サービス化していない。 ([cloud.google.com](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next25)) | 中〜強 | **8/10** | **参入済み、広範商用は6-12か月** |
| **Microsoft** | 4社の中で最も「OS化」している。**Azure AI Foundry + Azure ML + GitHub/VS Code + Azure Quantum + Discovery** が同じ戦略文脈に置かれている。 ([blogs.microsoft.com](https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/)) | 強 | **9/10** | **参入済み（0-6か月でさらに垂直化）** |
| **NVIDIA** | **DGX Cloud + Omniverse + CUDA-Q**で、計算・物理AIシミュレーション・量子ハイブリッドを一本化。アプリ層より**インフラ/シミュレーション基盤**として極めて危険。 ([nvidia.com](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/)) | 強 | **9/10** | **参入済み（既に拡大型）** |

---

## 1) AWS: SageMaker + Braket + RoboMaker

**最新発表/決算の読み筋**  
AWSは2025年3月に **SageMaker Unified Studio** をGA化し、EMR/Glue/Athena/Redshift/Bedrock/SageMaker AIを単一開発環境に集約しました。2025年12月には **serverless model customization** とAI agent-guided workflow previewを追加。Braket側では2025年にIonQ Forte EnterpriseやIQM Emeraldを追加し、2025年11月には **Braket notebook instancesのCUDA-Qネイティブ対応** を発表しています。一方で **AWS RoboMakerは2025年9月10日にサポート終了** となりました。決算ではAWS売上がQ4’25に**前年比24%増の356億ドル**、Amazon全社は**2026年に約2000億ドルの設備投資**を見込み、AI・チップ・ロボティクスを機会領域として明示しています。 ([aws.amazon.com](https://aws.amazon.com/blogs/aws/collaborate-and-build-faster-with-amazon-sagemaker-unified-studio-now-generally-available/))

**R&D統合の証拠**  
AWSに「統合の芽」はあります。Braketのノートブックは**SageMaker AI上に構築**され、IAM/Notebook/ライフサイクル構成もSageMaker AIを前提にしています。つまりML系ワークベンチと量子実験環境は**ノートブック層では接続済み**です。ですが、SageMaker Unified Studioの公式な統合対象一覧には **BraketもRoboMakerも入っていません**。加えてRoboMaker終了により、ロボティクスはManaged Serviceとしてはむしろ後退しました。したがってAWSは「データ/AI/GenAI統合」は強いが、**量子・ロボ・AIを1つのR&D OSとして束ねる戦略はまだ製品化されていない**、というのが妥当です。 ([docs.aws.amazon.com](https://docs.aws.amazon.com/braket/latest/developerguide/braket-cloudformation.html))

**AIXSへの脅威度: 5/10**  
脅威が中程度に留まる理由は、AWSの巨大な販売力・資本力そのものではなく、**AIXSと真正面にぶつかる統合プロダクトがまだ無い**からです。逆に言えば、AWSが将来Bedrock/AgentCore/SageMakerを核にAI-for-R&Dを再編すれば一気に上がります。現時点ではAIXSにとって、AWSは**競合というより下位基盤兼販売チャネル**として見る方が現実的です。 ([ir.aboutamazon.com](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx))

**参入タイムライン推定**  
**18-36か月。** 量子は既に参入済みですが、AIXS型の「統合R&Dプラットフォーム」への本格参入は、RoboMakerの穴埋めを別製品で行うか、M&A/パートナー戦略を伴わない限り少し遅いと見ます。 ([docs.aws.amazon.com](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateDeploymentJob.html?utm_source=openai))

---

## 2) Google: Vertex AI + Quantum AI + DeepMind AI Co-Scientist

**最新発表/決算の読み筋**  
Google Cloud Next ’25でGoogleは、**Vertex AIを包括的なAIアプリ/エージェント構築基盤**として再定義し、Gemini 2.5系、マルチモーダル生成モデル群、ADK/A2Aによるマルチエージェント、さらに **AlphaFold 3 High-Throughput** や **WeatherNext** をGoogle Cloud/Vertexへ流し込みました。2025年2月には **AI co-scientist** をGemini 2.0ベースのマルチエージェント科学協業システムとして公開。2026年2月には **Gemini 3 Deep Think** を科学・研究・工学向けに強化し、Gemini APIの早期アクセス対象にも広げています。決算ではGoogle CloudがQ4’25に**前年比48%増の177億ドル**、企業向けAI製品は**四半期ベースで数十億ドル規模**、バックログは**2400億ドル**に達しました。 ([cloud.google.com](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next25))

**R&D統合の証拠**  
Googleは公式に、**「Google DeepMindとGoogle Researchの最良部分をGoogle Cloudへ持ち込む」** と述べています。実際にAlphaFold 3 HTやWeatherNextがCloud/Vertexで利用でき、Vertex自体もモデル学習・デプロイ・エージェント運用まで担う中心基盤になっています。さらにDemis Hassabisは2026年3月時点で、AlphaGo由来の探索・推論原理が **AI co-scientist** にも統合されていると明言しています。弱点は、**AI co-scientistがまだTrusted Tester/早期アクセス段階**であり、**Quantum AIがVertexネイティブな商用クラウド製品になっていない**点です。つまり、研究資産の統合は非常に強いが、量子を含む完全な商用R&Dスイートとしてはまだ一段手前です。 ([cloud.google.com](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next25))

**Quantum AIの位置づけ**  
Google Quantum AIは、Willowで**below-threshold error correction**を示し、2025年10月には**verifiable quantum advantage**と、次のマイルストーンである**long-lived logical qubit**へのロードマップを示しました。これは強力ですが、Azure Quantumのようなエンタープライズ向け制御面とはまだ違い、**研究主導の優位**が中心です。 ([blog.google](https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/))

**AIXSへの脅威度: 8/10**  
AIXSが **AI-for-Science中心**ならGoogleは非常に危険です。理由は、モデル性能だけでなく、DeepMind/Researchの科学アセットをCloudに落とし始めているからです。ただし、量子/実験装置/企業内運用まで一気通貫の業務OS化ではMicrosoftほど整理されていません。 ([cloud.google.com](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next25))

**参入タイムライン推定**  
**参入済み。広範商用化は6-12か月。** AI co-scientistとDeep Think APIがGA級に近づくタイミングで、GoogleはAIXSのど真ん中に入ってくる可能性があります。 ([blog.google](https://blog.google/feed/google-research-ai-co-scientist/))

---

## 3) Microsoft: Azure ML + Azure Quantum + GitHub Copilot

**最新発表/決算の読み筋**  
Microsoftは2025年1月の **CoreAI再編** で、AzureをAIインフラにし、その上に **Azure AI Foundry、GitHub、VS Code** をまたぐAIプラットフォーム/開発者ツールを築くと明言しました。Build 2025では、Azure AI Foundry Agent Service、GitHub Copilot coding agent、MCP/A2A、そして **Microsoft Discovery** を発表。Azure Quantum側では2025年2月の **Majorana 1** で100万量子ビット級への道筋と、DARPA向け fault-tolerant prototype を「years, not decades」で目指すロードマップを出しました。2026年1月にはQDK新機能を公開し、**Microsoft Quantum platformはAI/HPC/量子ハード/ソフトをAzure上で統合**、しかも **GitHub Copilot支援** を前提にしています。決算ではFY26 Q2売上が**813億ドル**、Azureは**39%成長**、Satya NadellaはMicrosoftのAI事業が既に同社の大フランチャイズの一部を上回る規模だと述べています。 ([blogs.microsoft.com](https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/))

**R&D統合の証拠**  
ここが4社で最も強いです。**Azure Machine LearningはAzure AI Foundryの上にあるtrusted workbench** と公式に位置づけられ、Foundry Agent Service、モデル管理、観測性、ガバナンスまで一貫しています。GitHub Copilotは2025年に **agent mode + MCP** をVS Codeへ広げ、2026年2月には **Copilot CLI** をGA化して、IDE/Terminal/Cloud agentを一続きの開発体験にしています。さらにMicrosoft Discoveryが研究発見プロセス全体をagentic AIで変革する、とBuildで明示されました。これは単なる機能寄せ集めではなく、**開発、モデル運用、研究、量子、ガバナンスが同一戦略に統合されている**状態です。 ([azure.microsoft.com](https://azure.microsoft.com/en-us/blog/microsoft-recognized-for-second-consecutive-year-as-a-leader-in-the-2025-gartner-magic-quadrant-for-data-science-and-machine-learning-platforms/?msockid=35ae5d2b9b146e181a6f4bde9ac26f6b))

**AIXSへの脅威度: 9/10**  
AIXSが「研究者/開発者向けの制御面・ワークフロー面」を狙うなら、Microsoftが最も危険です。理由は、**企業導入に必要な全部品** — 開発者導線、エージェント、モデルカタログ、ガバナンス、量子、科学Discovery — がほぼ揃っているからです。2025年5月時点でFoundryのモデル群は1,900+、2025年10月時点では11,000+へ拡大しており、増勢も速いです。 ([news.microsoft.com](https://news.microsoft.com/ja-jp/2025/05/20/250520-microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/?msockid=216e5633831e611c1ad3404482ce6091))

**参入タイムライン推定**  
**参入済み（0-6か月でさらに垂直化）。** 特にライフサイエンス、素材、製造、ソフトウェアR&D領域では、DiscoveryやFoundry上の業界別パッケージが出るたびにAIXSとの距離は縮みます。 ([news.microsoft.com](https://news.microsoft.com/ja-jp/2025/05/20/250520-microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/?msockid=216e5633831e611c1ad3404482ce6091))

---

## 4) NVIDIA: DGX Cloud + Omniverse + CUDA Quantum

**最新発表/決算の読み筋**  
NVIDIAは2025年5月に **DGX Cloud Lepton** を発表し、開発・訓練・推論をマルチクラウドGPU供給網の上で一貫させる「virtual global AI factory」を打ち出しました。Omniverse on DGX Cloudは2025年8月に初期プラットフォームリリースが始まり、Azure Private Link、低遅延ストリーミング、Observabilityまで備えた**運用可能な物理AIシミュレーション基盤**になっています。CUDA-Qは **QPU-agnostic** な量子開発基盤で、GPU/CPU/QPUを単一プログラムで扱うハイブリッドモデルを提供。さらにGTC 2026では、Cadence/Siemens/Synopsys等と組み、**CUDA-X + Omniverse + GPU加速ソフト** を製造/設計/CAEワークフローに持ち込みました。決算ではQ4 FY26売上が**681億ドル**、データセンター売上が**623億ドル**、Jensen Huangは **agentic AI inflection point has arrived** と述べています。 ([nvidia.com](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/))

**R&D統合の証拠**  
NVIDIAの統合は、Microsoftのような「業務OS」ではなく、**計算/シミュレーション/量子ハイブリッドの基盤統合**です。DGX Cloud Leptonはプロトタイプから本番までを同一ワークフローに寄せ、Omniverse on DGX Cloudは物理AIやデジタルツインの実行面をクラウド管理化し、CUDA-Qは量子ハイブリッド計算面を統合します。2026年の産業ソフトウェア連携は、この3層を実ワークフローに差し込む動きだと読めます。つまりNVIDIAは、AIXSの上位アプリを奪うというより、**AIXSが差別化したい下位能力をコモディティ化しに来ている**存在です。 ([nvidia.com](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/))

**AIXSへの脅威度: 9/10**  
AIXSが**製造、CAE、ロボティクス、デジタルツイン、量子ハイブリッド**に重いなら、NVIDIAは実質トップ脅威です。逆にAIXSが研究者UIやELN/LIMSや業務オーケストレーション寄りなら、Microsoftの方が上です。 ([investor.nvidia.com](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Industrial-Software-Giants-Bring-Design-Engineering-and-Manufacturing-Into-the-AI-Era/default.aspx))

**参入タイムライン推定**  
**参入済み。** 2025-2026で「部品群」から「プラットフォーム群」へ移行しており、今後6-12か月で産業別の完成度がさらに上がる可能性が高いです。 ([nvidia.com](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/))

---

## AIXSにとっての実務的インプリケーション

**最重要結論は2つです。**  
1つ目は、**Microsoftが最も“直接競合”になりやすい**ことです。理由は、AI Foundry/ML/GitHub/Quantum/Discoveryが同じ制御面に収束しているからです。2つ目は、**NVIDIAが最も“下位基盤を握る競合”**だということです。GoogleはAI-for-Scienceで急接近中、AWSは今はまだ土台側です。 ([blogs.microsoft.com](https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/))

したがってAIXSの防衛線は、**「モデルやGPUを持つこと」ではなく、「研究ドメイン固有のワークフロー、検証、監査、実験計画、シミュレーション連携、クロスクラウド中立性」を握ること**です。Microsoft/NVIDIA/Googleが強いのは基盤と汎用制御面であり、AIXSが勝てる余地は、**R&D現場の意思決定ループそのもの**を製品化する点にあります。 ([news.microsoft.com](https://news.microsoft.com/ja-jp/2025/05/20/250520-microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/?msockid=216e5633831e611c1ad3404482ce6091))

必要なら次に、  
**「AIXSが勝つための差別化戦略マップ（機能、提携先、買収候補、避けるべき正面衝突領域）」** まで落として作れます。

### URL Citations (Query 1)

- [A single data and AI development environment - Amazon SageMaker Unified Studio - AWS](https://aws.amazon.com/sagemaker/unified-studio/)
- [Welcome to Google Cloud Next '25 | Google Cloud Blog](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next25)
- [Introducing CoreAI – Platform and Tools - The Official Microsoft Blog](https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/)
- [Connect Developers to Global GPU Compute | NVIDIA DGX Cloud Lepton](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/)
- [Collaborate and build faster with Amazon SageMaker Unified Studio, now generally available | AWS News Blog](https://aws.amazon.com/blogs/aws/collaborate-and-build-faster-with-amazon-sagemaker-unified-studio-now-generally-available/)
- [Create a Braket notebook instance using CloudFormation - Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-cloudformation.html)
- [
	Amazon.com, Inc. - Amazon.com Announces Fourth Quarter Results
](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx)
- [CreateDeploymentJob - AWS RoboMaker](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateDeploymentJob.html?utm_source=openai)
- [Meet Willow, our state-of-the-art quantum chip](https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/)
- [Google Research launches new scientific research tool, AI co-scientist](https://blog.google/feed/google-research-ai-co-scientist/)
- [Microsoft recognized for second consecutive year as a Leader in the 2025 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms | Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/microsoft-recognized-for-second-consecutive-year-as-a-leader-in-the-2025-gartner-magic-quadrant-for-data-science-and-machine-learning-platforms/?msockid=35ae5d2b9b146e181a6f4bde9ac26f6b)
- [Microsoft Build 2025: AI エージェントの時代とオープンなエージェント型 Web の構築へ - News Center Japan](https://news.microsoft.com/ja-jp/2025/05/20/250520-microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/?msockid=216e5633831e611c1ad3404482ce6091)
- [
	NVIDIA Corporation - NVIDIA and Global Industrial Software Giants Bring Design, Engineering and Manufacturing Into the AI Era
](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Industrial-Software-Giants-Bring-Design-Engineering-and-Manufacturing-Into-the-AI-Era/default.aspx)

*Query time: 1144.1s | Tokens: 203,276*

---

# Query 2: Adjacent Market Invasion (隣接分野からの参入リスク)

2026年3月28日時点の公開情報ベースで整理します。  
まず前提として、AIXSは2017年設立・資本金3,000万円で、公開事業は **NLP/可視化を中心としたAIエンジン・プラットフォーム実装** と **IT構築/DX支援**。また小野薬品向けに、PubMed論文を解析するAIシステム「MaTCH」を共同開発・導入しています。公開VCラウンドや外部評価額は今回確認できず、現状のAIXSは「**科学・医療向けの知識処理/アプリケーション層**」が主戦場だと見るのが自然です。 ([ai-xs.co.jp](https://ai-xs.co.jp/?p=30))

**先に結論**  
- **最も危険なのは Databricks/MLflow 3**。データ基盤、ML/LLM運用、アプリ、OLTPまで一気にフルスタック化しており、資本力も圧倒的です。 ([prnewswire.com](https://www.prnewswire.com/news-releases/databricks-grows-55-yoy-surpasses-4-8b-revenue-run-rate-and-is-raising-4b-series-l-at-134b-valuation-302643445.html?utm_source=openai))  
- **ライフサイエンスR&Dの直接脅威は Benchling**。Benchling AI まで載せ始めており、AIXSが製薬/バイオの研究業務面に広がるほど競合色が強まります。 ([benchling.com](https://www.benchling.com/news/introducing-benchling-ai?utm_source=openai))  
- **CoreWeave+W&B は “AI開発OS” 化の方向**で強いが、AIXSにとっては競合でもありインフラ提携先でもあります。 ([coreweave.com](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases?utm_source=openai))  
- **Sakana AI / FutureHouse は今は compute platform というより “AI scientist layer”**。ただし将来、研究ワークフローの主導権を握る可能性があるので要警戒です。 ([sakana.ai](https://sakana.ai/series-b/?utm_source=openai))  
- **SkyPilot / dstack / Anyscale / Modal は基盤レイヤー寄り**で、AIXSにとっては現時点では「直接競合」より「採用すべき土台/提携候補」の色が強いです。 ([docs.skypilot.co](https://docs.skypilot.co/en/latest/docs/index.html?utm_source=openai))

---

## 1) CoreWeave + Weights & Biases
**リスク:** 高

- **最新状況**: CoreWeaveは2025年5月にW&B買収を完了。6月にはW&B上でMission Control連携など最初の統合機能を公開し、その後もMarimo、OpenPipe、Monolith AIなどを取り込み、AI開発フルスタックを拡張しています。 ([coreweave.com](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases?utm_source=openai))  
- **調達/評価額**: W&Bは2023年に **$50Mを$1.25B評価** で調達し、公式サイト上は **累計>$250M**。買収は発表時に **約$1.7B** とされましたが、CoreWeaveのSEC 10-Qでは取得対価は **約$1.4B（現金+株式、調整前）** と記載されています。 ([wandb.ai](https://wandb.ai/site/press-release/weights-biases-raises-50-million-round-led-by-daniel-gross-and-nat-friedman-announces-wb-prompts?utm_source=openai))  
- **AIXSとの関係**:  
  - AIXSが**実験管理/評価/監視/開発基盤**まで持ちたいなら競合。  
  - AIXSが**科学アプリ層やドメイン知識層**に集中するなら、W&B/CoreWeaveはむしろ有力な基盤パートナー候補。  

## 2) Databricks / MLflow 3
**リスク:** 最重要 / 非常に高い

- **最新状況**: Databricksは **MLflow 3** を2025年6月に公開し、その後も3.x系を継続拡張。加えて **Lakebase** を2026年1月にGA、**Databricks One** も2026年1月にGAにし、データ+AI+アプリ+トランザクションDBまで一体化しています。 ([mlflow.org](https://mlflow.org/blog/mlflow-3-0-launch?utm_source=openai))  
- **調達/評価額**: 2025年1月に **$15B financing / $62B valuation**、さらに2025年12月に **>$4B Series L / $134B valuation** を公式発表。 ([prnewswire.com](https://www.prnewswire.com/news-releases/databricks-announces-15b-in-financing-to-attract-top-ai-talent-and-accelerate-global-expansion-302356888.html?utm_source=openai))  
- **AIXSとの関係**:  
  - AIXSが「**R&D compute platform**」を広く定義するなら、Databricksは**最も危険な隣接参入者**。  
  - 特に **追跡・評価・ガバナンス・AIアプリ・データ統合** を全部まとめて飲み込む力がある。  
  - 一方でAIXSが**医療/科学ドメイン特化UX**に寄せるなら、Databricks上位に乗る戦略も成立。  

## 3) Benchling
**リスク:** 高い（特にライフサイエンスR&D）

- **最新状況**: 2025年10月に **Benchling AI** を立ち上げ、2026年2月には **500 biotech companies** で利用、GA化を発表。会社全体としては **1,300+ biotech companies / 7,500 academic institutions / 200,000 scientists** 規模の浸透をうたっています。 ([benchling.com](https://www.benchling.com/news/introducing-benchling-ai?utm_source=openai))  
- **調達/評価額**: 最新の公式大型ラウンドは2021年11月の **$100M Series F / $6.1B valuation**。公開・二次流通系の調査では累計調達は **約$412M** と見られますが、これは会社の最新公式開示ではありません。 ([benchling.com](https://www.benchling.com/news/benchling-raises-100m-in-series-f-financing-co-led-by-altimeter-and-franklin-templeton?utm_source=openai))  
- **AIXSとの関係**:  
  - AIXSが**製薬/バイオ研究現場の業務OS**に入るほど、Benchlingと真正面からぶつかります。  
  - 特に **科学データモデル、研究記録、AIを研究フローに埋め込む発想** が近い。  
  - 逆にAIXSが **文献/NLP/戦略立案/可視化** に寄せるなら、Benchling補完もあり得ます。  

## 4) Emerald Cloud Lab (ECL)
**リスク:** 中〜高

- **最新状況**: ECLは今もアクティブで、**200超の機器モデル**、**24/7運用**、**4,500超の分析関数**、**Command Center + Constellation knowledge graph** を前面に出しています。wet lab execution と data/analysis を一つのソフトウェア面で束ねているのが強みです。 ([emeraldcloudlab.com](https://www.emeraldcloudlab.com/?utm_source=openai))  
- **調達/評価額**: 古い公開発表では2014年時点で **累計$13.5M**。一方、Forge等の二次流通系ソースでは **2025年7月時点で約$336M post**、総調達 **約$92M** 見込みが見えますが、これは会社公式確認値ではありません。 ([fiercebiotech.com](https://www.fiercebiotech.com/biotech/emerald-therapeutics-completes-latest-financing-brings-total-to-13-5mm-launches-emerald?utm_source=openai))  
- **AIXSとの関係**:  
  - 現状のAIXSとは **補完寄り**。AIXSがdry-lab / NLP /知識処理、ECLがwet-lab execution。  
  - ただしAIXSが将来 **closed-loop experimentation** まで狙うなら、ECLは一気に強敵。  
  - **Benchling + ECL 的な世界観** が市場の標準になれば、AIXS単独での面展開は難しくなります。  

## 5) FutureHouse（+ Edison Scientific）
**リスク:** 中

- **最新状況**: FutureHouseは **501(c)(3) nonprofit** としてAI scientistを開発し、2025年5月に **Robin** で end-to-end scientific discovery を披露。2025年11月には商用スピンアウト **Edison Scientific** を立ち上げ、FutureHouseのプラットフォームはEdison側に移されています。 ([futurehouse.org](https://www.futurehouse.org/about?utm_source=openai))  
- **調達/評価額**: FutureHouse自体は **Eric Schmidtを主たる資金源とする非営利**で、株式評価額はありません。商用側のEdison Scientificは、外部ソースでは **$70M seed / 約$245M〜$250M valuation** とされています。 ([futurehouse.org](https://www.futurehouse.org/about?utm_source=openai))  
- **AIXSとの関係**:  
  - いまは compute platform というより **“研究者の代わりをする agent layer”**。  
  - AIXSが文献理解や仮説立案の上位UXを狙うなら競合化しやすい。  
  - 逆にAIXSのドメイン知識や医療データ整理を FutureHouse/Edison に繋ぐ提携余地はあります。  

## 6) Sakana AI
**リスク:** 高い（特に日本市場）

- **最新状況**: 2025年3月に事業開発本部を新設し、MUFGやGoogleとの提携を進め、2026年3月にはMUFG向けの「AI融資エキスパート」を実案件検証フェーズに進めています。研究面でも **The AI Scientist / AI Scientist-v2** を強く押し出しています。 ([sakana.ai](https://sakana.ai/business-team/?utm_source=openai))  
- **調達/評価額**: 2025年11月の公式Series Bで **¥20B（約$135M）調達、post-money 約¥400B（約$2.635B）**。累計調達は **約¥52B（約$347M）**。 ([sakana.ai](https://sakana.ai/series-b/?utm_source=openai))  
- **AIXSとの関係**:  
  - 日本発・日本企業提携・AI scientist路線という意味で、AIXSに最も近い“国内の大きな隣接脅威”。  
  - AIXSが日本の科学/医療R&D知能化を狙うなら、Sakanaの存在は無視できません。  
  - ただしSakanaは基盤モデル/agent研究色が濃く、AIXSはより業務実装・NLP・可視化に寄せれば差別化余地あり。  

## 7) Sciloop
**リスク:** 低〜中（ウォッチ対象）

- **最新状況**: SciloopはYC F25、MIT出身創業者の会社で、**Sciloop Lab v_0** を早期提供中。公式サイトでは **ML研究の全ライフサイクル自動化** を掲げ、**Sakana AIの AI Scientist 上に構築**していると明記しています。 ([sciloop.dev](https://www.sciloop.dev/))  
- **調達/評価額**: 公開されているのは **YC backing**。YCの公式説明ではバッチ採択企業への seed funding は **$500,000**。Sciloopの priced valuation は未公表です。 ([ycombinator.com](https://www.ycombinator.com/companies/sciloop?utm_source=openai))  
- **AIXSとの関係**:  
  - 現時点では **点の脅威**。対象はML research automationにかなり限定。  
  - ただし「研究自動化UI」として洗練されると、大手に買われる/統合される可能性があります。  

## 8) SkyPilot
**リスク:** 中（ただし競合というより基盤候補）

- **最新状況**: SkyPilotは **any infra 上のAI workload管理** を掲げるOSSで、2025年3月に **client-server architecture**、2025年7月に **SSO / dashboard / workspaces / SSH node pools** を追加して、個人ツールからチーム向け control plane に進化しました。 ([docs.skypilot.co](https://docs.skypilot.co/en/latest/docs/index.html?utm_source=openai))  
- **調達/評価額**: Race Capitalの公開ポートフォリオには掲載されていますが、**ラウンド額・評価額は未公表**です。 ([race.capital](https://www.race.capital/portfolio/skypilot?utm_source=openai))  
- **AIXSとの関係**:  
  - AIXSが generic multi-cloud scheduler を自作するなら競合。  
  - そうでなければ、AIXSは **SkyPilotを採用して上位の科学UXに集中**した方が合理的です。  

## 9) dstack
**リスク:** 中低

- **最新状況**: dstackは **GPU-native orchestration** を掲げるOSS。dstack Skyを展開し、2025年末には **0.20 GA**、2026年2月には **Prefill-Decode disaggregation** まで入れており、trainingだけでなく inference control plane に寄ってきています。 ([dstack.ai](https://dstack.ai/?utm_source=openai))  
- **調達/評価額**: CB Insights系ソースでは **約$0.53M seed VC**。公開投資家として **Rheingau Founders** と **Tensor Ventures** が確認できます。評価額は未公表です。 ([cbinsights.com](https://www.cbinsights.com/company/dstack/financials?utm_source=openai))  
- **AIXSとの関係**:  
  - 現状は **AIXSの競合というより部品**。  
  - 小回りが利くので、AIXSが軽量な GPU orchestration を組み込むなら相性は良いです。  

## 10) Anyscale (Ray)
**リスク:** 高い

- **最新状況**: AnyscaleはRayの商用本命で、2025年後半には **Anyscale Runtime**、**Lineage Tracking（MLflow/W&B/Unity Catalog連携）**、Google Cloud/Azureとの深い提携まで進め、AI-native compute platform色を強めています。 ([anyscale.com](https://www.anyscale.com/?utm_source=openai))  
- **調達/評価額**: 公式の最新大型ラウンドは **$100M Series C / $1B valuation**、累計 **$160M**。 ([anyscale.com](https://www.anyscale.com/press/anyscale-secures-100m-series-c-at-1b-valuation-to-radically-simplify-scaling-and-productionizing-ai-applications?utm_source=openai))  
- **AIXSとの関係**:  
  - AIXSが **分散学習/分散推論/大規模ジョブ実行** を主戦場にすると強い競合。  
  - ただ、AIXSが科学アプリ層に絞るなら Anyscale/Ray は有力な実行基盤です。  

## 11) Modal
**リスク:** 中高

- **最新状況**: Modalは **inference / sandboxes / batch / training / notebooks** を全部 code-first で提供する serverless AI infra。2025年6月に **Modal 1.0**、2026年には coding agent や GPU snapshotting を前に出しており、研究者向けというより「AI-native developer platform」に進化しています。 ([modal.com](https://modal.com/blog/introducing-client-1-0?utm_source=openai))  
- **調達/評価額**: 2025年9月に **$87M Series B / $1.1B post-money**、累計 **$111M**。2026年2月には **$2.5B valuationでの調達協議報道** が出ましたが、CEOは「actively fundraisingではない」と否定しており、未確定扱いが妥当です。 ([modal.com](https://modal.com/blog/announcing-our-series-b?utm_source=openai))  
- **AIXSとの関係**:  
  - AIXSにとっては **serverless execution の有力パートナー**。  
  - ただしAIXSが「研究者向け managed execution platform」を目指すと、Modalと衝突します。  

---

## 私の見立て：AIXSにとっての優先順位
1. **最大脅威**: **Databricks / MLflow 3**  
   理由は、資本力と製品カバレッジが桁違いで、データ・追跡・評価・アプリ・DBまで一気に来ているからです。 ([prnewswire.com](https://www.prnewswire.com/news-releases/databricks-grows-55-yoy-surpasses-4-8b-revenue-run-rate-and-is-raising-4b-series-l-at-134b-valuation-302643445.html?utm_source=openai))

2. **縦で最も危ない**: **Benchling**  
   AIXSが製薬/バイオR&D workflow に深く入るほど、Benchlingとぶつかります。Benchling AIのGAでその圧力はさらに強まりました。 ([benchling.com](https://www.benchling.com/blog/benchling-ai-now-generally-available?utm_source=openai))

3. **AI developer stackで危ない**: **CoreWeave + W&B**  
   これは「compute vendor」が「AI開発OS」に上がってきたケースで、AIXSが generic platform をやるなら相当強敵です。 ([coreweave.com](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases?utm_source=openai))

4. **日本市場の将来脅威**: **Sakana AI**  
   日本企業との提携、AI scientist、資本力の三拍子が揃っています。AIXSが日本の科学/医療AIの旗を立てたいなら、最も近い大物です。 ([sakana.ai](https://sakana.ai/series-b/?utm_source=openai))

5. **基盤は作るより借りるべき**: **SkyPilot / dstack / Anyscale / Modal**  
   AIXSの公開事業を見る限り、勝ち筋は generic orchestration ではなく **科学ドメインの知識・workflow・可視化・agent UX** にあります。基盤は提携/採用の方が勝ちやすいです。 ([ai-xs.co.jp](https://ai-xs.co.jp/business/))

必要なら次に、  
**「AIXS向けの競合マップ（機能×顧客×価格×参入確率）」** か、  
**「提携候補 / 買収候補リスト」**  
まで作れます。

### URL Citations (Query 2)

- [会社情報 | 株式会社アイエクセス](https://ai-xs.co.jp/?p=30)
- [Databricks Grows >55% YoY, Surpasses $4.8B Revenue Run-Rate, and is Raising >$4B Series L at $134B Valuation](https://www.prnewswire.com/news-releases/databricks-grows-55-yoy-surpasses-4-8b-revenue-run-rate-and-is-raising-4b-series-l-at-134b-valuation-302643445.html?utm_source=openai)
- [Introducing Benchling AI | Benchling News](https://www.benchling.com/news/introducing-benchling-ai?utm_source=openai)
- [CoreWeave Acquires Weights & Biases | CoreWeave](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases?utm_source=openai)
- [Announcing Our Series B](https://sakana.ai/series-b/?utm_source=openai)
- [SkyPilot: Run AI on Any Infrastructure — SkyPilot Docs](https://docs.skypilot.co/en/latest/docs/index.html?utm_source=openai)
- [Weights & Biases raises $50 Million round led by Daniel Gross and Nat Friedman](https://wandb.ai/site/press-release/weights-biases-raises-50-million-round-led-by-daniel-gross-and-nat-friedman-announces-wb-prompts?utm_source=openai)
- [Announcing MLflow 3.0 | MLflow](https://mlflow.org/blog/mlflow-3-0-launch?utm_source=openai)
- [Databricks Announces $15B in Financing to Attract Top AI Talent and Accelerate Global Expansion](https://www.prnewswire.com/news-releases/databricks-announces-15b-in-financing-to-attract-top-ai-talent-and-accelerate-global-expansion-302356888.html?utm_source=openai)
- [Benchling Raises $100M in Series F Financing Co-Led by Altimeter and Franklin Templeton](https://www.benchling.com/news/benchling-raises-100m-in-series-f-financing-co-led-by-altimeter-and-franklin-templeton?utm_source=openai)
- [Emerald Cloud Lab: Remote Controlled Life Sciences Lab](https://www.emeraldcloudlab.com/?utm_source=openai)
- [Emerald Therapeutics Completes Latest Financing, Brings Total to $13.5MM; Launches Emerald Cloud Lab, a New Approach to Biotech Research | Fierce Biotech](https://www.fiercebiotech.com/biotech/emerald-therapeutics-completes-latest-financing-brings-total-to-13-5mm-launches-emerald?utm_source=openai)
- [About](https://www.futurehouse.org/about?utm_source=openai)
- [Sakana AI「事業開発本部」を立ち上げ：AI技術のビジネス展開に着手](https://sakana.ai/business-team/?utm_source=openai)
- [Sciloop](https://www.sciloop.dev/)
- [Sciloop: AI Co-Scientist that automates ML experimentation and analysis. | Y Combinator](https://www.ycombinator.com/companies/sciloop?utm_source=openai)
- [Race Capital Website](https://www.race.capital/portfolio/skypilot?utm_source=openai)
- [AI container orchestration for AI teams - dstack](https://dstack.ai/?utm_source=openai)
- [dstack Stock Price, Funding, Valuation, Revenue & Financial Statements](https://www.cbinsights.com/company/dstack/financials?utm_source=openai)
- [Anyscale | Production-Ready AI with Ray](https://www.anyscale.com/?utm_source=openai)
- [Anyscale Secures $100M Series C at $1B Valuation to Radically Simplify Scaling and Productionizing AI Applications](https://www.anyscale.com/press/anyscale-secures-100m-series-c-at-1b-valuation-to-radically-simplify-scaling-and-productionizing-ai-applications?utm_source=openai)
- [Introducing: Modal 1.0](https://modal.com/blog/introducing-client-1-0?utm_source=openai)
- [Announcing our $87M Series B](https://modal.com/blog/announcing-our-series-b?utm_source=openai)
- [500 biotech companies are using Benchling AI, now generally available](https://www.benchling.com/blog/benchling-ai-now-generally-available?utm_source=openai)
- [事業内容 | 株式会社アイエクセス](https://ai-xs.co.jp/business/)

*Query time: 1110.0s | Tokens: 284,188*

---

# Query 3: Defensive Strategies for Startups vs Big Tech (スタートアップの防御戦略)

以下、**2026年3月28日時点の最新公開情報ベース**で整理します。なお **AIXS は同名候補が複数ヒットしたため**、ここでは「**AI/DevTools系のAIXS**」として防御戦略を抽象化しています。加えて、会社ごとに開示指標が違うので、**ARRがない会社は revenue / TPV / $100k+顧客数 / paid customers で代替**し、**市場シェアは revenue share がない場合 6sense の installed-base estimate か Fortune/Forbes 浸透率 proxy**を使います。 ([aixsolutions.ai](https://aixsolutions.ai/?utm_source=openai))

## 10事例

1. **Datadog**  
   **対応**: 単機能監視ではなく、**cloud-agnostic な統合 observability / security / workflow platform**に拡張して守った。年次報告書では public/private/on-prem/multi-cloud/hybrid をまたぐ中立性を差別化として明示し、2024年末時点で**83%が2製品以上**、**50%が4製品以上**、**26%が6製品以上**を利用している。  
   **実データ**: FY2025 revenue **$3.43B**、**$100k+ ARR顧客 4,310**、**$1M+ ARR顧客 603**、総顧客は **約30,500**（2025-03-31時点）。6sense の installed-base estimate では **IT/Server/Network Monitoring 71.75%**。 ([investors.datadoghq.com](https://investors.datadoghq.com/static-files/bf7296e6-b2cd-4464-973a-5f36abefa033))

2. **Snowflake**  
   **対応**: 巨大クラウドに対して「単一クラウド上のDWH」ではなく、**multi-cloud / multi-region の AI Data Cloud + data sharing + Marketplace**で差別化した。3大クラウド・47リージョン、shared-data architecture、cross-cloud sharing/replication で、むしろ lock-in 回避を価値に変えた。  
   **実データ**: FY2026 product revenue **$4.47B**、FY2026 total revenue **$4.68B**、**$1M+顧客 733**、**Forbes Global 2000顧客 790**。直近の総顧客公表は **11,159**（2025-01-31時点）。6sense では **Data Warehousing 20.78%**。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm))

3. **MongoDB**  
   **対応**: hyperscaler 対抗で、**developer mindshare + Atlas managed multi-cloud + workload expansion**に張った。Atlas は **AWS/GCP/Azure の115+リージョン**で提供され、multi-cloud cluster で vendor lock-in を回避。さらに Search / Vector Search / Stream Processing まで広げて「DB」から「developer data platform」に再定義した。  
   **実データ**: FY2026 revenue **$2.46B**、**総顧客 59,900+**（2025-07-31）、**Atlas customers 58,300+**、**$100k+顧客 2,564**。開発者コミュニティ面では Community Server の累計ダウンロード **5億回超**、MongoDB University 登録 **250万超**。6sense では **NoSQL Databases 45.50%**。 ([investors.mongodb.com](https://investors.mongodb.com/static-files/2e35ada9-36d6-4ea2-a03a-bbba3b559770))

4. **Elastic**  
   **対応**: 検索一点ではなく、**Search + Observability + Security + Vector/AI + Serverless** に広げて生き残った。直近決算でも Serverless、OpenTelemetry、vector search、AI SOC を前面に出しており、「検索エンジン」から「Search AI Platform」に進化している。  
   **実データ**: FY2025 revenue **$1.483B**、FY2025 subscription customers **約21,500**、FY2026 Q3 時点で **$100k+ ACV顧客 1,660超**。6sense の Hosted Search では **ELK 34.15% / Elastic Cloud 33.64% / Elasticsearch 31.92%**で、Elastic系のデプロイが検出 installed base を実質支配しているとみてよい。 ([ir.elastic.co](https://ir.elastic.co/news/news-details/2025/Elastic-Reports-Fourth-Quarter-and-Fiscal-2025-Financial-Results/default.aspx?utm_source=openai))

5. **Confluent**  
   **対応**: 「Kafka の商用版」に留まらず、**complete + everywhere** 戦略で、on-prem / cloud / cross-cloud を横断するデータストリーミング基盤になった。公式サイトでも **Confluent Cloud + Platform + Kora** を前面に出し、Kora は autoscaling と **20–90%+ throughput savings** を訴求している。  
   **実データ**: 2025-06-30 時点の IR ハイライトで **TTM subscription revenue $1.022B**、**$20k+ ARR顧客 2,497**、**$100k+ ARR顧客 1,439**。IBM の買収完了発表（2026-03-17）では、Confluent を **6,500+ enterprises** が利用し、**Fortune 500 の40%**に浸透としている。 ([investors.confluent.io](https://investors.confluent.io/news-releases/news-release-details/confluent-announces-second-quarter-2025-financial-results/))

6. **HashiCorp**  
   **対応**: どのクラウドのネイティブ機能とも正面比較せず、**multi-cloud workflow layer** を取った。年次報告書でも「技術単体ではなく、**multi-cloud 環境のオペレーターの現実課題を解く workflow** を作る」と明言している。Terraform Stacks や HCP で、point product から control plane へ寄せたのが効いた。  
   **実データ**: FY2024 revenue **$583.1M**、**総顧客 4,423**、**Fortune 500 205社超**、HUG は **51,000+ members / 180+ groups / 60+ countries**。Q1 FY2025 では **総顧客 4,558**、**$100k+ ARR顧客 918**、**HCP subscription revenue $24.6M**。6sense proxy では **Infrastructure Management 50.94%**、Terraform は **Configuration Management 35.94%**。IBM は **2025-02-27** に買収を完了した。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1720671/000114036124025955/ny20021845x3_ars.pdf))

7. **Twilio**  
   **対応**: API-first DX だけでなく、**communications + data + AI の Customer Engagement Platform** に上げた。SIGNAL 2025 では「every customer interaction の infrastructure layer」を明確に打ち出し、単なる SMS/Voice API 価格競争から抜けた。  
   **実データ**: FY2025 revenue **$5.067B**、**Active Customer Accounts 402,000+**（2025-12-31）、full-year DBNER **108%**。Twilio は **millions of developers** を抱え、2025年の公式発表では **10M+ developers** としている。6sense の application-development installed-base estimate は **0.79%**（約 **22,429** detected customers）。 ([investors.twilio.com](https://investors.twilio.com/news-releases/news-release-details/twilio-unveils-next-generation-customer-engagement-platform?utm_source=openai))

8. **Stripe**  
   **対応**: 決済そのものではなく、**developer experience + conversion performance + 周辺プロダクト束**で守った。Billing / Invoicing / Tax / stablecoins / AI / Atlas まで広げ、「決済API」から「programmable financial services」へ移行している。  
   **実データ**: 2025年の businesses on Stripe の TPV は **$1.9T**、前年比 **+34%**、**世界GDPの約1.6%**相当。Stripe は **5M+ businesses** を直接またはプラットフォーム経由で支え、Revenue suite は **$1B annual run rate** に向かっている。6sense では **Payment Management 33.75%**。 ([stripe.com](https://stripe.com/newsroom/news/stripe-2025-update?utm_source=openai))

9. **Zoom**  
   **対応**: suite bundle に対して、まず **simplicity / reliability** で勝ち、その後 **Phone / Contact Center / Workplace / AI Companion** へ拡張した。FY25 決算でも AI-first 変身を強く打ち出している。  
   **実データ**: FY2026 revenue **$4.869B**、Enterprise revenue は **売上の60.3%**、**$100k+顧客 4,468**（2026-01-31）。Zoom が最後に大きく開示した enterprise customer count は **192,600**（2025-01-31）。6sense の web/video conferencing estimate は **3.51%**、約 **196,676** detected customers。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1585521/000158552125000027/zm-20250224ex991.htm?utm_source=openai))

10. **Slack**  
   **対応**: 「chat」ではなく、**workflow / integration / search / AI の system of work** になったのが大きい。現在の公式メッセージも「AI-powered platform for work」で、Slack AI、workflow、Salesforce front-end 化に寄せている。  
   **実データ**: 公式 about page では **200k+ paid customers**、**Fortune 100 の77社**が利用、**150+ countries** に daily active users。2025 roadmap 資料では **700M messages/day**、**3M workflows/day**。2025年6月の公式資料では **38k+ custom AI apps**。なお、**現行の公式 global DAU は非開示**で、単独会社時代の最後の明確な公式開示は **2019年9月の12M DAU / 6M+ paid seats**。6sense の project-collaboration estimate は **約8.90%**。 ([slack.com](https://slack.com/about?utm_source=openai))

---

## この10社から見える「生き残り方」の共通項

一言でいうと、**生き残った会社は point product を売ったのではなく、①中立 control plane、②workflow の埋め込み、③land-and-expand、④adjacent bundle、⑤ecosystem/network effects に変えた**、ということです。Datadog の multi-product 化、Snowflake / MongoDB / HashiCorp の multi-cloud 中立性、Slack / Twilio の workflow hub 化が典型です。 ([investors.datadoghq.com](https://investors.datadoghq.com/static-files/bf7296e6-b2cd-4464-973a-5f36abefa033))

## AIXSに適用可能な防御戦略 Top 5

1. **「モデル」ではなく「中立 control plane」を取る**  
   AIXS が AI/DevTools 系なら、OpenAI/Anthropic/Gemini/OSS/local をまたぐ **routing・eval・guardrail・cost control・audit** を握るべきです。大手は単体モデルや単体クラウドを bundle できますが、**cross-vendor 最適化**はやりにくい。Snowflake、MongoDB、Datadog、HashiCorp が強かったのは、みな「特定ベンダーに閉じない運用層」を取ったからです。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm))

2. **AIXS を“workflow の system of record”にする**  
   代替されにくいのは UI ではなく、**承認フロー・履歴・ポリシー・監査証跡・再現性・自動化**です。Slack は chat を workflow hub に、Twilio は API を customer journey hub に、HashiCorp は infra tools を workflow layer に変えて残りました。AIXS でも prompt / agent / eval / deployment / incident の全履歴を持つべきです。 ([salesforce.com](https://www.salesforce.com/news/stories/slack-ai-news/slack-ai_summarize/?utm_source=openai))

3. **dev-first で入って enterprise governance で広げる**  
   まずは **CLI / SDK / free tier / self-serve** で個人・チームに入る。その後に **SSO / SCIM / RBAC / private deployment / compliance / FinOps** を売る。この順番を外すと、大手 bundle に飲まれやすい。Datadog、MongoDB、HashiCorp、Twilio はいずれもこの land-and-expand が強いです。 ([investors.datadoghq.com](https://investors.datadoghq.com/static-files/bf7296e6-b2cd-4464-973a-5f36abefa033))

4. **隣接バンドルを自分で先にやる**  
   大手に入られて死ぬ会社は、核機能が 1 個しかない会社です。Datadog は observability→security→workflow、Elastic は search→observability/security/vector、Stripe は payments→billing/tax、Zoom は meetings→phone/contact center/AI に拡張して守りました。AIXS も core 機能の周辺に **evaluation / observability / policy / simulator / cost / security** を早めに束ねるべきです。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/0001561550/000162828026006645/ex-991x20251231x8k.htm))

5. **ecosystem と community を moat にする**  
   Marketplace、partner SDK、テンプレート、certification、community event は地味ですが強いです。Snowflake Marketplace、MongoDB の developer community、HashiCorp HUG、Slack の app/AI app ecosystem がまさにそれです。AIXS も「製品単体」ではなく、**AIXS 上に他社が build する理由**を作るべきです。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm))

## AIXS向けに、最優先で見るべきKPI
- **3モジュール以上利用顧客比率**
- **2モデル以上/2クラウド以上をまたぐワークロード比率**
- **enterprise NRR**
- **partner-built integration / template 数**
- **AIXS を抜くと失われる監査・履歴・再現性の量**

必要なら次に、これを **AIXS向けの具体アクションプラン（90日 / 1年）** に落として、  
**どの moat を先に作るべきか**まで優先順位付きで出します。

### URL Citations (Query 3)

- [aixsolutions.ai](https://aixsolutions.ai/?utm_source=openai)
- [https://investors.datadoghq.com/static-files/bf7296e6-b2cd-4464-973a-5f36abefa033](https://investors.datadoghq.com/static-files/bf7296e6-b2cd-4464-973a-5f36abefa033)
- [snow-20250131](https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm)
- [Form 10-K for Mongodb INC filed 03/21/2025](https://investors.mongodb.com/static-files/2e35ada9-36d6-4ea2-a03a-bbba3b559770)
- [Elastic - Elastic Reports Fourth Quarter and Fiscal 2025 Financial Results](https://ir.elastic.co/news/news-details/2025/Elastic-Reports-Fourth-Quarter-and-Fiscal-2025-Financial-Results/default.aspx?utm_source=openai)
- [Confluent | The Data Streaming Platform](https://investors.confluent.io/news-releases/news-release-details/confluent-announces-second-quarter-2025-financial-results/)
- [EBook+V2_HASHICORP,+INC_PWO-38078_CWO-28432.pdf](https://www.sec.gov/Archives/edgar/data/1720671/000114036124025955/ny20021845x3_ars.pdf)
- [Twilio Inc. - Twilio Unveils Next-Generation Customer Engagement Platform Built for an AI and Data-Powered World at SIGNAL 2025](https://investors.twilio.com/news-releases/news-release-details/twilio-unveils-next-generation-customer-engagement-platform?utm_source=openai)
- [Stripe publishes 2025 annual letter and announces tender offer to provide liquidity to current and former employees](https://stripe.com/newsroom/news/stripe-2025-update?utm_source=openai)
- [https://www.sec.gov/Archives/edgar/data/1585521/000158552125000027/zm-20250224ex991.htm?utm_source=openai](https://www.sec.gov/Archives/edgar/data/1585521/000158552125000027/zm-20250224ex991.htm?utm_source=openai)
- [About Us | Slack](https://slack.com/about?utm_source=openai)
- [Salesforce Launches Trusted Generative AI for Customers in Slack - Salesforce](https://www.salesforce.com/news/stories/slack-ai-news/slack-ai_summarize/?utm_source=openai)
- [Document](https://www.sec.gov/Archives/edgar/data/0001561550/000162828026006645/ex-991x20251231x8k.htm)

*Query time: 996.0s | Tokens: 218,422*

---

# Query 4: Hidden Competitors & Emerging Threats (見落とされた競合と新興脅威)

以下、**2026年3月28日時点**で整理します。なお、**「AIXS」= AIXNET / AIX Cloud + AIX Mart 系**のこととして読んでいます。AIX Cloud は on-demand / reserved / clustered / private cloud、テンプレート、Kubernetes presets、observability、SLA credits を持つ中央集権型GPU platformで、AIX Mart は遊休GPU等をトークン化して束ねる DePIN 型マーケットプレイスです。もし別の AIXS を指していたら、その会社名だけください。 ([aix.net](https://www.aix.net/))

## 先に結論

- **2024-2026の新興GPU cloud/R&D platformは、かなり大きい波が来ています。** ただし勝ち筋は「単なるGPU貸し」ではなく、**AI factory/垂直統合インフラ**、**代替アクセラレータ（特にAMD）**、**推論・開発体験に寄せたAI-native platform**の3系統に分かれています。 ([together.ai](https://www.together.ai/blog/together-ai-announcing-305m-series-b))
- **中国発GPU cloud（AutoDL, MatPoolなど）は「中国内需/研究者/中小チーム向け」でかなり強い**一方、**グローバル・エンタープライズ標準の位置**まではまだ距離があります。ボトルネックはUXよりも、**国際サポート、コンプライアンス、輸出規制の変動、海外リージョン整備**です。 ([autodl.com](https://www.autodl.com/docs/gpu/))
- **OSSスタック（K8s + Ray + MLflow + JupyterHub）で、AIX Cloud 的な中央集権型 platform の大半は再現可能**です。  
  ただし、**AIX Mart 的な DePIN/permissionless marketplace/token economics** までは、その4点セットだけでは再現できません。そこは別物です。 ([docs.ray.io](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html))
- **GPU需要減少リスク**については、  
  - **エッジAI**: 近中期では「限定的」  
  - **モデル小型化/量子化/蒸留**: 「単位タスクあたりGPU需要」は下げるが、総需要をすぐ壊すとは見にくい  
  - **量子コンピュータ**: 少なくとも今のロードマップでは**GPU代替ではなくGPU補完**  
  という見方が妥当です。むしろ近い脅威は**推論専用ASIC/TPU系**と**ソフトウェア効率化**です。 ([deloitte.com](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html))

---

## 1) 2024-2026で目立つGPU cloud / R&D platform スタートアップ

### A. AI factory / neocloud 系
- **Lambda**  
  2024年2月に **$320M Series C**、2024年4月に **最大$500MのGPU-backed financing**、2025年2月に **$480M Series D**。GPU cloud を金融的にも拡張する典型例です。 ([businesswire.com](https://www.businesswire.com/news/home/20240215216669/en/Lambda-Raises-%24320M-to-Build-a-GPU-Cloud-for-AI))
- **Crusoe**  
  2024年12月に **$600M Series D**、2025年10月に **$1.375B Series E**。Crusoe自身が「AI factory company」と言っている通り、もう“GPUクラウド”より**電力・DC・クラウドを一体化したAI工場**の競争です。 ([y94.com](https://y94.com/2024/12/12/crusoe-secures-600-million-in-series-d-round-led-by-founders-fund/?utm_source=openai))
- **Nscale**  
  **2024年創業**で、2024年12月 **$155M Series A**、2025年に **$1.1B Series B**、2026年3月に **$2B Series C**。この伸びは、まさに欧州版neocloudの象徴です。 ([itpro.com](https://www.itpro.com/infrastructure/uk-infrastructure-firm-nscale-bags-record-breaking-usd2-billion-series-c-investment))

### B. 代替アクセラレータ / 非NVIDIA依存を売る系
- **TensorWave**  
  2024年に **$43M SAFE**、2025年5月に **$100M Series A**。AMD Instinct MI325X を8,000枚超規模で打ち出していて、**「AMDクラウドでNVIDIA偏重を崩す」**という明確なポジションです。 ([tensorwave.com](https://www.tensorwave.com/blog/tensorwave-raises-43m-in-safe-funding-the-largest-in-nevada-startup-history-to-advance-ai-compute-solutions?trk=public_post_comment-text&utm_source=openai))
- **GMI Cloud**  
  2024年10月に **$82M Series A**。会社自体が「**global access to advanced GPUs**」を前面に出していて、台湾/米国オペレーションを梃子にした**グローバル供給志向**が強いです。 ([prnewswire.com](https://www.prnewswire.com/news-releases/gmi-cloud-raises-82-million-in-total-series-a-funding-to-drive-global-access-to-advanced-gpus-and-cloud-infrastructure-302289529.html))

### C. R&D / inference platform 寄り
- **Together AI**  
  2025年2月に **$305M Series B**。GPUそのものより、**open-source modelを使うAI-native cloud** としての訴求が強く、研究開発〜本番化の中間レイヤーを取りに行っています。 ([together.ai](https://www.together.ai/blog/together-ai-announcing-305m-series-b))
- **Baseten**  
  2025年2月に **$75M Series C**、2026年2月に **$300M Series E**。完全に**推論プラットフォーム**文脈で伸びており、AIX系と比較するなら「R&D platform / inference ops」の代表格です。 ([businesswire.com](https://www.businesswire.com/news/home/20250218263765/en/Baseten-Lands-%2475M-from-IVP-and-Spark-to-Solve-AIs-Biggest-Bottleneck-to-Ubiquitous-Adoption-Inference))

### どう読むべきか
私の見立てでは、2024-2026の大型調達は、**「GPUの仕入れ能力」だけでなく、電力・DC・オーケストレーション・推論SaaSまで含めた“束ね方”に資本が入っている**、ということです。つまり、AIX的な事業をやるなら、今後は**GPU resaleだけでは粗利が薄く、上位レイヤーか供給網のどちらかに食い込む必要がある**です。 ([together.ai](https://www.together.ai/blog/together-ai-announcing-305m-series-b))

---

## 2) 中国発グローバルGPU cloud（AutoDL, MatPool等）の評価

### AutoDL
AutoDLの公開ドキュメントを見ると、かなり強いです。  
- GPU選定文書で **A800/H20/H800** まで含む幅広いGPUを扱い、**GPUはインスタンスごとに専有**。  
- **企業向けの「弹性部署」** では ReplicaSet / Job / Container という概念でバッチ調度を提供。  
- **英文インボイス**に対応。  
- 海外利用者向けに「**阿里云盘は海外でも速度が速い**」と明記。  
- さらに **Huawei Ascend NPU / Moore Threads GPU** のドキュメントもあり、国産・非NVIDIA系も視野に入れています。 ([autodl.com](https://www.autodl.com/docs/gpu/))

**つまりAutoDLは、単なる安い研究者向けGPUレンタルではなく、**  
1. C端の小口需要、  
2. 企業の軽量バッチ運用、  
3. 輸出規制を意識したヘテロジニアス化、  
を同時に押さえ始めています。公開資料ベースでは、**中国発の中ではかなり実戦的**です。 ([autodl.com](https://www.autodl.com/docs/gpu/))

### MatPool（矩池云）
MatPoolも、**研究室・教育・小中規模チーム向けにはかなり使いやすい**です。  
- メインサイトでは A100/4090 などのGPUサーバを即時レンタルでき、  
- **分布式集群** で multi-node / multi-GPU を組め、  
- **团队版** ではチーム内でデータ、環境、算力を共有できます。 ([matpool.com](https://matpool.com/?utm_source=openai))

ただし、公開資料の見え方は **中国語ベースの研究・高校・企業チーム向け** が中心で、AutoDLほど「海外利用」「英文請求」「国産チップ対応」みたいな国際訴求は前面に出ていません。なので、**MatPoolは“中国内で強いチーム向けGPU cloud”寄り**、AutoDLは**“中国内需に強く、かつ越境利用もある程度意識”**という位置づけです。 ([matpool.com](https://matpool.com/supports/doc-use-team-on-matpool/))

### 中国勢がグローバルで伸びるうえでの最大障害
本質的なリスクは、**技術より規制**です。NVIDIAは2025年4月9日に **H20輸出に新ライセンス要件**が課されたと開示し、さらに輸出規制の反復変更が中国外の市場にも影響し得ると述べています。議会調査局（CRS）も、2025年の AI Diffusion rule の撤回・代替ルール化など、**政策がまだ流動的**であることを整理しています。 ([s201.q4cdn.com](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q1/b6df1c5c-5cb6-4a41-9d28-dd1bcd34cc26.pdf))

なので、中国発GPU cloudのグローバル化で本当に問われるのは、  
**価格**ではなく、  
**(a) どのGPUを安定供給できるか**、  
**(b) どの法域で売れるか**、  
**(c) 国際顧客に対して請求・サポート・監査を回せるか**、  
です。ここが整えば伸びますが、ここが弱いと「安いが中国ローカル止まり」になりやすいです。 ([s201.q4cdn.com](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q1/b6df1c5c-5cb6-4a41-9d28-dd1bcd34cc26.pdf))

---

## 3) OSSスタック（K8s + Ray + MLflow + JupyterHub）でAIXSと同等にできるか

### 短答
**AIX Cloud 的な“中央集権型 platform”の大半はできる。**  
**AIX Mart 的な“DePIN/marketplace”は、そのままではできない。** ([aix.net](https://www.aix.net/))

### 何が足りるか
- **Kubernetes**: 基本オーケストレーション
- **KubeRay / Ray**: 分散学習・分散推論・autoscaling ([docs.ray.io](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html))
- **MLflow**: 実験追跡、モデル管理、registry ([mlflow.github.io](https://mlflow.github.io/mlflow-website/docs/latest/ml/tracking/))
- **JupyterHub**: multi-user notebook環境 ([jupyter.org](https://jupyter.org/hub))
- **Kueue**: batch/HPC/AI/ML 向け queueing / quota / fairness ([kueue.sigs.k8s.io](https://kueue.sigs.k8s.io/))
- **KServe + vLLM**: Kubernetes上の推論基盤、OpenAI互換API、LLM serving、autoscaling、scale-to-zero系 ([kserve.github.io](https://kserve.github.io/kserve/))
- **NVIDIA GPU Operator**: MIG / time-slicing によるGPU分割・共有 ([docs.nvidia.com](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/22.9.1/gpu-sharing.html))
- **OpenCost**: CPU/RAM/GPUのコスト配賦・chargebackの土台 ([opencost.io](https://opencost.io/docs/specification))

### つまり何が再現できるか
AIX Cloud が謳う **Kubernetes presets、observability、training-to-inference の流れ、透明課金** みたいな要素は、OSS側でもかなり作れます。特に、  
- notebook開発  
- 分散学習  
- 実験追跡  
- モデルregistry  
- LLM推論API  
- GPU共有  
- ジョブキュー  
- コスト配賦  
は十分に組めます。 ([aix.net](https://www.aix.net/))

### でも、そのままだと足りない部分
あなたが挙げた4点セットだけだと、実務上は次が足りません。  
- **推論プレーン**: KServe / vLLM / Ray Serve  
- **キュー/フェアネス**: Kueue or Volcano  
- **GPU共有/分割**: GPU Operator  
- **課金/配賦**: OpenCost + 自前billing  
- **SSO / IAM / audit / secrets / image registry / object storage / logging / SLA運用**  
です。ここを足して初めて“AIX Cloud相当”に近づきます。 ([kserve.github.io](https://kserve.github.io/kserve/))

### 何が再現しにくいか
AIX Mart の本丸である **permissionless participation、idle resourceの tokenization、DePIN marketplace** は、K8s+Ray+MLflow+JupyterHub では再現できません。これはMLOps stackではなく、**調達・価格付け・信頼・決済・ノード検証**まで含むマーケット設計だからです。 ([aix.net](https://www.aix.net/))

**結論としては**、  
- **AIX Cloud的な中央集権型AI platform** → OSSでかなり可能  
- **AIX Mart的な分散市場** → OSS MLOpsだけでは不可  
です。 ([aix.net](https://www.aix.net/))

---

## 4) エッジAI / モデル小型化 / 量子コンピュータはGPU需要を減らすか

### 4-1. エッジAI
**短中期の需要破壊要因としては弱い**です。  
Deloitteは、2026年には**推論が全AI計算の約3分の2**になる一方で、**計算の大半は依然として大規模データセンターや高価なオンプレAIサーバ上で行われる**と見ています。さらに、PC/スマホのNPUは増えるが、**2026年のAI計算のほぼ全てが edge ではなく data center / enterprise server で行われる**と予測しています。 ([deloitte.com](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html))

McKinseyも、2030年に向けて **AI inference がデータセンター需要の主役になり、35% CAGRで伸びる** と見ています。つまり、edgeは一部の軽量・低遅延推論を吸うものの、**総GPU需要を崩すというより、クラウド需要の中身を training から inference にシフトさせる**側面が強いです。 ([mckinsey.com](https://www.mckinsey.com/featured-insights/week-in-charts/the-future-ai-workload))

### 4-2. モデル小型化・量子化・蒸留
これは**単位タスクあたりのGPU需要を下げる**ので、リスクとしてはあります。  
Googleの AI Edge Quantizer は、FP32モデルを量子化して**edge deployment ready**なモデルに変換する前提で作られていますし、NVIDIAのJetson向け例でも、**knowledge distillation / quantization aware training / structured sparsity** が明示的に推奨されています。 ([github.com](https://github.com/google-ai-edge/ai-edge-quantizer))

ただし、ここは**単価下落リスク**であって、必ずしも**総量崩壊リスク**ではありません。Deloitteも、小型モデルや効率化が進んでも、**post-training 手法と推論回数の増加で総計算需要は増える**という整理をしています。 ([deloitte.com](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html))

私の見立てでは、モデル小型化は  
- **学習用H100/H200/B200の一部需要**  
- **単純な1-shot inferenceの高価格帯GPU需要**  
を削ります。  
でも逆に、  
- AI機能の埋め込み先が増える  
- エッジで前処理しつつクラウドで重い推論をする  
- 推論APIの呼び出し総量が増える  
ので、**総GPU需要の減少より「需要の細分化・価格圧縮」が先に起きる**と思います。 ([deloitte.com](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html))

### 4-3. 量子コンピュータ
**近中期ではGPU代替リスクはかなり低い**です。  
IBMの2025 roadmap自体が、量子は**HPCと一緒に使う**前提ですし、IBMとAMDの発表でも「quantum-centric supercomputing」は**quantum + CPUs/GPUs + HPC/AI accelerators** のハイブリッドです。NVIDIAも NVAQC で、量子研究のために **GB200 NVL72** を使うと言っています。 ([ibm.com](https://www.ibm.com/roadmaps/quantum/2025/))

要するに、少なくとも今見えているロードマップでは、量子は  
- AI学習をそのままQPUに置き換える、ではなく  
- 特定問題をQPUに任せ、周辺の最適化・誤り訂正・制御・シミュレーションをGPU/HPCが担う  
方向です。なので、**2030年前後までは“GPU需要減少要因”より“GPUの新しい補完需要”に近い**です。 ([ibm.com](https://www.ibm.com/roadmaps/quantum/2025/))

---

## 5) 本当に警戒すべきGPU需要リスク

ユーザーが挙げた3点より、**実務的にはこっちの方が近いリスク**です。

1. **推論専用ASIC / TPU / custom silicon**  
   Deloitteは、Meta、Google、Amazon、Groq、Cerebras などの inference-optimized chips の売上が2025年に既に大きく、2026年にさらに拡大すると見ています。GPU市場は “either-or” ではなく “both-and” だが、**推論側の多様化は確実**です。 ([deloitte.com](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html))

2. **ソフトウェア効率化**  
   vLLM、KServe、Ray Serve、各種scheduler最適化で、**同じGPUからより多くのtoken/s** を引き出せるようになるほど、クラウド事業者の粗利構造が変わります。これは需要をゼロにしませんが、**GPU時間の価格プレミアム**は圧縮します。 ([vllm.ai](https://www.vllm.ai/))

3. **輸出規制と供給の地政学**  
   中国系だけでなく、グローバル事業者全体に効きます。NVIDIA自身が、規制変更が中国外の市場にもコスト/供給/顧客運用へ波及しうると開示しています。 ([s201.q4cdn.com](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q1/b6df1c5c-5cb6-4a41-9d28-dd1bcd34cc26.pdf))

---

## 最終結論

- **2024-2026は neocloud / AI factory の資本競争が本格化した期間**で、Nscale、Crusoe、Lambda、TensorWave、GMI Cloud、Together AI、Baseten あたりは要注目です。 ([nscale.com](https://www.nscale.com/press-releases/ai-hyperscaler-nscale-secures-usd-155-million-in-series-a?utm_source=openai))
- **中国発GPU cloudは、研究者/教育/SMBでは強い**。特に AutoDL は思ったより platform 化しており、国産チップ対応も進めています。ただし、**グローバル企業向け標準になるには規制・サポート・海外運用が壁**です。 ([autodl.com](https://www.autodl.com/docs/gpu/))
- **OSSでAIX Cloud相当はかなり作れる**が、**AIX Mart相当は作れない**。差分は MLOps ではなく marketplace / settlement / trust layer です。 ([aix.net](https://www.aix.net/))
- **エッジAI・小型化・量子がGPU需要をすぐ壊す確率は低い**。近い脅威は、**推論専用チップ、ソフトウェア効率化、価格圧縮、規制**です。 ([deloitte.com](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html))

必要なら次に、以下のどれかで続けられます。  
1. **競合マップを表形式**で出す  
2. **AutoDL / MatPool / GMI Cloud / Lambda / Crusoe の比較表**を作る  
3. **AIX相当OSSアーキテクチャ**を具体構成まで落とす  
4. **GPU需要減少リスクを5年シナリオ**で定量っぽく整理する

### URL Citations (Query 4)

- [AIXNET - Decentralized AI Infrastructure](https://www.aix.net/)
- [Together AI Announces $305M Series B to Scale AI Acceleration Cloud for Open Source and Enterprise AI](https://www.together.ai/blog/together-ai-announcing-305m-series-b)
- [AutoDL帮助文档](https://www.autodl.com/docs/gpu/)
- [KubeRay Autoscaling — Ray 2.54.1](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html)
- [More compute for AI, not less | Deloitte Insights](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html)
- [Lambda Raises $320M to Build a GPU Cloud for AI](https://www.businesswire.com/news/home/20240215216669/en/Lambda-Raises-%24320M-to-Build-a-GPU-Cloud-for-AI)
- [Crusoe secures $600 million in Series D round led by Founders Fund | Y94](https://y94.com/2024/12/12/crusoe-secures-600-million-in-series-d-round-led-by-founders-fund/?utm_source=openai)
- [AI infrastructure firm Nscale bags record-breaking $2 billion Series C investment | IT Pro](https://www.itpro.com/infrastructure/uk-infrastructure-firm-nscale-bags-record-breaking-usd2-billion-series-c-investment)
- [TensorWave Raises $43M in SAFE Funding, the Largest in Nevada Startup History, to Advance AI Compute Solutions.](https://www.tensorwave.com/blog/tensorwave-raises-43m-in-safe-funding-the-largest-in-nevada-startup-history-to-advance-ai-compute-solutions?trk=public_post_comment-text&utm_source=openai)
- [GMI Cloud Raises $82 Million in Total Series A Funding to Drive Global Access to Advanced GPUs and Cloud Infrastructure](https://www.prnewswire.com/news-releases/gmi-cloud-raises-82-million-in-total-series-a-funding-to-drive-global-access-to-advanced-gpus-and-cloud-infrastructure-302289529.html)
- [Baseten Lands $75M from IVP and Spark to Solve AI’s Biggest Bottleneck to Ubiquitous Adoption: Inference](https://www.businesswire.com/news/home/20250218263765/en/Baseten-Lands-%2475M-from-IVP-and-Spark-to-Solve-AIs-Biggest-Bottleneck-to-Ubiquitous-Adoption-Inference)
- [矩池云 - 专注于人工智能领域的云服务商](https://matpool.com/?utm_source=openai)
- [使用团队版教程 - 矩池云支持中心 - 矩池云支持中心](https://matpool.com/supports/doc-use-team-on-matpool/)
- [0001045810-25-000116](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q1/b6df1c5c-5cb6-4a41-9d28-dd1bcd34cc26.pdf)
- [MLflow Tracking | MLflow](https://mlflow.github.io/mlflow-website/docs/latest/ml/tracking/)
- [Project Jupyter | JupyterHub](https://jupyter.org/hub)
- [Kueue](https://kueue.sigs.k8s.io/)
- [KServe | kserve](https://kserve.github.io/kserve/)
- [Time-Slicing GPUs in Kubernetes — gpu-operator 22.9.1 documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/22.9.1/gpu-sharing.html)
- [OpenCost Specification | OpenCost — open source cost monitoring for cloud native environments](https://opencost.io/docs/specification)
- [The future AI workload](https://www.mckinsey.com/featured-insights/week-in-charts/the-future-ai-workload)
- [GitHub - google-ai-edge/ai-edge-quantizer: AI Edge Quantizer: flexible post training quantization for LiteRT models. · GitHub](https://github.com/google-ai-edge/ai-edge-quantizer)
- [www.ibm.com](https://www.ibm.com/roadmaps/quantum/2025/)
- [vLLM](https://www.vllm.ai/)
- [AI hyperscaler Nscale secures $155 million in Series A | Press Release | Nscale](https://www.nscale.com/press-releases/ai-hyperscaler-nscale-secures-usd-155-million-in-series-a?utm_source=openai)

*Query time: 837.8s | Tokens: 193,232*

---

# Query 5: AIXS Unit Economics Deep Dive (ユニットエコノミクス詳細)

以下、**2026年3月28日時点で公開Web上で確認できる数字だけ**でまとめます。結論を先に言うと、**H100 SXMを自前保有して$3/hrで売るモデルは、新品保有なら“高稼働前提でぎりぎり成立”、中古保有なら成立しやすい、相場どおりのリース調達だとかなり厳しい**です。([shopblt.com](https://www.shopblt.com/item/emc-489-bbgj-nvidia-hgx-h100-4/legato_489bbgj.html))

## 1) H100 SXM の現在価格

### 新品 / OEM相当
- 公開カタログで追える**新規/OEM相当の基準値**として、Dell/EMCの**HGX H100 4-GPU SXM 80GB assembly**がShopBLTで**$112,484.27**、つまり**$28,121/GPU**です。別の市場トラッカーでもH100 SXM5新規購入相場は**$25k–$30k/GPU**帯です。([shopblt.com](https://www.shopblt.com/item/emc-489-bbgj-nvidia-hgx-h100-4/legato_489bbgj.html))

### 中古
- 現在の公開中古リスティングでは、H100 SXM5 80GBの実勢はだいたい**$17k–$20k/GPU**です。確認できた例は**$16,919.49**、**$16,999.99**、**$19,999.99**でした。([ebay.com](https://www.ebay.com/itm/205760203893))

### リース
- **ハードウェア・リースの市場ベンチマーク**としては、H100 SXM5 dedicated leaseが**12カ月 $2,800/mo、24カ月 $2,200/mo、36カ月 $1,800/mo**で、時間換算はそれぞれ**$3.89/hr、$3.06/hr、$2.50/hr**です。([gpuleaseindex.com](https://gpuleaseindex.com/gpu/h100-pricing-index))
- **クラウド予約価格（OPEX proxy）**だと、HyperstackはH100 SXMを**on-demand $2.40/hr、reserved $2.04/hr**、Genesis CloudはHGX H100 SXM5を**on-demand $2.19/hr、3–6カ月 $1.89/hr、6–12カ月 $1.75/hr、12カ月超 $1.60/hr**で出しています。Genesisは**最小8-GPUノード**です。([hyperstack.cloud](https://www.hyperstack.cloud/gpu-pricing))

## 2) データセンター rack 費用 / 電力コスト

### ラック費用
- **一般的なラックだけの相場感**は、2025年の公開ガイドで**フルラック $1,000–$2,500+/月**、電力は別建てで**$150–$300/kW/月**が目安です。Chicagoの公開ベンチマークでは平均**$115–$184/kW/月**、**15–30kW**の高密度ラックは標準ラック対比で**+25–40%**のプレミアムとされています。([cyfuture.cloud](https://cyfuture.cloud/kb/data-centers/get-the-real-data-center-colocation-pricing-in-2025-market))
- **公開契約の具体例**では、DR Fortressが**2kW cabinet $900/月、4kW cabinet $1,200/月**。Iron Mountainの2025年公開契約スニペットでは、**VA1/VA2の20kW colocationが$5,950.32/月**、さらに**1–4MW variable metered power license feeが$101.20/kW/月**です。([spo.hawaii.gov](https://spo.hawaii.gov/wp-content/uploads/2023/11/DR-Fortress_REVISED-05_Attachment-5_OF3_Schedule-A_RFP22002_SoH-RFP-22002-Pricing_7182023_FINAL-FOR-STATE-ETS-Approved-11-17-23.pdf))

### 電力コスト
- EIAの**2026年1月**の工業用電力単価は、**Texas 7.25¢/kWh、Virginia 10.59¢/kWh、Oregon 8.02¢/kWh**です。([eia.gov](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b))
- H100 SXM5自体の最大消費電力は**700W**です。加えて、Exxactの4x H100 SXM5構成サーバーは**3,785W**なので、ノード全体では**約946W/GPUのIT負荷**になります。PUE **1.2**を置くと、施設側消費は**約829 kWh/GPU/月**で、電力原価は**Texas 約$60、Virginia 約$88、Oregon 約$66 / GPU / 月**です。なお、**bundled colo契約ならこの電力を別計上すると二重計上**になります。([delltechnologies.com](https://www.delltechnologies.com/asset/zh-cn/products/servers/briefs-summaries/poweredge-server-gpu-matrix.pdf))

## 3) GPUクラウド startup の粗利率「実データ」

### CoreWeave
- CoreWeaveは公開会社なので**実データ**があります。FY2025は**Revenue $5.131B / Cost of revenue $1.453B**で、**GAAP gross margin 71.7%**です。Q4 2025は**67.6%**、Q1 2025は**73.3%**でした。なお現在の公開価格表では**HGX H100 8-GPU instanceが$49.24/hr**で、**$6.16/GPU-hr相当**です。([sec.gov](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000094/coreweave4q25earningspress.htm))

### Lambda
- Lambdaは非上場なので、**公開会社のようなGAAP粗利率開示はありません**。ただしDCDが、The Informationが確認した社内資料ベースとして、**2025年前半のgross margin 50%**、**旧来のnon-cloud事業を除くと61%**、**前半のnet loss 約$24M**と報じています。([datacenterdynamics.com](https://www.datacenterdynamics.com/en/news/ai-cloud-lambda-hires-investment-banks-in-preparation-for-ipo-report/))
- 価格面では、Lambdaの公開instancesページにあるH100 SXM価格は**2026年4月6日発効**のレートで、**8x $3.99/GPU-hr、4x $4.09、2x $4.19、1x $4.29**です。**今日は2026年3月28日**なので、これは“公開されている近未来レート”であって、厳密な「本日時点の課金単価」ではありません。([lambda.ai](https://lambda.ai/nvidia-h100-nvidia-h200-gpus))

### RunPod
- RunPodについて、今回確認した公開ソースで取れた**硬い数字**は、TechCrunch掲載の**annual revenue run rate $120M**と、パートナー企業のS-1に書かれた**標準termsではRunPodが約20%を保持し、約80%をcompute providerへ分配**という点です。([techcrunch.com](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/))
- **会社開示のgross margin数値そのものは今回確認した公開ソースでは見当たりませんでした。** 参考までにSacraはRunPodのgross marginを**mid-60s to high-70s**と推定していますが、これは**推定値であって会社開示ではありません**。([sacra.com](https://sacra.com/c/runpod/))

## 4) H100を **$3/hr** で売る場合の月間損益

### モデル前提
- 売価は**$3/hr**、月間稼働時間は**730h**なので、**100%稼働売上は$2,190/GPU/月**です。
- **新品保有モデル**は、Exxactの4x H100構成サーバーが**$161,397.01**なので**$40,349/GPU相当**で計算。([configurator.exxactcorp.com](https://configurator.exxactcorp.com/configure/TS4-101818584))
- **中古保有モデル**は、現在の中古平均**$17,973/GPU**に、同じ非GPUプラットフォーム原価**$12,228/GPU**を足した前提です。非GPU部分は、Exxactの4x H100サーバー価格とDell/EMC 4-GPU assembly価格との差から逆算しました。([ebay.com](https://www.ebay.com/itm/205760203893))
- coloは、Iron Mountainの**VA1/VA2 20kW cabinet $5,950.32/月**を使い、Exxactの**3.785kW/4-GPU node**から概算して**約5ノード=20 H100/rack**として、**$297.52/GPU/月**で置いています。([publicpromiseprocurement.org](https://publicpromiseprocurement.org/wp-content/uploads/2025/09/Copy-of-Iron_Mountain_-_Attachment_D-National_Pricing.pdf))

### 月次P/L（GPU 1枚あたり、36カ月償却、bundled colo）
| シナリオ | 月次直接原価 | 粗利 @100%稼働 | 粗利率 @100% | 粗利 @70%稼働 | 損益分岐稼働率 |
|---|---:|---:|---:|---:|---:|
| 新品保有 | $1,418.33 | $771.67 | 35.2% | $114.67 | 64.8% |
| 中古保有 | $1,136.44 | $1,053.56 | 48.1% | $396.56 | 51.9% |
| 36カ月リース | $2,097.52 | $92.48 | 4.2% | **-$564.52** | 95.8% |

この表の導出計算です。

### 新品保有モデルの稼働率感度
| 稼働率 | 売上 | 粗利 |
|---|---:|---:|
| 100% | $2,190 | $771.67 |
| 70% | $1,533 | $114.67 |
| 60% | $1,314 | **-$104.33** |
| 50% | $1,095 | **-$323.33** |

感度計算上、**新品保有で$3/hrは60%台前半を切ると赤字**、**中古保有でも50%前後が分岐**です。

### 実務的な補足
- ここには**SRE/サポート/回収不能/予備機/決済コスト/G&A**を入れていません。仮に**+$100/GPU/月**だけ追加しても、新品保有モデルの損益分岐は**64.8% → 69.3%**に上がります。
- 私の読みでは、**$3/hrは「新品 owner-operator」としては薄い価格**です。CoreWeaveの公開H100価格は**$6.16/GPU-hr相当**、Lambdaの公開予定レートも**$3.99–$4.29**なので、**$3/hrはRunPod寄りの低価格帯**です。CoreWeaveやLambda並みの粗利を狙うなら、**より高いASP、もっと安い調達、あるいはasset-lightな marketplace化**のどれかが必要です。([docs.coreweave.com](https://docs.coreweave.com/pricing/pricing-instances))

## 5) マーケットプレイスモデルの手数料率ベンチマーク

- **RunPod marketplace compute**: パートナー企業のS-1では、標準termsとして**RunPod 20% / provider 80%**。([sec.gov](https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm))
- **Vast.ai**: 公式FAQで**hosts receive 75%, Vast keeps 25%**。([console.vast.ai](https://console.vast.ai/faq))
- **TensorDock**: 公式hostページの公開情報で**25% revenue-share fee**。([tensordock.com](https://tensordock.com/host))
- **Akash**: 公式roadmapでは、初期take rateとして**AKT決済 4% / USDC決済 20%**。([akash.network](https://akash.network/roadmap/aep-23))

要するに、**GPU infra marketplaceの現実的なtake-rate帯は20–25%が中心**で、**分散型/トークン決済だと4%のような低手数料設計もある**、というのが公開ベンチマークです。([sec.gov](https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm))

## ひとことで結論
- **新品H100 SXMを自前保有して$3/hrで売る**: かなり稼働率勝負。**損益分岐は約65%**。
- **中古H100 SXMをうまく拾える**: かなり現実的。**損益分岐は約52%**。
- **相場どおりにリース調達して$3/hrで売る**: ほぼ無理。**36カ月リースでも分岐は約96%**。
- **より“儲かる”のは owner-operator ではなく marketplace**。公開ベンチでは**take rate 20–25%**が主流です。([sec.gov](https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm))

必要なら次に、  
**(a) 1ラック20 GPU / 3年DCF**、  
**(b) 1MW級 cluster economics**、  
**(c) $2.5/hr / $3/hr / $4/hr の感度表**、  
**(d) debt込みIRR/回収期間**  
まで作ります。

### URL Citations (Query 5)

- [https://www.shopblt.com/item/emc-489-bbgj-nvidia-hgx-h100-4/legato_489bbgj.html](https://www.shopblt.com/item/emc-489-bbgj-nvidia-hgx-h100-4/legato_489bbgj.html)
- [https://www.ebay.com/itm/205760203893](https://www.ebay.com/itm/205760203893)
- [https://gpuleaseindex.com/gpu/h100-pricing-index](https://gpuleaseindex.com/gpu/h100-pricing-index)
- [https://www.hyperstack.cloud/gpu-pricing](https://www.hyperstack.cloud/gpu-pricing)
- [https://cyfuture.cloud/kb/data-centers/get-the-real-data-center-colocation-pricing-in-2025-market](https://cyfuture.cloud/kb/data-centers/get-the-real-data-center-colocation-pricing-in-2025-market)
- [https://spo.hawaii.gov/wp-content/uploads/2023/11/DR-Fortress_REVISED-05_Attachment-5_OF3_Schedule-A_RFP22002_SoH-RFP-22002-Pricing_7182023_FINAL-FOR-STATE-ETS-Approved-11-17-23.pdf](https://spo.hawaii.gov/wp-content/uploads/2023/11/DR-Fortress_REVISED-05_Attachment-5_OF3_Schedule-A_RFP22002_SoH-RFP-22002-Pricing_7182023_FINAL-FOR-STATE-ETS-Approved-11-17-23.pdf)
- [https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b)
- [https://www.delltechnologies.com/asset/zh-cn/products/servers/briefs-summaries/poweredge-server-gpu-matrix.pdf](https://www.delltechnologies.com/asset/zh-cn/products/servers/briefs-summaries/poweredge-server-gpu-matrix.pdf)
- [https://www.sec.gov/Archives/edgar/data/1769628/000176962826000094/coreweave4q25earningspress.htm](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000094/coreweave4q25earningspress.htm)
- [https://www.datacenterdynamics.com/en/news/ai-cloud-lambda-hires-investment-banks-in-preparation-for-ipo-report/](https://www.datacenterdynamics.com/en/news/ai-cloud-lambda-hires-investment-banks-in-preparation-for-ipo-report/)
- [https://lambda.ai/nvidia-h100-nvidia-h200-gpus](https://lambda.ai/nvidia-h100-nvidia-h200-gpus)
- [https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
- [https://sacra.com/c/runpod/](https://sacra.com/c/runpod/)
- [https://configurator.exxactcorp.com/configure/TS4-101818584](https://configurator.exxactcorp.com/configure/TS4-101818584)
- [https://publicpromiseprocurement.org/wp-content/uploads/2025/09/Copy-of-Iron_Mountain_-_Attachment_D-National_Pricing.pdf](https://publicpromiseprocurement.org/wp-content/uploads/2025/09/Copy-of-Iron_Mountain_-_Attachment_D-National_Pricing.pdf)
- [https://docs.coreweave.com/pricing/pricing-instances](https://docs.coreweave.com/pricing/pricing-instances)
- [https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm](https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm)
- [https://console.vast.ai/faq](https://console.vast.ai/faq)
- [https://tensordock.com/host](https://tensordock.com/host)
- [https://akash.network/roadmap/aep-23](https://akash.network/roadmap/aep-23)

*Query time: 1346.1s | Tokens: 215,459*

---

# Query 6: VC Critique with Numbers (VCによる数字付き批判)

2026年3月28日時点の公開情報ベースでいうと、AIXS（株式会社アイエクセス）は**医療・医学向けNLP/可視化AI**を中核に、**SI/派遣**を併走させてきた会社です。資本金は3,000万円で、METI白書では**SIの安定収益でAI開発を回し、持株会社ベースで1億円超を調達**したと説明されています。公開で確認しやすい導入実績は、**2023年7月の小野薬品向けMaTCH運用開始**です。なので、以下は「AIXS案件が**GPU再販＋異種R&D統合＋ToC先行＋グローバル展開**を投資ストーリーに含むなら」という前提で、かなり厳しめに批判します。 ([ai-xs.co.jp](https://ai-xs.co.jp/?p=30))

**結論から言うと、現状は“見送り寄り”です。**  
理由は単純で、投資家が欲しいのは**ソフトウェア並みの粗利と再現性ある成長**ですが、このストーリーだとAIXSは、①低マージン化しやすいGPU流通/インフラ、②巨人がすでに握っているToC分配、③日本発スタートアップとしては低いグローバル勝率、の3つの逆風を同時に受けます。公開情報上のAIXS本体も、まだ**“1社導入が見える縦型AI会社”**の域を出ていません。 ([ono-pharma.com](https://www.ono-pharma.com/ja/news/20230718.html))

### 1) GPU再販の粗利10-20%は、むしろ「危ない」
GPU再販/AIサーバー販売で**粗利10-20%**を置くのは、一見悪くないようで実はかなり危ういです。チャネルの現実を見ると、TD SYNNEXのFY2025 Q4粗利率は**6.87%**、営業利益率は**2.29%**。Ingram MicroはFY2025 Q4で、**AI-enablement案件へのミックスシフト**が原因で営業利益率が**0.99%**まで低下しました。SupermicroですらFY2025 Q2のnon-GAAP粗利率は**11.9%**、営業利益率は**7.9%**です。DellもAIサーバーは**“margin rate-dilutive”**、しかも**BlackwellはHopperより低マージン**と説明しています。つまり、10-20%の粗利を達成しても、販管費・金融コスト・保守・在庫・値下がりリスクを引くと、営業利益はかなり薄くなりやすい、というのが上場大手の実績です。これはAIXSのような小規模プレーヤーにはさらに不利です。 ([ir.tdsynnex.com](https://ir.tdsynnex.com/news/news-details/2026/TD-SYNNEX-Reports-Record-Fiscal-2025-Fourth-Quarter-Results/default.aspx))

さらに価格面でも逃げ場がありません。AWSは2025年6月に、H100搭載P5の**オンデマンド価格を44%**、3年Savings Planで**45%**下げました。CoreWeaveの現行公開価格でも**8x H100が$49.24/時、8x H200が$50.44/時、8x B200が$68.80/時**で、LambdaもB200を**$4.62/GPU時**で出しています。要するに、GPU供給が逼迫している局面だけを切り取れば儲かって見えますが、価格公開・価格比較・世代更新が進むと、再販プレーヤーの“超過利潤”はすぐ削られます。GPU再販は**高成長に見えて、収益の質が低い**です。 ([aws.amazon.com](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/))

### 2) 後発劣位は「実行力」で埋まる差ではなく、**桁の差**
もしAIXSがToCやAIインフラまで取りに行くなら、後発劣位は定性的な話ではなく**数量で圧倒的**です。Alphabetは**2025年CapExが$91.4B、2026年ガイダンスが$175-185B**。Metaは**2025年CapExが$72.22B、2026年ガイダンスが$115-135B**です。OpenAIは**800M超の週次ユーザー**と**100万超の法人顧客**を公表し、Googleは**Gemini App 750M MAU**と**Gemini Enterprise 800万席超**、Metaは**Meta AIがほぼ10億MAU**と言っています。これに対してAIXSの公開資本金は**3,000万円**、白書上の資金調達も**持株会社合計で1億円超**レベルです。競争相手が巨人だから不利、ではなく、**必要な投資量・分配量・データ量が何桁も違う**のです。 ([abc.xyz](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx))

### 3) 異種R&D統合は「需要ゼロ」ではないが、**需要の形を誤解しやすい**
ここは重要で、私は「需要がない」とは言いません。需要はあります。日本製薬工業協会の17社アンケートでは、医薬品開発効率化のためのAI/機械学習活用について、**29%が実装済み、65%が検討中・開発中**でした。ただし同じ報告書は、実装例の多くが**機械翻訳、検索、文書作成、論文テキストマイニング、安全性情報収集、試験デザイン**などの**限定されたワークフロー**だと示しています。つまり市場が買っているのは、いきなり“異種R&Dを全部統合するOS”ではなく、**痛みの強い縦の業務を切る道具**です。 ([jpma.or.jp](https://www.jpma.or.jp/information/evaluation/results/allotment/tcjmdm0000001ecw-att/CL_202405_TF1_DX.pdf))

AIXSの公開導入事例も、その読みを裏づけます。小野薬品向けMaTCHは、**PubMedの3,500万件超の医学論文**を対象に、**メディカルアフェアーズの戦略構築**を支援するものです。これは良い実績ですが、証明しているのは**医療論文解析の垂直ニーズ**であって、**異種R&D統合プラットフォーム**の普遍需要ではありません。投資家として欲しいのは、①複数部門が同時に予算を出している証拠、②医療以外への有料横展開、③複数の継続課金ロゴ、です。公開情報だけではそこがまだ弱いです。 ([ono-pharma.com](https://www.ono-pharma.com/ja/news/20230718.html))

### 4) ToC先行は、今の市場構造だと**原則マイナス**
ToC先行が許されるのは、**圧倒的な口コミ成長**か、**独自データが貯まる参加型ネットワーク**がある場合だけです。現実には、ChatGPTは**800M超の週次ユーザー**、Gemini Appは**750M MAU**、Meta AIは**ほぼ10億MAU**です。しかもOpenAI自身が、**巨大な消費者認知が法人導入の摩擦を下げる**と説明し、実際に**100万超の法人顧客**を積んでいます。つまり今のToC AIは、ToCが独立した市場というより、**B2B/B2B2Cのための分配前線基地**です。ここに後発のAIXSが単独で入るのは、CACでも継続率でもかなり不利です。 ([openai.com](https://openai.com/index/1-million-businesses-putting-ai-to-work/))

しかもJETROの2025年レポートでは、日本のスタートアップはB2Cで**“子どもから高齢者まで”国内全体を狙いがち**で、対して米国スタートアップは**狭いニッチで強いトラクションを取ってから世界展開**する傾向があると整理されています。さらに、ある起業家は日本では成功パスが**大企業向けか、1.2億人市場の国内総取り**に寄りがちだと述べています。だからAIXSがもしToCをやるなら、「まず日本でマスを取る」は悪手で、**超狭い国際ニッチを先に取る**のでなければ、ToC先行は投資家目線では減点です。 ([jetro.go.jp](https://www.jetro.go.jp/ext_images/en/invest/investment_environment/ijre/2025/ijreENreport2025.pdf))

### 5) 日本スタートアップのグローバル勝率は、統計的にはかなり低い
JETROによると、**2024年の日本の資金調達企業数は3,480社、調達総額は8,748億円**でしたが、**2025年10月時点のユニコーン数は日本8社、米国724社、中国158社**です。AIに限るとStanford AI Indexは、**2024年の日本のAI民間投資額を$0.93B**、**2013-24累計を$5.89B**、**2024年の新規資金調達AI企業数を42社**としています。対する米国は**$109.08B、累計$470.92B、1,073社**です。これは「日本から世界企業は出ない」という意味ではありませんが、投資家は**“日本発だから応援する”のではなく、“低い事前確率を上回る異常値があるか”**で見ないといけません。AIXSの公開情報だけでは、その異常値はまだ十分見えません。 ([jetro.go.jp](https://www.jetro.go.jp/ext_images/en/invest/investment_environment/ijre/2025/ijreENreport2025.pdf))

### 6) AIバブル崩壊リスクは、**AI需要が消える**というより、**中間層の利益が消える**リスク
Stanford AI Indexでは、**2024年の企業AI投資は$252.3B**、**世界のAI民間投資は$150.79B**、**生成AI投資は$33.9B**まで膨らみました。一方で、同じStanfordは**GPT-3.5級性能の推論コストが2022年11月から2024年10月にかけて280倍超低下**し、ハードウェアコストは**年30%低下**、エネルギー効率は**年40%改善**したとまとめています。さらにGoogleは、2024年の上位モデル競争で**トップと10位の性能差が11.9%から5.4%に縮小**したと説明しています。これは、**需要は伸びるが供給側の差別化はどんどん薄まる**、ということです。 ([hai.stanford.edu](https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter4_final.pdf))

加えて、物理投資は重い。IEAによると、データセンターの電力消費は**2024年に415TWh**で、**2030年には945TWh**へ倍増超の見通しです。そこへAWSのH100大幅値下げのような価格圧縮が重なると、最も傷みやすいのは**GPUメーカーそのもの**よりも、**再販業者・ネオクラウド・中間統合層**です。だからAIXSがGPU再販やインフラ仲介に寄るほど、AIバブルの下落局面で一番危ないポジションを取りやすいです。 ([iea.org](https://www.iea.org/reports/energy-and-ai/executive-summary?utm_source=openai))

## 投資家としての最終判断
**今の公開情報だけなら、AIXSは「面白い技術会社」ではあるが、「大型リターンを狙う投資案件」としては弱い**です。  
特に弱いのは、  
1. **粗利構造**がソフトウェア型に見えないこと、  
2. **需要証拠**が縦型ユースケース止まりなこと、  
3. **ToCやGPU流通に出た瞬間、巨人と真正面衝突**すること、  
4. **日本発グローバル勝ち筋の事前確率が低い**こと、です。 ([ir.tdsynnex.com](https://ir.tdsynnex.com/news/news-details/2026/TD-SYNNEX-Reports-Record-Fiscal-2025-Fourth-Quarter-Results/default.aspx))

**逆に、投資判断を変える条件**は明確です。  
- GPU再販ではなく、**自社ソフト粗利70%+**が見えること。  
- 小野薬品以外に、**複数の有料導入ロゴ**が出ること。  
- 医療以外でも、**異種R&D統合に対する実課金**があること。  
- ToCをやるなら、**日本マス市場ではなく、国際ニッチでの継続率・CAC回収**が証明されること。  
- 海外売上比率や英語運用など、**最初からグローバル仕様**であること。  

必要なら次に、**この批判を投資委員会メモ形式（投資仮説 / 反証条件 / DD質問リスト）**に落として出します。

### URL Citations (Query 6)

- [会社情報 | 株式会社アイエクセス](https://ai-xs.co.jp/?p=30)
- [小野薬品とアイエクセス、共同で医学論文のトピック抽出分析AIシステムを開発 | ONO CORPORATE](https://www.ono-pharma.com/ja/news/20230718.html)
- [
	TD SYNNEX - TD SYNNEX Reports Record Fiscal 2025 Fourth Quarter Results
](https://ir.tdsynnex.com/news/news-details/2026/TD-SYNNEX-Reports-Record-Fiscal-2025-Fourth-Quarter-Results/default.aspx)
- [Announcing up to 45% price reduction for Amazon EC2 NVIDIA GPU-accelerated instances | AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/)
- [
	Alphabet Investor Relations - 2025 Q4 Earnings Call
](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx)
- [https://www.jpma.or.jp/information/evaluation/results/allotment/tcjmdm0000001ecw-att/CL_202405_TF1_DX.pdf](https://www.jpma.or.jp/information/evaluation/results/allotment/tcjmdm0000001ecw-att/CL_202405_TF1_DX.pdf)
- [1 million business customers: the fastest-growing business platform in history | OpenAI](https://openai.com/index/1-million-businesses-putting-ai-to-work/)
- [https://www.jetro.go.jp/ext_images/en/invest/investment_environment/ijre/2025/ijreENreport2025.pdf](https://www.jetro.go.jp/ext_images/en/invest/investment_environment/ijre/2025/ijreENreport2025.pdf)
- [https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter4_final.pdf](https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter4_final.pdf)
- [Executive summary – Energy and AI – Analysis - IEA](https://www.iea.org/reports/energy-and-ai/executive-summary?utm_source=openai)

*Query time: 875.2s | Tokens: 222,732*

---

# Query 7: Rebuttal with Evidence (証拠に基づく反論)

以下、**Query 6 の各批判に対する“数字ベースの反論”**です。  
先に1点だけ整理すると、④でいう「ToC先行」は厳密には**“個人・小チーム起点の self-serve / PLG → 管理・統制・セキュリティ要件で ToB/Enterprise に拡張”**と読むのが正確です。Slack、Figma、Notion、Hugging Faceはいずれもそのパターンです。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1764925/000162828019004786/slacks-1.htm))

## 1) 「GPU再販は粗利10–20%しか出ない」への反論
この批判は、**“GPUを自社で仕入れて再販するモデル”**と、**“第三者GPU供給を束ねる marketplace / agency モデル”**を混同しています。後者では論点はハードの転売粗利ではなく、**take rate × 流通総額 × 稼働率**です。Vast.ai は公式FAQで、**成功ジョブ売上の75%をホスト、25%をVastが保持**すると明記しており、これはまさに20–30%レンジの marketplace take rate です。しかも Vast は公式リリースで、**350超の独立ホスト、17,000超GPU**を束ねる marketplace であり、**2019年以降の平均 YoY 成長 265%**、2024年は**約310%成長**と説明しています。つまり、比較対象は「低粗利のGPU卸売」ではなく、「高付加価値の二面市場プラットフォーム」です。 ([console.vast.ai](https://console.vast.ai/faq))

投資家向けの返しとしては、**「粗利10–20%批判は owner-operator 前提。Marketplace は revenue recognition も unit economics も別物」**で十分です。少なくとも Vast のような現行プレイヤーは、すでに**25% take rate**で成立しており、GPU resale 批判の前提自体がずれています。 ([console.vast.ai](https://console.vast.ai/faq))

## 2) 「後発劣位。大手クラウドが全部取る」への反論
**未サーブ顧客セグメントは小さくありません。** UNESCO の Science Report では、世界の研究者プールは**2018年時点で 885.4万人（FTE）**、さらに UIS の 2025年アップデートでは、**世界の研究者密度は2015年の1,137人/100万人から2022年には1,420人/100万人へ上昇**しています。つまり、研究人材そのものが増えており、学術・研究用途の compute 需要母数は拡大しています。 ([unesco.org](https://www.unesco.org/reports/science/2021/en/statistics))

米国だけでも、NSF/NCSES によれば**2023年度の大学 R&D 支出は 1,088億ドル**、調査対象は**914機関**です。にもかかわらず、Brown 大学などの研究者調査では、**85%が cloud compute 予算ゼロ**、**66%が所属先計算資源への満足度を5点中3以下**、**41%は multi-node 支援なし**、典型的な学術環境は**1–8 GPUを数日〜数週間使える程度**と報告されています。Nature も 2024年に「学術研究者は強力なチップへのアクセス不足に不満」と報じました。つまり、**“大手が全部取っている”のではなく、“学術・小規模ラボに十分届いていない”**のが実態です。 ([ncses.nsf.gov](https://ncses.nsf.gov/pubs/nsf25313/section/21485))

さらに小規模事業者側も無視できません。NCSES によれば、**従業員10–249人の中小企業は2023年に米国 business R&D の9%を実施**しており、総額**7,220億ドル**に対して約**649.8億ドル相当**です。加えて**1–9人の microbusiness だけでも 2022年に 57億ドルの R&D を自社実施**しています。これは hyperscaler の最優先顧客ではないが、十分にお金を払う実需セグメントです。 ([ncses.nsf.gov](https://ncses.nsf.gov/pubs/nsf25353))

政策面でも未充足需要は明白です。NSF の NAIRR pilot は「AI資源へのアクセス民主化」を目的に始まり、**2024年10月時点で150件超の resource award** を出しています。もし大手クラウドだけで十分なら、こうした公的アクセス基盤はここまで急いで作られていません。 ([nsf.gov](https://www.nsf.gov/science-matters/us-nairr-pilot-brings-cutting-edge-ai-resources-researchers))

## 3) 「異種R&D統合の需要は本当にあるのか」への反論
厳密に「Lab-as-a-Service」単独の公的 TAM はまだ薄いですが、**隣接市場はすでに十分に大きく、しかも成長しています。** Grand View Research によれば、**lab automation** は**2024年 82.7億ドル → 2033年 183.9億ドル（CAGR 9.3%）**、**laboratory informatics** は**2025年 40.7億ドル → 2033年 59.8億ドル（CAGR 4.9%）**、**cloud-based LIMS** は**2025年 9.07億ドル → 2033年 15.69億ドル（CAGR 7.1%）**です。要するに、**自動化・データ管理・クラウド制御の予算は既に立っている**ので、Lab-as-a-Service は「ゼロから市場を作る話」ではなく、これらを束ね直す話です。 ([grandviewresearch.com](https://www.grandviewresearch.com/industry-analysis/lab-automation-market))

ワークフロー面の需要も強いです。Benchling の 2024 調査では、**大手バイオファーマの IT の43%が“20超の科学ソフト”を支えている**と回答し、**小規模企業で“R&D組織の60%以上の実験機器が自動データ取得されている”のは37%にとどまり**、**cloud-based scientific software / SaaS の採用は小規模23%、大企業17%**でした。2026年の Benchling 調査でも、AI導入は**“データが scattered / incomplete / hard to validate” な領域で失速**し、逆に**89%の科学者が copilot / reasoning tools を最初の入口として使う**とされています。つまり需要がないのではなく、**データとワークフローの断絶がボトルネック**です。そこを埋めるのが Lab-as-a-Service です。 ([benchling.com](https://www.benchling.com/blog/2024-state-of-tech-report))

研究者全般の業務負荷も追い風です。Elsevier の 2025年グローバル調査では、**研究に十分な時間があると答えたのは45% בלבד**、一方で**58%が既に AI ツールを使用**しています。研究者が求めているのは、単発の AI ではなく、**探索→実験→記録→解析→共有**を短縮する統合ワークフローです。 ([elsevier.com](https://www.elsevier.com/about/press-releases/elseviers-global-survey-of-3-000-researchers-reveals-less-than-half-have))

加えて、需要の制度面シグナルも強いです。米議会の **Cloud LAB Act of 2025** は、NSF に cloud laboratory network の構築を求め、**少なくとも2つの phase II cloud labs、さらに少なくとも3つの phase III cloud labs** を整備する設計です。Strateos も、**on-site cloud labs への顧客需要増加**を理由に戦略転換し、**top 20 バイオファーマ2社向けの multi-million-dollar 設計案件**完了を公表しました。市場がなければ、政策も大手顧客もここまで動きません。 ([congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/2676/text))

## 4) 「ToC先行は危険。最初からToBに行くべき」への反論
この批判は半分正しくて、半分ズレています。正確には**“ToC”ではなく、“個人起点・小チーム起点の PLG”**です。そして、workflow/DevTools ではこの型が非常に強い。Slack の S-1 では、**free version で初期利用と organic adoption を促し、enterprise decision-makers は社内の自然増殖を見て採用を決めることが多い**と明記されています。さらに Slack は、**free-to-paid conversion を customer experience team の中核KPI**としていました。これはまさに bottom-up → top-down の教科書例です。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1764925/000162828019004786/slacks-1.htm))

Figma も同じで、Adobe 向け S-4 では、**Figma の revenue growth のかなりの部分は “word-of-mouth” による組織内の organic growth**から来ると説明され、**free offering から paid customer への conversion**が明示的な論点になっています。さらに Figma の 2025年公式発表では、**Q4 2024 の MAU の約3分の2が伝統的デザイン職以外**、**約30%は developers**、**85%のMAUが米国外**でした。つまり、最初は個人/小チームが使い始め、やがて開発・PM・マーケ・経営層まで巻き込むことで Enterprise 化しているわけです。 ([adobe.com](https://www.adobe.com/content/dam/cc/en/investor-relations/pdfs/ADBE-S-4_Consent-Solicitation-Statement-of-Figma-Inc-And-Prospectus-of-Adobe-Inc.pdf))

Notion も典型例です。Notion の公式 product ページは**“Over 100M users worldwide”**、**“62% of Fortune 100”** を掲げつつ、入口は**“Try for free”**です。Pricing でも、**Free plan → per-member paid seat → Enterprise analytics / security** という設計が明確です。つまり free/self-serve を入口にしつつ、組織導入時に管理・統制・分析で monetization を深めています。 ([notion.com](https://www.notion.com/product))

Hugging Face はさらに分かりやすいです。2025年12月時点で、**13 million AI builders**、**300,000 organizations** が Hub に存在し、同社は Fortune 500 企業ですら**free organizations**を使っている実態を指摘しています。一方で Enterprise plan では **SSO、RBAC、audit logs、SCIM** などを提供しています。つまり、**コミュニティ/個人利用が先に広がり、ガバナンス需要が後から Enterprise 売上になる**。これを「ToC先行は危険」と切って捨てるのは、AI/DevTools の実例と逆です。 ([huggingface.co](https://huggingface.co/blog/jeffboudier/shadow-ai))

## 5) 「日本スタートアップはグローバルで勝てない」への反論
これは**“勝率が高い”とは言えないが、“勝率ゼロ”は明確に誤り**です。日本発/日本起点でも、少なくとも B2D・コラボレーション・OSS インフラでは成立例があります。最も分かりやすいのは Nulab で、**2004年に福岡で創業**、現在 **4M+ users、180+ countries、5 offices**。Backlog は **2019年に 10,000 paid customers**、2020年時点で**1.7 million active users**を超え、現在も **“Trusted by over 4 million users worldwide”** を公式に掲げています。これは日本本社のままグローバル化した collaboration / developer-adjacent SaaS の成立例です。 ([nulab.com](https://nulab.com/about/))

Treasure Data も重要です。公式 company page では、**550+ employees、80+ Forbes Global 2000 customers、75+ countries supported、2B+ profiles managed**、拠点も**Mountain View / New York / Tokyo / London / Nice / Vancouver** と明記されています。しかも 2012年の公式 launch 時点で、**paying customers を持ち、100 billion rows 超のデータを管理**していました。さらに共同創業者 Kaz Ohta は、同社公式リリースによれば**日本の Hadoop User Group 創設者**です。Treasure Data は厳密には CDP ですが、**日本人創業・OSS/data infrastructure 起点で世界企業に売る**という意味で、十分に「日本起点のグローバル開発者インフラ成功例」です。 ([treasuredata.com](https://www.treasuredata.com/company))

OSS では Fluentd がさらに強い反例です。Fluentd 公式サイトは**5,000+ data-driven companies rely on Fluentd**、**largest user 50,000+ servers** と記載し、CNCF の project page では**41,330 contributors、9,222 contributing organizations** を示しています。Treasure Data の紹介ページでも、**日本人創業者チームが Fluentd / Fluent Bit などを生み出した**とされています。つまり「日本発グローバルDevToolsは無理」ではなく、**英語・OSS・海外顧客を最初から取りに行く設計ができれば十分成立する**、が正しい言い方です。 ([fluentd.org](https://www.fluentd.org/))

## 6) 「AIバブルが崩れたら終わる」への反論
**むしろ今のデータは、効率改善が需要減ではなく需要増につながる“ジェヴォンズ型”を示しています。** TSMC は 2025 Q1 コールで、**AI accelerators revenue は 2025年に倍増**、さらに **2024–2029年の5年間で mid-to-high-50s% CAGR** まで見通しを引き上げました。しかも同社は、**reasoning models や DeepSeek のような効率化は barriers を下げ、AIモデルの wider usage / greater adoption を生み、結果として leading-edge silicon をより必要にする**と明言しています。これはジェヴォンズのパラドックスを、供給側の最重要プレイヤーがそのまま語っているに等しいです。 ([investor.tsmc.com](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-04/7630274eecc1197a4e3ea6a415f44a47204fe10a/TSMC%201Q25%20Transcript.pdf))

実需側でも同じです。Alphabet は 2025 Q3 コールで、**月間 token 処理量が 1.3 quadrillion、1年で20倍超**になったと開示しました。Q2 2025 の公式決算では、Cloud の需要増を受けて **2025年 capex を約850億ドルに引き上げ**、Q4 2025 コールでは **2025年実績 capex が 910億ドル**、2026年も同程度の投資を想定しつつ、なお**供給制約状態が続く**と説明しています。効率化しているのに、総需要は爆発的に増えているわけです。 ([abc.xyz](https://abc.xyz/investor/events/event-details/2025/2025-Q3-Earnings-Call-2025-4OI4Bac_Q9/default.aspx))

Microsoft と Meta も同方向です。Microsoft は公式ブログで、**FY2025 に AI-enabled datacenters へ約800億ドル投資**すると表明しました。Meta は 2025年に **722.2億ドルの capex** を使い、2026年ガイダンスを **1,150億〜1,350億ドル**に引き上げています。これは「バブル崩壊で capex が止まる」どころか、**2026年にさらに増やす**という意思表示です。 ([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/))

そして GPU 需要の最前線では、NVIDIA の 2026会計年度データセンター売上は**1,937億ドル、前年比68%増**、Q4 だけでも **623億ドル、前年比75%増**でした。NVIDIA CEO は同時に、**lower cost per token** と **enterprise adoption of agents is skyrocketing** を並べて語っています。つまり、**単価が下がるほど利用用途が増え、総需要はさらに伸びる**という構造です。これは「AIバブル」よりも、**AI compute が電力・ネットワークに近い基盤需要へ移行している**と読む方が実態に近いです。 ([nvidianews.nvidia.com](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026))

---

## そのまま投資家向けに使える短い結論
- **①粗利批判**：GPU再販ではなく marketplace take rate モデル。Vast の公式 fee は **25%**。比較前提が違う。 ([console.vast.ai](https://console.vast.ai/faq))
- **②後発劣位**：未サーブ市場は実在。**世界研究者 885万人超、米大学R&D 1,088億ドル、学術の85%が cloud budget なし**。 ([unesco.org](https://www.unesco.org/reports/science/2021/en/statistics))
- **③統合需要**：lab automation / informatics / cloud LIMS は **5–9%台 CAGR**、しかもワークフロー断絶は Benchling/Elsevier が確認。 ([grandviewresearch.com](https://www.grandviewresearch.com/industry-analysis/lab-automation-market))
- **④ToC先行**：厳密には self-serve/PLG。Slack/Figma/Notion/HF は全部 **個人起点→Enterprise課金**。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1764925/000162828019004786/slacks-1.htm))
- **⑤日本発勝率**：ゼロではない。**Nulab、Treasure Data、Fluentd** が反例。 ([nulab.com](https://nulab.com/about/))
- **⑥バブル崩壊**：効率化は需要減でなく需要増。**TSMC AI売上CAGR mid-high 50s%、Google tokens 20x、Meta 2026 capex 115–135B、NVIDIA DC売上 +68%**。 ([investor.tsmc.com](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf))

必要なら次に、これを  
**「投資家FAQ形式（Q→A）」** か **「3分ピッチ用の反論スライド6枚」** にそのまま再構成します。

### URL Citations (Query 7)

- [https://www.sec.gov/Archives/edgar/data/1764925/000162828019004786/slacks-1.htm](https://www.sec.gov/Archives/edgar/data/1764925/000162828019004786/slacks-1.htm)
- [https://console.vast.ai/faq](https://console.vast.ai/faq)
- [https://www.unesco.org/reports/science/2021/en/statistics](https://www.unesco.org/reports/science/2021/en/statistics)
- [https://ncses.nsf.gov/pubs/nsf25313/section/21485](https://ncses.nsf.gov/pubs/nsf25313/section/21485)
- [https://ncses.nsf.gov/pubs/nsf25353](https://ncses.nsf.gov/pubs/nsf25353)
- [U.S. NAIRR pilot brings cutting-edge AI resources to researchers and educators across the nation | NSF - U.S. National Science Foundation](https://www.nsf.gov/science-matters/us-nairr-pilot-brings-cutting-edge-ai-resources-researchers)
- [https://www.grandviewresearch.com/industry-analysis/lab-automation-market](https://www.grandviewresearch.com/industry-analysis/lab-automation-market)
- [https://www.benchling.com/blog/2024-state-of-tech-report](https://www.benchling.com/blog/2024-state-of-tech-report)
- [https://www.elsevier.com/about/press-releases/elseviers-global-survey-of-3-000-researchers-reveals-less-than-half-have](https://www.elsevier.com/about/press-releases/elseviers-global-survey-of-3-000-researchers-reveals-less-than-half-have)
- [https://www.congress.gov/bill/119th-congress/senate-bill/2676/text](https://www.congress.gov/bill/119th-congress/senate-bill/2676/text)
- [https://www.adobe.com/content/dam/cc/en/investor-relations/pdfs/ADBE-S-4_Consent-Solicitation-Statement-of-Figma-Inc-And-Prospectus-of-Adobe-Inc.pdf](https://www.adobe.com/content/dam/cc/en/investor-relations/pdfs/ADBE-S-4_Consent-Solicitation-Statement-of-Figma-Inc-And-Prospectus-of-Adobe-Inc.pdf)
- [https://www.notion.com/product](https://www.notion.com/product)
- [https://huggingface.co/blog/jeffboudier/shadow-ai](https://huggingface.co/blog/jeffboudier/shadow-ai)
- [https://nulab.com/about/](https://nulab.com/about/)
- [https://www.treasuredata.com/company](https://www.treasuredata.com/company)
- [https://www.fluentd.org/](https://www.fluentd.org/)
- [https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-04/7630274eecc1197a4e3ea6a415f44a47204fe10a/TSMC%201Q25%20Transcript.pdf](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-04/7630274eecc1197a4e3ea6a415f44a47204fe10a/TSMC%201Q25%20Transcript.pdf)
- [https://abc.xyz/investor/events/event-details/2025/2025-Q3-Earnings-Call-2025-4OI4Bac_Q9/default.aspx](https://abc.xyz/investor/events/event-details/2025/2025-Q3-Earnings-Call-2025-4OI4Bac_Q9/default.aspx)
- [https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/)
- [https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
- [https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf)

*Query time: 1324.9s | Tokens: 331,840*

---

# Appendix: All URL Citations (Deduplicated)

1. [A single data and AI development environment - Amazon SageMaker Unified Studio - AWS](https://aws.amazon.com/sagemaker/unified-studio/)
2. [Welcome to Google Cloud Next '25 | Google Cloud Blog](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next25)
3. [Introducing CoreAI – Platform and Tools - The Official Microsoft Blog](https://blogs.microsoft.com/blog/2025/01/13/introducing-core-ai-platform-and-tools/)
4. [Connect Developers to Global GPU Compute | NVIDIA DGX Cloud Lepton](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/)
5. [Collaborate and build faster with Amazon SageMaker Unified Studio, now generally available | AWS News Blog](https://aws.amazon.com/blogs/aws/collaborate-and-build-faster-with-amazon-sagemaker-unified-studio-now-generally-available/)
6. [Create a Braket notebook instance using CloudFormation - Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-cloudformation.html)
7. [
	Amazon.com, Inc. - Amazon.com Announces Fourth Quarter Results
](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx)
8. [CreateDeploymentJob - AWS RoboMaker](https://docs.aws.amazon.com/robomaker/latest/dg/API_CreateDeploymentJob.html?utm_source=openai)
9. [Meet Willow, our state-of-the-art quantum chip](https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/)
10. [Google Research launches new scientific research tool, AI co-scientist](https://blog.google/feed/google-research-ai-co-scientist/)
11. [Microsoft recognized for second consecutive year as a Leader in the 2025 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms | Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/microsoft-recognized-for-second-consecutive-year-as-a-leader-in-the-2025-gartner-magic-quadrant-for-data-science-and-machine-learning-platforms/?msockid=35ae5d2b9b146e181a6f4bde9ac26f6b)
12. [Microsoft Build 2025: AI エージェントの時代とオープンなエージェント型 Web の構築へ - News Center Japan](https://news.microsoft.com/ja-jp/2025/05/20/250520-microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/?msockid=216e5633831e611c1ad3404482ce6091)
13. [
	NVIDIA Corporation - NVIDIA and Global Industrial Software Giants Bring Design, Engineering and Manufacturing Into the AI Era
](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Global-Industrial-Software-Giants-Bring-Design-Engineering-and-Manufacturing-Into-the-AI-Era/default.aspx)
14. [会社情報 | 株式会社アイエクセス](https://ai-xs.co.jp/?p=30)
15. [Databricks Grows >55% YoY, Surpasses $4.8B Revenue Run-Rate, and is Raising >$4B Series L at $134B Valuation](https://www.prnewswire.com/news-releases/databricks-grows-55-yoy-surpasses-4-8b-revenue-run-rate-and-is-raising-4b-series-l-at-134b-valuation-302643445.html?utm_source=openai)
16. [Introducing Benchling AI | Benchling News](https://www.benchling.com/news/introducing-benchling-ai?utm_source=openai)
17. [CoreWeave Acquires Weights & Biases | CoreWeave](https://www.coreweave.com/blog/coreweave-completes-acquisition-of-weights-biases?utm_source=openai)
18. [Announcing Our Series B](https://sakana.ai/series-b/?utm_source=openai)
19. [SkyPilot: Run AI on Any Infrastructure — SkyPilot Docs](https://docs.skypilot.co/en/latest/docs/index.html?utm_source=openai)
20. [Weights & Biases raises $50 Million round led by Daniel Gross and Nat Friedman](https://wandb.ai/site/press-release/weights-biases-raises-50-million-round-led-by-daniel-gross-and-nat-friedman-announces-wb-prompts?utm_source=openai)
21. [Announcing MLflow 3.0 | MLflow](https://mlflow.org/blog/mlflow-3-0-launch?utm_source=openai)
22. [Databricks Announces $15B in Financing to Attract Top AI Talent and Accelerate Global Expansion](https://www.prnewswire.com/news-releases/databricks-announces-15b-in-financing-to-attract-top-ai-talent-and-accelerate-global-expansion-302356888.html?utm_source=openai)
23. [Benchling Raises $100M in Series F Financing Co-Led by Altimeter and Franklin Templeton](https://www.benchling.com/news/benchling-raises-100m-in-series-f-financing-co-led-by-altimeter-and-franklin-templeton?utm_source=openai)
24. [Emerald Cloud Lab: Remote Controlled Life Sciences Lab](https://www.emeraldcloudlab.com/?utm_source=openai)
25. [Emerald Therapeutics Completes Latest Financing, Brings Total to $13.5MM; Launches Emerald Cloud Lab, a New Approach to Biotech Research | Fierce Biotech](https://www.fiercebiotech.com/biotech/emerald-therapeutics-completes-latest-financing-brings-total-to-13-5mm-launches-emerald?utm_source=openai)
26. [About](https://www.futurehouse.org/about?utm_source=openai)
27. [Sakana AI「事業開発本部」を立ち上げ：AI技術のビジネス展開に着手](https://sakana.ai/business-team/?utm_source=openai)
28. [Sciloop](https://www.sciloop.dev/)
29. [Sciloop: AI Co-Scientist that automates ML experimentation and analysis. | Y Combinator](https://www.ycombinator.com/companies/sciloop?utm_source=openai)
30. [Race Capital Website](https://www.race.capital/portfolio/skypilot?utm_source=openai)
31. [AI container orchestration for AI teams - dstack](https://dstack.ai/?utm_source=openai)
32. [dstack Stock Price, Funding, Valuation, Revenue & Financial Statements](https://www.cbinsights.com/company/dstack/financials?utm_source=openai)
33. [Anyscale | Production-Ready AI with Ray](https://www.anyscale.com/?utm_source=openai)
34. [Anyscale Secures $100M Series C at $1B Valuation to Radically Simplify Scaling and Productionizing AI Applications](https://www.anyscale.com/press/anyscale-secures-100m-series-c-at-1b-valuation-to-radically-simplify-scaling-and-productionizing-ai-applications?utm_source=openai)
35. [Introducing: Modal 1.0](https://modal.com/blog/introducing-client-1-0?utm_source=openai)
36. [Announcing our $87M Series B](https://modal.com/blog/announcing-our-series-b?utm_source=openai)
37. [500 biotech companies are using Benchling AI, now generally available](https://www.benchling.com/blog/benchling-ai-now-generally-available?utm_source=openai)
38. [事業内容 | 株式会社アイエクセス](https://ai-xs.co.jp/business/)
39. [aixsolutions.ai](https://aixsolutions.ai/?utm_source=openai)
40. [https://investors.datadoghq.com/static-files/bf7296e6-b2cd-4464-973a-5f36abefa033](https://investors.datadoghq.com/static-files/bf7296e6-b2cd-4464-973a-5f36abefa033)
41. [snow-20250131](https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm)
42. [Form 10-K for Mongodb INC filed 03/21/2025](https://investors.mongodb.com/static-files/2e35ada9-36d6-4ea2-a03a-bbba3b559770)
43. [Elastic - Elastic Reports Fourth Quarter and Fiscal 2025 Financial Results](https://ir.elastic.co/news/news-details/2025/Elastic-Reports-Fourth-Quarter-and-Fiscal-2025-Financial-Results/default.aspx?utm_source=openai)
44. [Confluent | The Data Streaming Platform](https://investors.confluent.io/news-releases/news-release-details/confluent-announces-second-quarter-2025-financial-results/)
45. [EBook+V2_HASHICORP,+INC_PWO-38078_CWO-28432.pdf](https://www.sec.gov/Archives/edgar/data/1720671/000114036124025955/ny20021845x3_ars.pdf)
46. [Twilio Inc. - Twilio Unveils Next-Generation Customer Engagement Platform Built for an AI and Data-Powered World at SIGNAL 2025](https://investors.twilio.com/news-releases/news-release-details/twilio-unveils-next-generation-customer-engagement-platform?utm_source=openai)
47. [Stripe publishes 2025 annual letter and announces tender offer to provide liquidity to current and former employees](https://stripe.com/newsroom/news/stripe-2025-update?utm_source=openai)
48. [https://www.sec.gov/Archives/edgar/data/1585521/000158552125000027/zm-20250224ex991.htm?utm_source=openai](https://www.sec.gov/Archives/edgar/data/1585521/000158552125000027/zm-20250224ex991.htm?utm_source=openai)
49. [About Us | Slack](https://slack.com/about?utm_source=openai)
50. [Salesforce Launches Trusted Generative AI for Customers in Slack - Salesforce](https://www.salesforce.com/news/stories/slack-ai-news/slack-ai_summarize/?utm_source=openai)
51. [Document](https://www.sec.gov/Archives/edgar/data/0001561550/000162828026006645/ex-991x20251231x8k.htm)
52. [AIXNET - Decentralized AI Infrastructure](https://www.aix.net/)
53. [Together AI Announces $305M Series B to Scale AI Acceleration Cloud for Open Source and Enterprise AI](https://www.together.ai/blog/together-ai-announcing-305m-series-b)
54. [AutoDL帮助文档](https://www.autodl.com/docs/gpu/)
55. [KubeRay Autoscaling — Ray 2.54.1](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html)
56. [More compute for AI, not less | Deloitte Insights](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html)
57. [Lambda Raises $320M to Build a GPU Cloud for AI](https://www.businesswire.com/news/home/20240215216669/en/Lambda-Raises-%24320M-to-Build-a-GPU-Cloud-for-AI)
58. [Crusoe secures $600 million in Series D round led by Founders Fund | Y94](https://y94.com/2024/12/12/crusoe-secures-600-million-in-series-d-round-led-by-founders-fund/?utm_source=openai)
59. [AI infrastructure firm Nscale bags record-breaking $2 billion Series C investment | IT Pro](https://www.itpro.com/infrastructure/uk-infrastructure-firm-nscale-bags-record-breaking-usd2-billion-series-c-investment)
60. [TensorWave Raises $43M in SAFE Funding, the Largest in Nevada Startup History, to Advance AI Compute Solutions.](https://www.tensorwave.com/blog/tensorwave-raises-43m-in-safe-funding-the-largest-in-nevada-startup-history-to-advance-ai-compute-solutions?trk=public_post_comment-text&utm_source=openai)
61. [GMI Cloud Raises $82 Million in Total Series A Funding to Drive Global Access to Advanced GPUs and Cloud Infrastructure](https://www.prnewswire.com/news-releases/gmi-cloud-raises-82-million-in-total-series-a-funding-to-drive-global-access-to-advanced-gpus-and-cloud-infrastructure-302289529.html)
62. [Baseten Lands $75M from IVP and Spark to Solve AI’s Biggest Bottleneck to Ubiquitous Adoption: Inference](https://www.businesswire.com/news/home/20250218263765/en/Baseten-Lands-%2475M-from-IVP-and-Spark-to-Solve-AIs-Biggest-Bottleneck-to-Ubiquitous-Adoption-Inference)
63. [矩池云 - 专注于人工智能领域的云服务商](https://matpool.com/?utm_source=openai)
64. [使用团队版教程 - 矩池云支持中心 - 矩池云支持中心](https://matpool.com/supports/doc-use-team-on-matpool/)
65. [0001045810-25-000116](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q1/b6df1c5c-5cb6-4a41-9d28-dd1bcd34cc26.pdf)
66. [MLflow Tracking | MLflow](https://mlflow.github.io/mlflow-website/docs/latest/ml/tracking/)
67. [Project Jupyter | JupyterHub](https://jupyter.org/hub)
68. [Kueue](https://kueue.sigs.k8s.io/)
69. [KServe | kserve](https://kserve.github.io/kserve/)
70. [Time-Slicing GPUs in Kubernetes — gpu-operator 22.9.1 documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/22.9.1/gpu-sharing.html)
71. [OpenCost Specification | OpenCost — open source cost monitoring for cloud native environments](https://opencost.io/docs/specification)
72. [The future AI workload](https://www.mckinsey.com/featured-insights/week-in-charts/the-future-ai-workload)
73. [GitHub - google-ai-edge/ai-edge-quantizer: AI Edge Quantizer: flexible post training quantization for LiteRT models. · GitHub](https://github.com/google-ai-edge/ai-edge-quantizer)
74. [www.ibm.com](https://www.ibm.com/roadmaps/quantum/2025/)
75. [vLLM](https://www.vllm.ai/)
76. [AI hyperscaler Nscale secures $155 million in Series A | Press Release | Nscale](https://www.nscale.com/press-releases/ai-hyperscaler-nscale-secures-usd-155-million-in-series-a?utm_source=openai)
77. [https://www.shopblt.com/item/emc-489-bbgj-nvidia-hgx-h100-4/legato_489bbgj.html](https://www.shopblt.com/item/emc-489-bbgj-nvidia-hgx-h100-4/legato_489bbgj.html)
78. [https://www.ebay.com/itm/205760203893](https://www.ebay.com/itm/205760203893)
79. [https://gpuleaseindex.com/gpu/h100-pricing-index](https://gpuleaseindex.com/gpu/h100-pricing-index)
80. [https://www.hyperstack.cloud/gpu-pricing](https://www.hyperstack.cloud/gpu-pricing)
81. [https://cyfuture.cloud/kb/data-centers/get-the-real-data-center-colocation-pricing-in-2025-market](https://cyfuture.cloud/kb/data-centers/get-the-real-data-center-colocation-pricing-in-2025-market)
82. [https://spo.hawaii.gov/wp-content/uploads/2023/11/DR-Fortress_REVISED-05_Attachment-5_OF3_Schedule-A_RFP22002_SoH-RFP-22002-Pricing_7182023_FINAL-FOR-STATE-ETS-Approved-11-17-23.pdf](https://spo.hawaii.gov/wp-content/uploads/2023/11/DR-Fortress_REVISED-05_Attachment-5_OF3_Schedule-A_RFP22002_SoH-RFP-22002-Pricing_7182023_FINAL-FOR-STATE-ETS-Approved-11-17-23.pdf)
83. [https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b)
84. [https://www.delltechnologies.com/asset/zh-cn/products/servers/briefs-summaries/poweredge-server-gpu-matrix.pdf](https://www.delltechnologies.com/asset/zh-cn/products/servers/briefs-summaries/poweredge-server-gpu-matrix.pdf)
85. [https://www.sec.gov/Archives/edgar/data/1769628/000176962826000094/coreweave4q25earningspress.htm](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000094/coreweave4q25earningspress.htm)
86. [https://www.datacenterdynamics.com/en/news/ai-cloud-lambda-hires-investment-banks-in-preparation-for-ipo-report/](https://www.datacenterdynamics.com/en/news/ai-cloud-lambda-hires-investment-banks-in-preparation-for-ipo-report/)
87. [https://lambda.ai/nvidia-h100-nvidia-h200-gpus](https://lambda.ai/nvidia-h100-nvidia-h200-gpus)
88. [https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
89. [https://sacra.com/c/runpod/](https://sacra.com/c/runpod/)
90. [https://configurator.exxactcorp.com/configure/TS4-101818584](https://configurator.exxactcorp.com/configure/TS4-101818584)
91. [https://publicpromiseprocurement.org/wp-content/uploads/2025/09/Copy-of-Iron_Mountain_-_Attachment_D-National_Pricing.pdf](https://publicpromiseprocurement.org/wp-content/uploads/2025/09/Copy-of-Iron_Mountain_-_Attachment_D-National_Pricing.pdf)
92. [https://docs.coreweave.com/pricing/pricing-instances](https://docs.coreweave.com/pricing/pricing-instances)
93. [https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm](https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm)
94. [https://console.vast.ai/faq](https://console.vast.ai/faq)
95. [https://tensordock.com/host](https://tensordock.com/host)
96. [https://akash.network/roadmap/aep-23](https://akash.network/roadmap/aep-23)
97. [小野薬品とアイエクセス、共同で医学論文のトピック抽出分析AIシステムを開発 | ONO CORPORATE](https://www.ono-pharma.com/ja/news/20230718.html)
98. [
	TD SYNNEX - TD SYNNEX Reports Record Fiscal 2025 Fourth Quarter Results
](https://ir.tdsynnex.com/news/news-details/2026/TD-SYNNEX-Reports-Record-Fiscal-2025-Fourth-Quarter-Results/default.aspx)
99. [Announcing up to 45% price reduction for Amazon EC2 NVIDIA GPU-accelerated instances | AWS News Blog](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/)
100. [
	Alphabet Investor Relations - 2025 Q4 Earnings Call
](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx)
101. [https://www.jpma.or.jp/information/evaluation/results/allotment/tcjmdm0000001ecw-att/CL_202405_TF1_DX.pdf](https://www.jpma.or.jp/information/evaluation/results/allotment/tcjmdm0000001ecw-att/CL_202405_TF1_DX.pdf)
102. [1 million business customers: the fastest-growing business platform in history | OpenAI](https://openai.com/index/1-million-businesses-putting-ai-to-work/)
103. [https://www.jetro.go.jp/ext_images/en/invest/investment_environment/ijre/2025/ijreENreport2025.pdf](https://www.jetro.go.jp/ext_images/en/invest/investment_environment/ijre/2025/ijreENreport2025.pdf)
104. [https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter4_final.pdf](https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter4_final.pdf)
105. [Executive summary – Energy and AI – Analysis - IEA](https://www.iea.org/reports/energy-and-ai/executive-summary?utm_source=openai)
106. [https://www.sec.gov/Archives/edgar/data/1764925/000162828019004786/slacks-1.htm](https://www.sec.gov/Archives/edgar/data/1764925/000162828019004786/slacks-1.htm)
107. [https://www.unesco.org/reports/science/2021/en/statistics](https://www.unesco.org/reports/science/2021/en/statistics)
108. [https://ncses.nsf.gov/pubs/nsf25313/section/21485](https://ncses.nsf.gov/pubs/nsf25313/section/21485)
109. [https://ncses.nsf.gov/pubs/nsf25353](https://ncses.nsf.gov/pubs/nsf25353)
110. [U.S. NAIRR pilot brings cutting-edge AI resources to researchers and educators across the nation | NSF - U.S. National Science Foundation](https://www.nsf.gov/science-matters/us-nairr-pilot-brings-cutting-edge-ai-resources-researchers)
111. [https://www.grandviewresearch.com/industry-analysis/lab-automation-market](https://www.grandviewresearch.com/industry-analysis/lab-automation-market)
112. [https://www.benchling.com/blog/2024-state-of-tech-report](https://www.benchling.com/blog/2024-state-of-tech-report)
113. [https://www.elsevier.com/about/press-releases/elseviers-global-survey-of-3-000-researchers-reveals-less-than-half-have](https://www.elsevier.com/about/press-releases/elseviers-global-survey-of-3-000-researchers-reveals-less-than-half-have)
114. [https://www.congress.gov/bill/119th-congress/senate-bill/2676/text](https://www.congress.gov/bill/119th-congress/senate-bill/2676/text)
115. [https://www.adobe.com/content/dam/cc/en/investor-relations/pdfs/ADBE-S-4_Consent-Solicitation-Statement-of-Figma-Inc-And-Prospectus-of-Adobe-Inc.pdf](https://www.adobe.com/content/dam/cc/en/investor-relations/pdfs/ADBE-S-4_Consent-Solicitation-Statement-of-Figma-Inc-And-Prospectus-of-Adobe-Inc.pdf)
116. [https://www.notion.com/product](https://www.notion.com/product)
117. [https://huggingface.co/blog/jeffboudier/shadow-ai](https://huggingface.co/blog/jeffboudier/shadow-ai)
118. [https://nulab.com/about/](https://nulab.com/about/)
119. [https://www.treasuredata.com/company](https://www.treasuredata.com/company)
120. [https://www.fluentd.org/](https://www.fluentd.org/)
121. [https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-04/7630274eecc1197a4e3ea6a415f44a47204fe10a/TSMC%201Q25%20Transcript.pdf](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-04/7630274eecc1197a4e3ea6a415f44a47204fe10a/TSMC%201Q25%20Transcript.pdf)
122. [https://abc.xyz/investor/events/event-details/2025/2025-Q3-Earnings-Call-2025-4OI4Bac_Q9/default.aspx](https://abc.xyz/investor/events/event-details/2025/2025-Q3-Earnings-Call-2025-4OI4Bac_Q9/default.aspx)
123. [https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/)
124. [https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
125. [https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf)
