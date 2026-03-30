# AIXS 市場調査セクション（Section 3）品質保証チェックリスト

**レビュー日:** 2026-03-28
**対象ファイル:** `/Users/kumacmini/research-materials/AIXS_Competitive_Analysis_Market_Research.md`
**レビュアー:** QA Agent

---

## 1. 必須地域の網羅性

| 地域 | 判定 | 備考 |
|---|---|---|
| アメリカ (US) | **PASS** | Section 3.4.1 に詳細記載。ハイパースケーラー市場占有率、VC投資額($194B)、データセンター数(4,049)、DOE/NSF/NAIRR等の制度を網羅 |
| カナダ (Canada) | **PASS (条件付き)** | 米国と統合して「US/Canada」として記載 (3.4.1)。独立セクションはないが、サマリー表・詳細表ともに「US/Canada」として存在。カナダ固有の制度(CIFAR、Vector Institute等)やVC金額の個別記載がないため、深掘りは不足 |
| EU | **PASS** | Section 3.4.2 に詳細記載。EuroHPC 57,000アクセラレータ、Horizon Europe、InvestAI EUR 200B、AI Act/GDPR/CADA、ネオクラウド(Nscale等)を網羅 |
| UK | **PASS** | Section 3.4.3 に詳細記載。AIRR、Isambard-AI(5,448 GH200)、£500M Sovereign AI Fund、UK VC £1.8B等を網羅 |
| 中国 (China) | **PASS** | Section 3.4.4 に詳細記載。Alibaba 35.8%シェア、智算中心、算力券30+都市、GPU稼働率30%問題、国産GPU(Ascend/Cambricon)、輸出規制影響を網羅 |
| 日本 (Japan) | **PASS** | Section 3.4.5 に最も詳細に記載。METI予算¥1.23T、ABCI 3.0、GENIAC、さくら/GPUSOROBAN/GMO/WebARENA、科研費、AI推進法を網羅 |
| 韓国 (Korea) | **PASS** | Section 3.4.6 に詳細記載。KRW 10.1T AI予算、NACC、KISTI HANGANG、260,000+ GPU確約、財閥(Samsung/SK/Hyundai)、K-Moonshot、OpenAI Stargate連携を網羅 |
| 台湾 (Taiwan) | **PASS** | Section 3.4.7 に詳細記載。TWCC/NCHC、Foxconn AIファクトリー、NT$190B 4年計画、Taiwan Compute Alliance、TSMC製造拠点視点を網羅 |
| UAE | **PASS** | Section 3.4.8 に詳細記載。Core42、Stargate UAE(1GW)、MGX $100B基金、Microsoft $15.2B投資、MBZUAI、輸出許可35K GB300を網羅 |
| サウジアラビア (Saudi Arabia) | **PASS** | Section 3.4.9 に詳細記載。HUMAIN(PIF)、Project Transcendence $100B、KAUST Shaheen III、マルチベンダー戦略(NVIDIA+AMD+Qualcomm)、Vision 2030を網羅 |
| インド (India) | **PASS** | Section 3.4.10 に詳細記載。IndiaAI 38,000+ GPU(100,000目標)、40%補助金、Rs 115-150/GPU-hr、Yotta/E2E/Jio、AI市場$8B→$17Bを網羅 |
| シンガポール (Singapore) | **PASS** | Section 3.4.11 に詳細記載。NSCC ASPIRE 2A+、DC-CFA規制、RIE2030 S$37B、NVIDIA売上15%、Oracle $6.5B投資を網羅 |
| イスラエル (Israel) | **PASS** | Section 3.4.12 に詳細記載。342 GenAIスタートアップ、国家AIスパコン(4,000 B200/Nebius)、Innovation Authority、NVIDIA R&D拠点(5,000人)、防衛AI $1B+を網羅 |

**地域網羅率: 13/13 PASS**

---

## 2. 地域別必須データ

### 2.1 GPU Usage Channels（GPU利用チャネル）

| チャネル | US/CA | EU | UK | 中国 | 日本 | 韓国 | 台湾 | UAE | サウジ | インド | SG | イスラエル | 判定 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hyperscaler cloud | Yes | Yes | Yes | Yes(国内) | Yes | Yes | 部分的 | Yes | 部分的 | Yes | Yes | Yes | **PASS** |
| AI-specialized cloud | Yes | Yes | Yes | Yes(国内) | Yes | Yes | 部分的 | Yes(Core42) | Yes(HUMAIN) | Yes | 部分的 | 部分的 | **PASS** |
| University/research GPU clusters | 部分的 | Yes | Yes | 部分的 | Yes | Yes(KAIST) | Yes(NCHC) | Yes(MBZUAI) | Yes(KAUST) | 部分的 | 部分的 | Yes(Technion) | **PASS (条件付き)** |
| National supercomputers | Yes(DOE) | Yes(EuroHPC) | Yes(Isambard-AI/Dawn) | Yes(智算中心) | Yes(ABCI 3.0) | Yes(NACC/KISTI) | Yes(TWCC) | 部分的 | Yes(Shaheen III) | Yes(PARAM/C-DAC) | Yes(NSCC) | Yes(Nebius運営) | **PASS** |
| Corporate on-premise | Yes(Meta等) | 部分的 | 部分的 | Yes(大手GPU備蓄) | Yes(大企業DGX) | Yes(財閥) | Yes(Foxconn) | Yes(G42) | 部分的 | Yes(Reliance/Tata) | 部分的 | 部分的 | **PASS (条件付き)** |
| Government-provided compute | Yes(DOE HPC) | Yes(EuroHPC) | Yes(AIRR) | Yes(智算中心) | Yes(ABCI/GENIAC) | Yes(NACC) | Yes(NCHC) | Yes(Core42) | Yes(HUMAIN) | Yes(IndiaAI) | Yes(NSCC) | Yes(Innovation Authority) | **PASS** |
| Subsidized/voucher usage | 部分的 | Yes(AI Factory) | Yes(AIRR) | Yes(算力券) | Yes(GENIAC) | Yes | 部分的 | 部分的 | 部分的 | Yes(40%補助) | Yes(AI Singapore) | Yes(Innovation Authority) | **PASS (条件付き)** |
| Startup credits | Yes | Yes(OVH等) | 部分的 | 部分的 | Yes(HScredits) | Yes(NVIDIA Inception) | 部分的 | 部分的 | 部分的 | 部分的 | Yes(AI Singapore) | Yes(Innovation Authority) | **PASS (条件付き)** |
| Individual usage | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | **FAIL** |

**GPU利用チャネルの不足箇所:**

- **Individual usage (個人利用):** 全地域で体系的な記載なし。各地域における個人研究者・フリーランスのGPU利用パターン（Colab, RunPod個人利用, ABCI個人申請可否等）が明示的にカバーされていない。サマリー表(3.2)の詳細表(3.3)に「スタートアップクレジット利用」列はあるが「個人利用」列はない。
- **University/research GPU clusters:** 多くの地域で大学GPUクラスターの具体的構成（GPU数、利用資格）が言及されていない。日本(ABCI/mdx/8大学)、韓国(KAIST)は良いが、インド、シンガポール、UAE等は大学名のみで詳細なし。
- **Startup credits:** UAE、サウジ、台湾、インドでのスタートアップクレジットプログラムの具体的な金額・条件が不足。

---

### 2.2 Funding Sources（資金源）

| 資金源 | US/CA | EU | UK | 中国 | 日本 | 韓国 | 台湾 | UAE | サウジ | インド | SG | イスラエル | 判定 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Public research grants (プログラム名) | Yes(DOE/NSF/NIH) | Yes(Horizon/ERC) | Yes(UKRI) | Yes(国家基金) | Yes(科研費/JST AIP) | Yes(NRF/IITP) | Yes(NSTC) | 部分的 | 部分的 | Yes(IndiaAI) | Yes(RIE2030) | Yes(Innovation Authority) | **PASS** |
| University budgets | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | Yes(KAIST) | 部分的 | Yes(MBZUAI) | Yes(KAUST) | 部分的 | 部分的 | Yes(Technion) | **FAIL** |
| Corporate R&D | Yes | Yes(自動車/製薬) | 部分的 | Yes($70B+) | Yes(¥23T) | Yes(財閥) | Yes(Foxconn) | Yes(G42) | 部分的 | Yes(Reliance/Tata) | 部分的 | 部分的 | **PASS (条件付き)** |
| VC/startup funding (金額) | Yes($194B) | Yes($15.8B) | Yes(£1.8B) | Yes($13.9B) | Yes(Sakana ¥38.3B) | Yes($9B累計) | Yes(NT$10B基金) | 部分的 | 部分的 | Yes($643M) | Yes(S$8.4B) | Yes($15.6B) | **PASS** |
| Government subsidies (金額) | Yes(DOE/NAIRR) | Yes(InvestAI EUR 200B) | Yes(£500M×2) | Yes(RMB 1T) | Yes(METI ¥1.23T) | Yes(KRW 10.1T) | Yes(NT$190B) | Yes(MGX $100B) | Yes($100B) | Yes($1.25B) | Yes(S$37B) | Yes($45M) | **PASS** |
| Compute vouchers/credits | Yes(AWS/GCPcredits) | Yes(AI Factory 50K hr) | Yes(AIRR 2M hr) | Yes(算力券30+都市) | Yes(GENIAC 2/3) | Yes | 部分的 | 部分的 | 部分的 | Yes(40%割引) | Yes(AI SG) | Yes(Innovation Authority GPU) | **PASS** |
| Joint/contract research | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | Yes(Compute Alliance) | 部分的 | 部分的 | 部分的 | 部分的 | 部分的 | **FAIL** |

**資金源の不足箇所:**

- **University budgets (大学予算):** ほとんどの地域で大学独自のGPU/コンピュート予算が明示されていない。日本は科研費として別途カバーされているが、米国大学のGPU予算規模、EU各国大学のコンピュート予算は未記載。詳細表(3.3)に「大学GPU比重」列はあるが「中」「低」等の定性記載のみで、金額やGPU数はない。
- **Joint/contract research (共同研究/委託研究):** 全地域で企業-大学間の共同研究によるGPU利用の記載がほぼない。台湾のCompute Allianceが唯一の具体例。産学連携によるGPU共有・共同利用の実態が欠落。

---

### 2.3 Government Programs（政府プログラム）

| 項目 | US/CA | EU | UK | 中国 | 日本 | 韓国 | 台湾 | UAE | サウジ | インド | SG | イスラエル | 判定 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| National AI strategies named | Yes(NAIRR) | Yes(AI Act) | Yes(AIRR) | Yes(東数西算) | Yes(AI推進法/基本計画) | Yes(AI基本法) | Yes(AI基本法) | Yes(National AI Strategy 2031) | Yes(Vision 2030) | Yes(IndiaAI Mission) | Yes(NAIS 2.0) | Yes(Telem Program) | **PASS** |
| Specific compute programs | Yes(DOE HPC/NAIRR) | Yes(EuroHPC/AI Factories) | Yes(AIRR/Isambard-AI) | Yes(智算中心/算力券) | Yes(ABCI/GENIAC/Cloud Program) | Yes(NACC/KISTI HANGANG) | Yes(TWCC/10 AI Infrastructure) | Yes(Core42/Stargate UAE) | Yes(HUMAIN/Shaheen III) | Yes(IndiaAI Compute/PARAM) | Yes(NSCC ASPIRE) | Yes(国家AIスパコン) | **PASS** |
| Budget/funding amounts | Yes(Pax Silica $4T目標) | Yes(EUR 200B) | Yes(£500M×2) | Yes(RMB 1T) | Yes(¥1.23T) | Yes(KRW 10.1T) | Yes(NT$190B) | Yes(SWF $100B+) | Yes($100B) | Yes($1.25B) | Yes(S$37B) | Yes($45M+$140M) | **PASS** |
| GPU counts | 部分的 | Yes(57K) | Yes(5,448+1,024) | Yes(788 EFLOPS) | Yes(6,128 H200) | Yes(260,000+) | Yes(1,700+) | Yes(35K GB300) | Yes(18K GB300/2,800 GH200) | Yes(38,000+) | Yes(20 PFLOPS) | Yes(4,000 B200) | **PASS** |
| Eligibility criteria | 部分的 | Yes(SME/スタートアップ向け) | Yes(研究者/スタートアップ) | Yes(算力券条件) | Yes(ABCI申請/GENIAC条件) | 部分的 | 部分的 | 部分的 | 部分的 | Yes(認定プロバイダ/40%割引条件) | Yes(AI SG条件) | Yes(Innovation Authority) | **FAIL** |

**政府プログラムの不足箇所:**

- **Eligibility criteria (利用資格):** 複数の地域で政府コンピュートプログラムの具体的な利用資格条件が不十分。
  - **US:** NAIRR の具体的な申請資格・審査基準が未記載。
  - **韓国:** NACC/KISTIの利用資格（国籍要件、機関要件等）が未記載。
  - **台湾:** TWCCの利用資格が未記載。
  - **UAE:** Core42セルフサービスの利用条件が未記載。
  - **サウジ:** HUMAINの外部利用可否・条件が未記載。

---

### 2.4 AIXS Implications（AIXSへの示唆）

| 項目 | US/CA | EU | UK | 中国 | 日本 | 韓国 | 台湾 | UAE | サウジ | インド | SG | イスラエル | 判定 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Target customers identified | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | **PASS** |
| Effective messaging | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | **PASS** |
| Infrastructure integration | Yes | Yes | Yes | 部分的 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | **PASS** |
| Policy/regulatory considerations | 部分的 | Yes | Yes | Yes | Yes | Yes(AI基本法) | Yes(AI基本法) | Yes(輸出規制) | Yes(Vision 2030) | Yes(IndiaAI認定) | Yes(DC-CFA) | 部分的 | **PASS** |

**AIXS示唆は全項目PASS。** Section 3.5で地域横断のメッセージ表・統合先表が充実。

---

## 3. 必須テーブル

| テーブル | 判定 | 備考 |
|---|---|---|
| 地域別サマリー表 (Section 3.2) | **PASS** | 15地域を8列（GPU利用経路、資金源、政府施策、地域独自の仕組み、代表例、AIXSへの示唆、出典、調査日）で網羅 |
| 地域別詳細表 (Section 3.3) | **PASS** | 15地域を12列（クラウド利用比重、大学GPU比重、公的計算基盤比重、スタートアップクレジット利用、企業オンプレ比重、主な資金源、主な制度、政府提供資源、補助金/バウチャー、主な制約、AIXS機会、出典）で網羅。12列以上の要件を満たす |

---

## 4. Additional Market Axes（追加市場比較軸）

| 判定 | 備考 |
|---|---|
| **PASS** | Section 4.2 に9つの追加市場比較軸を記載: (1) GPU調達難易度、(2) 輸出規制の影響、(3) 大学と企業の計算資源格差、(4) 国内クラウド育成政策、(5) データ越境規制、(6) 研究者の言語・文化的障壁、(7) 電力・冷却・サステナビリティ要件、(8) AI人材の供給、(9) GPU価格の反発リスク。各軸に理由、地域間差異、AIXSへの示唆を記載。最低5軸の要件を大幅に上回る |

---

## 5. Cross-Regional Analysis（地域横断分析）

| 項目 | 判定 | 備考 |
|---|---|---|
| Key differences between regions | **PASS** | Section 3.5に「地域ごとに何が決定的に違うか」テーブル (6軸: 資金源性質、規制の重さ、GPU調達制約、国産GPU開発、MLプラットフォーム成熟度、価格感度) |
| Region-specific AIXS messaging | **PASS** | Section 3.5に「AIXSはどの地域でどのメッセージを使うべきか」テーブル (10地域の主要・副次メッセージ) |
| Infrastructure integration by region | **PASS** | Section 3.5に「各地域で接続すべき既存基盤」テーブル (10地域の最優先・高優先統合先) |

---

## 6. References（参考文献）

| 項目 | 判定 | 備考 |
|---|---|---|
| Sources cited for major claims | **PASS** | Section 8に100+の参考文献リンク。カテゴリ別（ハイパースケーラー、GPU特化、推論/Dev、日本市場、EU/UK、アジア、新興市場、市場分析、Deep Research補足）に整理 |
| Government program sources | **PASS** | METI、EuroHPC、AIRR、IndiaAI、Core42/HUMAIN等の公式ソースを個別に記載 |
| Pricing sources | **PASS** | 各プロバイダの公式料金ページ+サードパーティ比較サイト（Vantage, CloudPrice, GetDeploying, Cast AI, gpu.fm）を記載 |
| Date of research noted | **PASS** | レポート冒頭に「データ期間: 2024年後半〜2026年3月」、各比較表に「調査日」列、Deep Research補足に「調査日: 2026-03-28」を明記 |

---

## 7. 総合判定サマリー

| カテゴリ | 合計項目 | PASS | FAIL | PASS率 |
|---|---|---|---|---|
| 必須地域 | 13 | 13 | 0 | 100% |
| GPU利用チャネル | 9 | 8 | 1 | 89% |
| 資金源 | 7 | 5 | 2 | 71% |
| 政府プログラム | 5 | 4 | 1 | 80% |
| AIXS示唆 | 4 | 4 | 0 | 100% |
| 必須テーブル | 2 | 2 | 0 | 100% |
| 追加市場比較軸 | 1 | 1 | 0 | 100% |
| 地域横断分析 | 3 | 3 | 0 | 100% |
| 参考文献 | 4 | 4 | 0 | 100% |
| **合計** | **48** | **44** | **4** | **92%** |

---

## 8. FAIL項目の詳細と推奨アクション

### FAIL 1: Individual usage（個人利用チャネル）

**不足内容:** 各地域における個人研究者・フリーランス・趣味利用者のGPU利用パターンが体系的に記載されていない。

**推奨アクション:**
- 各地域で個人が利用可能なGPUサービス（Google Colab, Kaggle, RunPod個人アカウント, ABCI個人申請等）の可否・条件を追記
- 個人利用時の典型的なコスト・利用制限（時間制限、GPU制限等）を記載
- AIXSの個人向けプラン（フリーミアム等）の示唆を追加

### FAIL 2: University budgets（大学予算）

**不足内容:** 大学独自のGPU/コンピュート予算が定量的に記載されていない。詳細表(3.3)の「大学GPU比重」列は「中」「低」等の定性記載のみ。

**推奨アクション:**
- 主要地域の代表大学のGPU保有数・年間コンピュート予算を調査・追記（例: MIT, Stanford, 東大, ETH Zurich, Tsinghua等）
- 大学がGPUコンピュートに割いている予算規模の推定値を記載
- 大学向けAIXSアカデミックプランの示唆を強化

### FAIL 3: Joint/contract research（共同研究/委託研究）

**不足内容:** 企業-大学間、企業-政府間の共同研究によるGPU利用パターンが全地域で欠落。

**推奨アクション:**
- 各地域の主要な産学連携GPU共有スキーム（日本のNEDO委託研究、EUのPublic-Private Partnerships、米国のNSF Industry-University Cooperative Research等）を追記
- 共同研究でのGPU利用時のデータ管理・IP帰属のパターンを記載
- AIXSの共同研究向けマルチテナント機能の示唆を追加

### FAIL 4: Eligibility criteria（利用資格条件）

**不足内容:** 複数地域の政府コンピュートプログラムで、具体的な利用資格・申請条件が不十分。

**推奨アクション:**
- **US:** NAIRR の利用資格（教育機関限定か、企業も可か、外国籍可否等）を調査・追記
- **韓国:** NACC/KISTIの利用資格（韓国法人要件、外国企業利用可否等）を追記
- **台湾:** TWCCの利用資格を追記
- **UAE/サウジ:** Core42/HUMAINの外部企業向け利用条件を追記
- 各地域でAIXSがパートナー/リセラーとして政府コンピュートの利用資格をバイパスまたは活用できる可能性を検討

---

## 9. 追加所見（PASS判定だが改善余地あり）

### 9.1 カナダの独立記載

カナダは「US/Canada」として統合されているが、カナダ固有のAIエコシステム（CIFAR Pan-Canadian AI Strategy、Vector Institute、Mila、Amii、CCAI、Canadian Sovereign AI戦略）は世界的に重要であり、独立セクションでの記載が望ましい。

### 9.2 マレーシア・インドネシアの扱い

必須13地域には含まれないが、レポートにはマレーシア・インドネシアの記載がある（サマリー表・詳細表に含む）。これは良い追加だが、深掘りメモ（Section 3.4）には含まれていないため、セクション間の一貫性を検討すること。（ただし必須チェック項目の対象外のため、これ自体はFAILではない。）

### 9.3 価格データの鮮度

競合分析（Section 2）のGPU価格データは主に2025年3月時点、Deep Research補足は2026年3月時点。市場調査セクションでも価格言及がある場合の時点整合性に注意が必要。レポート冒頭に明記されているが、地域別深掘りメモ内の価格引用に時点が混在している箇所がある。

---

**総合評価: 92% PASS（44/48項目）**

レポートは全13必須地域をカバーし、各地域のGPU利用パターン、資金源、政府プログラム、AIXS示唆を高い網羅性で記載している。4つのFAIL項目はいずれも「体系的な欠落」であり、既存の記載内容が不正確というわけではない。推奨アクションに従って補完することで、市場調査セクションの完成度をさらに向上できる。
