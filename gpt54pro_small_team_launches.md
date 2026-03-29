# Small-Team Startup Launch Research (GPT-5.4-pro)

> Generated: 2026-03-29 13:45:22
> Model: gpt-5.4-pro with web_search_preview
> Duration: 1792.9s

---

以下、**「大型調達前のローンチ前〜初期」**に絞って、Webで確認できる数字を優先して整理しました。  
先に重要な補足だけ：

- **Runpod** の共同創業者名は、公開ソースでは **Zhen Lu / Pardeep Singh** です。ご指定の「Zhen Wang」は一致しませんでした。 ([techcrunch.com](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/))
- **Vast.ai** は公開ソース上、**2016年6月28日法人化・2018年9月プロダクトローンチ** が最も整合的です。ご指定の「2020年創業」ではありません。 ([vast.ai](https://vast.ai/about))
- **Lightning AI** は **2019年に Grid.ai として創業**、のちに Lightning AI へ改称しています。 ([lightning.ai](https://lightning.ai/pages/community/article/grid-ai-becomes-lightning-ai/))

また、**1ヶ月/3ヶ月/6ヶ月の users/MRR は公開していない会社が多い**です。そこは **「非公開」** と明記し、代わりに最も近い検証可能な指標を置いています。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

---

## まず結論だけ

**少人数で初期立ち上げに成功した会社の共通点**はかなりはっきりしています。

1. **ローンチ前に“配布面”を作っていた**  
   OSS（PyTorch Lightning, GPT Engineer, Cog）、既存コミュニティ（Reddit/HN/Discord/Product Hunt/X）、既存技術基盤（WebContainers）を先に作っていました。 ([baincapitalventures.com](https://baincapitalventures.com/insight/lightning-doesnt-strike-twice/))
2. **最初は“狭い1ユースケース”で刺している**  
   Runpod は「安いGPU」、Vast は「余剰GPUの市場化」、Cursor は「bug-fix / codebase Q&A」、Bolt/Lovable は「prompt→実動アプリ」、Replicate は「モデルを1行APIで使える」に絞っていました。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))
3. **最初の顧客獲得は広告ではなくコミュニティ起点**  
   Reddit、Hacker News、Product Hunt、X、Discord、OSS コミュニティが中心です。 ([reddit.com](https://www.reddit.com/r/deeplearning/comments/t8atpp))
4. **初期は founder-led support**  
   Runpod は Reddit/Discord/サポートチャット、Bolt は 12人チームで創業者自ら大量のサポート対応、Lovable もコミュニティ運営を強く回しています。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))
5. **大型資金調達前でも伸びる会社は、資金より“配布”が先**  
   Runpod/Vast/Kibela/MagicPod はかなり後ろまで小さく始め、Bolt/Lovable は高速成長したが、それでも爆発の起点は既存コミュニティと既存技術でした。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

---

# 1. 企業別ケース

## GPU / MLインフラ

### 1) Runpod
- **ローンチ前に何をしていたか**  
  2021年後半、Zhen Lu と Pardeep Singh は自宅地下の Ethereum マイニング用 GPU リグ約 **$50,000 相当** を AI 用に転用し、数ヶ月で最初のプロダクトを作りました。**2022年3月8日**の soft launch では、r/deeplearning に「**無料GPU時間と引き換えにフィードバック募集**」を投稿し、当初の無料提供マシンは **12x3070 / 4x3080 / 2x3090** でした。Discord とメールで応募を受け、創業者自身がフィードバックを回収していました。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))
- **ローンチ時の資金**  
  外部資金はなく、**実質ブートストラップ**です。創業後も「ほぼ2年間」資金調達せず、無料 tier も置かず、必要なキャパシティは **データセンターとの revenue-share 提携**で増やしています。最初の外部資金は **2024年5月の $20M seed** でした。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))
- **ローンチ時のチーム人数**  
  公開情報から確認できる立ち上げチームは **共同創業者2名** です。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))
- **traction獲得までの期間**  
  Reddit で集めた β テスターがそのまま最初の有料顧客になり、**9ヶ月で $1M revenue** に到達しています。2024年5月時点で **100,000 developers**、2026年1月時点で **500,000 developers** に拡大しました。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))
- **最初のユーザー獲得**  
  コアは **Reddit投稿 → Discord/サポート導線 → founder support** です。後に Dell Technologies Capital の Radhika Malik も Reddit 経由で発見し、Hugging Face共同創業者 Julien Chaumond も **support chat** から接触しています。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))
- **1/3/6ヶ月 users/MRR**  
  **非公開**。ただし strongest public datapoint は **9ヶ月で $1M revenue** です。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

**示唆**  
Runpod の本質は、**「最初のGPUを買う」のではなく、既に持っていたGPUを“実需に合わせて転用”した**ことと、**無料クレジットをばら撒くのではなく、フィードバック付き無料提供**にしたことです。 ([reddit.com](https://www.reddit.com/r/deeplearning/comments/t8atpp))

---

### 2) Vast.ai
- **ローンチ前に何をしていたか**  
  公式 About によれば、Jake Cannell と Christian Horne は **2016–2017 の約2年間**、ホスト onboarding、検索UI、価格エンジン、Docker ベースの instance management を2人で作り込みました。公式タイムライン上のプロダクト launch は **2018年9月** です。 ([vast.ai](https://vast.ai/about))
- **ローンチ時の資金**  
  公開情報では、立ち上げ時は **bootstrapped** と見るのが自然です。外部調達の確認できる最初のラウンドは **2024年7月の $4M seed** です。 ([vast.ai](https://vast.ai/about))
- **ローンチ時のチーム人数**  
  公開ソース上の立ち上げチームは **共同創業者2名** です。 ([vast.ai](https://vast.ai/about))
- **最初の供給者（GPUホスト）をどう集めたか**  
  公式には、ローンチは **friends & family + Hacker News**、別の公式発言では **friends & family + Reddit** とされています。つまり最初の供給は、既存ネットワーク由来のホストが中心だったと読むのが妥当です。2019年には **early independent hosts** が参加して marketplace が検証されたと明記されています。 ([vast.ai](https://vast.ai/about))
- **traction獲得までの期間**  
  2018年9月 launch の翌 **2019年** に「first hosts, first traction」。2024年5月には **350+ independent hosts / 17,000+ GPUs**、かつ **2019年以来平均 265% YoY growth** と発表しています。 ([vast.ai](https://vast.ai/about))
- **1/3/6ヶ月 users/MRR**  
  **非公開**。 ([vast.ai](https://vast.ai/about))

**示唆**  
Vast.ai は、Runpod と違って **最初から “demand” だけでなく “supply” の設計を先に作った**ケースです。P2P/marketplace 型なら、**host onboarding と pricing engine が MVP の中核**になります。 ([vast.ai](https://vast.ai/about))

---

### 3) Lightning AI（旧 Grid.ai）
- **ローンチ前に何をしていたか**  
  William Falcon は **2015年に PyTorch Lightning を OSS として開始**。BCV によると、OSS は **2ヶ月で 2,800+ GitHub stars / 65,000 downloads**、**1年弱で hundreds of thousands downloads per month** まで伸びました。会社は **2019年に Luis Capelo と創業**し、Grid を private beta で出し始めています。 ([baincapitalventures.com](https://baincapitalventures.com/insight/lightning-doesnt-strike-twice/))
- **OSSコミュニティからどうプラットフォーム化したか**  
  2020年時点で Falcon は「Lightning を core にして Grid サービス化する」と説明しており、**private beta** の段階で **$18.6M Series A** を調達。2021年6月には「Grid を数ヶ月前にローンチし、PyTorch Lightning コミュニティから強い反応を得た」と書いています。さらに docs 自体を OSS 化して、ユーザー例の投稿を受ける設計にしました。 ([techcrunch.com](https://techcrunch.com/2020/10/08/grid-ai-raises-18-6m-series-a-to-help-ai-researchers-and-engineers-bring-their-models-to-production/))
- **ローンチ時の資金**  
  **2020年10月に $18.6M Series A**。しかも TechCrunch では **pre-launch で lead した**と投資家が語っています。 ([techcrunch.com](https://techcrunch.com/2020/10/08/grid-ai-raises-18-6m-series-a-to-help-ai-researchers-and-engineers-bring-their-models-to-production/))
- **ローンチ時のチーム人数**  
  ここはユーザーの「少人数」とはズレます。2020年10月時点で **25 employees** でした。創業時は2人ですが、プロダクト launch 時点ではすでに 1–5人ではありません。 ([techcrunch.com](https://techcrunch.com/2020/10/08/grid-ai-raises-18-6m-series-a-to-help-ai-researchers-and-engineers-bring-their-models-to-production/))
- **初期ユーザー獲得**  
  実質、**PyTorch Lightning OSS コミュニティが distribution** でした。hundreds of companies で Lightning が使われ、そこから Grid へ隣接展開しています。 ([baincapitalventures.com](https://baincapitalventures.com/insight/lightning-doesnt-strike-twice/))
- **1/3/6ヶ月 users/MRR**  
  **非公開**。代替指標は OSS downloads。 ([baincapitalventures.com](https://baincapitalventures.com/insight/lightning-doesnt-strike-twice/))

**示唆**  
Lightning AI は、**“先に OSS で category を取ってから platform を載せる”**王道パターンです。少人数で始まったが、プロダクト launch までに組織化・資金化が先に進んだ例です。 ([baincapitalventures.com](https://baincapitalventures.com/insight/lightning-doesnt-strike-twice/))

---

## AI DevTools

### 4) Cursor
- **ローンチ前に何をしていたか**  
  Anysphere は **2022年に MIT の4人**で創業。Cursor の changelog では **2023年3月30日**時点で「ログイン必須AI」「OpenAI API key 持ち込み」があり、**2023年4月6日**には **CodeMirror から VSCodium fork へ移行**して「AI pair-programming 向け IDE」に舵を切っています。TechCrunch でも、当初から **bug finding/fixing と codebase Q&A** に注力していたと説明されています。 ([techcrunch.com](https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/))
- **ローンチ時の資金**  
  **2023年10月に $8M seed**、総調達額は **$11M**。つまり seed 前に約 **$3M pre-seed** があった計算です。 ([techcrunch.com](https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/))
- **ローンチ時のチーム人数**  
  **創業4人**です。 ([techcrunch.com](https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/))
- **traction獲得までの期間**  
  2024年4月時点の revenue は **$4M annualized ARR**、2024年8月には **40,000 customers** と **$60M Series A**、2024年10月には **$4M/month = $48M ARR**、**2025年1月には $100M+ recurring revenue**、**2025年6月には $500M+ ARR** を公表しています。 ([techcrunch.com](https://techcrunch.com/2024/12/19/in-just-4-months-ai-coding-assistant-cursor-raised-another-100m-at-a-2-5b-valuation-led-by-thrive-sources-say/))
- **最初のユーザー獲得**  
  公開情報を見る限り、**freemium / bottom-up PLG** が主戦略です。明確な最初の 1チャネルは公表されていませんが、Series A 時点で 40,000 customers、a16z 投資文脈でも **thousands of users signed up and many started paying** とされており、営業先行ではなくプロダクト先行です。 ([cursor.com](https://cursor.com/blog/series-a))
- **1/3/6ヶ月 users/MRR**  
  **非公開**。最初期の明示数値は 2024年4月 ARR ランレートです。 ([techcrunch.com](https://techcrunch.com/2024/12/19/in-just-4-months-ai-coding-assistant-cursor-raised-another-100m-at-a-2-5b-valuation-led-by-thrive-sources-say/))

**Cursor のポイント**  
Cursor は「IDE を fork して surface を自分で持つ」選択を早くしたのが大きいです。**extension ではなく editor を押さえた**ことで、AI workflow 全体を設計できています。 ([cursor.com](https://www.cursor.com/changelog/v0-2-0-introducing-cursor-0-2-0-2023-04-06-))

---

### 5) Bolt.new
- **ローンチ前に何をしていたか**  
  Bolt.new の爆発は突然に見えますが、前史は長いです。StackBlitz は **2017年以来** browser IDE を作り、**2022年には月間 200万人超の開発者**が使っていました。Bolt の原型は **2024年2月**には試作されたものの、当時のモデルでは成立せず棚上げ。**2024年6月に Claude 3.5 Sonnet の early access** を得て成立し、**約90日で** product 化して **2024年10月**にローンチしました。 ([blog.stackblitz.com](https://blog.stackblitz.com/posts/seed-funding/))
- **ローンチ時の資金**  
  Bolt 専用の新規調達は launch 時点ではなく、親会社 StackBlitz は **2022年に $7.9M seed** を調達済み、Bolt launch 後の **2025年1月に $83.5M 調達交渉** が報じられています。つまり Bolt は **既存会社のキャッシュと技術基盤で launch** したケースです。 ([blog.stackblitz.com](https://blog.stackblitz.com/posts/seed-funding/))
- **ローンチ時のチーム人数**  
  founder interview では、爆発時のチームは **12 people** とされています。 ([worldofdaas.com](https://www.worldofdaas.com/p/bolt-new-eric-simons))
- **traction獲得までの期間**  
  Anthropic の顧客事例では **4週間で $4M ARR**、**tens of thousands of new customers**。Eric Simons の後日の発言では **first month $4M ARR / second month $20M ARR / 5ヶ月で $40M ARR** です。 ([anthropic.com](https://www.anthropic.com/customers/stackblitz))
- **最初のユーザー獲得**  
  founder interview では明確に **word of mouth** とされています。StackBlitz の既存開発者コミュニティ、ViteConf 文脈、SNS上の demo 拡散が主要因です。 ([blog.stackblitz.com](https://blog.stackblitz.com/posts/viteconf-2024-recap/))
- **1/3/6ヶ月 users/MRR**  
  - **1ヶ月:** **$4M ARR**、tens of thousands of paying customers。 ([anthropic.com](https://www.anthropic.com/customers/stackblitz))
  - **3ヶ月:** primary sourceでは厳密非公開。近い公表値として **2ヶ月で $20M ARR**。 ([worldofdaas.com](https://www.worldofdaas.com/p/bolt-new-eric-simons))
  - **6ヶ月:** primary sourceでは厳密非公開。近い公表値として **5ヶ月で $40M ARR**。 ([worldofdaas.com](https://www.worldofdaas.com/p/bolt-new-eric-simons))

**Bolt の本質**  
Bolt は「launch 前に何をしていたか」の答えが明確で、**7年かけて WebContainers を作っていた**、です。AI そのものではなく、**AI が動いた瞬間に勝てる土台**を作っていた。 ([blog.stackblitz.com](https://blog.stackblitz.com/posts/seed-funding/))

---

### 6) Lovable（旧 GPT Engineer）
- **ローンチ前に何をしていたか**  
  Lovable の源流は Anton Osika の **OSS「GPT Engineer」** です。公式には、**OSS が先にバズり、それが product 化の起点**になったとされています。しかも初期に **2回の failed launch** があり、3回目で「プロトタイプ用ツール」ではなく「**本番に近い full product builder**」へ軸足を置き、**Supabase 連携**・**ブランド再設計**・**Product Hunt / X / content / partner co-marketing** をやって PMF に当てています。 ([lovable.dev](https://lovable.dev/pt-br/blog/company-news/2025-01-29-zero-to-10m-arr-in-2-months))
- **ローンチ時の資金**  
  **2024年10月に €6.8M pre-seed** を調達。**2025年2月に $15M pre-Series A**。TechCrunch によると、2025年2月時点の **$17M ARR / 30,000 paying / 500,000 users** は **“only $2M spent”** で達成しています。 ([techcrunch.com](https://techcrunch.com/2025/02/25/swedens-lovable-an-app-building-ai-platform-rakes-in-16m-after-spectacular-growth/))
- **ローンチ時のチーム人数**  
  厳密な day-1 headcount は非公開。ただし公式 funding post では、**“in just a few months, our 15-person team”** とあり、初期フェーズがかなり lean だったのは確実です。 ([lovable.dev](https://lovable.dev/pt/blog/fundraise-series-a-announcement))
- **正式ローンチ日**  
  公式 1-year post から逆算すると **2024年11月18日** launch です。 ([lovable.dev](https://lovable.dev/pt-br/blog/one-year-of-lovable))
- **traction獲得までの期間**  
  公式には **2ヶ月で $10M ARR**、2025年2月時点で **$17M ARR / 30k paying / 500k users**、2025年5月時点で **$50M ARR**、2025年7月時点で **$100M ARR / 2.3M active users / 180k paying subscribers**、2025年11月に **$200M ARR**。 ([lovable.dev](https://lovable.dev/pt-br/blog/company-news/2025-01-29-zero-to-10m-arr-in-2-months))
- **最初のユーザー獲得**  
  公式が明示しているのは、**Product Hunt**、**X**、**quality content**、**Supabase などとの co-marketing**、そして既存 OSS コミュニティからの転換です。TechCrunch でも **Product Hunt と Hacker News の front page** を取ったとあります。 ([lovable.dev](https://lovable.dev/pt-br/blog/company-news/2025-01-28-lovables-two-failed-launches-and-what-we-got-wrong-about-plg))
- **1/3/6ヶ月 users/MRR**  
  - **1ヶ月:** 非公開。  
  - **約3ヶ月（2025年2月）:** **500k users / 30k paying / $17M ARR**。 ([techcrunch.com](https://techcrunch.com/2025/02/25/swedens-lovable-an-app-building-ai-platform-rakes-in-16m-after-spectacular-growth/))
  - **約6ヶ月（2025年5月）:** **$50M ARR**。 ([techcrunch.com](https://techcrunch.com/2025/07/02/lovable-on-track-to-raise-150m-at-2b-valuation/))

**Lovable の本質**  
Lovable は、**OSSバズ → product化 → 2回失敗 → branding/integration/distribution をやり直して爆発**、という非常に再現性のある学びを出しています。 ([lovable.dev](https://lovable.dev/pt-br/blog/company-news/2025-01-29-zero-to-10m-arr-in-2-months))

---

### 7) Replicate
- **ローンチ前に何をしていたか**  
  Replicate は **2019年創業**、Ben Firshman と Andreas Jansson の **2 founders**。最初の iteration は **Cog / “ML版Fig” 的な reproducibility ツール**でしたが、研究者は継続利用が弱く、初期の open-source AI hacker コミュニティへ pivot します。Ben は Latent Space で、**2021年初頭の CLIP+GAN / Discord / Eleuther 周辺**に「早期コミュニティ」を見つけ、そこ向けに作り始めたと話しています。 ([ycombinator.com](https://www.ycombinator.com/companies/replicate))
- **ローンチ時の資金**  
  prototype は YC 応募用に作り、Cloudflare を day one から使っていたと後に書いています。public “out of stealth” は **2023年2月**で、その時点の累計調達は **$17.8M**（**$12.5M Series A + undisclosed seed**）です。外部報道では earlier seed は **$5.3M** とされています。 ([replicate.com](https://replicate.com/blog/replicate-cloudflare/))
- **ローンチ時のチーム人数**  
  創業時は **2人**。 ([ycombinator.com](https://www.ycombinator.com/companies/replicate))
- **最初のユーザー獲得**  
  最初の real community は **Discord の open-source image model hackers**。mid-2021 の **Pixray** が初期の代表モデルで、Replicate blog でも **“first text-to-image model on Replicate that reached tens of thousands of runs by early 2022”** とされています。最初の有料顧客は、内部APIを reverse engineer したユーザーにドキュメントを渡したところ、**月 ~$1,000 規模**で払ってくれたケースでした。そこから紹介も生まれています。 ([replicate.com](https://replicate.com/blog/painting-with-words-a-history-of-text-to-image-ai))
- **traction獲得までの期間**  
  founder transcript では **“two years to the first paying customer”**。その後、**Stable Diffusion（2022）** と **Llama 2（2023）** が最大の成長波となり、2023年12月時点で **2M signups / 30,000 paying customers** まで拡大しました。 ([latent.space](https://www.latent.space/p/replicate))
- **1/3/6ヶ月 users/MRR**  
  **非公開**。ただし初期マイルストーンとしては **mid-2021 Pixray**、**early-2022 tens of thousands of runs**、**2023年末 30k paying** が確認できます。 ([replicate.com](https://replicate.com/blog/painting-with-words-a-history-of-text-to-image-ai))

**Replicate の本質**  
Replicate は、**研究者向けの“正しそうなプロダクト”から、ハッカー向けの“毎日使われるプロダクト”へ pivot** したのが決定打です。 ([latent.space](https://www.latent.space/p/replicate))

---

## 日本の少人数 DevTools / インフラ系

### 8) MagicPod（日本の DevTools 事例）
- **ローンチ前に何をしていたか**  
  創業者 Nozomi Ito はもともと test automation のコンサル/受託をしており、「Selenium を簡単に使えない日本企業が多い」ことから no-code 化に賭けました。**Version 0.1 は 2017年7月**に日本でローンチ。 ([techcrunch.com](https://techcrunch.com/2023/10/30/japans-magicpod-takes-its-no-code-testing-platform-global/))
- **ローンチ時の資金**  
  最初期は公表されておらず、後から確認できる最初の調達は **2021年7月の 3000万円（約 $2.4M）** です。 ([magicpod.com](https://magicpod.com/en/news/press-release/Version1/))
- **チーム人数**  
  立ち上げ当初の正確な headcount は公開されていません。ただし 2023年10月時点で **23 employees**。創業者中心のかなり小さい立ち上がりだったことは分かります。 ([techcrunch.com](https://techcrunch.com/2023/10/30/japans-magicpod-takes-its-no-code-testing-platform-global/))
- **初期ユーザー獲得**  
  Selenium / Appium の既存コミュニティと専門性が distribution になっています。Ito 自身が **Japan Selenium User Community** や **SeleniumConf Tokyo 2019** の文脈を持っていました。 ([techcrunch.com](https://techcrunch.com/2023/10/30/japans-magicpod-takes-its-no-code-testing-platform-global/))
- **traction**  
  2023年10月時点で **500+ companies** が導入。 ([techcrunch.com](https://techcrunch.com/2023/10/30/japans-magicpod-takes-its-no-code-testing-platform-global/))
- **1/3/6ヶ月 users/MRR**  
  **非公開**。 ([magicpod.com](https://magicpod.com/en/news/press-release/Version1/))

---

### 9) Kibela（日本の少人数立ち上げの好例）
- **ローンチ前に何をしていたか**  
  Kibela はクックパッドの社内ツール文化を外部化したもので、創業者 井原氏が **まず1人で開発**を開始。**2016年5月の teaser site** で **数百チーム登録**、**2016年8月 beta**、**2017年3月正式版**という流れです。 ([techcrunchjapan.com](https://techcrunchjapan.com/2018/06/18/bitjourney-fundraising/))
- **ローンチ時の資金**  
  かなり後ろまで自己資本寄りで進め、最初の公表資金調達は **2018年6月の約 5,500万円**。 ([prtimes.jp](https://prtimes.jp/main/html/rd/p/000000006.000024220.html))
- **チーム人数**  
  2018年6月時点で、**正社員エンジニア2名 + 創業者 + 業務委託数名**、開発に関わる人数は **約8名**。それ以前は実質ソロ創業です。 ([blog.kibe.la](https://blog.kibe.la/entry/2018/06/28/114716))
- **初期ユーザー獲得**  
  teaser 段階で数百チームが登録しており、最初は **Tech系の小規模チーム** から入っています。無料枠（5ユーザーまで無料）もあり、PLG 的です。 ([techcrunchjapan.com](https://techcrunchjapan.com/2018/06/18/bitjourney-fundraising/))
- **traction**  
  **2018年6月時点で数千チーム利用**。 ([prtimes.jp](https://prtimes.jp/main/html/rd/p/000000006.000024220.html))
- **1/3/6ヶ月 users/MRR**  
  **非公開**。ただし teaser→beta→正式版の各段階で、**数百チーム→数千チーム** と伸びたのは確認できます。 ([techcrunchjapan.com](https://techcrunchjapan.com/2018/06/18/bitjourney-fundraising/))

**日本の結論**  
日本でも少人数 DevTools 立ち上げ事例はありますが、**米欧ほど 1/3/6ヶ月の revenue 指標を公開しない**傾向が強いです。公開度が高い early case としては **MagicPod / Kibela** が扱いやすいです。 ([magicpod.com](https://magicpod.com/en/news/press-release/Version1/))

---

# 2. 共通パターンの抽出

## ローンチ前の共通行動
かなり高頻度で出てくるのは次の5つです。

1. **OSSか、OSSに近い配布物を先に出す**  
   PyTorch Lightning、GPT Engineer、Cog が典型です。 ([baincapitalventures.com](https://baincapitalventures.com/insight/lightning-doesnt-strike-twice/))
2. **コミュニティで β を取る**  
   Runpod は Reddit、Vast は HN/Reddit、Lovable は Product Hunt / HN / X、Replicate は Discord です。 ([reddit.com](https://www.reddit.com/r/deeplearning/comments/t8atpp))
3. **“1つの強い unlock” を待つ / 活かす**  
   Claude 3.5 Sonnet（Bolt）、Stable Diffusion / Llama 2（Replicate）、Supabase integration（Lovable）がそれです。 ([anthropic.com](https://www.anthropic.com/customers/stackblitz))
4. **Founder 自身を first user にする**  
   Cursor は daily-use IDE 化、Bolt も自社で codegen tools を使い倒しています。 ([cursor.com](https://www.cursor.com/changelog/v0-2-0-introducing-cursor-0-2-0-2023-04-06-))
5. **インフラ会社でも最初から“売り方”を実装している**  
   Runpod は support/Discord、Vast は host onboarding/price engine、Replicate は internal API → doc化 → billing で最初の商売を作りました。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

---

## 初期資金の中央値
私の集計では、**“launch 時点または pre-launch 時点の外部資金が明確なケース”**を並べると、

- Runpod: **$0 external**
- Vast.ai: **$0 external**
- Cursor: **約 $3M pre-seed 相当（$11M total - $8M seed）**
- Lightning/Grid: **$18.6M**
- Lovable: **€6.8M pre-seed**
- Replicate: **$5.3M seed（後追い公表ベース）**
- MagicPod: **$0 公開**
- Kibela: **$0 公開**
- Bolt.new: **$0 incremental（既存 StackBlitz 資産で launch）**

となり、**全体の中央値は実質 $0**、つまり **“最初の launch は外部資金なし”** が多数派です。  
ただし **VC-backed launch のみ**に絞ると、中央値は **だいたい $6M 前後**です。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

**解釈**  
少人数で勝つ会社は、**資金を集めてから launch するより、何かしらの配布/技術/コミュニティ資産を作ってから launch する**ほうが多いです。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

---

## ローンチから traction までの期間
“traction” の定義を各社の最初の公表マイルストーン（$1M revenue、$10M ARR、数千/数万顧客など）でざっくり揃えると、**全体の rough median は約 12ヶ月**です。  
ただしこれは **二極化** しています。

- **2024年の vibe-coding / AI app cohort**（Bolt, Lovable）は **1–2ヶ月**で爆発。 ([anthropic.com](https://www.anthropic.com/customers/stackblitz))
- **OSS/infra 変換型**（Replicate, Kibela, Lightning）は **1年〜2年**かけて monetization が立ち上がることがあります。 ([latent.space](https://www.latent.space/p/replicate))

**つまり median だけ見ると危険**で、実際には  
- **AI app / devtool 表層** = 速い  
- **infra / OSS → platform** = 遅い  
です。 ([anthropic.com](https://www.anthropic.com/customers/stackblitz))

---

## 最初の100人をどう集めたか
共通パターンはほぼこれです。

- **手で集める 10–20人**  
  Reddit / Discord / HN / OSS users / Product Hunt の反応者を直接拾う。 ([reddit.com](https://www.reddit.com/r/deeplearning/comments/t8atpp))
- **使い方を決めるテンプレを見せる**  
  Runpod の free GPU、Bolt の prompt→app、Lovable の Supabase 連携、Replicate の stable diffusion API など。 ([reddit.com](https://www.reddit.com/r/deeplearning/comments/t8atpp))
- **ユーザーの成果物が marketing asset になる設計**  
  Bolt/Lovable は作ったアプリ自体がシェアされる。 Replicate は作例モデルが増える。 Lightning は examples/docs が増える。 ([anthropic.com](https://www.anthropic.com/customers/stackblitz))
- **founder support を高速で回す**  
  Bolt は大量の support mail、Runpod は Discord/Reddit、Lovable は community/Discord。 ([worldofdaas.com](https://www.worldofdaas.com/p/bolt-new-eric-simons))

---

# 3. AIXS への具体的示唆（3人チーム・$500K seed 前提）

## 結論
**3人・$500K なら、platform を作るのではなく “1つの熱い wedge を作る” のが正解**です。  
上の事例で最初から platform 全体を勝った会社はなく、みな最初は狭い入口でした。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

### AIXS が学ぶべきこと
1. **launch 前に distribution asset を必ず1つ持つ**  
   OSS、テンプレ、waitlist、Discord、Reddit/HN の常連ポジション、どれでもいいので1つ。  
2. **初期の課金は“本番利用者”だけに絞る**  
   Runpod のように infra コストが重いなら、無料 tier より **feedback 付き credits** のほうが健全。  
3. **support は founder job と割り切る**  
   最初の 50–100人までは support が最重要の growth loop。  
4. **1つの integration を早く握る**  
   Lovable の Supabase、Bolt の Claude、Cursor の VS Code fork、Replicate の Stable Diffusion/Llama2 が伸びたのはここ。  
5. **日本発でも docs は英語先行気味が有利**  
   MagicPod も global push のために英語化を後追いで入れています。最初から英語 docs がある方が再現性が高いです。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

---

## ローンチまでに最低限やるべき5つ
### 1. “誰のどの5分を消すか” を1文で言えるようにする
例:
- 「SRE が○○を手でやる5分を消す」
- 「PM が prototype を作るまでの3日を15分にする」
- 「ML engineer が GPU/モデル起動で詰まる2時間を5分にする」

この level まで削ると、Runpod/Bolt/Lovable 型の口コミが起きやすいです。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

### 2. 10社ではなく “10人の design partners” を取る
会社単位ではなく、毎週触ってくれる個人を取る。Runpod の beta testers、Replicate の early hacker community がこれです。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

### 3. 公開できる artifact を1つ用意する
- OSS repo
- template
- sample workflow
- live demo
- benchmark script

Lightning, GPT Engineer, Cog, StackBlitz は全部これを先に持っていました。 ([baincapitalventures.com](https://baincapitalventures.com/insight/lightning-doesnt-strike-twice/))

### 4. 課金ロジックを先に決める
Bolt は最初の $9 プランが危険で、48時間で pricing を直しています。Launch 前に  
- 原価  
- 粗利  
- ヘビーユーザーの赤字化ライン  
は必須です。 ([worldofdaas.com](https://www.worldofdaas.com/p/bolt-new-eric-simons))

### 5. ローンチ先を1つに絞る
最初から全方位に打つより、  
- Reddit
- Hacker News
- Product Hunt
- X
- Discord
のどこか **1つ**で勝つほうが良いです。 ([reddit.com](https://www.reddit.com/r/deeplearning/comments/t8atpp))

---

## ローンチ初週にやるべきこと
### Day 1
- 1本の明確な launch post
- 3つの実例（動画/スクショ/テンプレ）
- CTA は1つ（waitlist ではなく「使う」か「相談」）

### Day 2–3
- 触ったユーザー全員に founder が返信
- 失敗ログを手で見る
- “どこで詰まったか” を 10件単位で整理

### Day 4–7
- pricing/UX/onboarding を即修正
- 使われた事例を再投稿
- コミュニティ内の champion を見つける

Bolt, Runpod, Lovable は、**launch をイベントではなくサポート週間**として扱っていたのが強いです。 ([worldofdaas.com](https://www.worldofdaas.com/p/bolt-new-eric-simons))

---

## 最初の10人をどう獲得するか
### もっとも再現性が高い順
1. **既存コミュニティで credits / concierge onboarding 提供**  
   Runpod 型。 ([reddit.com](https://www.reddit.com/r/deeplearning/comments/t8atpp))
2. **OSS users を product users に変換**  
   Lovable / Lightning / Replicate 型。 ([lovable.dev](https://lovable.dev/pt-br/blog/company-news/2025-01-29-zero-to-10m-arr-in-2-months))
3. **既存ワークフローへの integration を front に出す**  
   Supabase / VS Code / GitHub / Docker 的な既存 surface。 ([lovable.dev](https://lovable.dev/blog/company-news/2025-01-13-rebranding-gpt-engineer-to-lovable))
4. **“実際に作れたもの” を user-generated content にする**  
   Bolt / Lovable 型。 ([anthropic.com](https://www.anthropic.com/customers/stackblitz))

**実務的には**  
- 10人中 5人は自分で DM  
- 3人はコミュニティ反応者  
- 2人は友人/既存ネットワーク  
くらいで十分です。上手くいく会社はここで ads を使っていません。 ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

---

## 最初の100人をどう獲得するか
100人までは、だいたいこの順番です。

### フェーズ1: 10 → 30
- founder-led onboarding
- 週1で user interview
- issue を public changelog で返す

### フェーズ2: 30 → 60
- best use case をテンプレ化
- チュートリアル/動画を増やす
- champion user を前に出す

### フェーズ3: 60 → 100
- referral / affiliate / ambassador を入れる
- integration partner と co-marketing
- 事例記事を量産

Lovable は Supabase 連携、Runpod は Reddit→Discord、Replicate は model publisher → builder の両面市場、Bolt は user demo の拡散が効いています。 ([lovable.dev](https://lovable.dev/pt-br/blog/company-news/2025-01-28-lovables-two-failed-launches-and-what-we-got-wrong-about-plg))

---

# 4. かなり短い総括

**最も重要な学びはこれです。**

- **small team で勝った会社は、launch 前に code だけでなく distribution を作っていた。**
- **最初の顧客は paid ads ではなく community から来ている。**
- **初期資金の中央値は surprisingly low で、むしろ $0 launch が多い。**
- **でも traction は二極化していて、2024年の AI app/devtools は 1–2ヶ月、OSS/infra は 1–2年も普通。**
- **AIXS が 3人/$500K なら、platform を夢見るより “1 workflow を圧倒的に速くする” で入るべき。** ([runpod.io](https://www.runpod.io/blog/a-note-to-the-developers-who-built-runpod-with-us/))

必要なら次に、
1. **この内容をスプレッドシート形式**に整理する  
2. **AIXS向けに 30日ローンチ計画**へ落とす  
3. **各社のソースURL一覧だけ抜き出す**  
のどれかをやります。