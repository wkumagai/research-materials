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

## 3. 中国のGPU利用実態

以下、**2026年3月28日時点**の公開情報ベースで、中国におけるAI用途GPU/AIアクセラレータ利用実態を、**米国輸出規制の影響**に焦点を当てて整理します。結論だけ先に言うと、**中国のAI計算需要そのものは強い**一方、利用先は「少数の大手クラウド/大手企業」に集中し、地方主導の新設センターには**20～30%稼働**の低利用案件も目立ちます。輸出規制は中国のAI開発を止めたというより、**NVIDIA最先端品への依存を崩し、国産チップ・異種混成クラスタ・GPU時貸し・海外リース・ソフト最適化**へと利用経路を変えました。中国の智能算力規模は2024年に**725.3 EFLOPS**、2025年予測で**1037.3 EFLOPS**まで拡大見通しです。 ([scjgj.beijing.gov.cn](https://scjgj.beijing.gov.cn/zwxx/mtjj/202502/t20250217_4013210.html))

## 1. GPUの利用経路

### 1-1. 中国国内クラウドのAI GPU市場シェア
ここは**定義で順位が変わる**のが重要です。  
- **IDCの2024年「AI public cloud services」**では、**Baidu AI Cloud と Alibaba Cloud が各約25%**で首位、続いてTencentとHuaweiでした。 ([scmp.com](https://www.scmp.com/tech/article/3322250/alibaba-baidu-lead-chinas-ai-cloud-boom-market-surges-55-us27-billion))  
- **Omdiaの1H25「China AI Cloud Market」**（IaaS+PaaS+MaaS）では、**Alibaba 35.8%**、Volcano Engine 14.8%、**Huawei 13.1%**、**Tencent 7.0%**、**Baidu 6.1%**です。つまり「大模型クラウド全体」ではAlibaba優位です。 ([asiatechwire.com](https://www.asiatechwire.com/International-authoritative-report-Alibaba-Cloud-ranks-first-in-Chinas-AI-cloud-market-with-a-358-share.html))  
- 一方、**Frost & Sullivanの1H25「国産GPUクラウド」**では、**Baidu 40.4%**、**Huawei 30.1%**で、両社合計が**70%超**でした。ここでは**自研チップからクラウドまでの垂直統合**が評価軸になっています。 ([datacenterdynamics.com](https://www.datacenterdynamics.com/en/news/baidu-and-huawei-account-for-70-of-chinas-gpu-cloud-market/))

**要するに**、  
- **輸入NVIDIA中心のAIクラウド全体**ではAlibabaが強い。  
- **国産アクセラレータ前提のGPUクラウド**ではBaidu/Huaweiが強い。  
という二重構造です。 ([asiatechwire.com](https://www.asiatechwire.com/International-authoritative-report-Alibaba-Cloud-ranks-first-in-Chinas-AI-cloud-market-with-a-358-share.html))

### 1-2. 国産GPU/アクセラレータの性能比較（H100比）と導入実績
まず注意点として、**H100比は単純比較が危険**です。NVIDIA公式のH100 BF16/FP16 1,979 TFLOPSには**sparsity込み**の値が含まれます。したがって、以下は**理論値ベースの概算**、または**公開された実運用情報**として読むのが安全です。 ([nvidia.com](https://www.nvidia.com/en-us/data-center/h100/))

- **Huawei Ascend 910C**  
  Huaweiは2025年3月公開の**Atlas 900超节点**について、**384カードで最大300 PFLOPS**、しかも**累計300セット超を20超の顧客に配備**と公表しています。これを単純に1カード当たりへ割り戻すと、H100のdense相当と比べて**ざっくり7～8割級**の理論水準になります。Huawei自身も、2025年4月末までに**Ascend 910B/910Cの推理能力が顧客の基本要求に到達した**と説明しています。中国国内で**唯一、大規模商用配備が明確に見える国産AIアクセラレータ**です。 ([huawei.com](https://www.huawei.com/cn/news/2025/9/hc-xu-keynote-speech))

- **Biren BR100**  
  BirenのHot Chips資料では、**BF16 1,024 TFLOPS**が示されており、理論値だけなら**H100 dense相当級**です。ただし、実運用の成否はCUDA互換、分散学習、供給制約に大きく左右され、**Huaweiほど大規模な商用導入台数は公開されていません**。IPO関連報道では、**千卡級集群案件**や通信・データセンター顧客との案件は示されるものの、公開ソースで検証できる配備量はまだ限定的です。 ([hc34.hotchips.org](https://www.hc34.hotchips.org/assets/program/conference/day1/GPU%20HPC/HC2022.BirenTech.MikeHong.LingjieXu.v01.pdf))

- **Moore Threads MTT S4000**  
  Moore Threads公式仕様は**48GB GDDR6、768GB/s、FP16/BF16 100 TFLOPS**で、H100 dense比では**約1割**の理論水準です。他方で同社は、**千卡級のKUAEクラスタ**を早くから商用訴求しており、2025年には**万卡級智算集群**対応を前面に出しています。つまり単カード性能より、**国産クラスタ運用基盤**としての位置付けが強いです。 ([docs.mthreads.com](https://docs.mthreads.com/s4000/s4000-doc-online/product_specifications/))

- **Cambricon MLU370-X8**  
  Cambricon公式仕様は**48GB LPDDR5、614.4GB/s、FP16/BF16 96 TFLOPS**で、H100 dense比では**約1割**です。公式には「**4つの一般的AIモデルで主流350W RTX GPU相当**」と説明しており、前線の大規模学習よりは、**推論や特定業務向け**の色が濃いです。大規模配備台数は公開情報がかなり薄いです。 ([cambricon.com](https://cambricon.com/index.php?a=lists&c=index&catid=406&m=content))

- **補足: Baidu Kunlun**  
  ユーザー指定外ですが、中国の現場実装では重要です。Baiduは2025年に**3万～3.2万卡規模の昆仑芯P800集群**を点灯・実運用したと自社イベントで説明しており、IDCベースでは**Kunlunxinの2024年出荷が約7万枚**と報じられています。中国の国産AIチップで、**Huaweiに次ぐ“数量が見える”実装**です。 ([cloud.baidu.com](https://cloud.baidu.com/news/news_f7c48617-386d-4e57-a88f-e7e16c5b7693))

### 1-3. 地方政府の計算プラットフォーム
主要都市では、政府や国資が**公共算力平台**を整備し、大学・研究機関・中小企業に貸し出す形が定着しています。 ([kw.beijing.gov.cn](https://kw.beijing.gov.cn/xwdt/kcyx/xwdtshgg/202401/t20240110_3817157.html))

- **北京**  
  2024年1月の**北京人工智能公共算力平台（上庄）**は**一期500P**で、大学・科研院所・中小企業向け普惠サービスとして開始しました。2024年3月には**亦庄AI公共算力平台**が**3000P**で点灯し、北京市は2025年Q2に**2つの万卡智算集群**建設を進めると公表しています。 ([kw.beijing.gov.cn](https://kw.beijing.gov.cn/xwdt/kcyx/xwdtshgg/202401/t20240110_3817157.html))

- **上海**  
  上海は2025年7月の市政策で**6億元の算力券**を出しつつ、**上海市智能算力公共服务平台**を整備しています。上海超级计算中心が運営する公共平台は**100 PFLOPS（FP16）**の国産算力を掲げ、別の市公式記事では、上海儀電系の公共平台群が**“複数の万卡集群”**を建成済みと紹介されています。市としては2025年までに**100 EFLOPS**を目標にしています。 ([sheitc.sh.gov.cn](https://sheitc.sh.gov.cn/cmsres/3e/3ea46b718d084ec080672b09428642a1/8cea381294498b9a97300a9428f88e9f.pdf))

- **深圳**  
  深圳の2025–2026行動計画は、2026年までに**实时可用智能算力 80 EFLOPS超**を目標にし、**1ms都市算网・3ms韶关算网・10ms贵安算网**を掲げています。2025年3月には**深智城3000 PFLOPS智算中心**が稼働し、同月に**深圳（東部）人工智能产业公共服务平台**の**一期千卡集群**も点灯しました。 ([sz.gov.cn](https://www.sz.gov.cn/szzt2010/zdlyzl/jjshzc/content/post_12052815.html))

### 1-4. 大学・研究機関の計算資源
大学では、**自前HPC**と**GPUカード時サービス調達**の併用が進んでいます。 ([hpcc.cs.tsinghua.edu.cn](https://hpcc.cs.tsinghua.edu.cn/jszy/yjzy.htm))

- **清華大学**  
  清華大学高性能計算センターの**開拓1000**は、**91 GPUノード・728 GPUカード**で、内訳は**87ノード×8 A800 + 4ノード×8 H800**です。旧システムにも**10ノード×8 V100**があります。 ([hpcc.cs.tsinghua.edu.cn](https://hpcc.cs.tsinghua.edu.cn/jszy/yjzy.htm))

- **北京大学**  
  北京大学高性能計算平台の共有系だけでも、**GPUカード40枚**（P100/V100混在）が公開されています。別系統では、北京大学医学系・AI4Drug系で**8×A800**やA100系の個別クラスタも見えます。 ([hpc.pku.edu.cn](https://hpc.pku.edu.cn/resource.html))

- **中科院系**  
  中科院全体の統一集計は見つけにくいですが、研究所単位では比較的大きいGPU保有が確認できます。たとえば**中科院上海免疫与感染研究所**の高性能計算機集群は**3090/A40/A100系GPUノード28台**、**中科院生物物理所**の生物成像中心は**8×A100 40GB**構成を公開しています。さらに**中科院計算机网络信息中心**は2025年に**中国科技云GPU服务器6套**を追加調達しました。 ([siii.cas.cn](https://siii.cas.cn/kyzc/yqss/djpt/202403/t20240308_7021178.html))

### 1-5. 国のスパコン（天河、曙光等）
この領域は**公開度が低い**です。現時点で確実に言えるのは、**国家超算天津中心（天河）**は「天河一号」「天河新一代」を保有し、**超算・智算・大规模数据管理の三位一体**で、**双百亿亿級能力**から**三百亿亿級能力**へ拡張中だということです。また、天河系の**多模态千亿参数模型公共服务平台**は**E級の混合精度算力**を提供するとされています。公式サイトには**GPU集群**と**人工智能环境**の専用ページもありますが、**現在のAI向けGPUカード枚数までは開示していません**。 ([teda.gov.cn](https://www.teda.gov.cn/contents/14/25755.html))

補助情報として、中国国家网格の公開メタデータでは、**天津のGPUサブシステムが約3.7 PF GPU**、**深圳国家超算中心が約1.3 PF GPU**と整理されていますが、これはフルシステムではなく共有GPU資源側の数字とみるのが妥当です。 ([cngrid.org](https://www.cngrid.org/hjjs/wjccxx/))

**曙光（Sugon）**については、古典的な国家超算というより、2025年に**96アクセラレータ/ラック**・**百万卡拡張対応**の**AI超集群**を前面に出しており、中国のAI用途では「超算」より**AIスーパー・クラスタ**の文脈で見るほうが実態に合います。 ([semi.org.cn](https://www.semi.org.cn/site/semi/article/f888da1fd41e4916bc157281ceac7d23.html))

### 1-6. 企業オンプレの推定GPU保有台数
ここは**公開下限**と**強い推定**を分けるべきです。中国企業は正確なカード枚数を開示しないことが多いです。 ([arxiv.org](https://arxiv.org/abs/2509.16293))

- **ByteDance**  
  arXiv上のByteDance論文の要約では、本番GPUプラットフォームが**20万GPU超**と示されています。加えてSCMP報道では、ByteDanceは**約1000億元相当のチップを備蓄**し、そのうち**1割未満**をVolcano Engine経由で外販しているとされます。中国で最も大きいAI GPU保有者の一つとみてよいです。 ([arxiv.org](https://arxiv.org/abs/2509.16293))

- **Baidu**  
  Baiduは自社イベントで**3万～3.2万卡の昆仑芯クラスタ**を点灯・実用化したと説明しています。これは**公開確認できる中国企業オンプレの大規模国産クラスタ**の代表例です。 ([cloud.baidu.com](https://cloud.baidu.com/news/news_f7c48617-386d-4e57-a88f-e7e16c5b7693))

- **Alibaba**  
  AlibabaはHPCA 2026の業界発表で、**5年間安定運用されている1万GPU超クラスタ**を前提にしたeGPUフレームワークを公表しています。総保有枚数は未公開ですが、**“1万GPU超の本番クラスタ”が存在**するのは確定です。さらにAlibabaは**今後3年で3800億元**をAI・クラウド基盤に投じると発表しており、保有量はなお増える方向です。 ([2026.hpca-conf.org](https://2026.hpca-conf.org/details/hpca-2026-industry-track/3/eGPU-Production-Scale-Elastic-Sharing-over-10-000-GPUs))

- **Tencent**  
  Tencentは正確なカード枚数を開示していません。ただし、公式資料では**AI cloud revenueがFY24に約2倍**、**Q4 2024からGPU調達を加速**と述べ、同時に**星脉ネットワーク2.0が10万卡級に対応**する設計であることが広く報じられています。他方、2025年Q3には**GPU調達制約でcapexが130億元へ低下**したとも説明しており、**大規模インフラは用意しているが、チップ供給制約を受けた**という見方が妥当です。 ([static.www.tencent.com](https://static.www.tencent.com/uploads/2025/03/19/f55938d61be94cf9700a971a4db08809.pdf))

---

## 2. 資金源

### 2-1. 算力券（compute vouchers）
中国のAI算力支援で最も実務上効いているのは、中央研究費よりむしろ**地方の算力券/训力券**です。2024年時点で公式整理でも**10余城市**が確認され、2025年には制度がさらに広がっています。浙江省の2025年通知では、**国家人工智能券（算力券）が超長期特別国債資金を使う試点政策**だと明示されています。 ([xxzx.fj.gov.cn](https://xxzx.fj.gov.cn/jjxx/xxhdt/202404/t20240424_6438610.htm))

**公的文書で詳細を確認できた代表例**は次の通りです。  
- **上海**: 2025年7月の市措置で**算力券6億元**、**模型券3億元**、**語料券1億元**。算力券は**市級で家賃補助最大30%**、市区協同で**最長1年・最大100%**まで上積み可。 ([sheitc.sh.gov.cn](https://sheitc.sh.gov.cn/cmsres/3e/3ea46b718d084ec080672b09428642a1/8cea381294498b9a97300a9428f88e9f.pdf))  
- **深圳**: **毎年最大5億元の“训力券”**、**最大1億元の模型券**、**最大5000万元の語料券**。大模型訓練向けは**契約額の50%まで、最大1000万元**、初創企業は**60%**まで。2025年3月の初回配布は**約2億元**で約40社が受領。さらに深圳市は**2025年に市区合計45億元の政策資金**を用意すると公表。 ([sz.gov.cn](https://www.sz.gov.cn/zfgb/zcjd/content/post_11932960.html))  
- **北京経開区（亦庄）**: **毎年1億元の算力券**、通常**30%**、国産算力なら**40%**まで、**年上限2000万元**。モデル券も別途**1億元/年**。 ([beijing.gov.cn](https://www.beijing.gov.cn/zhengce/zhengcefagui/202406/t20240613_3711893.html))  
- **寧波**: 2025実施細則で、四半期ごとの該当費用に対し**50%を算力券で発行**。 ([qf.ningbo.gov.cn](https://qf.ningbo.gov.cn/qfpt/fwbk/sjfw/rmzx/art/2025/art_86c0b9ae347245b3920c8d56f3052c9c.html))  
- **重慶**: 2025年の算力券は**実際の算力サービス金額の20%**補助。 ([cq.gov.cn](https://www.cq.gov.cn/ywdt/jrcq/202508/t20250831_14950848.html))  
- **無錫**: **毎年5000万元**の算力券予算。 ([wuxi.gov.cn](https://www.wuxi.gov.cn/doc/2024/02/29/4186695.shtml))  
- **呼和浩特**: **毎年5000万元**の算力券。 ([nea.gov.cn](https://www.nea.gov.cn/20250718/410e42d872e4417687cb5b0ab357d088/c.html))  
- **余杭区**: **毎年最高5000万元の算力券**、同額の模型券もあり。 ([yuhang.gov.cn](https://www.yuhang.gov.cn/art/2025/2/21/art_1532133_59131954.html))  
- **武漢**: 中小企業向け**千万元級算力券**、垂直モデルには**年最大1000万元補助**。 ([wuhan.gov.cn](https://www.wuhan.gov.cn/zwgk/xxgk/zcjd/mtzj/202502/t20250219_2535934.shtml))  
- **珠海**: **総額最大5億元の算力券**を計画し、备案済み生成AI企業では**60%支援**まで引上げ。 ([gdstc.gd.gov.cn](https://gdstc.gd.gov.cn/kjzx_n/gdkj_n/content/post_4684544.html))

### 2-2. NSFC・MOST
- **NSFC**  
  国家自然科学基金委の2025年度予算では、**自然科学基金項目予算が394.58億元**で、前年比**+8.65%**です。AI専用ではありませんが、大学・研究所のGPU購入/クラウド利用の原資としては重要です。 ([nsfc.gov.cn](https://www.nsfc.gov.cn/Portals/0/fj/fj20250326_01.pdf))  
- **MOST（科技部）**  
  科技部の2025年度一般公共予算支出は**118.48億元**。うち**基礎研究**が**37.76億元**で、前年比**+80%**でした。これもAI専用ではありませんが、AI for Science・計算資源整備に波及します。 ([most.gov.cn](https://www.most.gov.cn/xxgk/xinxifenlei/fdzdgknr/bmyjs/202503/P020250326559263483414.pdf))

### 2-3. 地方政府AI予算・基金
- **上海**は、公式報道で**225億元の人工智能母基金**、**600億元の国家AI大基金**、**100億元のAI生態基金**を紹介しており、**ほぼ1000億元級**の資本支援基盤を形成しています。加えて2026年2月時点で、算力券・語料券・模型券の年間配布は**10億元超**と説明しています。 ([shanghai.gov.cn](https://www.shanghai.gov.cn/nw4411/20250407/3cd35fd60b4c47c7982e79d09a83c110.html))  
- **深圳**は2025年に**45億元の政策資金**を用意し、同時に**百億基金投資生態**の構築も打ち出しています。 ([m.cyol.com](https://m.cyol.com/gb/articles/2025-02/23/content_nypYR0Fey9.html))  
- **北京経開区**は算力券・模型券で**各1億元/年**を出し、さらにAI算力中心単体プロジェクトとして**127億元投資・2000P**規模案件も推進しています。 ([beijing.gov.cn](https://www.beijing.gov.cn/zhengce/zhengcefagui/202406/t20240613_3711893.html))

### 2-4. 企業R&D/AI投資
- **Alibaba**は2025年2月、**今後3年で3800億元**をクラウド・AIハード基盤に投じると発表しました。これは同社の過去10年のクラウド/AI投資総額を上回る水準です。 ([english.news.cn](https://english.news.cn/20250224/e289b92275a64a22a9f9ceba843687d9/c.html))  
- **Tencent**は2025年Q1のcapexが**275億元**、Q2が**191億元**。2024年通期資料では、**AI cloud revenueが前年比約2倍**、Q4 2024から**GPU購入を積み増した**と説明しています。 ([static.www.tencent.com](https://static.www.tencent.com/uploads/2025/05/16/2af4e73edd208df236dadd8b9df89fc4.pdf))  
- **ByteDance**はReutersベースで、2025年capexが**1500億元超**、その多くがAI向けと報じられています。 ([investing.com](https://www.investing.com/news/stock-market-news/exclusivebytedance-plans-20-billion-capex-in-2025-mostly-on-ai-sources-say-3826261))

### 2-5. VC/スタートアップ資金
OECDの2026年政策ブリーフでは、**2025年に中国のAI企業が受けたVC投資額は139億ドル（世界の約5%）**、一方で**中国投資家による対AI投資の“発信”側は172億ドル（世界の約8%）**でした。AI VCの世界シェアでは米国に大きく劣るものの、中国はなお**世界第3～4位級のAI資本市場**です。 ([oecd.org](https://www.oecd.org/en/publications/venture-capital-investments-in-artificial-intelligence-through-2025_a13752f5-en/full-report.html))

---

## 3. 政府施策・独自の取り組み

### 3-1. 東数西算（East Data West Computing）
「東数西算」は2022年に始まり、現在は**8つの国家枢纽节点**と**10の国家データセンター集群**を核に進んでいます。2025年9月時点で、公式報道は**社会投資1兆元超**、**14省をカバー**としています。2023年末の実施意見では、2025年末までに**全国一体化算力网**の基本形を作る目標が示され、2025年5月の**算力互联互通行动计划**では、2026年までの標準整備、2028年までの全国公共算力標準接続が掲げられました。 ([gov.cn](https://www.gov.cn/zhengce/zhengceku/202401/content_6924596.htm))

2025年6月末時点では、中国の**在用算力中心標準ラック数は1085万架**、**智能算力は788 EFLOPS**、平均**PUEは1.42**まで低下しています。つまり、量だけでなく**電力効率・広域接続・標準化**へ政策軸が移っています。 ([caheb.gov.cn](https://www.caheb.gov.cn/system/2025/08/25/030355687.shtml))

### 3-2. 国産GPU推進政策
最も明確な公的義務付けは、**上海の智算基盤行動方案**です。ここでは**2025年までに新建智算中心の国産算力チップ比率を50%以上**、国産ストレージも50%以上にすると明記しています。北京経開区も、算力券で**国産算力は40%補助**、非国産は30%補助と差を付けています。つまり「国産化」は、**補助条件と公共施設の調達条件**を通じて進められています。 ([tjdsj.tjcac.gov.cn](https://tjdsj.tjcac.gov.cn/tjsg/202404/t20240408_6593787.html))

### 3-3. 米国輸出規制の影響
米BISの2022/2023年規制で、A100/H100に加えA800/H800なども対象化されました。さらにNVIDIAのSEC開示によれば、**2025年4月9日にはH20も中国向け輸出にライセンスが必要**になりました。ところがNVIDIAは**2025年7月14日にH20販売再開へ向けた申請と、ライセンス付与の保証を受けた**と公表しています。つまり、中国企業から見ると、問題は単に「禁止」ではなく、**ルールが非常に不安定**なことです。 ([bis.doc.gov](https://www.bis.doc.gov/index.php/policy-guidance/advanced-computing-and-semiconductor-manufacturing-items-controls-to-prc))

### 3-4. H100/A100入手難後の代替戦略
中国側の対応はだいたい5つです。  
1. **規制準拠品の前倒し確保**: H20の大量発注・在庫化。  
2. **企業間の二次市場化**: 2025年にはTencentとAlibabaが**ByteDance備蓄GPUを買った**と報じられました。 ([scmp.com](https://www.scmp.com/tech/big-tech/article/3308254/tencent-alibaba-buy-nvidia-gpus-bytedance-stockpile-report-says))  
3. **国産チップへの垂直統合**: Baidu/Kunlun、Huawei/Ascend、Baidu/Huaweiの国産GPUクラウド支配が象徴的です。 ([datacenterdynamics.com](https://www.datacenterdynamics.com/en/news/baidu-and-huawei-account-for-70-of-chinas-gpu-cloud-market/))  
4. **海外データセンター経由のリース**: SemiAnalysisは、中国プレイヤーが**非規制国での計算リース**を使っていると指摘しています。 ([semianalysis.com](https://semianalysis.com/2025/09/08/huawei-ascend-production-ramp/))  
5. **ソフト/アルゴリズム最適化**: AlibabaはAegaeonで**GPU消費82%削減**、Tencentは**同じチップでより多くの推論を載せるソフト改善**を明言しています。 ([alibabacloud.com](https://www.alibabacloud.com/blog/602623))

### 3-5. GPU稼働率30%問題
中国では、地方主導でAIデータセンター建設が先行した結果、**新設センターの一部は20～30%稼働**に留まり、MIT Technology ReviewやReuters系報道でも**新規容量のかなりの部分が遊休化**したと整理されています。背景は、  
- 東部需要に対して西部立地が多く**遅延面で不利**、  
- 多くのセンターが**推論需要より訓練需要を過大評価**、  
- ラック電力密度が低く、最先端学習に必要な**40kW超級要件を満たせない**案件がある、  
- 異種混成ハードのため**使い勝手が悪い**、  
という構造です。 ([tomshardware.com](https://www.tomshardware.com/desktops/servers/china-is-developing-nation-spanning-network-to-sell-surplus-data-center-compute-power-latency-disparate-hardware-are-key-hurdles))

### 3-6. GPU価格70%下落の背景
中国の算力レンタル市場では、Sinaが引用した市場レポートで、**H100のGPU時間単価が2023年初の約8ドルから2025年半ばには約2.4ドルへ下がり、70%超下落**したとされます。A800/H800/H20系も下落傾向です。背景は、  
- 地方主導の**供給先行**、  
- DeepSeek型の**低計算コスト学習**で“必要GPU時間”の見積もりが下方修正、  
- 需要が「基盤モデル訓練」から「推論」へ移り、旧式訓練リグの価格決定力が低下、  
- クラウド/プーリング/スケジューリングで**実効利用率が上がった**、  
ことです。 ([finance.sina.cn](https://finance.sina.cn/2025-06-20/detail-infatrka6078972.d.html))

---

## 4. 研究者のGPU調達パターン

### 4-1. 中国の研究者はどうGPUを使うか
研究者の利用パターンは、今や**「GPUを買う」より「GPU時間を確保する」**に寄っています。具体的には、  
- **校内HPC**を使う（清華728枚、北大40枚公開分など）、  
- **大学名義でGPUカード時を外部調達**する、  
- **公共算力平台**を使う、  
- **算力券/训力券でクラウド費用を落とす**、  
- 企業と共同で**異種混成クラスタ**へ載せる、  
の5ルートです。 ([hpcc.cs.tsinghua.edu.cn](https://hpcc.cs.tsinghua.edu.cn/jszy/yjzy.htm))

### 4-2. 算力券の実際の利用体験
北京の官方記事では、大模型企業CEOが**以前は“あちこちでGPUカードをかき集めていた”**が、公共算力平台により**安定した算力**を得られるようになったと述べています。Tsinghuaは2024年に、気象・時系列・強化学習研究向けに**541,440カード時**の高性能GPU算力サービスを外部調達しました。中科院地球化学研究所も2025年に**GPU机时服务**を調達しています。これは、研究現場が**所有からサービス契約へ**寄っていることを示します。 ([beijing.gov.cn](https://www.beijing.gov.cn/ywdt/gzdt/202403/t20240330_3606130.html))

### 4-3. 輸出規制による研究への影響
輸出規制の研究現場への影響は、**“研究が止まる”より“研究の組み方が変わる”**という形です。大学・研究所は、最先端GPUの自前増設よりも、**共有平台・外部GPU時間・国産チップ適配**へ動いています。深圳の训力券は**高校・科研机构も対象**ですし、浙江の国家AI券も**サービス契約ベース**です。企業側でもTencentは、**GPU不足をソフト改善で補う**と説明しています。 frontier級の基盤モデル事前学習は、公開情報を見る限り、大学より**ByteDance/Baidu/Alibaba/Tencent/Huaweiの企業クラスタ**へ一段と集中しています。 ([sz.gov.cn](https://www.sz.gov.cn/zfgb/zcjd/content/post_11932960.html))

---

## 総括
中国のAI用途GPU利用実態を一言で言うなら、**「需要は強いが、使われ方が二極化している」**です。  
- **上位層**では、Alibaba/Baidu/Huawei/ByteDance/Tencentが、国産・輸入・異種混成を組み合わせた**大規模クラスタ**を運用。  
- **中間層**では、地方政府の公共算力平台と算力券が、中小企業・大学・研究機関の入口になっている。  
- **下位層**では、過剰建設された地方センターが、**20～30%稼働**や**価格崩れ**に直面している。 ([asiatechwire.com](https://www.asiatechwire.com/International-authoritative-report-Alibaba-Cloud-ranks-first-in-Chinas-AI-cloud-market-with-a-358-share.html))

米国輸出規制は、H100/A100の不足を通じて中国のAIを減速させましたが、同時に、**国産チップの実装、公共算力市場、異種混成ソフト、海外リース、推論効率化**を一気に前進させました。したがって、中国のAI GPU問題は「量が足りるか」より、今は**“どの層に、どの品質の算力が、どのコストで届くか”**が本質です。 ([sec.gov](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000116/nvda-20250427.htm))

補足すると、**Biren/Cambriconの正確な大規模導入台数**や、**天河/曙光系のAI向けGPUカード枚数の最新内訳**、**“30都市超”の算力券を完全網羅した単一公式台帳**は、公開ソースでは透明性が高くありません。必要なら次に、  
1. **都市別の算力券一覧表**、  
2. **企業別GPU保有下限/推定レンジ表**、  
3. **輸出規制年表（2022→2026）**  
の3つに分けて、さらに深掘りできます。

[ERROR: Query terminated after 2510.8s: Rate limit reached for gpt-5.4-pro (for limit gpt-5.4-pro-long-context) in organization org-iFKQWRIi6HMKTiyZPcWpUVRi on tokens per min (TPM): Limit 10000000, Used 9636469, Requested 369457. Please try again in 35ms. Visit https://platform.openai.com/account/rate-limits to learn more.]

---

## 4. 日本のGPU利用実態

以下、**2026年3月28日時点**で確認できた**2025–2026年の公開情報**を使って、日本の「AI用途のGPU利用実態」を整理します。結論だけ先に言うと、日本のGPU利用は **①米国ハイパースケーラー依存がなお強い、②ただし政府補助を受けた国内GPUクラウドが急拡大、③公的研究ではABCI/HPCI/大学GPUが重要、④最先端の大規模学習は大企業オンプレにも急速にシフト**、という4層構造です。METIは日本の基盤クラウド市場で**国内事業者シェアが約3割**と明示しており、裏を返すと約7割は主に海外勢です。一方で、METI資料ではクラウドプログラムで整備された**国内AI計算資源は2025年11月末時点で約21.1 EFLOPS、2027年度末までに累計60 EFLOPS規模**に達する見込みです。IDCも日本のAIインフラ市場が**2026年に55億ドル超**へ成長すると予測しています。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))

## 0. エグゼクティブサマリー

- **商用利用の主戦場は依然としてAWS/Azure/GCP**ですが、**政府が補助した国内GPUクラウド（さくら、GMO、ハイレゾ、KDDI系など）が“代替”ではなく“本流の一部”になり始めた**のが2025–2026年の最大変化です。ABCI自身も、ABCI 3.0で計算資源が逼迫する場合は国内GPUクラウドの利用を検討するよう案内しています。 ([abci.ai](https://abci.ai/ja/cloud_program/))

- **公的研究のGPU中核はABCI 3.0**です。ABCI 3.0は**H200を6,128基**搭載し、2025年1月に開始しましたが、**2025年度中に需要が想定超過**となり、8月にはポイント発行制限が入っています。 ([docs.abci.ai](https://docs.abci.ai/v3/en/system-overview/))

- **富岳は“AIに使えない”わけではない**ものの、現行機はGPU機ではなくCPU中心です。理研はそのギャップを埋めるため、**2025年にAI for Science用GB200系GPU機（1,600 GPU級）**を別系統で整備し、さらに**2030年ごろ稼働予定のFugakuNEXTで初めてGPUアクセラレータを採用**します。 ([r-ccs.riken.jp](https://www.r-ccs.riken.jp/en/assets/uploads/sites/2/2021/07/f_riken_fugaku_kitei_en.pdf))

- **大学・共同利用の層**では、HPCI経由で**Miyabi（GH200）、TSUBAME4.0（H100×4/ノード）、Wisteria Aquarius（A100×8/ノード）、Pegasus（H100）**など複数のGPU資源にアクセスできます。さらに**mdx II**が2025年に**H200×4/ノードのGPUノード**を開始し、すでに需要超過状態です。 ([hpci-office.jp](https://www.hpci-office.jp/en/using_hpci/hardware_software_resource/2025))

- **企業オンプレは“持っている企業はかなり持っている”**状態です。ソフトバンクは**総GPU 1万基超・13.7 EFLOPS**のAI計算基盤を公表し、SB Intuitionsが利用中です。NECは**A100×928基相当（116台×8GPU）・580 PFLOPS超**の自社AIスパコンを構築済み、NTT Comは**3拠点分散H100環境でtsuzumi学習実証**に成功しています。 ([softbank.jp](https://www.softbank.jp/corp/news/press/sbkk/2025/20250723_01/))

---

## 1. GPUの利用経路

### 1-1. 米国ハイパースケーラー（AWS/GCP/Azure）の日本利用

### 日本市場シェア
- 日本の基盤クラウド市場では、METIが**「国内に事業基盤を有する事業者のシェアは約3割」**と明記しており、残る約7割は主に海外クラウドです。ベンダー別の**2025–2026年の無料公開シェア**は見当たりませんでしたが、最新の無料で詳細な国内内訳として確認できたMM総研の2022年6月調査では、**PaaS利用企業で AWS 60.0%、Azure 48.2%、GCP 28.8%、IaaS利用企業で AWS 54.7%、Azure 44.0%、GCP 26.2%**でした。したがって、**日本市場では今もAWS優位、Azure追随、GCP拡大**という構図で見るのが妥当です。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))

### 日本リージョンのGPU構成
- **AWS**は、少なくとも**東京リージョン**で **P5（H100）** と **P5e/P5en（H200）** が公式料金ページ上で確認できます。ABCIのクラウドプログラム連携ページに掲載されたAWSの2025年9月30日更新情報では、日本国内リージョンで**B200/H200/H100/L4/L40**まで含む豊富なGPUサービスを提供すると案内されています。なお、私が確認できたAWS一次情報で**東京のH100/H200は明確**でしたが、**大阪リージョンの同等ラインアップは公開ページ上で即確認できませんでした**。 ([aws.amazon.com](https://aws.amazon.com/ec2/capacityblocks/pricing/))

- **Google Cloud**は、GPU配置表（**2026年3月26日更新**）で、**東京（asia-northeast1）**に **A4、A3 Mega、A3 High、A3 Edge、A2 Standard、G2、N1+T4** を提供しています。他方、**大阪（asia-northeast2）はGPU対応として表示されていません**。つまりGCPの日本リージョンGPUは、現時点では実質的に**東京集中**です。 ([cloud.google.com](https://cloud.google.com/compute/docs/gpus/gpu-regions-zones))

- **Azure**は、H100系VMとして **NCads_H100_v5** や **ND H100 v5** 系列そのものは公式ドキュメントで確認できます。さらにMicrosoft Learnの**2026年1月の公式Q&A**では、APACで **NCads_H100_v5 は Japan East をサポート**し、**H200はAPACではAustralia Eastのみ**、**A100もJapan Eastで利用可能**と案内されています。少なくとも公開情報ベースでは、**日本でのAzure GPU重点リージョンは Japan East** です。 ([learn.microsoft.com](https://learn.microsoft.com/ja-jp/azure/virtual-machines/sizes/gpu-accelerated/ncadsh100v5-series))

### 実態としてどう見ればよいか
- 日本のAI開発者がハイパースケーラーを使う理由は、**即時性・マネージド性・モデル周辺サービス（SageMaker/Vertex/Azure AI Foundry等）**にあります。一方で、日本市場全体としては**海外依存が高く**、その反動として経産省は国内GPU整備に補助を入れています。したがって、**“日常開発はハイパースケーラー、主権性や長時間学習は国内GPUクラウド/オンプレへ”**という使い分けが増えています。これはMETIの市場認識とABCIの国内クラウド誘導からも読み取れます。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))

---

### 1-2. 国内GPUクラウド

### さくらインターネット（高火力 / さくらONE）
- さくらのGPU群は**高火力 DOK（コンテナ）／VRT（VM）／PHY（ベアメタル）／さくらONE**で多層化されています。総合ページでは**H100/H200/B200**対応を掲げ、**DOKは57.6円/時間〜、VRTは481円/時間〜、PHYは大規模専有向け**です。VRTの公開料金では **V100 481円/時間、H100 990円/時間** が確認できます。 ([gpu.sakura.ad.jp](https://gpu.sakura.ad.jp/))

- 2025年8月にはPHYの**B200プラン**を開始し、この時点で高火力全体の**総計算能力は4.81 EFLOPS**に達したと公表しました。決算資料では、GPUクラウド向け投資として**2024–2025年度に273億円を実行**し、**2026年度に289億円**を予定しています。 ([sakura.ad.jp](https://www.sakura.ad.jp/corporate/information/newsreleases/2025/08/15/1968220622/))

- 政府補助は**最大501億円**で、国内事業者の中でも最大です。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))

### GPUSOROBAN（ハイレゾ）
- GPUSOROBANは、一般インスタンスを**1時間50円から**提供しつつ、H200/B200の高性能クラスタも持つ、**“安価な入口＋高性能上位系”**の二層モデルです。共用型の**計算クラスター**は **1 GPU・1分あたり20ポイント（=20円）**、**1pt=1円**、最低購入**100,000pt**で、**累計2,000件超の利用実績**を公表しています。 ([soroban.highreso.jp](https://soroban.highreso.jp/))

- 上位の**AIスパコンクラウド**では、**HGX H200 8GPU**構成を**月額2,783,000円（税込）**で提供し、比較対象として他社H100×8より安価と訴求しています。ポイント購入は**クレジットカード／請求書（メール手続き）対応**で、研究費処理との相性が比較的よいです。 ([soroban.highreso.jp](https://soroban.highreso.jp/aispacon))

- 政府補助は**最大77.0億円**です。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))

### GMO GPUクラウド
- GMO GPUクラウドは**H200 + NVIDIA Spectrum-X + DDN高速ストレージ + Slurm + NVIDIA AI Enterprise**を前面に出すサービスです。2025年2月には**MIG**対応を追加し、2025年5月には**H200を256基追加投資**、2025年Q4稼働予定と発表しました。 ([gmo.jp](https://www.gmo.jp/en/news/article/838/))

- Green500 2025年6月版では、**32ノード・256基のH200**で**10.05 PFLOPS**、**53.81 GFLOPS/W**を達成し、**世界34位・国内1位**でした。 ([gmo.jp](https://www.gmo.jp/news/article/9537/))

- 政府補助は**最大19.3億円**です。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))

### IDCフロンティア
- IDCフロンティアは、**“H100/H200を気軽に借りるGPUクラウド”よりも、“GPU向け高負荷ハウジング/DLC対応DC”の色が強い**のが現状です。公開クラウド側では従来から**P100系GPU VM**がありますが、2025年は**東京府中DCの高負荷ハウジングを約100ラックへ増床**し、さらに**DLCハウジングを1ラック150kWまで対応**へ拡張しました。 ([idcf.jp](https://www.idcf.jp/cloud/spec/vm.html))

- つまりIDCフロンティアは、日本のAI GPU供給では**“GPUクラウド事業者”というより“GPUサーバーを置ける電力・冷却・ハウジング基盤”**として重要です。CyberAgentやTokyo-1のような事例がこの位置づけを示しています。 ([idcf.jp](https://www.idcf.jp/case/cyberagent.html))

### 国内GPUクラウド全体の実勢
- METI資料によれば、クラウドプログラム認定事業者などによる国内整備済みAI計算資源は**2025年11月末で約21.1 EFLOPS**、**2027年度末までに60 EFLOPS規模**の見込みです。ここまで来ると、国内GPUクラウドは「ニッチ代替」ではなく、**公的・企業向けの本格供給路**です。 ([meti.go.jp](https://www.meti.go.jp/policy/mono_info_service/joho/conference/semicon_digital/0014/handeji14-5.pdf))

---

### 1-3. ABCI 3.0（産総研）

- ABCI 3.0は、**766計算ノード、NVIDIA H200 6,128基、75PB物理ストレージ**を備え、**2025年1月20日**に提供開始しました。各Hノードは**H200 SXM 141GBを8基**搭載します。 ([docs.abci.ai](https://docs.abci.ai/v3/en/system-overview/))

- 料金は**1ポイント=220円**です。単一GPUの**rt_HG**は標準利用で**3 point/h=660円/GPUh**、開発加速利用で**1.5 point/h=330円/GPUh**です。8GPUノードの**rt_HF**をGPU時間換算すると、標準利用は**440円/GPUh**、開発加速利用は**約206円/GPUh**です。質問にある**330–660円/GPUh**は、単一GPUノード換算としては正しいです。 ([abci.ai](https://abci.ai/en/how_to_use/tariffs.html))

- 利用条件は、**ユーザーポータルから新規申請→承認→公開鍵登録→利用開始**が基本です。2025年度は**4月15日**に本格サービス開始、ポータルは**4月14日**開始でした。ポータルやガイドの一部は**日本語のみ**です。加えて、**特定類型該当性**や**非居住者チェック**などの輸出管理手続があり、日本の学生等は責任者経由で処理されます。 ([docs.abci.ai](https://docs.abci.ai/v3/en/getting-started/))

- ABCI 3.0は、**国研・大学・スタートアップ等の公的なAI R&D**を優先する運用で、**開発加速利用**や**地方優先枠**を設けています。その反面、**標準利用、非公的法人、東京圏法人**では使えない／十分な資源が確保できない場合があると、ABCI自身が明示しています。 ([abci.ai](https://abci.ai/ja/cloud_program/))

- 実需はかなり強く、ABCIは**2025年8月にポイント発行制限**を実施しました。理由は、**ABCI 3.0への拡充後も需要が想定を大きく超え、特に公的部門利用が伸びた**ためです。 ([abci.ai](https://abci.ai/news/2025/08/14/en_early_restriction_on_point_issuance_fy2025.html))

- 利用者数そのものの**ユニーク人数は公開確認できませんでした**。ただし、産総研レポート2025は**FY2024のABCI利用324件**を公表しています。加えて、2024年度のABCI 3.0開発加速利用の成果概要は少なくとも数十件公開されており、利用は活発です。 ([aist.go.jp](https://www.aist.go.jp/pdf/aist_j/aist_report/2025/aist_report_2025.pdf))

---

### 1-4. 富岳（理研）

- 富岳の利用規程は、データサイエンスやAIを含む広い分野への支援を明記しています。実際、理研は**Fugaku-LLM**やAI for Science関連の成果を継続的に打ち出しています。つまり、**富岳はAI利用“可”**です。 ([r-ccs.riken.jp](https://www.r-ccs.riken.jp/en/assets/uploads/sites/2/2021/07/f_riken_fugaku_kitei_en.pdf))

- ただし、**現行富岳はGPU機ではありません**。そのため、最先端の大規模学習という意味でのGPU需要は、ABCIや国内GPUクラウドに流れやすいです。理研自身も、2025年7月に**GB200系1,600 GPU超のAI for Science専用スパコン**を決定し、**2026年度冒頭の本格運用**を目指すとしました。これは、富岳単体では不足するAI性能を補う明確な動きです。 ([riken.jp](https://www.riken.jp/pr/news/2025/20250728_1/index.html))

- 後継の**FugakuNEXT**では、**日本のフラッグシップ機として初めてGPUアクセラレータを採用**します。2025年度中に基本設計、2026年度以降に詳細設計へ移行し、**2030年ごろの稼働**を目指します。 ([riken.jp](https://www.riken.jp/en/news_pubs/news/2025/20250822_1/))

---

### 1-5. HPCI / mdx

- HPCIは、**富岳と全国の大学・研究機関のスパコンやストレージをSINET6で結ぶ共用計算基盤**です。2025年度のHPCI資源一覧では、GPU系として **Grand Chariot 2（H100×4）**、**Pegasus（H100）**、**Miyabi-G（GH200）**、**Wisteria Aquarius（A100×8）**、**TSUBAME4.0（H100×4）** などが並んでいます。 ([hpci-office.jp](https://www.hpci-office.jp/about_hpci))

- **mdx II**は学術向けIaaS型クラウドです。2025年6月にGPUノードサービスを開始し、当初は**7ノード、各ノード H200 SXM×4**でした。料金は**1 GPUパック（30仮想コア）で198,000円/月（税込）**です。2025年10月には**申込多数で希望通り提供が難しい**と案内され、2026年4月から**8ノード追加（合計15ノード）**予定です。 ([mdx.jp](https://mdx.jp/en/mdx2/news/4515))

- mdxは、**学術版GPUクラウド**としてかなり重要です。ABCIより柔らかく、大学横断のデータ駆動研究や隔離仮想環境に向く一方、**大規模バッチ学習の絶対量はABCIや大企業GPU群ほどではない**、という位置づけです。 ([mdx.jp](https://mdx.jp/en/mdx2/p/system))

---

### 1-6. 大学の計算資源（東大・京大・東京科学大など）

- **東京大学 / JCAHPC**では、2025年1月に**Miyabi**が運用開始しました。Miyabi-Gは**GH200 1,120ノード**、Miyabi-CはXeon Max 190ノードで、総ピーク性能は**80.1 PFLOPS**です。東大単独では、**Wisteria/BDEC-01 Aquarius** が **A100×8/ノード** を持ち、HPCIでも共有されています。 ([jcahpc.jp](https://www.jcahpc.jp/eng/supercomputer/miyabi-e.html))

- **京都大学**は、2024年度年報でスーパーコンピュータの**System G**を **A100×4/ノード**、**GPU総演算性能20.0 PFLOPS（半精度）** としています。サービス面でも、パーソナルの**Type G**やグループの**G0/G1**があり、全国共同利用を継続しています。 ([iimc.kyoto-u.ac.jp](https://www.iimc.kyoto-u.ac.jp/sites/default/files/2025-11/iimc_nenpou2024.pdf))

- **東京科学大学（旧東工大）TSUBAME4.0** は、**240ノード、H100 SXM5 94GB×4/ノード、全体でH100を960基、66.8 PFLOPS（FP64）/952.4 PFLOPS（FP16）**です。学外向けの**TSUBAME共同利用**も継続しており、2025年度も随時受け付けています。 ([gsic.titech.ac.jp](https://www.gsic.titech.ac.jp/sites/default/files/spec40j.pdf))

- 実務的には、大学院生や若手研究者はまず**所属大学のGPU**、次に**JHPCN/HPCI/ABCI/mdx**へ進むことが多いです。大学センターは“入口”として非常に重要ですが、**兆パラ級学習を安定運用できる規模は限られる**ため、大規模案件ほどABCI・国内GPUクラウド・企業GPU群へ流れます。これは各システム規模の差からの推論です。 ([hpci-office.jp](https://www.hpci-office.jp/en/using_hpci/hardware_software_resource/2025))

---

### 1-7. 企業オンプレ

- **ソフトバンク**は、2025年7月時点で**4,000基超のBlackwell GPU**を使うDGX SuperPODを完成させ、**AI計算基盤全体ではGPU 1万基超、13.7 EFLOPS**を公表しました。まずは**SB Intuitions**が利用し、同社は**FY2024に約4,600億パラメータのLLM**を構築済みです。 ([softbank.jp](https://www.softbank.jp/corp/news/press/sbkk/2025/20250723_01/))

- **NTT Com**は、2025年3月に**3拠点データセンターへ分散配置したH100 GPUサーバー**環境で、**tsuzumi** の学習実証に成功しました。公開情報からはGPU総数までは読めませんが、**分散私設GPU基盤**を持つこと自体が重要です。 ([ntt.com](https://www.ntt.com/about-us/press-releases/news/article/2025/0319.html))

- **NEC**は、2022年公表の自社AIスパコンで **A100 80GB×8GPUサーバー116台**、つまり**928 GPU相当**、**580 PFLOPS超**を構築しました。2025–2026年にはさらに、H100NVLを遠隔共有する**Composable/Disaggregated GPU**の実証・製品化も進めています。 ([jpn.nec.com](https://jpn.nec.com/press/202205/20220517_02.html))

- したがって企業オンプレは、**日本全体では少数だが、上位企業はハイパースケーラー級に近い私設GPU群を持ち始めた**というのが実態です。特にソフトバンクは、もはや“クラウド利用者”というより“国内AI計算基盤の供給者”です。 ([softbank.jp](https://www.softbank.jp/corp/news/press/sbkk/2025/20250723_01/))

---

## 2. 資金源

### 科研費（KAKENHI）
- 令和7年度（2025年度）の科研費予算は**2,379億円**です。ただし、**GPUやクラウドに使われた割合の公的統計は見当たりません**。JSPSハンドブックと使用区分表では、直接経費は**研究遂行に必要な物品費・旅費・人件費・その他**に広く使えるとされており、クラウドGPUは制度上は十分に支出可能ですが、**“GPU計算費シェア”は未集計**です。 ([mext.go.jp](https://www.mext.go.jp/content/20250129-mxt_kiso-000040094_4.pdf))

### NEDO
- NEDOの**GENIAC公募**では、助成対象の計算資源利用料として**GPUリソースとGPU以外の計算リソース費用が対象**と明記されています。NEDOはGENIACのほか、**AIセーフティ**や**ロボティクス分野の生成AI基盤モデル**なども進めています。 ([nedo.go.jp](https://www.nedo.go.jp/koubo/CD2_100421.html))

### JST（CREST / さきがけ / ACT-X / Moonshot）
- JSTの戦略的創造研究推進事業では、共通経費区分表に**「クラウド利用料等」**が明記されており、GPUクラウド代を研究費で処理できます。研究費規模は、**CRESTが1課題あたり直接経費1.5〜5億円**、**ACT-Xは数百万円規模**です。さきがけは領域にもよりますが、2025年度新規領域資料では**1課題4,000万円上限**の例が確認できます。 ([jst.go.jp](https://www.jst.go.jp/contract/download/2025/2025kisokens309betsu.pdf))

- **Moonshot**も、少なくとも2025年公募のGoal 10では、**最初の2年間で約2億円、最初の4年間で約20億円**を上限目安とする大型予算です。こちらもJST契約ルールに基づくため、クラウド利用料は制度上処理可能です。 ([jst.go.jp](https://www.jst.go.jp/moonshot/en/application/202504/files/besshi1_goal10.pdf))

### GENIAC
- GENIACはMETI/NEDOが**2024年2月に開始**した生成AI開発支援です。公開確認できた採択数では、**第2期で基盤モデル開発20件＋データ実証3件**、**第3期で基盤モデル開発24件**が採択されています。2025年からは**GENIAC-PRIZE（懸賞金総額約8億円）**も開始しました。 ([meti.go.jp](https://www.meti.go.jp/english/policy/mono_info_service/geniac/))

- ご提示の**「GENIAC=339億円」**は、今回確認した**公開一次資料では明確に裏取りできませんでした**。公開一次資料で確実に確認できたのは、採択件数やPRIZE約8億円、そして親制度であるポスト5G/クラウドプログラムの大規模支援です。したがって、**GENIAC単独の総額として339億円を断定するのは避ける**のが無難です。 ([meti.go.jp](https://www.meti.go.jp/press/2025/07/20250715001/20250715001.html))

### 経産省のAI計算基盤整備・クラウドプログラム
- **クラウドプログラム**では、2024年4月時点で**5件合計最大725億円**の助成が決定されています。内訳は、**さくら501億円、KDDI 102.4億円、ハイレゾ77.0億円、GMO 19.3億円、RUTILEA/AI福島25.6億円**です。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))

- その後のMETI資料では、R4・R5補正を活用しつつ国内計算資源整備が進み、**2025年11月末で21.1 EFLOPS**、**2027年度末で60 EFLOPS**見込みとされています。 ([meti.go.jp](https://www.meti.go.jp/policy/mono_info_service/joho/conference/semicon_digital/0014/handeji14-5.pdf))

- ご提示の**「FY2026で1.23兆円・4倍増」**については、私が確認した**公式資料では“AI単独”としては確認できません**。内閣府・経産省のAI関連予算資料では、**FY2026当初予算案のAI関連予算は約5,027億円、FY2025補正は約4,380億円**です。別のMETI公式資料で確認できる大きな数字は、**AI・半導体産業基盤強化フレームの2030年度まで7年間で10兆円以上の公的支援**です。したがって、**1.23兆円はAI+半導体の広義合算を指すメディア表現の可能性が高い**、というのが現時点の整理です。 ([meti.go.jp](https://www.meti.go.jp/policy/mono_info_service/joho/conference/seichosenryakuwg/aisemicon01/shiryo04.pdf))

### 大学予算
- 全国合計の**「大学がGPUに何円出しているか」**という公的統計は見当たりません。ただ、大学センターは利用料と内部補助を組み合わせて回しています。例えば京都大学は**Type G基本100,000円/年**、TSUBAME共同利用は**400 point=110,000円、1 point=250円**の例が公開されています。JHPCNでも論文掲載料等への**50万円上限助成**があります。 ([iimc.kyoto-u.ac.jp](https://www.iimc.kyoto-u.ac.jp/sites/default/files/2025-02/futankin.pdf))

### 企業R&D
- 総務省統計局の科学技術研究調査では、**2024年度の科学技術研究費は23兆7,925億円**です。ここからGPU投資だけを切り出した統計はありませんが、日本企業のAI/GPU投資余地が公的研究費より桁違いに大きいことは明白です。 ([stat.go.jp](https://www.stat.go.jp/data/kagaku/index.html))

### 個人利用（Colab等）
- 個人利用の入口としてはColabが依然強く、Google公式情報では、**無料プランは計算ユニット保証なし・GPU利用は限定的**、**Colab Proは100 compute units/月で9.99ドル（柔軟プラン）**、**Pro+は500 units/月で49.99ドル**です。研究室予算に載らない初期試行では、ここが実質的な“最初のGPU”になりやすいです。 ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))

---

## 3. 政府施策・独自の取り組み

### AI基本計画
- 日本初の**人工知能基本計画**は、**2025年12月23日に閣議決定**され、**2026年2月6日に内閣府が公表**しました。柱は **①AIを使う、②AIを創る、③AIの信頼性を高める、④AIと協働する** の4本で、**当面毎年変更**する前提です。なお、この基本計画の公開ページ自体には**「5年間1兆円」**という金額は確認できませんでした。 ([cao.go.jp](https://www.cao.go.jp/press/new_wave/20260206.html))

### AI・半導体産業基盤強化フレーム
- 政府の大きな数字として確実に確認できるのは、**2024年11月の経済対策で策定されたAI・半導体産業基盤強化フレーム**で、**2030年度までの7年間に10兆円以上の公的支援**を行い、**10年間で50兆円超の官民投資**を促すというものです。 ([meti.go.jp](https://www.meti.go.jp/policy/mono_info_service/ai_semiconductor_frame/ai_semiconductor_frame.html))

### GENIACの位置づけ
- GENIACは、**計算資源提供支援、データ実証、コミュニティ運営、マッチング、グローバル連携**をまとめた“開発加速の場”です。第3期では**24件採択**、第2期成果からはPLaMo Liteや創薬・気候・カスタマーサポート特化モデルなど、**用途特化モデル志向**が鮮明です。 ([meti.go.jp](https://www.meti.go.jp/english/policy/mono_info_service/geniac/))

### ABCI 3.0の位置づけと課題
- ABCI 3.0は、**日本の公的AI研究の中核GPU基盤**ですが、運用方針は**公的利用優先**で、かつ**2025年度に需要超過**が顕在化しました。そのため、ABCIは**国内GPUクラウドとの連携ページ**を設け、利用者を国内民間GPUへも誘導しています。これは、ABCIが“唯一の国産AI計算基盤”ではなく、**国内GPUエコシステムのハブ**に位置づけ直されつつあることを示します。 ([abci.ai](https://abci.ai/ja/cloud_program/))

### 富岳NEXT
- FugakuNEXTは、**AI-HPC統合基盤**として設計され、**GPUを初採用**します。理研はFugakuNEXTを通じ、AI for Scienceと量子計算連携も含めた新しいフラッグシップ像を目指しています。 ([riken.jp](https://www.riken.jp/en/news_pubs/news/2025/20250822_1/))

### mdx
- mdxは、**学術IaaS型データ基盤**として、大学横断の隔離環境・データ管理・仮想GPU利用に向きます。2025年からH200 GPUノードが入り、2026年4月に15ノードへ拡張予定で、学術用途の“柔らかいGPUクラウド”として存在感が増しています。 ([mdx.jp](https://mdx.jp/en/mdx2/p/system))

### ISMAPと政府調達
- ISMAPは、**政府が求めるセキュリティ要求を満たすクラウドサービスを事前評価・登録する制度**で、政府のクラウド調達を円滑化するためのものです。クラウドサービスリストは**2025年12月22日**にも更新されました。ガバメントクラウド側でも、FY2025調達で**305項目の技術要件**を課しており、国内勢にとっては**GPU性能だけでなく政府調達適合性**が重要です。 ([digital.go.jp](https://www.digital.go.jp/policies/security/ismap-liu))

### 半導体戦略（Rapidus等）とGPU国産化
- Rapidusは、**2nm世代の先端ロジック半導体とチップレット/パッケージ**に集中しており、**2025年4月にパイロットライン立上げ、2027年量産開始目標**を掲げています。つまり現在の日本の戦略は、**“日本版NVIDIA GPUをすぐ作る”より、“先端ロジック/パッケージ/製造能力を取り戻す”**ことに重心があります。したがって、**GPU国産化はまだ“製造基盤強化の段階”**であって、完成した国産汎用GPU製品が普及している状況ではありません。これはRapidusの公開説明からの整理です。 ([rapidus.inc](https://www.rapidus.inc/news_topics/news-info/nedo-fy2025-approval/))

---

## 4. 研究者の実際のGPU調達パターン

### 4-1. 日本の大学院生の典型ルート
これは統計ではなく、上の制度・料金・可用性から見た**典型パターンの整理**です。

1. **Colab無料**で試す。無料枠はGPUアクセスが限定的で、計算ユニット保証もありません。 ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))  
2. 足りなくなると **Colab Pro/Pro+** に上げる。 ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))  
3. 研究室・大学センターGPU（京都 System G、TSUBAME4、Wisteria、Miyabi 等）へ移る。 ([iimc.kyoto-u.ac.jp](https://www.iimc.kyoto-u.ac.jp/sites/default/files/2025-11/iimc_nenpou2024.pdf))  
4. 大規模学習が必要になると、**JHPCN/HPCI/ABCI** を申請する。 ([jhpcn-kyoten.itc.u-tokyo.ac.jp](https://jhpcn-kyoten.itc.u-tokyo.ac.jp/ja/expense_subsidy))  
5. さらに **ABCIが混雑**、または**納期・年度都合・ソフト要件**が合わない場合、**国内GPUクラウド（さくら、GPUSOROBAN、GMO）か、AWS/GCP/Azure** を科研費/JST/NEDO資金で使う。ABCI自身がその動線を案内しています。 ([abci.ai](https://abci.ai/ja/cloud_program/))

### 4-2. ABCIの利用体験（申請〜利用）
- ABCI 3.0では、**研究テーマを定めてポータルで利用申請**し、**公開鍵を登録**して利用開始する流れです。2025年度のポータル開始は**3月18日/4月14日–15日**でした。 ([docs.abci.ai](https://docs.abci.ai/v3/en/getting-started/))

- 料金は**ポイント前払**で、**1,000ポイント単位**、**10月以降の追加取得に上限がかかることがある**、**3月30日17時で未使用ポイント失効**という、かなり日本的な**年度管理**です。 ([abci.ai](https://abci.ai/en/how_to_use/tariffs.html))

- 2025年度は利用が予想超過となり、**8月21日から発行制限**が入ったため、採択されても“取り放題”ではありません。**「採択された＝必要GPUが常に取れる」ではない**のが実務上の注意点です。 ([abci.ai](https://abci.ai/news/2025/08/14/en_early_restriction_on_point_issuance_fy2025.html))

### 4-3. 科研費でクラウドGPUを使う際の手続き
- 制度上、科研費の直接経費は**研究遂行に必要な経費へ広く充当可能**です。クラウド利用料は多くの研究機関で「その他」扱いになることが多く、JSTの共通経費区分でも**クラウド利用料等**が明示されています。 ([jsps.go.jp](https://www.jsps.go.jp/file/storage/kaken_15_2025/r7_handbook_kenkyusha_e.pdf))

- ただし執行実務は**所属機関ルール依存**です。研究費は**研究期間内に発注・納品・利用**される必要があり、大阪大学の公開ハンドブックも、**3月発注でも4月納品や4月使用は不可**と明記しています。したがって、**年度末に従量課金GPUをまとめて使う**のは会計的に扱いにくいです。 ([osaka-u.ac.jp](https://www.osaka-u.ac.jp/ja/research/policy/fuseiboushi/files/HandbookJP_APR2021.pdf/%40%40download/file))

### 4-4. 日本の研究者特有の課題
- **年度予算制約**：ABCIポイントは**3月30日失効**、mdx IIも**年度を越えて利用できない**と明記しています。大学の公的研究費ルールも**研究期間内利用**を厳格に求めます。GPUを“必要な時に後ろ倒しで使う”より、“年度内にきれいに締める”圧力が強いです。 ([abci.ai](https://abci.ai/en/how_to_use/tariffs.html))

- **支払い方式の摩擦**：九州大学の研究費ハンドブックは、**大学クレジットカードではなく大学IDで購入**すること、**請求書払い業者との契約代金の立替払いは適当でない**としています。一方、GPUSOROBANは**請求書対応**を明示しています。つまり、**消費者向けSaaS/クラウドの自助的カード決済**と、**大学会計の請求書・IDベース運用**が噛み合いにくいです。 ([kyushu-u.ac.jp](https://www.kyushu-u.ac.jp/f/57896/research_fund_handbook_6.pdf))

- **言語の壁は“英語だけ”ではなく二方向**です。海外ハイパースケーラーのGPU配置・SKU情報は英語の一次資料が多い一方、ABCIユーザーポータルは**Japanese only**です。実務上は、**英語サービスの壁**と**日本語専用公的インフラの壁**の両方があります。これは本調査で参照した一次資料の構造からの推論です。 ([cloud.google.com](https://cloud.google.com/compute/docs/gpus/gpu-regions-zones))

- **輸出管理/居住性チェック**：ABCIでは**特定類型該当性**、京都大学の教育利用でも**非居住者・特定類型該当者は経産大臣許可が必要な場合がある**とされており、海外籍・留学生・共同研究者が絡むと、GPU以前に手続きが重くなります。 ([abci.ai](https://abci.ai/news/2025/03/06/ja_news-uketsuke_2025.html))

---

## 5. 実態を一言でまとめると

- **商用AI開発の量**は依然としてAWS/Azure/GCPが大きい。だが、**政策・主権・価格・請求書対応**を理由に、**国内GPUクラウドの比重が2025–2026で明確に上がった**。 ([meti.go.jp](https://www.meti.go.jp/press/2024/04/20240419002/20240419002.html))  
- **公的研究**ではABCI 3.0が中核だが、**需給逼迫**のため、mdx・HPCI・大学GPU・国内クラウドへ分散している。 ([abci.ai](https://abci.ai/news/2025/08/14/en_early_restriction_on_point_issuance_fy2025.html))  
- **富岳はAI利用されているが、現行の主役GPU基盤ではない**。日本はそこを**AI for Science専用GPU機**と**FugakuNEXTのGPU化**で埋めようとしている。 ([riken.jp](https://www.riken.jp/pr/news/2025/20250728_1/index.html))  
- **企業の最前線**では、ソフトバンク級の私設GPU群が新しい層を作り始めている。 ([softbank.jp](https://www.softbank.jp/corp/news/press/sbkk/2025/20250723_01/))  

---

## 6. 今回の調査で「公開ソースでは未確認」だった点
- **2025–2026時点の日本市場における AWS / Azure / GCP の厳密な売上シェア**。  
- **ABCI 3.0 のユニーク利用者数**。確認できたのはFY2024の**利用324件**まででした。 ([aist.go.jp](https://www.aist.go.jp/pdf/aist_j/aist_report/2025/aist_report_2025.pdf))  
- **GENIAC単独の総予算が339億円であること**。公開一次資料では裏取りできませんでした。  
- **Azure Japan West の最新GPU SKUの明確な公開一次情報**。Japan Eastは確認できました。 ([learn.microsoft.com](https://learn.microsoft.com/en-us/answers/questions/5700093/request-for-azure-gpu-capacity-availability-and-pl))  

必要なら次に、  
1. **この内容を表形式（サービス名 / GPU / 価格 / 用途 / 資金源 / 制約）に再整理**する、  
2. **研究者向けの「どこから申請するか」実務フローチャート**を作る、  
3. **国内GPUクラウドの価格比較表（ABCI / Sakura / GPUSOROBAN / mdx / Colab / AWS/GCP/Azure）**を作る、  
のどれかに進めます。

---

## 5. その他の重要地域

以下、**2026-03-28時点の公開情報ベース**で簡潔に整理します。  
※ **AIXS** は文脈上、**「AI/GPUインフラを調達・運用・仲介する事業者」**という前提で解釈しています。  
※ 数字の注意点：**韓国**は「4兆ウォン級構想」と「最新MSIT資料の最大2兆ウォン本体予算＋別枠GPU調達/金融支援」が併存、**イスラエル**は「Nebiusの4,000 B200配備」と「公的割当1,000 B200枠」が別概念、**台湾**の**NT$190B**は報道ベースの4年枠で、行政院が明示した**2026年度AI新十大建設予算はNT$31.1B**です。 ([en.yna.co.kr](https://en.yna.co.kr/view/AEN20241127006500320?utm_source=openai))

---

## 1) カナダ
- **利用経路**：研究向けはDigital Research Alliance主導の**PAICE**（Mila/Vector/Amii連携）やMilaの**TamIA**、商用は**AI Compute Access Fund（AICAF）**と**AI Compute Challenge**経由で国内クラウド/AIデータセンターへ流れる構図です。 ([mila.quebec](https://mila.quebec/en/news/mila-launched-canadas-first-ai-computing-cluster-dedicated-to-academic-research))
- **主な資金源**：連邦の**Canadian Sovereign AI Compute Strategy**が中核で、**総額最大C$2B**、うち**AICAF最大C$300M**、**AI Compute Challenge最大C$700M**、**公的スーパーコンピュート最大C$1B**。AICAFは**カナダ所在クラウド費用の2/3補助**です。 ([ised-isde.canada.ca](https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy))
- **政府施策**：主権AI計算基盤の整備、SCIPによる**カナダ所有・カナダ設置**のAIスーパーコンピュータ、Alliance経由の近距離増強（Rapid Deployment）を進めています。 ([ised-isde.canada.ca](https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy))
- **独自の取り組み**：**Mila/Vector/Amii**の研究拠点が計算資源整備と一体で動いており、MilaのTamIAは**学術研究専用として国内初**のAI計算クラスターです。VectorもPAICEの中核で、独自HPC環境を拡張中です。 ([mila.quebec](https://mila.quebec/en/news/mila-launched-canadas-first-ai-computing-cluster-dedicated-to-academic-research))
- **AIXSにとっての意味**：**示唆**として、カナダは「**主権・国内設置・研究連携**」が強い市場です。AIXSは**現地クラウド/大学/研究機関との提携型**が有効で、単純な国外GPU仲介より相性が良いです。 ([ised-isde.canada.ca](https://ised-isde.canada.ca/site/ised/en/canadian-sovereign-ai-compute-strategy))

## 2) 韓国
- **利用経路**：国の計算資源は**National AI Computing Center**、**KISTI/HANGANG**、さらに**NAVER Cloud/NHN/Kakao**などの主権クラウドへ。民間は**Samsung/SK/HyundaiのAI Factory**が大口需要を作っています。 ([msit.go.kr](https://www.msit.go.kr/eng/bbs/view.do%3Bjsessionid%3D-yDmX-KD-xn-O2Mu84AbdFFLZR7IH1HK_ufzshoC.AP_msit_1?bbsSeqNo=42&mId=4&mPid=2&nttSeqNo=1179&sCode=eng))
- **主な資金源**：初期には**官民合計KRW4T級**構想が報じられましたが、MSIT資料ではセンター本体は**最大KRW2T**、別途**GPU調達予算・低利融資・信用保証**で積み上げる形です。2026年のAI計算資源アクセス関連予算案は**KRW2.1087T**です。 ([en.yna.co.kr](https://en.yna.co.kr/view/AEN20241127006500320?utm_source=openai))
- **政府施策**：2025年に**13,000 GPU**を確保し、2026年には累計**37,000 GPU**想定、さらに税優遇・国産AI半導体（NPU/PIM）採用を政策で後押ししています。 ([msit.go.kr](https://www.msit.go.kr/eng/bbs/view.do?bbsSeqNo=42&mId=4&mPid=2&nttSeqNo=1163&sCode=eng&searchOpt=ALL))
- **独自の取り組み**：**KISTI×NVIDIA**で量子-GPU CoEを整備し、**HANGANG**を核に科学AI/量子融合を推進。加えて、韓国は**AI-RAN/Physical AI**まで一体展開しているのが特徴です。 ([kisti.re.kr](https://www.kisti.re.kr/eng/news/post/eng_news/6825))
- **AIXSにとっての意味**：**示唆**として、韓国は単なるGPUレンタル市場ではなく、**国家主権クラウド＋製造業AI Factory**市場です。AIXSは**産業向け運用、相互接続、電力効率、国産半導体混載**に強みを出す必要があります。 ([nvidianews.nvidia.com](https://nvidianews.nvidia.com/news/south-korea-ai-infrastructure))

## 3) インド
- **利用経路**：中核は**IndiaAI Compute Portal**で、政府が共有計算基盤を管理し、**E2E Networks**や**Yotta**などの民間CSPからスタートアップ・研究者・政府機関へ配分しています。 ([indiaai.gov.in](https://indiaai.gov.in/article/meity-accelerates-empanelment-of-agencies-to-provide-ai-compute-and-services-for-the-indiaai-mission))
- **主な資金源**：**IndiaAI Mission**は**₹10,372 crore（約US$1.25B）**。2026年2月時点で**既存38,000 GPU**、さらに**20,000 GPU追加**が発表されました。政府補助でGPU利用料を**世界価格の約1/3**まで下げる方針です。 ([indiaai.gov.in](https://indiaai.gov.in/news/cabinet-approves-india-ai-mission-at-an-outlay-of-rs-10-372-crore))
- **政府施策**：IndiaAI Missionの下で、**基盤モデル公募**、**IndiaAI Safety Institute**、AIスキリング拡大を並行実施。官民PPPで計算資源不足を埋めています。 ([indiaai.gov.in](https://indiaai.gov.in/news/cabinet-approves-india-ai-mission-at-an-outlay-of-rs-10-372-crore))
- **独自の取り組み**：**実利用単価を明示した計算ポータル**と、実際の配分履歴の公開が特徴です。Yotta/E2E経由で**政府案件・学術・民間**が同一枠組みで回る点は他国より運用志向です。 ([indiaai.gov.in](https://indiaai.gov.in/hub/indiaai-compute-capacity))
- **AIXSにとっての意味**：**示唆**として、インドは**最大のボリューム市場**候補です。AIXSはグリーンフィールド投資よりも、**政府ポータル接続、現地CSP提携、補助金適合パッケージ**で入る方が勝ちやすいです。 ([pib.gov.in](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2216958))

## 4) UAE
- **利用経路**：中心は**Stargate UAE**と**Core42**。政府・規制産業向けはCore42の**Sovereign Public Cloud / AI Cloud**、広域展開は**Abu Dhabiの1GW Stargate UAE**と**5GW UAE-U.S. AI Campus**です。 ([openai.com](https://openai.com/index/introducing-stargate-uae/))
- **主な資金源**：**G42/Core42/MGX**の国家資本が軸で、MGXはBlackRock/Microsoftらとの**AIP**で**当初$30Bエクイティ、総投資ポテンシャル最大$100B**を狙っています。 ([blackrock.com](https://www.blackrock.com/corporate/newsroom/press-releases/article/corporate-one/press-releases/ai-infrastructure-partnership))
- **政府施策**：**U.S.-UAE AI Acceleration Partnership**、OpenAIの**OpenAI for Countries**第1号案件、国内全体へのAI普及を国策として進めています。 ([openai.com](https://openai.com/index/introducing-stargate-uae/))
- **独自の取り組み**：**米国外初のStargate**で、**GB300**採用、**ChatGPT全国展開**まで含む「国家OS」型の構想がユニークです。 ([openai.com](https://openai.com/index/introducing-stargate-uae/))
- **AIXSにとっての意味**：**示唆**として、UAEは**MENA/アフリカ向けハブ**として魅力が高いです。AIXSには**主権クラウド準拠、政府案件対応、超大規模パートナー連携**が必須です。 ([g42.ai](https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae))

## 5) サウジアラビア
- **利用経路**：国家側の中心は**HUMAIN**で、AIファクトリー/クラウドをフルスタックで整備。AWS・AMD・Ciscoなどとの提携で周辺エコシステムも拡張しています。 ([pif.gov.sa](https://www.pif.gov.sa/en/news-and-insights/press-releases/2025/hrh-crown-prince-launches-humain-as-global-ai-powerhouse/?_bhlid=8975d7e9f7d2b5c40c2133b351af7c584a4b6148&utm_source=openai))
- **主な資金源**：**PIF**が中核で、HUMAINは今後5年で**最大500MW**・**数十万GPU級**を目指し、第一段として**18,000 GB300**を導入。加えて、Saudi MCITの公式白書でも**Project Transcendence $100B**が言及されています。 ([nvidianews.nvidia.com](https://nvidianews.nvidia.com/news/humain-and-nvidia-announce-strategic-partnership-to-build-ai-factories-of-the-future-in-saudi-arabia))
- **政府施策**：**Vision 2030**と**National Data and AI Strategy**の下で、AI投資・計算基盤・人材育成を一体推進。公式白書ではAI/計算基盤を「国家計算インフラ」として整理しています。 ([mcit.gov.sa](https://www.mcit.gov.sa/sites/default/files/2025-04/KSA%20Computing%20Infrastructure%20Whiter%20Paper.pdf))
- **独自の取り組み**：**アラビア語LLM（ALLAM/HUMAIN）**、大規模AI工場、エネルギー優位を活かしたデータセンター拡張が特徴です。SPA報道では**“One Million Saudis in AI”**も進行中です。 ([pif.gov.sa](https://www.pif.gov.sa/en/our-investments/our-portfolio/humain/?utm_source=openai))
- **AIXSにとっての意味**：**示唆**として、サウジは**巨大案件は取れるが国家主導で競争も重い**市場です。AIXSは**共建・運用受託・ソフトウェア制御層**で入る方が現実的です。 ([nvidianews.nvidia.com](https://nvidianews.nvidia.com/news/humain-and-nvidia-announce-strategic-partnership-to-build-ai-factories-of-the-future-in-saudi-arabia))

## 6) シンガポール
- **利用経路**：研究・公的利用の中心は**NSCC**で、**ASPIRE 2A**と**ASPIRE 2A+**が大学・研究機関・政府・企業の計算需要を支えます。 ([nscc.sg](https://www.nscc.sg/))
- **主な資金源**：国家予算中心で、2024年に**AI compute/talent/industry developmentへS$1B超**、2024年10月にはNSCC向けに**S$270M**、さらに2026年1月には**NAIRD Planで追加S$1B超（2025-2030）**が公表されました。 ([smartnation.gov.sg](https://www.smartnation.gov.sg/media-hub/press-releases/20240301a/?utm_source=openai))
- **政府施策**：**NAIS 2.0**を軸に、AI for Science、研究人材誘致、計算基盤強化を進めています。 ([smartnation.gov.sg](https://www.smartnation.gov.sg/nais/?utm_source=openai))
- **独自の取り組み**：**ASPIRE 2A+**は**320基のH100**・約**20 PFLOPS**、一方**ASPIRE 2A**は熱帯環境での**温水冷却**を採用した先進HPCです。 ([nscc.sg](https://www.nscc.sg/aspire-2a-plus/))
- **AIXSにとっての意味**：**示唆**として、シンガポールは**規模より品質・安定性・リージョナル統括**が価値になる市場です。AIXSには**APACの制御拠点/高付加価値運用拠点**として向きます。 ([mddi.gov.sg](https://www.mddi.gov.sg/newsroom/singapore-invests-over-s-1-billion-in-national-ai-research-and-development-plan-to-strengthen-ai-research-capabilities-and-our-position-as-global-ai-hub/?utm_source=openai))

## 7) イスラエル
- **利用経路**：**Israel Innovation Authority**が選定した**Nebius**経由で国家計算資源を供給し、企業・研究機関には**割引バウチャー**で配分します。Nebiusの現地Blackwellサイトも民間利用の重要経路です。 ([innovationisrael.org.il](https://innovationisrael.org.il/en/press_release/supercomputer-access-2026/))
- **主な資金源**：**National AI Program第2フェーズはNIS500M（〜2027）**。加えて、Nebius利用バウチャーは**企業30%引き、学術80%引き**で公的支援されます。 ([innovationisrael.org.il](https://innovationisrael.org.il/en/press_release/second-phase-ai-program/))
- **政府施策**：**National AI Program**の下で、**National AI Research Institute**、計算基盤、データ基盤、人材の4点を強化しています。 ([innovationisrael.org.il](https://innovationisrael.org.il/en/press_release/second-phase-ai-program/))
- **独自の取り組み**：Nebiusは2025年10月にイスラエルで**4,000 HGX B200**を配備。一方、Innovation Authorityの公的利用枠は現在**1,000 B200**規模です。なお、NVIDIAのイスラエル拠点は最新現地報道では**米国外で2番目に大きい開発拠点**とされており、少なくとも「最大」とは言い切らない方が安全です。 ([nebius.com](https://nebius.com/newsroom/nebius-brings-nvidia-blackwell-to-israel-with-one-of-the-country-s-first-ai-infrastructure-deployments))
- **AIXSにとっての意味**：**示唆**として、イスラエルは**高単価・高密度なAI/Cyber/Health需要**が魅力です。AIXSは**国家プログラム連携＋民間Blackwell需要**の両取りが可能ですが、競争はかなり先進的です。 ([innovationisrael.org.il](https://innovationisrael.org.il/en/press_release/second-phase-ai-program/))

## 8) 台湾
- **利用経路**：公的側は**NCHC/国網雲端算力中心**、**TAIWAN AI RAP/TWCC**、民間・産業側は**Foxconn Big Innovation Company**のAIファクトリーを**NSTC・TSMC・スタートアップ**が使う形です。 ([nstc.gov.tw](https://www.nstc.gov.tw/folksonomy/detail/c263059e-6b66-4008-a6a3-594e1f46f0cf%3Fl%3Dch))
- **主な資金源**：行政院は**2026年度のAI新十大建設にNT$31.1B**を計上。加えて、政府の**10年AIスタートアップ投資計画はNT$10B**。なお、**NT$190B**はNDC/NSTC草案に関する**報道ベースの4年投入見通し**です。 ([ey.gov.tw](https://www.ey.gov.tw/Page/9277F759E41CCD91/12a641e2-c2b7-4336-80e0-0645e666a879))
- **政府施策**：**AI新十大建設**は「スマート応用・重要技術・デジタル基盤」の3本柱で、**主権AI**も明示。さらに**Taiwan Chip-based Industrial Innovation Program (Taiwan CbI)**で半導体×生成AIを推進しています。 ([english.ey.gov.tw](https://english.ey.gov.tw/Page/878D1F23A9E61177/492c3353-04fe-460c-bba3-f57e76bb4bb2))
- **独自の取り組み**：**Foxconn×NVIDIA×台湾政府**で**10,000 Blackwell GPU**級AIファクトリーを構築し、**TSMCがR&Dのアンカーユーザー**。NCHC系では**TAIWAN AI RAP**の無料GPU試行も走っています。 ([nvidianews.nvidia.com](https://nvidianews.nvidia.com/news/foxconn-ai-factory-tsmc-taiwan-nvidia))
- **AIXSにとっての意味**：**示唆**として、台湾は**GPU需要国**であると同時に**半導体供給網の中核**です。AIXSは単純販売より、**ODM/OEM・TSMC周辺・NSTC/NCHC連携**で「共同開発/運用基盤」に寄せる方が強いです。 ([nvidianews.nvidia.com](https://nvidianews.nvidia.com/news/foxconn-ai-factory-tsmc-taiwan-nvidia))

---

必要なら次に、これを  
**(A) 8地域比較表（1ページ）**、  
**(B) AIXS向け優先進出順位**、  
**(C) “公的案件向け / 民間案件向け” の2軸マップ**  
のどれかに整形します。

---

