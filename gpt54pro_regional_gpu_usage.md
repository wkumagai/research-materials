# GPT-5.4-pro 地域別GPU利用実態調査

Model: gpt-5.4-pro (Responses API + web_search_preview)
調査日: 2026-03-28

---

## 1. アメリカのGPU利用実態

以下、**2025–2026年の公開データを優先**し、**公開されていない指標は代理指標か推定**で補った、米国におけるAI用途GPU利用実態の市場調査です。なお、**ハイパースケーラーの「AI向けGPUインスタンス稼働率」そのものは公開されていない**ため、需要逼迫・顧客数・容量増設・売上成長を代理指標として使います。Microsoftは2025年に明示的に**capacity constraints**を認め、AWS/Googleも大幅な容量増強を続けています。([microsoft.com](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q1))

## エグゼクティブサマリー

- **商用GPU利用の中心**は依然として **AWS/Azure/GCP と Big Techの自社クラスター**です。Synergyによると2025年Q4のクラウド基盤市場シェアは **AWS 28%、Azure 21%、Google Cloud 14%**、上位3社合計で**68%**でした。AWS Bedrockは**10万超の組織**、Azure AI Foundryは**8万社**、Googleは**8.5万超の企業がGeminiを利用**と公表しています。([srgresearch.com](https://www.srgresearch.com/articles/genai-helps-drive-quarterly-cloud-revenues-to-119-billion-as-growth-rate-jumped-yet-again-in-q4))
- **Neocloud（CoreWeave/Lambda/Runpod/Vast等）**はまだ上位3社より小さいものの、2025年は**フルイヤー売上$23B超見込み、前年比205%成長**と極めて高成長です。CoreWeaveは2025年売上**$5.13B**、Runpodは**50万人の開発者**、Vast.aiは**10万人超ユーザー / 1.4万人超の月次課金顧客**、Lambdaは**15万人超のCloud users**を公表しています。([srgresearch.com](https://www.srgresearch.com/articles/neoclouds-currently-growing-by-over-200-per-year-will-reach-180-billion-in-revenues-by-2030))
- **大学・公共研究側**では、UT Austinが**5,000超の先端NVIDIA GPU**、CMUが**296基のH100**、Stanfordは共有分だけで**少なくとも440基**、MITは2025年公開資料ベースで**少なくとも1,500基超**のキャンパス可視GPU資源があります。([news.utexas.edu](https://news.utexas.edu/2025/11/17/ut-eclipses-5000-gpus-to-increase-dominance-in-open-source-ai-strengthen-nations-computing-power/))
- **公共・国家研究インフラ**では、NAIRRは現在**600超の研究/教育プロジェクト、6,000人の学生**を全50州+DC+Puerto Ricoで支援。ACCESSは最新月次で**7,022 users / 3,260 projects**、Frontierを含むOLCFは**2,072 users / 639 projects**、ALCFは**2,013 users / 565 active projects**、NERSC Perlmutterは**7,168基のA100**を背景に**11,000超の科学者**を支えています。([nsf.gov](https://www.nsf.gov/focus-areas/ai/nairr))
- **資金面**では、学術・公的研究向けのAI compute支援は公開観測できる範囲でも**年率で数千万ドル規模**ですが、民間は別次元です。MicrosoftはFY2025に**約$80B**、Metaは2025年capex見通し**$66–72B**、Alphabetは2025年capexを**$85B**まで引き上げ、AWS/Amazonも2025年に**$100B超**の投資水準が見込まれていました。民間AI compute投資は、公開研究支援を**桁違いで上回る**状態です。([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/))

---

## 1. GPUをどのように利用しているか

### 1-1. 商用アクセス経路

| 経路 | 公開定量データ | 利用者規模/重要度 |
|---|---|---|
| **ハイパースケーラークラウド** | 2025年Q4クラウド基盤市場シェアは **AWS 28% / Azure 21% / Google 14%**、上位3社で**68%**。AWS Bedrockは**10万超組織**、Azure AI Foundryは**8万社**、Googleは**8.5万超企業がGeminiで構築**。Google I/O 2025では**700万人超の開発者がGeminiで開発**、**Vertex AI利用は40倍**と公表。([srgresearch.com](https://www.srgresearch.com/articles/genai-helps-drive-quarterly-cloud-revenues-to-119-billion-as-growth-rate-jumped-yet-again-in-q4)) | **重要度 5/5**。米国の商用AI GPU利用の主戦場。なお**GPU稼働率%は非公開**だが、Microsoftは2025年に**capacity constraints**を明示し、AWSは**過去1年で3.8GW**のDC容量を追加、MicrosoftはFY2026で**AI capacityを80%以上増強**予定。実務的には「高稼働・供給制約下」と見るのが妥当です。([microsoft.com](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q1)) |
| **Neocloud全体** | Synergyによるとneocloud売上は2025年Q2時点で**$5B超 / 前年比205%成長**、**2025年通年$23B超**見込み。GPUaaS/GenAI platform servicesは**約165%成長**。([srgresearch.com](https://www.srgresearch.com/articles/neoclouds-currently-growing-by-over-200-per-year-will-reach-180-billion-in-revenues-by-2030)) | **重要度 4/5**。市場シェアはまだ小さいが、GPU需要の逃げ場として戦略的重要度が急上昇。 |
| **CoreWeave** | 2025年売上**$5.131B**、売上バックログ**$66.8B**、**43 data centers / 850MW超 active power / 3.1GW contracted power**。SynergyはQ4 2025時点でCoreWeaveが**top 10 cloud provider入り**と報告。([investors.coreweave.com](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results)) | **重要度 4/5**。AI lab・大企業向けの本格トレーニング先。公開された総ユーザー数は未開示。 |
| **Lambda** | 2025年3月時点で**15万人超のCloud users**。ハードウェア/プライベートクラウド事業は**5,000超顧客**。2025年11月には**$1.5B超**調達、Microsoft向けに**tens of thousands of NVIDIA GPUs**のマルチイヤー契約、Kansas City拠点は**10,000超GPU**計画。([lambda.ai](https://lambda.ai/blog/lambdalabs.com-is-now-lambda.ai)) | **重要度 3.5/5**。研究者・スタートアップ・政府向けの「純AIクラウド」。 |
| **Runpod** | 2026年1月時点で**50万人超の開発者**、**$120M ARR**、売上**+90% YoY**、signup **+155% YoY**。最大**64 H100**のinstant cluster対応。([runpod.io](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr)) | **重要度 3/5**。個人〜中堅スタートアップのバースト用途で強い。 |
| **Vast.ai** | 2026年3月時点で**10万人超ユーザー**、**月次課金顧客1.4万人超**、GPU供給**約2万基**、signup **27倍**、売上**13倍**。([vast.ai](https://vast.ai/article/ramp-brex-fastest-growing-vendor)) | **重要度 2.5/5**。コスト感度の高い個人/小規模チームで非常に重要。 |

**解釈**：  
米国のAI GPU利用は、**「上位3社で大半の企業本番需要を吸収」＋「neocloudが供給制約のボトルネックを解消」**という二層構造です。特に2025年はGenAIがクラウド市場全体を押し上げ、Q4のクラウド基盤市場は**$419B**に達しました。([srgresearch.com](https://www.srgresearch.com/articles/genai-helps-drive-quarterly-cloud-revenues-to-119-billion-as-growth-rate-jumped-yet-again-in-q4))

### 1-2. 大学の共有GPUクラスター

| 大学 | 公開GPU数 | コメント |
|---|---:|---|
| **MIT** | 少なくとも**1,542基超**（ORCD一般利用**308基** + EngagingのPI所有共有**384基** + MIT SuperCloud **850基超Volta**）([orgchart.mit.edu](https://orgchart.mit.edu/letters/new-research-computing-services-available)) | さらにMassachusetts州AICRの**hundreds of NVIDIA B200/RTX**への共有アクセス予定あり。([orgchart.mit.edu](https://orgchart.mit.edu/letters/new-research-computing-services-available)) |
| **Stanford** | 少なくとも**440基**（Sherlock共有GPU partition **192基** + Marlowe **248 H100**）([sherlock.stanford.edu](https://www.sherlock.stanford.edu/docs/tech/)) | これに加え、Sherlock owners partition側のPI購入GPUが存在。([sherlock.stanford.edu](https://www.sherlock.stanford.edu/docs/tech/)) |
| **CMU** | **296 H100**（37ノード）([cmu.edu](https://www.cmu.edu/rcd/faq.html)) | **256 H100**がFLAME partition、**40 H100**がcommunity partition。([cmu.edu](https://www.cmu.edu/rcd/faq.html)) |
| **UT Austin** | **5,000超の先端NVIDIA GPU**、うち**1,000超**がCenter for Generative AI向け。([news.utexas.edu](https://news.utexas.edu/2025/11/17/ut-eclipses-5000-gpus-to-increase-dominance-in-open-source-ai-strengthen-nations-computing-power/)) | 2026稼働予定の**Horizon**でさらに拡張。Texas LegislatureはこのAI基盤の一部に**$20M**を拠出。([news.utexas.edu](https://news.utexas.edu/2025/11/17/ut-eclipses-5000-gpus-to-increase-dominance-in-open-source-ai-strengthen-nations-computing-power/)) |

**解釈**：  
大学共有クラスターは**ユーザー数は多いが、GPU絶対量では民間に大きく劣る**一方、**博士課程・教員の最初の本格GPUアクセス先**としては非常に重要です。UT Austinのような例外を除けば、大学共有資源は**数百GPU規模**が中心です。([news.utexas.edu](https://news.utexas.edu/2025/11/17/ut-eclipses-5000-gpus-to-increase-dominance-in-open-source-ai-strengthen-nations-computing-power/))

### 1-3. 国のスーパーコンピュータ / 研究用公共経路

| 経路 | GPU数 / 規模 | 利用者数 / 割当規模 |
|---|---|---|
| **NAIRR** | 単一クラスターではなく連邦+民間の**連合型資源**。2025年9月時点で **NSF 336 projects / 4.5M GPU-hours、DOE 8 / 2.3M GPU-hours、industry 226 / 7.4M GPU-hours**。([nsf-gov-resources.nsf.gov](https://nsf-gov-resources.nsf.gov/files/NAIRR-Sept-4th-webinar.pdf?VersionId=A8cZDQf8K53NHbJBvZjxw1X5qPfZHWFH)) | 現在は**600超の研究・教育プロジェクト、6,000人の学生**を全50州+DC+Puerto Ricoで支援。将来計画では、フルスケールNAIRRは**年1で48–60M quad-GPU node hours**、年2終盤で**140–180M hours**を視野。([nsf.gov](https://www.nsf.gov/focus-areas/ai/nairr)) |
| **ACCESS** | 20資源を束ねる配分制度。GPU専用のAnvil GPU, Delta GPU, Expanse GPU, Bridges-2 GPU等を含む。([access-ci.org](https://access-ci.org/wp-content/uploads/2025/07/ACCESS-Highlights_Book_PY3.pdf)) | 最新月次で**7,022 users / 3,260 projects / 2.49M jobs / 20 resources**。2024年秋のMaximize回では**90プロジェクトに4M超GPU-hours**を配分。多くの申請は**24–48時間**で承認。([allocations.access-ci.org](https://allocations.access-ci.org/)) |
| **DOE OLCF / Frontier** | **37,000超のAMD MI250X GPU**。([olcf.ornl.gov](https://www.olcf.ornl.gov/2025/12/11/frontier-supercomputer-ushers-in-new-era-of-nuclear-ai/)) | OLCF全体でCY2024に**2,072 users / 639 projects**。Frontierの2024 allocated program performanceは**68.95M allocation hours**。([olcf.ornl.gov](https://www.olcf.ornl.gov/wp-content/uploads/2024-OLCF-Operational-Assessment-Report.pdf)) |
| **DOE ALCF / Aurora** | **63,744 GPU**。([alcf.anl.gov](https://www.alcf.anl.gov/aurora)) | ALCF FY2024は**2,013 users / 565 active projects / 4.2M node-hours**。([ar24.alcf.anl.gov](https://ar24.alcf.anl.gov/year-in-review/about-alcf)) |
| **NERSC / Perlmutter** | GPUノード**1,792**（1,536+256）×4 A100 = **7,168 A100**。([docs.nersc.gov](https://docs.nersc.gov/systems/perlmutter/architecture/)) | DOE Office of Science mission向けに**11,000超の科学者 / 800超機関**。配分はERCAPで、AY2026は**2026-01-21〜2027-01-19**。([nersc.gov](https://www.nersc.gov/what-we-do/computing-for-science/perlmutter)) |

**解釈**：  
公共経路は**市場規模では小さい**ですが、**研究の民主化効果は極めて大きい**です。特にNAIRRとACCESSは、大学院生や小規模PIが「民間クラウドを現金で買えない」局面を埋める役割を担っています。([nsf.gov](https://www.nsf.gov/focus-areas/ai/nairr))

### 1-4. 企業のオンプレGPUクラスター

| 企業 | 公開できるGPU数 | 補足 |
|---|---|---|
| **Meta** | Mark Zuckerbergは2024年1月時点で、2024年末までに**350,000 H100**、他GPU込みで**約600,000 H100-equivalent**と表明。2025年Q2時点のcapex見通しは**$66–72B**。([facebook.com](https://www.facebook.com/zuck/posts/some-updates-on-our-ai-efforts-our-long-term-vision-is-to-build-general-intellig/10115439462041101/)) | 公開企業の中では**最も明示的なGPU台数開示**。 |
| **Microsoft** | **正確なGPU台数は未公表**。ただしFY2026 Q1で**AI capacityを80%以上増やす**計画、Azure AI Foundryは**8万顧客**、FY2025にはAIデータセンターへ**約$80B**投資見通し。([microsoft.com](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1)) | 公開値は台数ではなく**容量・顧客・投資額**中心。 |
| **Google** | **正確なNVIDIA GPU台数は未公表**。しかもGoogleはTPU依存が大きく、GPU数だけでは総アクセラレータ規模を捉えにくい。2025年Q2時点で**8.5万超企業がGeminiで構築**、2025 capexは**$85B**まで引き上げ。([blog.google](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2025/)) | Googleは**GPUよりTPU-heavy**と考えるべき。 |

**結論**：  
**企業オンプレの実GPU数はMeta以外ほぼ非公開**です。したがって市場実務では、**capex、GW、データセンター増設、AI顧客数**が実態把握の主指標になります。([microsoft.com](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1))

### 1-5. スタートアップ向けクラウドクレジット

| プログラム | 規模 |
|---|---|
| **AWS Activate** | **最大$100,000**。2013年以降の累計提供額は**$7B**。([aws.amazon.com](https://aws.amazon.com/startups/lp/aws-activate-credits)) |
| **Google for Startups Cloud Program** | 通常**最大$200,000**、AI-firstなら**最大$350,000**。Google Cloudは「**nearly all AI unicorns are Google Cloud customers**」とも表明。([startup.google.com](https://startup.google.com/cloud/)) |
| **NVIDIA Inception** | 無償。**22,000超のスタートアップ**を支援、米国内だけでも**10,000社**支援。([investor.nvidia.com](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-CEO-Jensen-Huang-and-Industry-Visionaries-to-Unveil-Whats-Next-in-AI-at-GTC-2025/default.aspx)) |

### 1-6. 個人利用（Colab, Kaggle, Vast.ai 等）

| サービス | ユーザー規模 |
|---|---|
| **Google Colab** | **1,000万超MAU**。学生を含む巨大な裾野。2025年には**高等教育向けに無料Colab Pro**提供も開始。([blog.google](https://blog.google/innovation-and-ai/products/democratizing-access-to-ai-enabled-coding-with-colab/)) |
| **Kaggle** | **2,500万登録ユーザー**、**150万 public notebooks**、**50万 datasets**。([kaggle.com](https://www.kaggle.com/static/slides/meetkaggle.pdf)) |
| **Vast.ai** | **10万人超ユーザー**、**1.4万人超の月次課金顧客**。([vast.ai](https://vast.ai/article/ramp-brex-fastest-growing-vendor)) |
| **Runpod** | **50万人超の開発者**。([runpod.io](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr)) |

---

## 2. 何のお金を使っているか

### 2-1. 資金源別の規模感

| 資金源 | 定量化できる最新値 | コメント |
|---|---|---|
| **NSF/NIH/DOE等の公的研究費** | **CloudBank 2.0: $20M grant / 5年 / 年500プロジェクト**。NCARは**855,000 GPU-hours/年**。NAIRRは2025年9月時点累計**14.2M GPU-hours**、ACCESSは一つのMaximize窓口で**4M超GPU-hours**。([nsf.gov](https://www.nsf.gov/news/nsf-expands-access-advanced-cloud-computing-scientific)) | **狭義の年額推定**：観測可能なAI向け公的/補助GPU時間をクラウド等価で置くと、**少なくとも年率$30M–$50M規模のフロア**はある、というのが私の見立てです（NAIRR年率換算+NCAR+CloudBank+ACCESS窓口ベース、DOE大型施設の機会費用は除外）。これは**保守的下限**です。([nsf.gov](https://www.nsf.gov/news/nsf-expands-access-advanced-cloud-computing-scientific)) |
| **大学予算（内部資金）** | StanfordはMarloweに**$30M**、MIT ORCDは2025年に**$6.5Mで276 GPU発注**し、年末までに**392新GPU**見込み。UTはAI基盤の一部に**Texas Legislature $20M**。([news.stanford.edu](https://news.stanford.edu/stories/2024/12/stanford-welcomes-first-gpu-based-supercomputer)) | 先端校では**単発で$6M–$30M級**の投資が確認できる。 |
| **企業R&D/compute投資** | Microsoft **$80B**、Meta **$66–72B**、Alphabet **$85B**、AWS/Amazonは2025年投資が**$100B超見込み**。4社合計のAI/クラウドcapexベンチマークは**$330B超**。([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/)) | 学術・公的研究支出を**圧倒**。 |
| **VC/スタートアップ資金** | OECDによると**2025年の世界AI VCは$258.7B**。PitchBookベースではH1 2025の米国VCドルの**64%**がAI、J.P. Morgan系ではQ1 2025の米国VCの**71%**がAI。([oecd.org](https://www.oecd.org/en/about/news/announcements/2026/02/ai-firms-capture-61-percent-of-global-venture-capital-in-2025.html)) | ユーザー指定の**compute比率40–60%**を当てると、AIスタートアップのcompute原資は**世界で約$103B–$155B**、米国がその大半という推定になります。これはかなり大きいですが、OpenAI/Anthropic/xAI/Scale級のメガラウンドを考えると整合的です。([oecd.org](https://www.oecd.org/en/about/news/announcements/2026/02/ai-firms-capture-61-percent-of-global-venture-capital-in-2025.html)) |
| **スタートアップクレジット** | AWS Activateは累計**$7B**。単純平均すると**年約$538M（世界）**。GoogleはAI startupに**最大$350k**、対象は「thousands of startups」。([aws.amazon.com](https://aws.amazon.com/startups/lp/aws-activate-credits)) | **米国向け年間発行総額推定**は、AWSが主要部分を占め、Googleを合わせると**数億ドル/年**が妥当レンジ。公開統計がないためこれは**推定**です。 |
| **自費（個人研究者/学生）** | Colabは**1,000万超MAU**だが、**有料契約者数は非公開**。([blog.google](https://blog.google/innovation-and-ai/products/democratizing-access-to-ai-enabled-coding-with-colab/)) | 私の推定では、有料転換率1–3%なら**10万–30万人規模の課金者**がいても不思議ではありませんが、これは**非公開情報に基づく推定**であり確証はありません。 |
| **共同研究費/受託研究費** | NCAR External Projectsには**45,000 GPU-hours/年**の基礎枠があり、外部賞獲得に応じて拡張されます。([ncar-hpc-docs.readthedocs.io](https://ncar-hpc-docs.readthedocs.io/en/latest/allocations/ncar-allocations/)) | このカテゴリは多くの大学で**スポンサー研究費に埋もれて集計不可**。ただし実務上は、ここから**$10k–$100k級のcompute line item**が出ることが多いです。 |

---

## 3. 政府の施策・独自の取り組み

### 3-1. NAIRR
- NAIRRは現在、**600超の研究/教育プロジェクト、6,000人の学生**を支援し、**13の他連邦機関**と**28の非政府パートナー**を束ねています。([nsf.gov](https://www.nsf.gov/focus-areas/ai/nairr))
- 2025年9月時点では、配分済み規模として**少なくとも14.2M GPU-hours**が確認できます。([nsf-gov-resources.nsf.gov](https://nsf-gov-resources.nsf.gov/files/NAIRR-Sept-4th-webinar.pdf?VersionId=A8cZDQf8K53NHbJBvZjxw1X5qPfZHWFH))
- 今後はNSFが**NAIRR Operations Center**を立ち上げ、パイロットから恒久的国家基盤へ移行する方針です。([nsf.gov](https://www.nsf.gov/funding/opportunities/nairr-oc-foundations-operating-national-artificial-intelligence/nsf25-546/solicitation))

### 3-2. ACCESS
- ACCESSは**無料**で、U.S.-basedの研究者・大学院生・教育者が利用できます。最新月次では**7,022 users / 3,260 projects / 20 resources**です。([allocations.access-ci.org](https://allocations.access-ci.org/))
- 申請は**Explore / Discover / Accelerate / Maximize**に分かれ、Maximizeは2026年から**年2回**のサイクルです。([allocations.access-ci.org](https://allocations.access-ci.org/prepare-requests))
- 研究室レベルでは、ACCESSは「大学クラスターで足りない分を無料で取る」経路として非常に重要です。([allocations.access-ci.org](https://allocations.access-ci.org/))

### 3-3. DOE Genesis Mission
- White Houseは**2025年11月24日**にGenesis Missionを開始し、DOEに**American Science and Security Platform**の構築を命じました。DOE超計算機・安全なクラウドAI環境・AI agent・foundation models・データ統合を含み、**270日以内**に初期運用能力を目指します。([whitehouse.gov](https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/))
- DOEは**2025年12月10日**、Genesis向けに**$320M超**を投じると発表し、内訳は**American Science Cloud、Transformational AI Models Consortium、14件のrobotics/automation、37件のfoundational AI awards**です。([energy.gov](https://www.energy.gov/articles/energy-department-advances-investments-ai-science))

### 3-4. CHIPS ActのAI computeへの影響
- CHIPS R&D Officeは**$11B**を管理し、AI/5G向けの次世代半導体R&Dを支えています。([nist.gov](https://www.nist.gov/chips/chips-rd-funding-opportunities))
- 具体案件として、**$825MのEUV Accelerator**、**$285MのSMART USA（digital twins）**、**SK hynixの$3.87B AI向け先端パッケージ工場**、Micronの**HBM packaging/R&Dを含む$200B投資**があります。([nist.gov](https://www.nist.gov/news-events/news/2024/10/biden-harris-administration-announces-ny-creates-albany-nanotech-complex))
- つまりCHIPSはGPUそのものではなく、**HBM・先端パッケージ・EUV・製造デジタルツイン**を通じて、AI compute供給制約の上流を改善する政策です。([nist.gov](https://www.nist.gov/news-events/news/2025/06/president-trump-secures-200b-investment-micron-technology-memory-chip))

### 3-5. CalCompute
- Californiaの**SB 53**は**2025年9月29日**に成立し、GovOps配下で**CalCompute**のフレームワークを作る**14 member consortium**を設置しました。**2027年1月1日まで**に設計報告を提出する計画です。([leginfo.legislature.ca.gov](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53))
- 2025年時点では**まだ公共GPUクラウドは稼働しておらず、設計段階**です。委員会分析では設計コストは**$2.5M–$7.5M**見積もりでした。([billtexts.s3.amazonaws.com](https://billtexts.s3.amazonaws.com/ca/ca-analysishttps-leginfo-legislature-ca-gov-faces-billAnalysisClient-xhtml-bill-id-202520260SB53-ca-analysis-384033.pdf))

### 3-6. 各大学への連邦政府GPU投資
- **NSF CloudBank 2.0** はUC San Diego / UC Berkeley / UWを中心に**$20M**、**年500プロジェクト**を支援。([nsf.gov](https://www.nsf.gov/news/nsf-expands-access-advanced-cloud-computing-scientific))
- **UT Austin Horizon** はNSF Leadership Class Computing Facilityで支えられる大型投資です。([news.utexas.edu](https://news.utexas.edu/2025/11/17/ut-eclipses-5000-gpus-to-increase-dominance-in-open-source-ai-strengthen-nations-computing-power/))
- **NSF AI Institutes** には2025年に**$100M**が投じられ、大学を核にAI研究能力を拡張しています。([nsf.gov](https://www.nsf.gov/news/nsf-announces-100-million-investment-national-artificial))

### 3-7. NVIDIA Inception等の民間プログラム
- NVIDIA Inceptionは**22,000超のスタートアップ**を支援し、無償の技術訓練、優遇価格、クラウドクレジット、VC接続を提供しています。米国内だけでも**10,000社**支援。([investor.nvidia.com](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-CEO-Jensen-Huang-and-Industry-Visionaries-to-Unveil-Whats-Next-in-AI-at-GTC-2025/default.aspx))

### 3-8. 輸出規制による国内GPU供給への影響
- BISは**2025年1月15日**にAI Diffusion Ruleを出しましたが、**2025年5月13日**に撤回し、同時に対中・迂回輸出防止のガイダンスを強化しました。([bis.doc.gov](https://www.bis.doc.gov/index.php/documents/federal-register-notices-1/3563-90-fr-4544-framework-for-artificial-intelligence-diffusion-ifr-0694-aj90-1-15-2025))
- 私の見立てでは、この変更は**「世界一律の強い管理」は後退したが、中国向け高性能AI chipの締め付けは維持・強化**という形です。その結果、**最先端GPU供給は引き続き米国内とtrusted marketsに厚く残りやすい**一方、正確に「米国に何台余るか」は公開されていません。これは**推論**です。([bis.gov](https://www.bis.gov/press-release/department-commerce-announces-recission-biden-era-artificial-intelligence-diffusion-rule-strengthens-chip))

---

## 4. 研究者の実際のGPU調達パターン

### 4-1. 典型的な大学院生の経路
実務上の典型パスは次です。

1. **大学共有クラスター**  
   まずMIT/Stanford/CMU/UTのような学内資源を使う。無料または内部配分だが、**待ち行列**がある。([orgchart.mit.edu](https://orgchart.mit.edu/letters/new-research-computing-services-available))

2. **Colab / Kaggle / 個人向けGPUクラウド**  
   試作・授業・小規模fine-tuningにはColab/Kaggleが圧倒的に便利。Colabは**1,000万超MAU**、Kaggleは**2,500万登録**です。([blog.google](https://blog.google/innovation-and-ai/products/democratizing-access-to-ai-enabled-coding-with-colab/))

3. **少額クラウド予算（研究室カード / CloudBank / neocloud）**  
   実際の公開例では、UIUCのNAIRR/CloudBank申請で**4xA10を1日8時間×6か月**使う予算が**$8,281.14**、API込み総額**$9,931.14**でした。([cloudbank.org](https://www.cloudbank.org/example-nairr-pilot-project-request))

4. **ACCESS / NAIRR に移行**  
   本格実験・再現実験・大型評価はここ。ACCESSは最新月次で**7,022 users**、多くの申請を**24–48時間**で処理。NAIRRは**600超プロジェクト**を支援中です。([allocations.access-ci.org](https://allocations.access-ci.org/))

### 4-2. 研究グループのGPU予算の典型規模
- **小規模AI研究室**: 年**$10k–$30k**のクラウド/creditsでも十分ありうる。上のCloudBank例を年率化すると約**$20k**です。([cloudbank.org](https://www.cloudbank.org/example-nairr-pilot-project-request))
- **中規模ML研究室**: 年**$30k–$150k**程度のGPU支出は自然。  
- **大規模/基盤モデル寄り研究室**: 単月で**$100k超**が飛ぶため、通常のPI grantだけでは厳しい。  

その理由は単純で、Lambdaの2026年4月時点の価格では**H100 SXMが$3.99/GPU-hour**です。すると  
- **8x H100を30日**で約**$22,982**、  
- **64x H100を30日**で約**$183,859**  
になります。([lambda.ai](https://lambda.ai/service/gpu-cloud/reserved-cloud-pricing))

### 4-3. 研究費の中でGPU計算に充てられる割合
NSFのFY2025の**competitive awardsの平均 annual award sizeは $260,362**です。([nsf-gov-resources.nsf.gov](https://nsf-gov-resources.nsf.gov/files/FY-2025-Agency-Financial-Report_0.pdf?VersionId=AvgXAo9hdNqJluUSH9lg4ZGlZcVG25g8))

これに対して、
- 上の**年$20k**級クラウド利用は、平均NSF年額の**約7.7%**、  
- **8x H100を1か月**回すだけで**約8.8%**、  
- **64x H100を1か月**だと**約70.6%**  
に相当します。

したがって、私の実務的な見立ては次です。

- **通常のAI論文研究**: grantの**5–10%**がcomputeでも十分重い  
- **モデル開発寄り**: **10–25%**  
- **frontier training寄り**: **25%超**、普通のNSF grant単体では持ちにくい  

このため、米国の研究者は実際には  
**「大学クラスター → Colab/小額クラウド → ACCESS/NAIRR」**  
という多段調達でcomputeを賄っています。([cloudbank.org](https://www.cloudbank.org/example-nairr-pilot-project-request))

---

## 最終結論

**米国のAI GPU利用実態**を一言で言うと、

1. **ドル規模では Big Tech自社保有 + 上位3クラウドが支配**  
2. **アクセス性では neocloud が最重要の逃げ道**  
3. **研究民主化では ACCESS/NAIRR/大学クラスター/Colab が不可欠**  
4. **通常の学術grantでは frontier-class computeは買い切れない**  

です。公開データベースと企業開示を突き合わせると、**民間のAI compute投資は年$300B超級**に達しつつある一方、学術・公的側の可視化できるAI compute支援は**年率数千万ドル級**が下限です。したがって、**米国のAI研究者の現実的なGPU調達は「公的無料枠を最大活用し、足りない分をneocloud/クレジットで埋める」構造**になっています。([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/))

必要なら次に、
- **この調査をExcel風の比較表**に整形する  
- **「研究者タイプ別（学部生/PhD/PI/スタートアップ）」のGPU調達フローチャート**を作る  
- **各経路のコスト比較（A100/H100/B200、オンデマンド/予約、大学/NAIRR/ACCESS）**を作る  
こともできます。

---

## 2. EU・UKのGPU利用実態

以下は**2026年3月28日時点の公開情報**だけで組んだ調査です。まず前提として、EuroHPCの最新公表は**「19 AI Factories」＋「13 AI Factory Antennas」**で、ユーザーの「19+13拠点」という表現はこの2層を合わせたものです。なお、**第3波の新設AI Factoryの多くは2026〜2027年稼働予定で、GPU台数が未公表**です。以下では、**公開済み定量値**と**未公表**を分けて書きます。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories_en))

## エグゼクティブサマリー

- **商用GPU需要の主経路は依然として米系ハイパースケーラー**です。欧州クラウド市場は**2024年 €61bn**、**2025年上期 €36bn**まで拡大し、**AWS/Azure/GCPの3社で欧州市場の70%**、欧州事業者全体は**15%**です。英国の公的調査でも、**2024年のUKクラウド支出は£10.5bn**、**AWSとMicrosoftが各30–40%**で、Googleはかなり小さいとされました。 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15))
- ただし**主権・規制対応の需要**は急増しています。Microsoftは**2025年2月にEU Data Boundaryを完成**、AWSは**2026年1月にEU内独立運用のEuropean Sovereign Cloudを一般提供**、Google Cloudも**T‑Systems/S3NS等のパートナー主権制御**を独・仏・蘭などで提供しています。 ([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/02/26/microsoft-completes-landmark-eu-data-boundary-offering-enhanced-data-residency-and-transparency/))
- **公的・研究用GPU利用はすでにかなりAI寄り**です。LUMIでは**利用資源の過半がAI関連**、**約7,000ユーザー**が**1.4億GPU時間**を使っています。CINECAでは**AI/MLがアクティブユーザーの15%**、**配分資源の14.2%**。フランスGENCIでも**2025年の通常配分案件の40%**、**ダイナミック配分案件の75%**がAI手法を使っています。 ([lumi-supercomputer.eu](https://www.lumi-supercomputer.eu/top500_june_2025/))
- **欧州の“主権側”のGPU供給は急速に増えているが、まだ個社ごとの差が大きい**です。Nscaleは**2027年までに欧州へ10万超GPU**を掲げ、Nebiusは**2025年3月末時点で全世界3万GPU**、OVHcloudは**50万台超サーバー・46 DC・160万顧客**の基盤を持ちます。一方、Nebiusの**EU限定ユーザー数**などは未公表です。 ([nscale.com](https://www.nscale.com/press-releases/nscale-nvidia-vera-rubin))
- **EUの資金面は厚くなっている**ものの、**VCのスケールギャップは依然大きい**です。Horizon Europeは**2021–2022年にAI R&Dへ€2.6bn**、2025年のAI関連テーマは**約€1.6bn**、2026–2027年は**€2.023bn**が見込まれています。GenAI4EUは**約€700m**、InvestAIは**€200bn動員目標**で、そのうち**€20bnがAI gigafactories向け facility**です。他方で、**2025年の世界AI VC投資額に占めるEU27のシェアは6%**、**米国は75%**でした。ユーザーが挙げた「6% vs 61%」は**旧い比較軸**で、最新OECDデータでは**61%は“AIが世界VC全体に占める比率”**です。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/european-ai-research))

---

## 1. GPUの利用経路

### 1-1. ハイパースケーラー（AWS/GCP/Azure）のEU・UK利用

| 項目 | 定量データ | 出典 |
|---|---:|---|
| 欧州クラウド市場規模 | **€61bn（2024年）**、**€36bn（2025年上期）** | 公式/公表値 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15)) |
| 欧州でのAWS/Azure/GCP合算シェア | **70%** | 公式/公表値 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15)) |
| 欧州事業者の合算シェア | **15%** | 公式/公表値 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15)) |
| 欧州事業者上位 | **SAP 2%**, **Deutsche Telekom 2%** | 公式/公表値 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15)) |
| AI系クラウドの成長 | GenAI専用GPUaaS/GenAI PaaSは**140–160%成長** | 公式/公表値 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15)) |
| UK市場集中度 | **2024年 UK cloud spend £10.5bn**、AWS/Microsoftが**各30–40%** | 公式/公表値 ([assets.publishing.service.gov.uk](https://assets.publishing.service.gov.uk/media/688b8891fdde2b8f73469544/final_decision_report_.pdf)) |

**解釈**：欧州のAI用GPU需要は、商用ワークロードでは今もBig 3中心です。ただし、**規制産業・公共部門・越境個人データを含む案件**ほど、次の「主権ラッパー」を被せた利用が増えています。これは後述のGDPR/AI Act/主権クラウド政策と整合的です。 ([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/02/26/microsoft-completes-landmark-eu-data-boundary-offering-enhanced-data-residency-and-transparency/))

### 1-2. データ主権対応の状況

| 事業者 | 主権対応の公開定量/マイルストーン | 出典 |
|---|---|---|
| Microsoft | **2025年2月**にEU Data Boundary完了。EU/EFTA内で顧客データ・擬似匿名個人データ・サポートデータを処理/保存可能に | 公式/公表値 ([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/02/26/microsoft-completes-landmark-eu-data-boundary-offering-enhanced-data-residency-and-transparency/)) |
| AWS | **2026年1月14日**、AWS European Sovereign Cloudを一般提供。最初のリージョンは**ドイツ・ブランデンブルク** | 公式/公表値 ([aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2026/03/network-firewall-european-sovereign-cloud-region/)) |
| Google Cloud | Sovereign Controls by Partnersは**Frankfurt, Paris, Eemshaven(蘭), Belgium, Italy, Spain**などで提供 | 公式/公表値 ([cloud.google.com](https://cloud.google.com/sovereign-controls-by-partners/docs/locations)) |

---

### 1-3. EU発のGPUクラウド / sovereign cloud

| 事業者 | 規模 | ユーザー/顧客 | コメント |
|---|---|---|---|
| **Nscale** | **2027年までに欧州へ10万超GPU**、UKのLoughton AI campusは**23,040 GB300 GPU**（Q1 2027）、Norwayは**2026年末までに10万GPU**目標 | 推論ではなく公開値として**5,000超ユーザー**（inference service） | 欧州主権AIインフラ色が強い。UK/Norway中心に大規模拡張中。 ([nscale.com](https://www.nscale.com/press-releases/nscale-nvidia-vera-rubin)) |
| **Nebius** | **2025年3月末で約30,000 GPU**、主にH200。DCは**フィンランド・フランス・アイスランド**。**2025年6月に欧州初のGB200一般提供** | 顧客数は**未公表** | 研究・企業・開発者向け。EU内処理を前面に出す。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1513845/000155837025005991/nbis-20241231x20f.htm)) |
| **OVHcloud** | **500,000超サーバー**, **46 data centers**, **140+か国**, **FY2025 Public Cloud売上 €219.3m** | **1.6m customers** | 欧州最大級の既存顧客基盤。H100は**$2.99/h**から、**$200無料クレジット**あり | 公式/公表値 ([corporate.ovhcloud.com](https://corporate.ovhcloud.com/asia/newsroom/news/summit-2025/)) |
| **Scaleway** | カスタムAIクラスタは**最大1,016 H100**、KyutaiのMoshiも**1,016 H100**クラスタで運用 | 顧客数は未公表 | フランス発の主権クラウド。大規模H100クラスタを公開 | 公式/公表値 ([scaleway.com](https://www.scaleway.com/en/docs/gpu/reference-content/choosing-gpu-instance-type)) |
| **Fluidstack**（UK発、欧州展開） | **100,000超GPU under management**。Mistral向けフランス拠点は**18,000 GPU超**まで拡張設計 | 顧客数未公表 | UK拠点企業だが、欧州主権クラスタ供給の実勢では重要 | 公式/公表値 ([businesswire.com](https://www.businesswire.com/news/home/20250303970989/en/Fluidstack-Delivering-Europes-Largest-AI-Supercomputer-to-Mistral-AI-in-2025)) |

**実態**としては、**“大規模・グローバルでハイパースケーラー”**と、**“規制/主権要件で欧州系neocloud”**の二層化が進んでいます。とくにNebius/Nscale/Scaleway/OVHcloudは、**EU内処理・主権・GPU特化**で差別化しています。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1513845/000155837025005991/nbis-20241231x20f.htm))

---

### 1-4. EuroHPC（汎欧州スパコン基盤）の主要GPU資源

| システム | GPU数（公開値） | AI利用の公開値 | 補足 |
|---|---:|---:|---|
| **LUMI**（FI） | **2,978 GPU nodes × 4 MI250X = 11,912 MI250X modules**（ソフトウェア上は8 GPU/node扱い） | **利用資源の過半がAI関連**、**約7,000 users**、**1.4億GPU時間**、**3,000超プロジェクト** | 欧州で最もAI利用実績が見える公的GPU基盤のひとつ。 ([docs.lumi-supercomputer.eu](https://docs.lumi-supercomputer.eu/hardware/lumig/)) |
| **Leonardo Booster**（IT） | **3,456 nodes × 4 A100 = 13,824 GPUs** | CINECA全体で**6,925 active users**、**AI/ML 15% of users**、**AI/ML 14.2% of allocated resources** | AI比率はCINECA全体指標で、Leonardo単体の比率ではない点に注意。 ([leonardo-supercomputer.cineca.eu](https://leonardo-supercomputer.cineca.eu/hpc-system/)) |
| **MareNostrum 5 ACC**（ES） | **1,120 nodes × 4 H100 = 4,480 GPUs** | **全体AI利用率は未公表** | ただしスペインAI戦略では**MareNostrum 5容量の20%を産業向け**に充て、システムは**450+ PF**へほぼ**+50%**拡張予定。 ([bsc.es](https://www.bsc.es/marenostrum/marenostrum-5)) |
| **JUPITER Booster**（DE） | **約24,000 GH200**（技術文書ベースでは**5,884 nodes × 4 = 23,536**） | AI学習向け**40+ exaFLOPS (8-bit)**見込み | GermanyのJAIFの中核。 ([fz-juelich.de](https://www.fz-juelich.de/en/ias/jsc/news/news-items/news-flashes/2025/record-breaking-computing-power-jupiter-ranks-fourth-in-the-global-top500-list)) |

**AI利用の“実需”を見ると**、LUMIはすでに**AIが過半**、Leonardo/CINECAでも**AIが最大ドメイン**、MareNostrum 5でも**LLM・医療・気候・産業AI用途**が政策上の主戦場です。つまり、EuroHPCは「HPCにAIが乗った」段階ではなく、**AIが公的GPU時間の主要消費者**になりつつあります。 ([lumi-supercomputer.eu](https://www.lumi-supercomputer.eu/top500_june_2025/))

---

### 1-5. EuroHPC AI Factories（19拠点）の公開定量データ

#### まず共通ルール
- **AI Factoriesは19拠点、別に13 Antennas**。スタートアップ/SME向けに**free, customised support**を提供。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories_en))
- **Industry Innovation track**は、**Playground**（2営業日）、**Fast Lane**（4営業日、**最大50,000 GPUh**）、**Large Scale**（10営業日、**50,000 GPUh超**）で、**AI SMEs/startupsは無料**。他の産業用途はpay-per-useの商用アクセスも可。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en))
- **AI for Science**は**6か月配分**、**2か月ごとのcut-off**、**審査最大1か月**、**推論は配分の10%以下**。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/document/download/9acb9942-5c34-40d1-9f7f-9e01087cae83_en?filename=AI+for+Science+Access+-+Terms+of+Reference.pdf))
- **AI Factory利用は、利用者の居住国がそのAI Factory/antenna参加国である必要はない**。対象国の適格組織なら申請可能です。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/document/download/c7279c41-4510-45de-9122-3b52f3524e7c_en?filename=AIFA_Application+peculiarities_presented_completed.pdf))

#### 既存/公開値のある拠点
| 拠点 | 公開されている定量値 | コメント |
|---|---|---|
| **Finland / LUMI AIF** | 既存LUMIを使用。**11,912 MI250X**。LUMI AIFは**2027年のLUMI‑AIまで既存LUMIで運用** | 料金は**startups/SMEs/academic researchers無料**。小規模パッケージありだがGPUhの固定値は未公表。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/finland_en)) |
| **Germany / JAIF** | **JUPITER 約24,000 GH200** | Jülichベース。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/germany_en)) |
| **Germany / HammerHAI** | **€55m予算**、**15+ exaFLOPS AI inference**、**2026年下期稼働見込み** | GPU台数そのものは未公表。GB200 NVL4ベース。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en)) |
| **Italy / IT4LIA** | **Leonardo 13,824 A100**、LISAは**166基の8-way GPU server**。CINECA年報では**IT4LIA予算 €430m** | AI最適化新システム自体のGPU台数は未公表。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-systems_en)) |
| **Spain / BSC AI Factory** | **MareNostrum 5 ACC 4,480 H100** | AI upgradeの詳細GPU数は未公表。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-systems_en)) |
| **Spain / 1HealthAI (Galicia/CESGA)** | **総投資 €82m**、うちスペイン政府**€24m**、専用AI supercomputerを取得 | GPU台数は未公表。 ([commission.europa.eu](https://commission.europa.eu/projects/healthai-artificial-intelligence-factory-cesga-galicia_en)) |
| **France / AI2F** | **予算 €30.7m / 3年 / 20 partners**。当面は**Jean Zay, Adastra, Joliot‑Curie**、その後**Alice Recoque** | Alice Recoqueの総投資は**€554m**、GPU型番は**AMD MI430X**だが台数未公表。 ([genci.fr](https://www.genci.fr/actualites/le-projet-ai-factory-france-voit-le-jour-afin-de-developper-lusage-de-lintelligence)) |
| **Greece / Pharos** | **プロジェクト €30m / 36 months**、DAEDALUSは**89 PF sustained / 115 PF peak**、初期仕様では**4 accelerators per node**要求 | 実装後の総GPU数は未公表。 ([grnet.gr](https://grnet.gr/en/2025/04/17/pr-mindigitalgr-pharos-aifactoryeu-kickoff-15april2025/)) |
| **Luxembourg / Luxembourg AI Factory** | MeluXinaは**200 GPU nodes × 4 A100 = 800 A100**。加えてクラウドGPUとして**16 H200 NVL**を文書化 | Lux AI Factory自体の“新規追加分”は未公表。 ([docs.lxp.lu](https://docs.lxp.lu/system/overview/)) |
| **Sweden / Mimer** | Arrheniusは**382 GPU nodes × 4 GH200 = 1,528 GH200** | Mimer本体の新AI専用機の台数は未公表。 ([naiss.se](https://www.naiss.se/resource/arrhenius/)) |
| **Netherlands / NLAIF** | **EuroHPC award €70m**、**総投資 €200m**、**フル稼働は2027見込み** | AI supercomputerのGPU台数は未公表。 ([surf.nl](https://www.surf.nl/en/news/netherlands-gets-ai-factory-european-funding-awarded)) |
| **Bulgaria / BRAIN++** | Discoverer+は**32 H200 GPU accelerators** | Discoverer++側の拡張総量は未公表。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en)) |

#### 選定済みだが、GPU台数が未公表の拠点
**Austria (AI:AT), Slovenia (SLAIF), Poland (PIAST), Poland (Gaia AI Factory), Czechia (CZAI), Lithuania (LitAI), Romania (RO AI Factory)** などは、**2026年3月時点で新AI最適化システムのGPU数が公開されていません**。ただし、AI:ATは「state-of-the-art AI‑optimised supercomputer」、SLAIFは「new EuroHPC AI‑optimized supercomputer」、PIASTは既存施設のGPU拡張、CZAI/NLAIF/LitAI/RO AI Factory/Gaiaは新AI最適化システムの取得が公式に示されています。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/austria_en))

#### 既存システムで今すぐ使える“公開枠”
EuroHPCの既存AI/Data-Intensive accessでは、**1 cut-offあたり合計約1,065,918 node-hours**が公開され、固定枠は**LUMI-G 35,000**, **Leonardo Booster 50,000**, **MareNostrum 5 ACC 32,000**, **MeluXina GPU 25,000**, **Karolina GPU 7,500**, **Vega GPU 7,100**です。これはAI Factories本格稼働前の“現行の即時利用可能枠”として重要です。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/document/download/dc58b298-05f7-497c-aba4-918632177545_en?filename=02.+Vangelis+Floros+-+EuroHPC+and+AI+Access.pdf))

---

### 1-6. 各国の大学・国立クラスタ

| 拠点 | 定量データ | 実際の利用/配分制度 |
|---|---|---|
| **Germany / JUWELS** | Boosterは**936 nodes × 4 A100 = 3,744 GPUs**、Cluster側に**56 nodes × 4 V100 = 224 GPUs**、合計**3,968 GPUs** | GCS経由で無料の配分制度。大規模案件は**年2回**。JUWELS/GCS large-scaleはFLOP基準。 ([apps.fz-juelich.de](https://apps.fz-juelich.de/jsc/hps/juwels/booster-overview.html)) |
| **UK / Isambard‑AI** | **5,448 GH200** | AIRRの中核。UK公表ではIsambard/Dawnに**£300m**、2030までにAIRR関連**£350m超**、かつ**20倍拡張**方針。 ([dera.ioe.ac.uk](https://dera.ioe.ac.uk/id/eprint/41375/1/AIRR%20advanced%20supercomputers%20for%20the%20UK%20-%20GOV.UK.pdf)) |
| **UK / Dawn** | **1,024 Intel Data Center GPU Max 1550** | AIRRのもう1本柱。 ([hpc.cam.ac.uk](https://www.hpc.cam.ac.uk/access-dawn)) |
| **UK / AIRR無償枠** | Rapid: **20,000 GPUh/3か月**、Gateway: **10,000 GPUh/3か月**、Innovator: **50,000–150,000 GPUh/6か月** | Rapidのtime-to-accessは**最大2か月**。 ([gov.uk](https://www.gov.uk/government/publications/ai-research-resource/airr-rapid-access-route-ukri-guidance)) |
| **France / Jean Zay** | **1,456 H100**, **416 A100**, **1,832 V100**、合計**3,700+ NVIDIA GPUs**。**125.9 PF** | 2025年配分実績: 通常配分**514件**, うちAI手法**202件(40%)**; ダイナミック配分**1,725件**, うちAI手法**1,302件(75%)**; 通常GPU時間**65,653,320**、動的GPU時間**50,437,261**（V100換算） | 公式/公表値 ([cnrs.fr](https://www.cnrs.fr/en/press/genci-and-cnrs-choose-eviden-make-jean-zay-supercomputer-one-most-powerful-france)) |
| **Netherlands / Snellius** | **2024年に352 H100（88 nodes）追加**、理論性能**15→38 PF**近くへ増強 | NWO/SURFのSmall Computeでは**Spider/Dataprocessingに最大10,000 GPUh**、Snellius/Cloud/LUMI等の総容量も公開 | 公式/公表値 ([surf.nl](https://www.surf.nl/en/news/gpu-expansion-of-supercomputer-snellius-enables-even-faster-data-processing-for-dutch)) |
| **Sweden / Alvis** | **884 GPUs**（160 T4 + 44 V100 + 4 A100 + 340 A40 + 336 A100） | AI/ML専用 national resource。今後Arrheniusへ移行。 ([naiss.se](https://www.naiss.se/resource/alvis/)) |

---

### 1-7. 企業のオンプレ / 専用計算投資（公開値ベース）

**ここは“真の社内オンプレ”より、実際には“専用ホスト型・主権型・プライベートスタック型”の公開が多い**です。EU大企業は、自前GPU台数をIRで細かく開示しないことが多く、以下は**公開定量値がある代表例**です。 ([telekom.com](https://www.telekom.com/en/media/media-information/archive/ai-sovereignty-for-germany-and-europe-1098708))

| 企業・案件 | 定量データ | 位置づけ |
|---|---|---|
| **Deutsche Telekom + NVIDIA** | **10,000 Blackwell GPUs**, **0.5 ExaFLOPS**, **20 PB storage**, **€1bn超パートナーシップ** | ドイツ製造業向け主権AIファクトリー。企業の専用AI計算投資として最も具体的。 ([telekom.com](https://www.telekom.com/en/media/media-information/archive/ai-sovereignty-for-germany-and-europe-1098708)) |
| **Mistral AI + Fluidstack + Eclairion (France)** | Essonneの専用クラスタは**18,000 GPUs超**へ拡張設計、サイトは**40MW**から**100MW+**へ拡張計画 | 欧州最大級の企業専用AIクラスタ。Mistral Computeは**private / bare metal / managed PaaS / on-premises**を掲げる。 ([businesswire.com](https://www.businesswire.com/news/home/20250303970989/en/Fluidstack-Delivering-Europes-Largest-AI-Supercomputer-to-Mistral-AI-in-2025)) |
| **Nscale UK campus** | **23,040 GB300 GPUs**（Q1 2027予定）、**50MW**から**90MW**へ拡張可能 | UK主権AI計算の大型案件。 ([nscale.com](https://www.nscale.com/press-releases/nscale-uk-ai-infrastructure-announcement)) |
| **Stargate Norway (Nscale/Aker/OpenAI)** | **100,000 NVIDIA GPUs by end-2026**, **230MW**、初期フェーズに**約$1bn**コミット | 欧州域内の主権AI向け巨大計算設備。 ([nscale.com](https://www.nscale.com/press-releases/stargate-norway-nscale-aker-openai)) |

---

## 2. 資金源

### 2-1. EUレベル

| 項目 | 金額 | コメント |
|---|---:|---|
| **Horizon Europe総額** | **€93.5bn (2021–2027 indicative)** | AI専用ではなく総額。 ([research-and-innovation.ec.europa.eu](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_et)) |
| **Horizon EuropeのAI R&D** | **€2.6bn (2021–2022)** | 既公表の累計。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/european-ai-research)) |
| **Horizon Europe 2025のAI関連投資** | **約€1.6bn** | 2025 work programmeベース。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/eu-invests-eu73-billion-horizon-europe-enhance-its-competitiveness-and-talent-growth)) |
| **Horizon Europe 2026–2027のAI関連投資** | **€2.023bn** | “topics that encourage the development of AI”。 ([ec.europa.eu](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-1-general-introduction_horizon-2026-2027_en.pdf)) |
| **Horizon Europe + Digital Europe** | **AIに年€1bn超** | Commission公表。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/european-ai-research)) |
| **Digital EuropeのAI投資** | **2021–2024で€1bn超** | 配備・採用側。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/european-ai-research)) |
| **AI Innovation Package** | **2027年までに公私あわせて約€4bn** | 生成AI・AI Factories等を後押し。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/factpages/ai-innovation-package)) |
| **GenAI4EU** | **約€700m** | Horizon Europe, DEP, EICを跨ぐ。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/genai4eu)) |
| **InvestAI** | **€200bn動員目標**、うち**€20bn**がgigafactories向け facility | 公式Q&AではEIB Groupと組成するfacilityが明示。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/eu-launches-investai-initiative-mobilise-eu200-billion-investment-artificial-intelligence)) |
| **EuroHPC全体（AI Factories込み）** | **2021–2027で€10bn** | 超計算基盤+AI Factories投資。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/ai-factories)) |

### 2-2. ERC / 研究助成機関

| 機関 | GPU調達に関係する公開ルール |
|---|---|
| **ERC** | Starting Grantは**€1.5m/5年**＋**追加€1m**（移転時は**€2m**）まで。追加分は**major equipment**や**access to large facilities**に充当可。グラントは**eligible direct costs 100% + indirect 25%**。 ([erc.europa.eu](https://erc.europa.eu/funding/starting-grants)) |
| **DFG** | 研究助成に付随する**機器購入**が可能。**€50k以上**をmajor instrumentationと定義。大学向けMajor Research Instrumentation Programmeでは**投資額の50%**をDFGが負担し、対象機器の下限は**€100k（応用大）/ €200k（その他大学）**。さらに、**内部コア施設の利用料**もproject-specific costとして請求でき、**€10k超**なら見積書が必要。 ([dfg.de](https://www.dfg.de/en/research-funding/funding-opportunities/programmes/infrastructure/scientific-instrumentation/funding-opportunities/equipment-dfg-programmes)) |
| **ANR** | 2025年7月3日承認の新ルール。**eligible costs**に研究機器・装置・サービス費が含まれる。FAQでは**service costsカテゴリ上限50%**、また**hébergeur part 13.5%**が公表。GPUクラウド外注を“service cost”で計上する場合の上限制約として効く可能性がある。 ([anr.fr](https://anr.fr/fr/rf/)) |
| **UKRI** | 原則**80% FEC**。**£25k超のequipment**、**national/international facilities**、**specialist computer costs**が対象。基本PC等は対象外。 ([ukri.org](https://www.ukri.org/apply-for-funding/develop-your-application/what-costs-are-eligible-for-ukri-funding/)) |

### 2-3. VCと民間資本

- **最新OECD（2025年）**では、世界のAI VC投資のうち**EU27は6%（$15.8bn）**、**米国は75%（$194bn）**でした。同時に、**AIそのものが世界VC全体の61%**を占めています。つまり、ユーザーが書いた「6% vs 61%」は**現在では比較対象がズレている**ので、最新値で見るなら**EU27 6% vs US 75%**です。 ([oecd.org](https://www.oecd.org/en/about/news/announcements/2026/02/ai-firms-capture-61-percent-of-global-venture-capital-in-2025.html))
- Commissionの投資能力分析では、**2020–2025に米国はVCの34%をAIへ、欧州は18%をAIへ**振り向け、さらに**€25m超の大型AIラウンドではEU投資家比率が26%まで低下**しています。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/library/funding-ai-economy-strengthening-europes-investment-capacity))
- EIBの2025/26投資報告では、**過去10年のEU AI企業へのVCの42%が米国由来、33%がEU由来、14%がUK/CH/NO由来**でした。つまり、**EU域内のAI計算需要そのものより、“成長資金の出し手”が欧州外寄り**というのが構造問題です。 ([eib.org](https://www.eib.org/files/publications/20250379-030326-investment-report-2025-chapter5-en.pdf))

---

## 3. 政府施策・独自取り組み

### 3-1. EuroHPC AI Factories / 13 Antennas
- 2025年10月時点で**19 AI Factories + 13 Antennas**。Antennaには**Belgium, Cyprus, Hungary, Ireland, Latvia, Malta, Slovakia**に加え、**Iceland, Moldova, North Macedonia, Serbia, Switzerland, United Kingdom**が入っています。EUはAntennasに**約€55m**を拠出。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en))
- AI Factoriesは**スタートアップ/SMEに無料・カスタム支援**を提供し、Antennaはその裾野を広げる制度です。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories_en))

### 3-2. GenAI4EU
- GenAI4EUは当初の**€500m**想定を超え、**約€700m**へ拡大。例として、**生物医学マルチモーダルGenAI callは€15–17m**級で、過去のAI Boostでは**4社に€1m + 8m GPUh**が配られました。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/genai4eu))

### 3-3. EU AI Actのcompute要件
- **GPAI obligationsは2025年8月2日適用開始**、AI Act全体は**2026年8月2日全面適用**。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))
- **10^25 FLOP**超で学習したGPAIモデルは、原則として**systemic risk**と推定され、**通知・評価・リスク低減・重大インシデント報告・サイバーセキュリティ確保**が必要です。通知は**遅滞なく、遅くとも2週間以内**。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers))
- 一方で、**市場投入前の研究・試験・開発**にはAI Actの明確な**研究 exemption**があります。したがって、**一般的な学術GPU利用への直接影響は限定的**で、効くのは主に**フロンティア級モデル提供者**です。 ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/european-ai-research))

### 3-4. GAIA-X / 主権クラウド
- **GAIA‑Xはクラウド事業者そのものではなく、federated system / rules / verification framework**です。目的は、**secure, transparent, sovereign control over data**。 ([gaia-x.eu](https://gaia-x.eu/about/))
- 欧州委員会は**2025年10月に€180m tender**を出し、**Cloud Sovereignty Framework**で6年間の主権クラウド調達を進めています。 ([commission.europa.eu](https://commission.europa.eu/news-and-media/news/commission-moves-forward-cloud-sovereignty-eur-180-million-tender-2025-10-10_en))

### 3-5. GDPR / データ越境
- EDPBは、**第三国当局への個人データ提供もGDPR上のtransfer**であり、**Chapter V**と**適切な法的根拠**が必要だと明言しています。また、第三国移転では**essentially equivalent level of protection**が必要です。 ([edpb.europa.eu](https://www.edpb.europa.eu/news/news/2024/edpb-clarifies-rules-data-sharing-third-country-authorities-and-approves-eu-data_en))
- そのため、**医療・公共・防衛・金融**では、GPU調達先の選択が**価格/性能だけでなく、データ所在地・支配権・サポート要員の居場所**まで含めた調達条件になります。これはMicrosoft/AWS/Googleが欧州向け主権オプションを強化している理由でもあります。 ([blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2025/02/26/microsoft-completes-landmark-eu-data-boundary-offering-enhanced-data-residency-and-transparency/))

### 3-6. UK独自
- **AIRR**は現在**Isambard‑AI + Dawn**の2本柱で、政府は**2030年までに20倍**へ拡張する方針。AIRRクラスタへの投資は**£350m超 by 2030**、AI for Science StrategyではAIRR拡張に**£1bn**。 ([dera.ioe.ac.uk](https://dera.ioe.ac.uk/id/eprint/41375/1/AIRR%20advanced%20supercomputers%20for%20the%20UK%20-%20GOV.UK.pdf))
- **Sovereign AI Unit**は**up to £500m**でBritish Business Bankと連携し、Compute Roadmapでは**専用compute tracks**も与えられます。既に**OpenBind £8m**、Anthropic/Cohere連携、Encode Fellowship等が例示されています。 ([assets.publishing.service.gov.uk](https://assets.publishing.service.gov.uk/media/6878b5dda52cca025ef5bd87/uk_compute_roadmap_web_accessible.pdf))
- **Spending Review 2025**ではAI Opportunities Action Plan実装に**£2bn超**、この中に**20倍AIRR**、**Sovereign AI Unit £500m**, **AISI £240m**が入っています。 ([assets.publishing.service.gov.uk](https://assets.publishing.service.gov.uk/media/6849171796e63bce58e4e705/E03349913_HMT_Spending_Review_June_2025_Elay.pdf))

---

## 4. 研究者のGPU調達パターン

### 4-1. 典型パターン（制度を総合した実務フロー）
これは**公開制度から見える典型経路の合成**ですが、かなり現実に近いです。 ([gauss-centre.eu](https://www.gauss-centre.eu/for-users/hpc-access/allocation-pgms))

1. **小規模PoC / first experiments**  
   - 学内GPU、国内small compute、AIRR Gateway/Rapid、AI Factory Playground。  
   - 典型量は**10,000〜20,000 GPUh級**。英国ではGateway **10k**, Rapid **20k**、SURF small computeでは**10k GPUh**。 ([gov.uk](https://www.gov.uk/government/publications/ai-research-resource/airr-rapid-access-route-ukri-guidance))

2. **中規模学習 / HPC-ready**  
   - AI Factory Fast Lane（**最大50k GPUh**）、AIRR Innovator（**50k–150k GPUh**）、GCS regular/large-scale、GENCI regular。 ([eurohpc-ju.europa.eu](https://eurohpc-ju.europa.eu/fast-lane-access-ai-factories_en))

3. **大規模学習 / foundation model級**  
   - EuroHPC AI for Science、EuroHPC Regular/Extreme、国のGrand Challenge。  
   - 例：EuroHPC Large AI Grand Challengeは**8m GPUh**、Leonardoでは**2m GPUhずつ**のSME案件があった。 ([eurohpc-ju.europa.eu](https://eurohpc-ju.europa.eu/winners-announced-large-ai-grand-challenge-2024-06-26_en))

4. **商用展開 / 規制データ**  
   - Mistral Computeのような**private/on-prem stack**、Deutsche Telekom industrial AI cloud、OVHcloud/Nebius/Nscale等の**sovereign / EU-resident**構成へ移行。 ([mistral.ai](https://mistral.ai/news/mistral-compute))

### 4-2. EuroHPC割当の実際（申請→利用）
| 経路 | 公表リードタイム |
|---|---|
| **AI Factory Playground** | **2 working days**、FIFO、1–3か月配分 | 公式/公表値 ([eurohpc-ju.europa.eu](https://eurohpc-ju.europa.eu/playground-access-ai-factories_en)) |
| **AI Factory Fast Lane** | **4 working days**、最大50,000 GPUh、1–3か月 | 公式/公表値 ([eurohpc-ju.europa.eu](https://eurohpc-ju.europa.eu/fast-lane-access-ai-factories_en)) |
| **AI Factory Large Scale** | **cut-off後10 working days**、50,000 GPUh超、3/6/12か月 | 公式/公表値 ([eurohpc-ju.europa.eu](https://eurohpc-ju.europa.eu/large-scale-access-ai-factories_en)) |
| **AI for Science** | **審査最大1か月**、6か月配分、2か月ごとcut-off | 公式/公表値 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/document/download/9acb9942-5c34-40d1-9f7f-9e01087cae83_en?filename=AI+for+Science+Access+-+Terms+of+Reference.pdf)) |
| **Regular Access** | **cut-off後最大4か月**で利用開始 | 公式/公表値 ([eurohpc-ju.europa.eu](https://eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-regular-access-mode_en)) |
| **UK AIRR Rapid** | **submission後最大2か月** | 公式/公表値 ([gov.uk](https://www.gov.uk/government/publications/ai-research-resource/airr-rapid-access-route-ukri-guidance)) |

### 4-3. 審査基準・制約
- EuroHPC AI for Scienceでは、**小型HPCで代替できない理由**、**コードの適合性**、**大規模CPU/GPU時間の必要性**、**GANTT chart**まで要求されます。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/document/download/9acb9942-5c34-40d1-9f7f-9e01087cae83_en?filename=AI+for+Science+Access+-+Terms+of+Reference.pdf))
- 産業向けAI Factoriesは**AI SMEs/startupsは無料**ですが、**民生目的のみ**、**AI Act準拠**が条件です。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en))
- **利用者の国籍/居住地ではなく、所属組織の適格性**が重要で、AI Factory参加国かどうかは必須条件ではありません。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/document/download/c7279c41-4510-45de-9122-3b52f3524e7c_en?filename=AIFA_Application+peculiarities_presented_completed.pdf))

### 4-4. データ主権要件がGPU選択に与える制約
- **個人データ**や**第三国アクセス懸念**があると、GDPR Chapter Vのtransfer論点が発生するため、研究者は**EU内データレジデンシー**や**EU-based support**のある基盤を選ぶ傾向が強くなります。 ([edpb.europa.eu](https://www.edpb.europa.eu/news/news/2024/edpb-clarifies-rules-data-sharing-third-country-authorities-and-approves-eu-data_en))
- 実務上は、**非機微データはBig 3、機微/公共/国策案件はEuroHPC・国内HPC・欧州主権クラウド**という住み分けが最も自然です。これは制度設計と公開製品群からの**妥当な推論**です。 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15))

---

## 総括

**実態**として、EU/UKのAI用GPU利用は次のように整理できます。  
1. **商用の主流**はまだAWS/Azure/GCP。  
2. **研究・主権用途**ではEuroHPC/国立HPCが急速に存在感を高めている。  
3. **欧州系GPUクラウド**は、規制適合・EU内処理・専用スタックで伸びているが、公開データを見る限り**規模はまだまちまち**。  
4. **資金面**は公的にはかなり厚くなったが、**大型VC・スケール資本では依然米国優位**。 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15))

## なお、公開情報として不足している点
- **19 AI FactoriesすべてのGPU台数**は、2026年3月時点でまだ出揃っていません。特に**第3波（Czechia, Lithuania, Netherlands, Romania, Spain 1HealthAI, Poland Gaia）**は、予算や稼働時期は出ていても、**GPU台数未公表**が多いです。 ([eurohpc-ju.europa.eu](https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en))
- **欧州全体のAWS/Azure/GCP個社別シェア**は、最新公開の欧州プレスリリースでは**合算70%**までしか出ていません。UKだけはCMAが**AWS/Microsoft各30–40%**と出しています。 ([srgresearch.com](https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15))
- **EU大企業の“純粋な社内オンプレGPU台数”**は開示が非常に少なく、公開値の大半は**専用ホスト型・主権クラウド型・共同投資型**です。 ([telekom.com](https://www.telekom.com/en/media/media-information/archive/ai-sovereignty-for-germany-and-europe-1098708))

必要なら次に、  
**(A) 国別（ドイツ/フランス/オランダ/UK）に4ページ程度の比較表へ再整理**、または  
**(B) 19 AI Factories全拠点を1行ずつ並べた完全一覧CSV風フォーマット**  
で出します。

---

