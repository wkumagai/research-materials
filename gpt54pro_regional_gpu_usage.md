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

