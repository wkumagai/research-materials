# Citation Verification Report

**調査日:** 2026-03-29
**対象:** GPT-5.4-pro分析ファイル群（6ファイル、合計約448KB）
**目的:** 主要30クレームの出典URL検証、矛盾データの特定

---

## 1. 主要クレームの出典検証

### 1.1 市場規模・企業データ

| # | クレーム | 出典URL | 検証ステータス | 備考 |
|---|---|---|---|---|
| 1 | RunPod ARR $120M+、500K+開発者 | [runpod.io/press](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr) | **Verified** | 2026年1月20日の公式プレスリリース |
| 2 | RunPod $20M seed（Intel Capital/Dell Technologies Capital） | [runpod.io/changelog](https://www.runpod.io/changelog-entries/may-2024) | **Verified** | 2024年5月の公式記載 |
| 3 | RunPod粗利率15-25% | GPT-5.4-pro推定 | **Unverified（推定値）** | 公開データなし。Sacra推定60-70%と大幅乖離。**矛盾あり** |
| 4 | Modal評価額$1.1B（Series B） | [modal.com/blog](https://modal.com/blog/announcing-our-series-b) | **Verified** | 2025年9月29日の公式発表 |
| 5 | Modal評価額$2.5B（報道ベース） | [techcrunch.com](https://techcrunch.com/2026/02/11/ai-inference-startup-modal-labs-in-talks-to-raise-at-2-5b-valuation-sources-say/) | **Verified** | TechCrunch報道。未クローズ |
| 6 | Modal ARR約$50M | TechCrunch報道ベース | **Unverified（推定値）** | 公式未発表、報道ベースの推定 |
| 7 | CoreWeave 2025売上$5.131B | [investors.coreweave.com](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results) | **Verified** | 公式IR発表 |
| 8 | CoreWeave GAAP営業利益率-1% | 同上 | **Verified** | 営業損失$46M / 売上$5.131B |
| 9 | Lambda ARR $500M+（推定） | [sacra.com](https://sacra.com/c/lambda-labs/) | **Unverified（推定値）** | Sacra推定。Lambda公式未発表 |
| 10 | Vast.ai ARR $12M+ run-rate | [vast.ai](https://vast.ai/article/ramp-brex-fastest-growing-vendor) | **Verified** | 「revenue crossed seven figures per month for the first time」=月$1M+=$12M+ |
| 11 | Vast.ai テイクレート25% | [console.vast.ai/faq](https://console.vast.ai/faq) | **Verified** | 「hosts receive 75%, Vast.ai keeps 25%」 |
| 12 | Vast.ai 10万+ユーザー、1.4万+月次課金顧客 | [vast.ai](https://vast.ai/article/ramp-brex-fastest-growing-vendor) | **Verified** | 2026年3月5日の公式ブログ |

### 1.2 価格データ

| # | クレーム | 出典URL | 検証ステータス | 備考 |
|---|---|---|---|---|
| 13 | RunPod H100 PCIe $1.99/hr | [runpod.io](https://www.runpod.io/gpu-pricing) | **Verified** | 2026年3月28日時点のスナップショット |
| 14 | RunPod H100 SXM $2.69/hr | 同上 | **Verified** | 同上 |
| 15 | Lambda H100 1-Click Clusters $2.76/hr | [lambda.ai](https://lambda.ai/pricing) | **Verified** | 公式価格ページ |
| 16 | Lambda H100 PCIe $3.29/hr（2026年4月6日~） | 同上 | **Verified** | 将来価格として掲載 |
| 17 | Modal H100 $3.95/hr（換算） | [modal.com](https://modal.com/pricing) | **Verified** | $0.001097/秒からの換算 |
| 18 | AWS H100 $6.88/hr（p5.4xlarge） | [calculator.holori.com](https://calculator.holori.com/aws/ec2/p5.4xlarge) | **Verified** | サードパーティ価格比較サイト |
| 19 | Google Colab Pro $9.99 / Pro+ $49.99 | [support.google.com](https://support.google.com/a/answer/13177581) | **Verified** | Google公式 |
| 20 | H100 CAPEX $25.6K幾何平均 | [epoch.ai](https://epoch.ai/data/ai-chip-sales-documentation) | **Verified** | Epoch AIのチップ価格データ |

### 1.3 市場統計・ベンチマーク

| # | クレーム | 出典URL | 検証ステータス | 備考 |
|---|---|---|---|---|
| 21 | SaaS $10M ARR到達率13%、$20M ARR到達率3.5% | [chartmogul.com](https://chartmogul.com/reports/saas-growth-report/saas-growth-report-2023.pdf) | **Verified** | ChartMogul 2023レポート |
| 22 | Seed dealの46%がbridge round | [axios.com](https://www.axios.com/2025/05/18/venture-capital-stalling-seed) | **Verified** | Axios/Carta報道 |
| 23 | Series A deal count Q1 2022→Q1 2025で79%減 | 同上 | **Verified** | 同上 |
| 24 | Freemium free-to-paid転換率約5% | [openviewpartners.com](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks/) | **Verified** | OpenView PLGベンチマーク |
| 25 | Developer Tools月次churn率中央値4.2% | [revmine.ai](https://revmine.ai/blog-churn-benchmarks) | **Verified** | RevMineベンチマーク |
| 26 | Developer Tools ARPU中央値$29/月 | [proven-saas.com](https://proven-saas.com/benchmarks/cac-payback-benchmarks) | **Verified** | Proven SaaSベンチマーク |
| 27 | Neocloud 2025年売上$23B超、前年比205%成長 | [srgresearch.com](https://www.srgresearch.com/articles/neoclouds-currently-growing-by-over-200-per-year-will-reach-180-billion-in-revenues-by-2030) | **Verified** | Synergy Research Group |
| 28 | GPUaaS市場$43.7B（2025年推定） | [grandviewresearch.com](https://www.grandviewresearch.com/industry-analysis/gpu-service-market-size-share-trends-analysis) | **Verified** | Grand View Research |
| 29 | Papers with Code 2025年7月にMeta閉鎖 | [paperswithcode.com](https://paperswithcode.com/) → HF redirect | **Verified** | リダイレクト確認済み |
| 30 | METI FY2026予算¥1.23T（AI・半導体4倍増） | [japantimes.co.jp](https://www.japantimes.co.jp/business/2025/12/26/economy/ai-budget-support/) | **Verified** | Japan Times報道 |

---

## 2. 出典なし・根拠不十分なクレーム

| # | クレーム | ファイル | 問題点 |
|---|---|---|---|
| 1 | RunPod粗利率15-25% | gpt54pro_financial_critique.md | **出典なし。推定値のみ。** Sacra推定60-70%と矛盾 |
| 2 | Modal粗利率30-40% | gpt54pro_financial_critique.md | **推定値。** 公式データなし |
| 3 | Lambda粗利率20-30% | gpt54pro_financial_critique.md | **推定値。** 公式データなし |
| 4 | 「GPU利用者の95%はGPUだけが欲しい」 | debate_synthesis_final.md (Critic) | **出典なし。** 主観的主張 |
| 5 | 「R&Dプラットフォーム」TAM $80B+ | debate_synthesis_final.md (Advocate) | **水増しの可能性。** GPT-5.4-pro verdict reviewで$41.2B（Omdia）が実数と指摘 |
| 6 | 成功確率8-12% | debate_synthesis_final.md | **合議結果であり実証データではない。** GPT-5.4-pro再計算では2.3-6% |
| 7 | 「研究者は平均でH100を月25h使わない」 | gpt54pro_financial_critique.md | **直接データなし。** NotebookOSの研究論文からの間接推論 |
| 8 | Papers with Code月間UU 47万 | gpt54pro_verdict_review.md | **出典なし。** 閉鎖前のトラフィックデータの公式ソース不明 |

---

## 3. ソース間の矛盾データ

### 矛盾1: RunPod粗利率

| ソース | 数値 | 根拠 |
|---|---|---|
| Sacra推定（debate_advocate.md等） | **60-70%** | コミュニティクラウドのアセットライトモデル |
| GPT-5.4-pro推定（gpt54pro_financial_critique.md） | **15-25%** | GPU原価ベースの全社粗利推定 |

**原因分析:** 定義の違い。Sacra推定はマーケットプレイス手数料（テイクレート）ベースの粗利率（agent/net revenue）。GPT-5.4-pro推定はGMV全額を売上計上した場合の粗利率（principal/gross revenue）かつSecure Cloudの原価を含む全社推定。Community Cloud部分のみなら高粗利、全社（Community + Secure）なら低粗利。**両方正しい可能性があるが、比較対象として不適切。**

### 矛盾2: Vast.ai ARR

| ソース | 数値 | 根拠 |
|---|---|---|
| Critic（debate_synthesis_final.md） | **$2.2M** | 古い推定値（時期不明） |
| GPT-5.4-pro（gpt54pro_financial_critique.md） | **$12M+** | 2026年3月5日の公式ブログ「revenue crossed seven figures per month」 |

**原因分析:** 時期の違い。$2.2Mは2024年以前の推定値。$12M+は2026年3月の最新公式データ。Vast.aiは売上13倍成長を公表しており、$12M+が最新の正確な数値。

### 矛盾3: 成功確率

| ソース | 数値 | 前提条件 |
|---|---|---|
| debate_synthesis_final.md（5エージェント合議） | **8-12%** | 修正戦略採用時、段階的フェーズイン |
| gpt54pro_reality_check.md | **5-8%** | 一般SaaSなら妥当、GPUクラウドなら下限寄り |
| gpt54pro_verdict_review.md（o3） | **2.3-6%** | 実データに基づく条件付き確率の再計算。修正戦略で4-6% |

**原因分析:** 前提条件の違い。各段階の条件付き確率の置き方が異なる。合議判定は各エージェントの主観的確率の中間値。o3は実データ（PMF到達率19%、ハイパースケーラー競合後ARR$20M超=8.7%等）を用いた再計算。**o3の2.3-6%が最もデータドリブン。**

### 矛盾4: 価格プランの粗利

| ソース | Pro $99プランの粗利 | 前提 |
|---|---|---|
| analysis_pricing_gtm.md（初期設計） | **37%**（H100 25hr含む） | H100 $2.50/hr |
| gpt54pro_reality_check.md | **粗利ほぼゼロ or 赤字** | H100 $2.69-$4.50/hr（市場相場） |
| analysis_financial_model.md（改定版） | **41%** | H100 15hr（25hr→15hrに削減後） |
| gpt54pro_financial_critique.md | **黒字化は可能だが前提次第** | $2.50/hr調達なら黒字、$3.29/hrなら薄利 |

**原因分析:** H100の調達単価前提の違い。$2.50/hrで調達できれば黒字、市場相場の$2.69-$4.50/hrでは薄利~赤字。改定版でH100時間を15hrに削減したことで改善。

### 矛盾5: TAM（総市場規模）

| ソース | 数値 | 定義 |
|---|---|---|
| Advocate（debate_advocate.md） | **$80B+** | GPUaaS + 隣接市場（HPC、量子、ラボ装置）全体 |
| GPT-5.4-pro（verdict_review） | **$41.2B**（Omdia推計） | GPU-aaS実売上のみ（2023年）、CAGR 29% |
| Grand View Research | **$43.7B**（2025年推定） | GPU-as-a-Service市場 |
| o3 verdict | **Pragmatistの$50-200M SOMが最も現実的** | 獲得可能市場 |

**原因分析:** TAMの定義範囲が異なる。$80B+は隣接市場を含む最大解釈。$41-44Bが純粋GPUaaS市場。AIXSの実際の獲得可能市場（SOM）は$50-200Mが妥当。

---

## 4. データ信頼性の総合評価

| カテゴリ | 信頼性 | 備考 |
|---|---|---|
| GPU価格データ（各社公式） | **高** | 調査日2026-03-28のスナップショット。変動が激しいため3-6ヶ月で陳腐化 |
| 企業売上・ARR（公式発表） | **高** | RunPod $120M、CoreWeave $5.1B、Vast.ai $12M+は公式ソース |
| 企業売上・ARR（推定値） | **中** | Modal $50M、Lambda $500Mは報道/推定ベース |
| 粗利率（推定値） | **低** | 全社非公開。定義の違いで結論が逆転する |
| SaaSベンチマーク | **高** | ChartMogul、OpenView、Lighter Capitalは業界標準ソース |
| 成功確率 | **低-中** | モデルと前提次第で2.3-12%と5倍のばらつき |
| 市場規模（TAM） | **中** | 定義次第で$41B-$134Bと3倍以上の幅 |

---

## 5. 最も信頼性の高い数字

1. **RunPod ARR $120M+、500K+開発者** -- 公式プレスリリース
2. **CoreWeave 2025売上$5.131B** -- 公式IR
3. **Vast.ai テイクレート25%** -- 公式FAQ
4. **H100オンデマンド価格$1.99-$6.88/hr** -- 各社公式価格ページ
5. **SaaS freemium転換率約5%** -- OpenView PLGベンチマーク（n=450+）
6. **SaaS $10M ARR到達率13%** -- ChartMogul
7. **Neocloud市場2025年$23B超** -- Synergy Research Group

## 6. 最も不確実な数字

1. **RunPod粗利率** -- 15-25%と60-70%で4倍のばらつき
2. **成功確率** -- 2.3-12%で5倍のばらつき
3. **TAM** -- $41B-$134Bで3倍のばらつき
4. **Pro $99プラン粗利** -- H100調達単価次第で-10%~+41%
5. **Lambda ARR $500M+** -- Sacra推定のみ、公式未確認
