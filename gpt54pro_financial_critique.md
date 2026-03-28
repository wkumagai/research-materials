# GPT-5.4-pro 財務モデル批判的レビュー
Model: gpt-5.4-pro
調査日: 2026-03-28

---

## Query 1: GPU Cloud Startup Financial Benchmarks

以下、**調査基準日を 2026年3月28日**として整理します。  
**開示値**はそのまま、**未開示項目は「推定」**と明記します。

## 1) RunPod の財務データ

- **ARR（最新）:** **$120M+**。Runpod が **2026年1月20日**に公式発表しています。 ([runpod.io](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr))
- **成長率:** **+90% YoY**（公式発表の revenue growth）。 ([runpod.io](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr))
- **チーム人数:** **約90人**。CEO Zhen Lu の LinkedIn 投稿で「2人から90人へ成長」と記載。 ([linkedin.com](https://www.linkedin.com/company/runpod-io))
- **調達額:** **$20M seed**（公表ベース）。**2024年5月**に Intel Capital / Dell Technologies Capital 主導で調達。 ([runpod.io](https://www.runpod.io/changelog-entries/may-2024))
- **ユーザー数:** **50万人超の developers**。 ([runpod.io](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr))
- **ARPU（推定）:** **$240/年**（= **$20/月**）/登録developer。計算は **$120M ARR ÷ 500k developers**。  
  ※これは**登録developerベース**なので、**課金ユーザーARPUはこれよりかなり高い**はずです。 ([runpod.io](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr))
- **粗利率（推定）:** **15%–25%**。理由は、Runpod は **Community Cloud** で外部ホストのGPUを使う資産ライト部分を持つ一方、**Secure Cloud** は自前/提携DC側の経済性に近く、同社の現行H100価格帯だけで見るとGPU単体粗利は低めだからです。Community Cloud の存在は公式ブログで確認でき、Secure Cloud はT3/T4 DCへ拡張中です。 ([runpod.io](https://www.runpod.io/blog/an-update-on-the-community-cloud-hosting-application-process))

## 2) Modal の財務データ

- **評価額（確定済み最新）:** **$1.1B post-money**。**2025年9月29日**の Series B 公式発表。 ([modal.com](https://modal.com/blog/announcing-our-series-b))
- **評価額（報道ベース最新）:** **約$2.5B**。**2026年2月11日**時点で TechCrunch が「その条件で増資交渉中」と報道。**未クローズ**です。 ([techcrunch.com](https://techcrunch.com/2026/02/11/ai-inference-startup-modal-labs-in-talks-to-raise-at-2-5b-valuation-sources-say/))
- **ARR（推定）:** **約$50M**。同じく TechCrunch の報道ベース。 ([techcrunch.com](https://techcrunch.com/2026/02/11/ai-inference-startup-modal-labs-in-talks-to-raise-at-2-5b-valuation-sources-say/))
- **チーム人数:** **112人**（LinkedIn 表示ベースの headcount proxy）。LinkedIn では company size は **51–200**。 ([linkedin.com](https://www.linkedin.com/company/modal-labs))
- **粗利率（推定）:** **30%–40%**。Modal の現行 H100 価格は **$0.001097/秒 = 約$3.95/時**で、後述のH100原価モデルを当てると**約36%粗利**になります。 serverless / autoscaling のソフトウェア付加価値を考えると、このレンジが妥当です。 ([modal.com](https://modal.com/pricing))

## 3) CoreWeave の財務データ

- **売上（2025）:** **$5.131B**。**2026年2月26日**の FY2025 結果発表。 ([investors.coreweave.com](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results))
- **営業利益率（GAAP）:** **-1%**（営業損失 **$46M** / 売上 **$5.131B**）。 ([investors.coreweave.com](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results))
- **営業利益率（Adjusted）:** **13%**。 ([investors.coreweave.com](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results))
- **粗利率について:** あなたの提示した **「35%」は一次資料では確認できませんでした**。  
  - FY2025 の公式 line items をそのまま使う標準的な **(Revenue - Cost of revenue) / Revenue** だと **71.7%**。  
  - もし **Technology & infrastructure** も直接原価に含める “delivery margin” 的な見方をすると **14.6%**。  
  つまり CoreWeave は**原価の定義で見え方が大きく変わる会社**です。 ([investors.coreweave.com](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results))

## 4) Lambda Labs の財務データ

- **ARR / annualized revenue run-rate（推定）:** **$500M+**。Sacra は **2025年5月時点で $500M revenue run-rate** と推定。 ([sacra.com](https://sacra.com/c/lambda-labs/))
- **チーム人数:** **約750人**（LinkedIn の “Discover all 750 employees” ベース）。LinkedIn company size は **501–1,000**。 ([linkedin.com](https://www.linkedin.com/company/lambda-cloud))
- **粗利率（推定）:** **20%–30%**。  
  Lambda の公式価格では、H100 は  
  - **1-Click Clusters: $2.76/hr**  
  - **Instances: $3.29–$4.29/hr**。  
  後述モデルではこの価格帯は **約9%〜43%** のGPU単体粗利に対応するため、売上ミックスを考えた会社全体の粗利は **20%–30%** を置くのが自然です。 ([lambda.ai](https://lambda.ai/pricing))

## 5) Vast.ai の財務データ

- **ARR（推定）:** **少なくとも $12M run-rate**。Vast.ai は **2026年3月5日**に「**revenue crossed seven figures per month for the first time**」と公式記載しているため、**最低でも $1M/月 × 12 = $12M/年**です。  
  → したがって、あなたの挙げた **$2.2M** は**古い推定値**で、最新の公式データとは整合しません。 ([vast.ai](https://vast.ai/article/ramp-brex-fastest-growing-vendor))
- **ユーザー数:**  
  - **120,000+ customers**（**2024年12月10日**の公式プレス） ([vast.ai](https://vast.ai/press-release/vast-ai-adds-virtual-machine-support-gpu-rental))  
  - **100,000+ users** と **14,000+ monthly active paying customers**（**2026年3月5日**の公式ブログ） ([vast.ai](https://vast.ai/article/ramp-brex-fastest-growing-vendor))  
  実務上は、**最新KPIとしては 14,000+ paying customers** を重視すべきです。 ([vast.ai](https://vast.ai/article/ramp-brex-fastest-growing-vendor))
- **手数料率:** **25%**。FAQで「hosts receive 75%, Vast.ai keeps 25%」と明記。 ([console.vast.ai](https://console.vast.ai/faq))

## 6) 研究者向けSaaSのベンチマーク

**注:** 研究者向けSaaSそのものの公開ベンチは薄いので、ここでは **self-serve の technical / developer-tool 型SaaS** を proxy にしています。

- **月次 churn rate 中央値:** **4.2%**（Developer Tools）。 ([revmine.ai](https://revmine.ai/blog-churn-benchmarks))
- **ARPU 中央値:** **$29/月**（Developer Tools）。 ([proven-saas.com](https://proven-saas.com/benchmarks/cac-payback-benchmarks))
- **フリーミアム転換率 中央値（proxy）:** **約5%**。OpenView の PLG benchmark では freemium は **5%**、2026年の ChartMogul/ProductLed 連携調査でも freemium self-serve は概ね **5%前後**です。 ([openviewpartners.com](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks/))
- **LTV 中央値（推定）:** **約$560**。  
  計算は **ARPU $29 × Subscription gross margin 81% ÷ monthly churn 4.2%**。 ([proven-saas.com](https://proven-saas.com/benchmarks/cac-payback-benchmarks))
- **CAC 中央値:** **$248 / customer**（Developer Tools）。 ([proven-saas.com](https://proven-saas.com/benchmarks/cac-payback-benchmarks))

## 7) GPUクラウドのユニットエコノミクス実態（H100 1台）

### 前提
- **H100の市場価格前提（推定）:** Epoch AI の整理では、**2025年のH100価格レンジは $22k–$30k、幾何平均 $25.6k**。また、8-GPU H100 server は **GPU単体合計に対して約38% premium**。 ([epoch.ai](https://epoch.ai/data/ai-chip-sales-documentation))
- したがって、**サーバ込みの1GPUあたりCAPEX（推定）**は  
  **$25.6k × 1.38 = $35.3k**。 ([epoch.ai](https://epoch.ai/data/ai-chip-sales-documentation))
- **減価償却:** 3年直線で **$11,776/年**。 
- **電力前提:** DGX H100 の system power は **10.2kW max / 8 GPUs = 1.275kW per GPU-equivalent**。 ([nvidia.com](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/nvidia-dgx-h100-datasheet.pdf))
- **電力単価:** 米国 industrial average は **2025年平均 8.62¢/kWh**。 ([eia.gov](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_3))
- **コロケーション:** CBRE の primary wholesale colocation asking rate は **$196.25/kW/month**。 ([cbre.com](https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025))

### 年間コスト
- **減価償却:** **$11,776/年**。 
- **電力:**  
  - **70%稼働に合わせて比例配賦**すると **$674/年**。   
  - 参考: **24/7フル負荷上限**で見ると **$963/年**。 
- **コロケーション:** **$3,003/年**。 

### H100 1台の年間コスト（推定）
- **$15,453/年**  
  = **$11,776 減価償却 + $674 電力 + $3,003 コロケーション**。 

### H100 1台を $2.50/hr で販売、稼働率70% の年間収益
- **年間収益:** **$15,330/年**。  
  計算: **$2.50 × 24 × 365 × 70%**。 

### 粗利計算
- **年間粗利:** **-$123/年**。 
- **粗利率:** **-0.8%**。 
- **ブレークイーブン価格:** **約$2.52/hr**。  
  つまり、**$2.50/hr・70%稼働だとほぼ損益分岐**です。 

### 感度分析
- **低CAPEXケース**（GPU-only $22k 前提）だと粗利率は **+10.0%**。 
- **高CAPEXケース**（GPU-only $30k 前提）だと粗利率は **-14.0%**。 

---
**要点だけ一言でまとめると**:
- **Runpod:** ARR **$120M**, 500k users, 90人規模。  
- **Modal:** ARR **~$50M推定**, valuation は **$1.1B確定 / $2.5B報道**。  
- **CoreWeave:** 2025 revenue **$5.131B**, GAAP operating margin **-1%**、adjusted **13%**。  
- **Lambda:** annualized revenue run-rate **$500M+推定**, headcount **~750**。  
- **Vast.ai:** **$12M+ run-rate** が最新公式データに整合。  
- **H100 economics:** **$2.50/hr × 70% util はほぼブレークイーブン**。 ([runpod.io](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr))

必要なら次に、これを **CSV形式** か **投資家向けコンプ表（比較表）** に整形します。

---

## Query 2: AIXS Pricing Critique

結論から言うと、**この価格表は「全体として破綻」ではないが、かなり歪んでいます。**  
特に **Starter と Team は粗利を作りやすい一方、Power は低コスト調達と未消化前提に強く依存**しています。**Pro は「絶対赤字」ではない**ですが、H100の調達条件が少し悪化すると一気に薄利化します。なので、この案の本当の勝負所は「H100を何時間付けるか」よりも、**H100の種別（PCIe/SXM）、供給保証、オーバー利用時の課金、そして実利用の breakage（未消化）**です。 ([runpod.io](https://www.runpod.io/gpu-pricing?utm_source=openai))

まず市場価格を置きます。専門GPUクラウドでは、**Runpod**が H100 PCIe **$1.99/hr**、H100 SXM **$2.69/hr**、A100 PCIe **$1.39/hr**を掲示しています。**Hyperstack**は H100 **$1.90/hr**、H100 SXM **$2.40/hr**、A100 **$1.35/hr**です。**Lambda**の公開ページでは、H100 systems の on-demand commitment が **$2.76/hr**、さらに**2026年4月6日から有効**として 1x H100 PCIe **$3.29/hr**、H100 SXM **$4.29/hr**を表示しています。上限側の比較として、**AWS Capacity Blocks**は H100 あたり **$3.933/hr**、**Google Vertex AI**は H100 80GB **$9.7966/hr**に管理費 **$1.4695/hr**が乗ります。つまり、あなたの置いている **$2.50/hr は「激安側だが非現実ではない」**ものの、**PCIe/ベストエフォート/コミット寄り**の前提です。SXM保証やマネージド寄りに寄ると成立性はかなり落ちます。 ([runpod.io](https://www.runpod.io/gpu-pricing?utm_source=openai))

### プラン別のまずい/良いポイント
- **Starter $29 / A100 5hr** = **$5.80/A100hr**。市場の A100 は $1.35〜$1.99/hr なので、GPU原価だけで見ればかなり余裕があります。これは**重いH100プランの赤字吸収源**としては合理的です。 ([runpod.io](https://www.runpod.io/gpu-models/a100-pcie?utm_source=openai))
- **Pro $99 / H100 25hr** = **$3.96/H100hr**。これは Runpod/Hyperstack の安値H100よりは高いですが、AWSの $3.933/hr とほぼ同水準です。なので **「必ず赤字」ではない**です。 ([runpod.io](https://www.runpod.io/gpu-pricing?utm_source=openai))
- **Team $79/人 / H100 15hr** = **$5.27/H100hr**。GPU economics はむしろ健全です。問題は原価ではなく、**なぜ個人Proより時間が少ないのに、Teamに強いWTPが立つのか**の説明です。 
- **Power $299 / H100 100hr** = **$2.99/H100hr**。Runpod H100 SXM $2.69/hr に対し約 **11%** 上、Hyperstack H100 SXM $2.40/hr に対し約 **25%** 上しかなく、**SaaS・サポート・不稼働・与信コスト込みではかなり薄い**です。 ([runpod.io](https://www.runpod.io/gpu-pricing?utm_source=openai))

---

## 1. Pro $99 で H100 25hr は本当に黒字か？
**結論: 黒字化は可能。ただし「かなり良い調達」と「未消化」が前提です。** 

あなたの前提どおり **$2.50/hr** なら、$99 の売上で理論上買える H100 は **39.6時間**です。仮に非GPUの固定オーバーヘッドを **$15/月/アカウント** と置いても、損益分岐は **33.6時間**で、同梱の 25時間はまだ下です。したがって、**Pro は数理的には十分黒字になりえます。**「37%粗利しかないから危ない」というより、**25時間に対して必要な原価ハードルはまだそこまで高くない**、が正しいです。 

ただしその結論は、H100 を **Hyperstack/Runpodの安値帯**や、少なくとも Lambda の **$2.76/hr コミット帯**で調達できる場合に限ります。もし AIXS が実際には **Lambda公開の1x self-serve級（2026年4月6日から H100 PCIe $3.29、SXM $4.29）**や、それに近い保証付き在庫を使うなら、Pro の余裕はかなり消えます。つまり **Pro の採算は「H100」というラベルではなく、供給品質の定義次第**です。 ([hyperstack.cloud](https://www.hyperstack.cloud/gpu-pricing))

---

## 2. Power $299 で H100 100hr はほぼ赤字か？
**結論: 「$2.50/hr なら即赤字」は言い過ぎ。ただし、現実の市場条件では最も危険なプランです。** 

$2.50/hr なら、$299 の売上で **119.6時間**ぶんの H100 を買えます。非GPUオーバーヘッドを $15 としても損益分岐は **113.6時間**なので、100時間同梱でもまだ少し余地があります。したがって、**「$2.50/hr なのに100時間はほぼ赤字」は数式上は強すぎます。** 

しかし、現実の安値H100でも **$2.40〜$2.69/hr** が多く、ここまで来ると分岐は **105.6〜118.3時間**まで下がります。しかも100時間同梱だと、**$2.69/hr 前提ではGPU原価を引いた残りが $30**しかありません。ここからサポート・課金失敗・不稼働・製品開発を払うのは苦しいです。さらに Lambda 公開の 1x self-serve 級の **$3.99/hr 近辺**なら、分岐は **71.2時間**まで落ちます。つまり Power は、**安いPCIe在庫を十分な稼働率で回し、かつ相当数のユーザーが100時間を使い切らない**ことを前提にしたプランです。ヘビーユーザーの逆選択を受けやすい点が最大の欠点です。 ([runpod.io](https://www.runpod.io/gpu-pricing?utm_source=openai))

---

## 3. そもそも研究者は H100 を月25hr使うか？
**Google Colab も Runpod も、公開資料では平均GPU時間/ユーザーを出していません。** Google の公開資料が出しているのは **Pro $9.99 / 100 compute units**、**Pro+ $49.99 / 500 compute units** といったパッケージ情報で、平均使用時間ではありません。Runpod も公開しているのは価格表や、**50万人超の本番ワークロード傾向**であって、平均時間/ユーザーではありません。なので、**「Google Colab平均◯時間」「Runpod平均◯時間」は公開一次情報では確認できませんでした。** ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))

ただし、公開研究から見ると、**ノートブック型の研究ワークロードはかなりバースティ**です。NotebookOS は、Jupyter/Colab型の interactive deep learning training を、**長寿命セッションだが GPU 使用は intermittent and sporadic** と明示しています。Microsoft の ICSE 2024 論文でも、平均GPU利用率 50%以下の 400本の実ジョブを調べると、**interactive job** や **Jupyter notebook** が低利用の一因で、例として **4x V100 を約252分確保しながら平均GPU利用率 <1%** のジョブまで報告されています。つまり、**多くの研究者は「壁時計の25時間」を毎月きっちり燃やすわけではない**、という仮説にはかなり整合的です。 ([arxiv.org](https://arxiv.org/abs/2503.20591))

一方で、少数の本気の fine-tuning / long-context / multimodal ユーザーは、25時間を簡単に使い切ります。なので実務上は、**平均ではなく分布**を見るべきです。AIXS に必要なのは「平均25時間か？」ではなく、**25h未満のライト層がどれだけ多く、25h超のヘビー層がどれだけ少ないか**です。そこが見えないまま固定バンドルを切るのは危険です。これは上の研究結果からの**推論**です。 ([arxiv.org](https://arxiv.org/abs/2503.20591))

---

## 4. ARPU $85/月 は現実的か？
**研究者中心のセルフサーブ事業としては、かなり強気です。** Google Colab の公表価格は **Pro $9.99**、**Pro+ $49.99**です。AIXS の ARPU を $85 にしたいなら、Starter $29 と Pro $99 だけで考えても、**有料ユーザーの80%がProを選ばないと到達しません。** これは個人研究者が多いミックスでは重い前提です。 ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))

しかも SaaS 追加価値の相場感も甘く見ない方がいいです。W&B の公開価格は **Pro starts at $60/month** ですが、同社は**学術機関向けに Pro ライセンスを無料提供**しており、しかも **unlimited tracked hours、200GB storage、up to 100 seats** を含みます。加えて **MLflow は 100% open source / forever free**、**ClearML も self-hosted かつ 100% open source** を打ち出しています。したがって、**研究者個人に対して SaaS 機能だけで $20–30/月の追加WTPを広く期待するのは弱い**です。払われるとしたら、RBAC/SSO/監査/共有クォータ/組織管理などの**チーム機能**です。 ([wandb.ai](https://wandb.ai/site/pricing/))

私なら ARPU は分けて考えます。**個人研究者 ARPU = $20–50、ラボ/チーム ARPU = $80–150/seat、ヘビー層は overage で回収**、というモデルの方が現実に近いです。Colab の価格アンカーと OSS 代替の強さを見る限り、**ブレンドARPU $85 は「チーム比率がかなり高い」前提**です。これは市場価格からの**推論**です。 ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))

---

## 5. フリーミアム転換率 3% は現実的か？
**数字としては十分ありえる。だが、GPUクラウドでは“3%でも危ない”です。** OpenView の 450+ software companies ベンチマークでは、**freemium の free-to-paid は 5%**、**free trial は 17%** です。したがって **3% は「非常識に低い」わけではなく、むしろコストの高いインフラ商材では十分起こりうる水準**です。Slack や Spotify の 27–30% と比較するのは、習慣性・ネットワーク効果・無料原価の違いが大きすぎて不適切です。 ([openviewpartners.com](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks/))

問題は economics です。無料枠の **T4 20時間**は、Google Cloud Spot の T4 **$0.14/hr** なら **$2.8/月**、Vertex の T4 **$0.4025/hr** なら **$8.05/月** 相当です。もし free-to-paid が 3% なら、**100人の無料ユーザーを獲得したときの compute-only CAC は $93〜$268/有料転換者**になります。ここにサポートや不正利用対策が乗るので、**GPU無料枠を出す freemium は、SaaSの一般論よりはるかに重い**です。 ([cloud.google.com](https://cloud.google.com/spot-vms/pricing?utm_source=openai))

さらに OpenView は、平均 freemium 企業の retention が **month 1で19%、month 2で11%、month 3で9%** とかなり低いことも示しています。GPUクラウドは多くの場合**single-player**で、チーム共有が弱いと retention も上がりにくいです。よって 3% という転換率そのものより、**無料枠の濃さ**の方がはるかに重要です。 ([openviewpartners.com](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks/))

---

## 6. 月次 churn 8% は正しいか？
**B2B SaaS benchmark としては高すぎます。研究者向け project tool としてならありうる、という位置づけです。** Lighter Capital の 2025 B2B SaaS ベンチマークでは、**median customer churn は年率 16.25%**、**median revenue churn は年率 12.5%** です。月次換算するとそれぞれ **約1.47%**、**約1.11%**。一方、**月次 8% churn は年率 63.2% churn** に相当します。だから 8% を置くときは、**あなたは“sticky B2B SaaS”をモデルしているのではなく、“使い捨てに近い self-serve project tool”をモデルしている**、と理解すべきです。 ([lightercapital.com](https://www.lightercapital.com/blog/2025-b2b-saas-startup-benchmarks))

しかも研究用途には季節性があります。CloudLab の公開論文では、**夏は利用が下がり、晩春に論文締切と授業終盤が重なってピークになる**と説明されています。学術ユーザーを取るなら、月次 churn を単一係数で置くより、**semester/quarter cohort** や **pause/reactivate** を分けるべきです。 ([usenix.org](https://www.usenix.org/sites/default/files/atc19-full-proceedings.pdf?utm_source=openai))

したがって、8% を「正しい平均」として財務モデルに一本で入れるのは雑です。**個人研究者セルフサーブ**、**研究室/チーム**、**企業PoC** の少なくとも3コホートに分けるべきです。これは上のベンチマークと academic seasonality からの**推論**です。 ([lightercapital.com](https://www.lightercapital.com/blog/2025-b2b-saas-startup-benchmarks))

---

## 7. SaaS機能に $20–30/月 の WTP は本当か？
**個人研究者には弱い。チームにはありえる。** ここはかなり懐疑的に見ます。W&B の **Free** でも experiment tracking / registry / lineage / alerts が入っており、**Pro は $60/月**ですが、学術向けには **Pro 無料**です。MLflow は **100% open source / forever free**、ClearML も **100% open source** と self-host を打ち出しています。つまり、**研究者個人が “実験管理が便利だからさらに $20–30 払う” のは一般解ではない**です。 ([wandb.ai](https://wandb.ai/site/pricing/))

逆に、**チーム管理・権限・共有クォータ・組織課金・監査ログ・SLA** まで入るならWTPは作れます。W&B が Pro を $60/month で売っているのも、その方向の証拠です。だから AIXS の SaaS 価値は **“研究者個人の便利機能”ではなく、“チームの運用負荷削減” に寄せないと monetization しにくい**です。 ([wandb.ai](https://wandb.ai/site/pricing/))

---

# 改善提案（定量つき）

### 1) Power は **100h同梱を維持しない**。まず 70–80h に下げる
Runpod H100 SXM の **$2.69/hr** を原価 proxy にすると、Power 100h は GPU原価を引いた残りが **$30**しかありません。80h に下げると **$83.8**、70h なら **$110.7** 残ります。**100h→80h**にするだけで、サポート/開発/不稼働を吸収できる余地が大きく増えます。保証付きH100を名乗るなら、私は **70–80h** が安全圏です。 ([runpod.io](https://www.runpod.io/gpu-pricing?utm_source=openai))

### 2) **“H100”を1 SKUで売らない**。PCIe/SXM/保証有無で分ける
市場では H100 の価格差が大きく、Hyperstack で **H100 $1.90 / SXM $2.40**、Runpod で **PCIe $1.99 / SXM $2.69**、Lambda 公開の 1x 価格でも **PCIe $3.29 / SXM $4.29（2026年4月6日から有効）**です。単に “H100” と書くと、**20–30%超の原価差**を価格表が吸収できません。**Best-effort H100 PCIe** と **Guaranteed H100 SXM** を分けるべきです。 ([hyperstack.cloud](https://www.hyperstack.cloud/gpu-pricing))

### 3) 個人向け主力は H100 ではなく **A100/L4 寄り**にする
A100 は **$1.35〜$1.99/hr**、L4 は **$0.39/hr**、T4 でも Vertex で **$0.4025/hr** です。$99 の売上なら、理論上 **A100 を約50〜73時間**、L4/T4級なら **約246〜254時間** 買えます。研究者のノートブック用途がバースティなら、**$99でH100 25h**より、**$99でA100 40–50h + H100は従量課金**の方が使われ方に合います。 ([hyperstack.cloud](https://www.hyperstack.cloud/gpu-pricing))

### 4) 無料枠は縮めるか、**reverse trial** に寄せる
OpenView では **freemium 5%** に対し **free trial 17%** です。GPU無料枠は原価が重いので、**永続Free + 20h T4** より、**7–14日 reverse trial + 小さな永続無料枠**の方が筋がいいです。少なくとも現状の 20h T4 無料は、3%転換だと compute-only CAC が **$93〜$268/paid** になり得ます。GPU business でこれは重すぎます。 ([openviewpartners.com](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks/))

### 5) SaaS追加課金は **個人 $0–10 / チーム $20–60+** に切る
W&B Pro は **$60/month**、ただし academic は無料。MLflow/ClearML は OSS 無料です。なので、**個人研究者に $20–30 を広く課す前提**は弱い。代わりに、**共有ワークスペース、RBAC、SSO、監査ログ、請求統合**など、チーム運用機能に $20–60+/seat を寄せるべきです。個人には compute で課金し、SaaS は薄く。 ([wandb.ai](https://wandb.ai/site/pricing/))

### 6) churn は月次定数で置かず、**学期/締切 seasonality を織り込む**
B2B benchmark は年率 **16.25% customer churn** で、月換算は **約1.47%**。それに対して月次8%は年率 **63.2%** です。CloudLab でも学術利用は**夏に低く、晩春に高い**。したがって、AIXS は **monthly churn 1本**ではなく、**semester pack / paused account / reactivation** をモデル化した方が精度が出ます。 ([lightercapital.com](https://www.lightercapital.com/blog/2025-b2b-saas-startup-benchmarks))

### 7) ARPUは1本ではなく、**セグメント別に置く**
Colab の価格アンカーは **$9.99 / $49.99**です。AIXS が blended ARPU **$85** を狙うなら、Starter $29 と Pro $99 だけで考えても**80%がPro**でないと届きません。なので、**個人研究者ARPU $20–50、ラボ/チームARPU $80–150、Powerは usage overage で伸ばす**という形に分ける方が、現実に沿っています。 ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))

---

## 最終評価
**一番危ないのは Pro ではなく Power です。**  
Pro は「安いH100が取れる」「未消化がある」なら成立します。むしろ **Starter/Team がしっかり儲かる**ので、全体ポートフォリオとしては組めます。  
ただし、今のままでは **Power がヘビーユーザーの逆選択を招きやすく、ARPU $85 と churn 8% と SaaS WTP $20–30 を同時に置くのは楽観的**です。AIXS が本当に勝てる形は、**H100時間を配る会社**ではなく、**研究チームの GPU運用を失敗なく回す会社**として設計し直した価格表です。 ([lightercapital.com](https://www.lightercapital.com/blog/2025-b2b-saas-startup-benchmarks))

補足すると、あなたが求めていた **Google Colab / Runpod の平均利用時間の公開値**は、私が確認した公開一次情報では見つかりませんでした。見つかったのは **価格・compute units・広い利用傾向**までで、**平均GPU時間/ユーザー**は非公開でした。そのため、その部分は公開研究のワークロード論文で代替的に評価しています。 ([support.google.com](https://support.google.com/a/answer/13177581?co=DASHER._Family%3DEducation&hl=en&sjid=345567951837466528-EU))

必要なら次に、**この価格表をそのままP/Lモデルに落として、3シナリオ（楽観/現実/悲観）で月次粗利・LTV/CAC・損益分岐会員数まで数値化**します。

---
