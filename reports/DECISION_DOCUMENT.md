# AIXS 意思決定ドキュメント

調査日: 2026-03-28〜29 | 使用ツール: Claude Opus 4.6 + GPT-5.4-pro + Gemini Deep Research
分析ファイル: 14ファイル、合計約448KB | 独立検証: GPT-5.4-pro 26クエリ + o3フォールバック

---

## 1. 結論（先に読むべき）

### やるべきか？

**Conditional Go（条件付き実行）。**

GPUクラウド市場は実在し急成長中（$43.7B、CAGR 16-38%）であり、日本市場には「GPU + 実験管理統合」の明確なホワイトスペースが存在する。フルビジョン（GPU+量子+ラボ装置統合）の直行は自殺行為だが、「1つのワークフロー特化 → 段階拡張」戦略で$500K以下の初期投資で実験可能であり、失敗時の最大損失が限定的。ただし成功確率は楽観的に見ても4-6%であり、厳格なKill Criteriaの適用が条件。[README.md / gpt54pro_verdict_review.md]

### 成功確率

| 分析者 | 確率 | 前提 |
|---|---|---|
| 5エージェント合議（Claude x3 + GPT-4o + Gemini DR） | 8-12% | 修正戦略採用、段階的フェーズイン [debate_synthesis_final.md] |
| GPT-5.4-pro リアリティチェック | 5-8% | 一般SaaSなら妥当、GPUクラウドなら下限寄り [gpt54pro_reality_check.md] |
| o3 独立検証（実データベース） | 2.3-6% | PMF到達率19%、ハイパースケーラー競合後生存率8.7%を使用 [gpt54pro_verdict_review.md] |
| o3 修正戦略採用時 | 4-6% | コンサル+SaaS+論文再現に集中した場合 [gpt54pro_verdict_review.md] |
| o3 フルビジョン | 2-3% | GPU+量子+ラボ装置統合を同時追求した場合 [gpt54pro_verdict_review.md] |

**統合判断: 4-6%（データドリブンの中央推定）。8-12%は「全てがうまくいった場合」の上限。**

矛盾の理由: 合議の8-12%は各エージェントの主観的確率の中間値。o3の2.3-6%はPLG型B2R SaaSのPMF到達率19%（n=27社）、ハイパースケーラー競合後のARR$20M超達成率8.7%（n=126社）等の実データに基づく再計算。[citation_verification.md]

### もしやるなら、最初にやるべき3つのこと

1. **研究者50人インタビューでWTP（支払意向）を検証する。** 月額2万円以上の支払意向が30%以上なければ即ピボット。o3は独自調査（n=136）で「GPU以外も一元管理したい」が57%と報告しており、需要の方向性は確認済みだが、「AIXSに払うか」は未検証。[gpt54pro_verdict_review.md]

2. **「LoRAファインチューニング+評価」など1つのワークフローで圧倒的UXを作る。** 汎用プラットフォームではなく特定ワークフローに集中。GPT-5.4-proの#1推奨。RunPod/Lambda/さくらDOKのAPI統合で供給側Day 1確保。[README.md / gpt54pro_reality_check.md]

3. **自社GPUを絶対に購入しない。** 自社GPU所有モデルの粗利は-28.9%、リースモデルは-44.9%。マーケットプレイス/再販モデル（粗利66.7%、手数料ベース）で開始し資本効率を最大化。[analysis_viability_moat.md]

### 絶対にやってはいけない3つのこと

1. **初日からフルビジョン（GPU+HPC+量子+ラボ装置）を追わない。** 成功確率が4-6% → 2-3%に半減する。量子のNISQ期は実用的用途限定、ラボ装置API標準化は未成熟。量子・ラボ装置は2028年以降。[debate_synthesis_final.md / gpt54pro_verdict_review.md]

2. **GPU価格で競争しない。** RunPod H100 PCIe $1.99/hr（市場最安）に価格で勝つのは不可能。Layer 1（GPU単体）ではなくLayer 2-3（GPU+実験管理+ワークフロー統合）で勝負する。[README.md / gpt54pro_price_comparison.md]

3. **6ヶ月間フィードバックなしで走らない。** AI中央値寿命は18ヶ月。Month 1で有料1人ゼロなら強い警告、Month 3で有料50人未満なら市場からの明確な「No」。元のKill Criteria「6ヶ月で有料10人」はYC基準で「既に死んでいる」と同義。[analysis_kill_criteria_v2.md]

---

## 2. 市場：誰に売るか

### ターゲット顧客（優先順）

| 順位 | ペルソナ | 月予算 | ペイン | なぜAIXS？ | 根拠 |
|---|---|---|---|---|---|
| 1 | AI論文再現研究者（30-45歳、企業研究者） | $200-1,000 | 環境依存性解消に数日〜数週間、再現結果の比較ツールなし | 論文再現テンプレート+自動比較ダッシュボード。Papers with Code閉鎖後の空白 | analysis_pricing_gtm.md |
| 2 | AI/ML研究者（院生〜ポスドク） | 自費$0-50 / 研究費$100-500 | ABCIキュー待ち数時間〜数日、Colab不安定、実験管理が手動 | 即時GPU確保+実験管理統合、ABCI/さくら併用 | analysis_pricing_gtm.md |
| 3 | AIスタートアップ創業者（1-3人） | $500-15,000 | インフラ管理に時間、スケール設計の負債 | 開発→本番の一気通貫、チーム機能 | analysis_pricing_gtm.md |
| 4 | 自動研究システム運用者 | $500-5,000 | インフラ構築が研究以上に時間消費 | API-first、ワークフローエンジン内蔵、リソース自動スケーリング | analysis_pricing_gtm.md |
| 5 | バイオ・材料科学ML研究者 | $500-3,000 | GPU計算とHPC計算が別インフラ、データ連携が手作業 | GPU+HPC統合（Phase 2以降） | analysis_pricing_gtm.md |

### 市場規模

| レベル | 金額 | 根拠 |
|---|---|---|
| TAM | $43.7B（2025年）→ $144.6B（2033年） | Grand View Research GPU-as-a-Service市場 [citation_verification.md: Verified] |
| SAM | $8B-$15B（2030年） | R&D特化コンピュート。GPUaaS市場の10-15%がR&D用途 [analysis_viability_moat.md] |
| SOM（初年度） | $65K-$261K | 日本市場R&Dコンピュート。SAM x 5%(日本) x 0.5-2%(新規参入シェア) [analysis_financial_model.md] |

**注意:** Advocate主張のTAM $80B+はハードウェアリセール・コロケーションを重複計上した水増し。o3はOmdia実売上$41.2Bが実数と指摘。[gpt54pro_verdict_review.md]

---

## 3. 競合：誰と戦うか

### 価格比較（H100 1台 x 72時間、論文再現実験の総コスト）

| 順位 | プロバイダー | 総コスト | GPU単価/hr | 強み | 弱み |
|---|---|---|---|---|---|
| 1 | Vast.ai | **$131** | $1.80 | 市場最安、秒課金 | ホスト品質不安定、データ永続は自己管理 |
| 2 | RunPod | **$219** | $2.99 | 秒課金、Serverless、永続ストレージ | 実験管理なし、GPU枯渇報告頻発（2026年3月） |
| 3 | Paperspace | $185 | $2.24 | Notebook共有、秒課金 | InfiniBand無し、H100は北米のみ |
| 4 | Lambda Cloud | $225 | $2.99 | JupyterLab標準、1-Click Clusters | 東京リージョンなし、永続ストレージ別途 |
| 5 | Together AI | $259 | $3.49 | 研究〜推論まで同一クラスタ | Notebook限定的、日本語サポートなし |
| 6 | Modal | $284 | $3.95 | 最高DevX、Python SDK | セッション終了でボリューム削除、分散は自己構築 |
| 7 | ABCI 3.0 | $318 | $4.40 | 6,128 H200、学術価格 | 事前審査・キュー制約、カード払い不可 |
| 8 | HF Endpoints | $337 | $4.50 | ワンクリックデプロイ | 大規模学習非想定 |
| 9 | CoreWeave | $464 | $6.42 | InfiniBand 3200Gbps、K8s native | 日本語・学割なし |
| 10 | Azure | $504 | $6.98 | エンタープライズ統合 | 最高価格帯 |

出典: gpt54pro_price_comparison.md（2026-03-28時点のスナップショット。GPU価格は3-6ヶ月で大幅変動する）

### 直接競合トップ5と各社の弱点

| 競合 | 強み | 弱点（AIXSが突ける） | 根拠 |
|---|---|---|---|
| Modal（ARR ~$50M、評価額$2.5B報道） | 最高DevX、Python SDK、サーバーレス | 実験管理なし、長時間学習タイムアウト、Python限定 | gpt54pro_financial_critique.md / README.md |
| RunPod（ARR $120M、50万開発者） | 市場最安級、秒課金、50万ユーザー | 実験管理なし、チーム管理なし、GPU枯渇問題 | gpt54pro_financial_critique.md / gpt54pro_price_comparison.md |
| CoreWeave+W&B（売上$5.1B、W&Bを$1.7Bで買収） | GPU+実験管理統合実現済み、圧倒的規模 | 研究ラボ向けUXが弱い、価格が高い、物理世界統合なし | gpt54pro_verdict_review.md |
| Lambda Labs（ARR $500M+推定） | シンプル、1-Click Clusters | SSH+JupyterLabのみ、実験管理なし | gpt54pro_financial_critique.md |
| Together AI | 研究→推論一貫 | A100/L40S提供なし、汎用ワークロード不可 | README.md |

### 最大脅威

**Microsoft Discovery（脅威度9/10）。** 2025年5月Build発表済み。研究者向けAIエージェントチームによるR&D加速プラットフォーム。200時間で新型冷却材プロトタイプを発見した実績。AIXSのビジョンと直接競合。[analysis_competitive_scenarios.md]

**対策:** Discoveryは製薬・材料科学に特化傾向。AIXSはCS/AI/物理/工学研究のワークフローに特化 + マルチクラウド中立性 + 日本市場のローカル優位性（ISMAP、日本語、年度予算）で差別化。大手参入はカテゴリー認知度を上げる効果もある（Salesforce参入後にCRM市場が急拡大した前例）。[analysis_competitive_scenarios.md]

**CoreWeave+W&B統合（脅威度8/10）。** AIXSのコアバリュー「GPU+実験管理」を$1.7B買収で実現済み。ただし量子・ロボット・物理実験装置の統合は射程外。[debate_synthesis_final.md]

---

## 4. ビジネスモデル：どう稼ぐか

### 推奨モデル（3段階移行）

| Phase | 期間 | モデル | 粗利 | 根拠 |
|---|---|---|---|---|
| 1 | 0-12ヶ月 | コンサル+API統合再販 | 30-40% | PMF検証、顧客ペイン理解。ただしコンサル売上比率は30%以下に制限（人月商売化リスク）。Accenture粗利31.9% [gpt54pro_reality_check.md] |
| 2 | 12-24ヶ月 | SaaS+GPU仲介 | 40-55% | プロダクト化、スケール準備。RunPod/Lambda API統合、クレジット包含型サブスク [debate_synthesis_final.md] |
| 3 | 24-36ヶ月+ | マネージドマーケットプレイス | 55-65% | スケール、ネットワーク効果。SaaS比率60%以上で65%粗利が射程内 [README.md] |

### 価格プラン（GPT-5.4-pro批判を反映した改定版）

| プラン | 月額 | 内容 | 原価（1.3倍補正後） | 粗利 | GPT-5.4-proの批判と対応 |
|---|---|---|---|---|---|
| Free | $0 | T4/L4 20hr | $7-12 | -- | **無料枠が厚すぎる** → T4 3-5hrに削減、または学術認証付き無料枠に変更を推奨 [gpt54pro_reality_check.md] |
| Starter | $29 | T4換算30hr（改定後） | $16.51 | **43%** | 元50hr→30hrに削減で粗利改善。Colab Pro($10)との価格ギャップを意識 [analysis_financial_model.md] |
| Pro | $99 | T4換算120hr、H100 15hr相当（改定後） | $58.18 | **41%** | 元H100 25hr→15hrに削減。$2.50/hr調達なら黒字だが$3.29/hrなら薄利 [gpt54pro_financial_critique.md] |
| Team | $79/人 | T4換算250hr/チーム（改定後） | $118.95(3人) | **50%** | GPU economics は健全。「なぜ個人Proより時間少ないのにTeamに高WTP？」→チーム管理機能で正当化必要 [gpt54pro_financial_critique.md] |
| Power | $299 | T4換算400hr、H100 50hr相当（改定後） | $185.25 | **38%** | 元H100 100hr→50hrに削減。100hr維持では粗利$30しか残らない [gpt54pro_financial_critique.md] |

### ユニットエコノミクス（現実的な数字）

- **H100 1台の年間コスト:** $15,453（減価償却$11,776 + 電力$674 + コロケーション$3,003）[gpt54pro_financial_critique.md: Epoch AI + EIA + CBRE計算]
- **H100 1台の年間売上（稼働率70%、$2.50/hr）:** $15,330 [gpt54pro_financial_critique.md]
- **粗利:** -0.8%（ほぼブレークイーブン）。**$2.50/hrでの自社GPU所有は利益が出ない。**
- **RunPodの実際のテイクレート:** 20% [SEC開示、citation_verification.md: Verified]
- **Vast.aiの実際のテイクレート:** 25% [公式FAQ、citation_verification.md: Verified]
- **RunPodの粗利率:** Sacra推定60-70% vs GPT-5.4-pro推定15-25%
  - **矛盾の理由:** 会計定義の違い。Sacraはマーケットプレイス手数料売上ベース（agent/net revenue）のCommunity Cloud部分のみ。GPT-5.4-proはGMV全額売上計上の全社粗利率（Secure Cloud含む、GPU原価が乗る）。AIXSの事業計画では売上=プラットフォーム手数料（net revenue）と明記すべき。その場合66.7%粗利は成立しうる。[citation_verification.md]

---

## 5. 資金計画

### 18ヶ月P&L（基本シナリオ）

| 月 | 有料ユーザー | MRR | 月間コスト | 月間損益 | 累積損益 |
|---|---|---|---|---|---|
| M1 | 0 | $0 | $19,500 | -$19,500 | -$19,500 |
| M3 | 3 | $120 | $19,578 | -$19,458 | -$58,448 |
| M6 | 20 | $1,160 | $20,254 | -$19,094 | -$116,193 |
| M12 | 110 | $10,450 | $31,493 | -$21,043 | -$252,212 |
| M18 | 289 | $36,703 | $53,757 | -$17,054 | -$381,147 |

出典: analysis_financial_model.md（バイアス補正適用：ユーザー数=楽観の50%、転換率=業界中央値の70%、churn=業界平均+20%、コスト=1.3倍）

### 必要資金

| 項目 | 金額 | 根拠 |
|---|---|---|
| **推奨シード** | $500K-$750K | 18ヶ月バーン$381K + バッファ30% = $495K [analysis_financial_model.md] |
| ランウェイ（$500K） | 約24ヶ月 | M18時点残高~$119K [analysis_financial_model.md] |
| BEP（損益分岐点） | M30-M36（Y3） | 自社インフラ移行による粗利改善+NRR向上で初の営業黒字+5% [analysis_financial_model.md] |
| **公的資金活用** | $100K-$500K（1年目） | NEDO DTSU STS 最大¥75M、ものづくり補助金最大¥1,250万、JST CREST等 [analysis_financial_model.md / README.md] |

### 資金調達ステップ

| ラウンド | 時期 | 調達額 | バリュエーション | トリガー |
|---|---|---|---|---|
| Pre-seed | 0-3ヶ月 | $200K-$500K | $2M-$5M | MVP完成、初期ユーザー |
| Seed | 6-12ヶ月 | $1M-$3M | $8M-$15M | MRR $30K+、PMFの兆候 |
| Series A | 18-24ヶ月 | $5M-$15M | $30M-$60M | MRR $200K+、NDR 120%+ |

出典: README.md。ただし日本VC市場$2.22Bは米国の1/63であり、シード$500K-$2Mが現実的。[debate_synthesis_final.md]

---

## 6. タイムライン：いつ何をやるか

### ローンチ前に学ぶべき事例

| 企業 | チーム | 資金 | ローンチ前にやったこと | 結果 |
|---|---|---|---|---|
| RunPod | 2人（Comcastエンジニア） | $50K自費 | 自宅地下室のマイニングリグをAIサーバーに転用。Redditに「フィードバックと引き換えに無料アクセス」投稿 | 9ヶ月で$1M売上、2年ブートストラップ後$20Mシード。現在ARR $120M [analysis_small_team_launches.md] |
| Cursor | 4人（MITクラスメート） | $400Kプレシード | VS Code fork。AI統合のためExtension APIの限界を回避。10Kアーリーテスター | 7ヶ月で$1M ARR。マーケティング費用ゼロ。現在ARR $1B+、評価額$29.3B [analysis_small_team_launches.md] |
| Bolt.new | StackBlitz内チーム | StackBlitz社内 | WebContainers技術7年開発。Claude 3.5 Sonnet早期アクセスで突破口。90日開発 | 1週間で$1M ARR。ツイート1本でローンチ。5ヶ月で$40M ARR [analysis_small_team_launches.md] |
| Lovable | 小規模チーム | 不明 | AI-nativeコーディングツール | 1週間で$1M ARR。8ヶ月で$100M ARR [analysis_kill_criteria_v2.md] |
| Modal | 少人数 | VC調達 | 最初の1年は顧客ゼロ、さらに6ヶ月収益ゼロ。Stable Diffusion公開後にトラクション開始 | ユニコーン$1.1B確定。ARR ~$50M推定 [analysis_financial_model.md] |

**教訓:** RunPodとModalは「トリガーイベント」まで忍耐した。Bolt.new/Lovable/Cursorは既存技術基盤があった。AIXSにはどちらもないため、より保守的に見積もるべき。

### Week-by-Weekアクションプラン

| 期間 | やること | 達成基準 | 未達の場合 |
|---|---|---|---|
| Week 1-2 | LP公開+ウェイトリスト収集、研究者20人にインタビュー、MVPプロトタイプ作成 | ウェイトリスト100人以上 | ターゲット顧客の再定義。問題の選択が間違っている可能性 |
| Month 1 | MVP公開（RunPod/Lambda API統合+基本実験管理）、Product Hunt/HN投稿 | 有料1人+、MRR $500+ | 強い警告。2週間で改善なければピボット検討開始 |
| Month 2 | フィードバック反映、ワークフローテンプレート追加、日本AI研究コミュニティへの認知拡大 | 有料20人+、MRR $2K+ | ピボット準備。既存顧客全員にインタビュー |
| Month 3 | 機能改善、初期ケーススタディ作成、大学研究室直接アプローチ開始 | **有料50人+、MRR $5K+** | **Go/No-Go判断。** $3K未満→ピボット実行。$1K未満→撤退検討 |
| Month 6 | チーム機能リリース、国プロ案件向けGPU調達BPO機能追加、海外マーケティング小規模開始 | **有料200人+、MRR $20K+** | **撤退判断。** $10K未満→即撤退。$10-20K→最後の30日で方向転換 |

出典: analysis_kill_criteria_v2.md。補正: GPU/インフラスタートアップは消費者向けアプリより初回課金まで2-4週間遅い。Month 6目標は$200K+ ARR（$500K+ではなく）が現実的。

---

## 7. リスクと対策

### Kill Scenarios（致命シナリオ）

| シナリオ | 確率 | 致命度 | 対策 | 根拠 |
|---|---|---|---|---|
| Microsoft Discoveryが研究者向けR&Dプラットフォームとして普及 | 60% | 9/10 | CS/AI/工学研究に特化（Discovery は製薬・材料に傾斜）。マルチクラウド中立性で「補完」ポジション | analysis_competitive_scenarios.md |
| CoreWeave+W&B統合が研究ラボ向けUXを完成させる | 80% | 7/10 | 物理世界統合（Wet Lab）とローカル市場対応で差別化。日本市場のISMAP/日本語がMoat | debate_synthesis_final.md |
| GPU価格が更に30-50%下落しテイクレートを圧縮 | 70% | 6/10 | SaaS層（実験管理、コスト最適化）の比率を60%以上に引き上げ、GPU再販依存度を下げる | gpt54pro_verdict_review.md |
| PMF未達（Month 6で有料50人未満） | 50% | 10/10 | 厳格なKill Criteria適用。Month 3でGo/No-Go判断。GPU-less SaaSまたはMLOpsコンサルへピボット | analysis_kill_criteria_v2.md |
| 資金調達失敗（日本VC市場の構造的制約） | 40% | 8/10 | 公的資金（NEDO DTSU STS最大$500K）併用。ブートストラップ期間はコンサル売上で延命 | README.md / analysis_financial_model.md |

### 主要批判と反論

| 批判 | 反論 | 根拠 | 信頼度 |
|---|---|---|---|
| GPU再販の粗利率は10-20%で事業不成立 | マーケットプレイス手数料ベース（net revenue）なら粗利66.7%。テイクレート10%超で成立 | gpt54pro_reality_check.md（Vast.ai FAQ、RunPod SEC開示で確認済み） | **高** |
| Modal/RunPod/Lambdaが強すぎて後発は無理 | どのプロバイダも「コンピュート+実験管理+モデル比較」を統合提供していない。これが最大のギャップ | README.md（16社比較で確認） | **中** |
| 成功確率8-12%は楽観的すぎる | 実データベースでは4-6%が中央推定。ただし$3-5M ARR・黒字化が目標なら8-12%は妥当 | gpt54pro_verdict_review.md / gpt54pro_reality_check.md | **高** |
| Papers with Code閉鎖は本当に機会か | 空白は「市場そのもの」ではなく「統合UX」。HF Trending Papers+OpenMLが部分代替済み。狭い縦領域に絞るべき | gpt54pro_reality_check.md | **高** |
| コンサル+APIリセールは低リスク | 資本リスクは低いが事業リスクは低くない。人月商売化リスク大。コンサルは3-6ヶ月限定の楔として使い売上比率30%以下に制限 | gpt54pro_reality_check.md（Accenture粗利31.9%、EPAM営業利益率10-11%） | **高** |
| 日本発グローバルDevToolsの前例がない | Sakana AI $2.65B、Treasure Data $600M買収の前例。ただしグローバル展開は段階的に（日本→アジア→欧州） | debate_synthesis_final.md | **中** |
| SaaS機能に$20-30/月のWTPは研究者個人には弱い | 個人には弱い（W&B学術Pro無料、MLflow/ClearML OSS）。チーム管理機能に寄せればWTPは成立。ブレンドARPU $85は「チーム比率がかなり高い」前提 | gpt54pro_financial_critique.md（W&B/MLflow価格で確認） | **高** |

---

## 8. 地域戦略

### どの市場から攻めるか

| 優先度 | 地域 | 理由 | 攻め方 | 根拠 |
|---|---|---|---|---|
| 1 | **日本** | METI FY2026予算¥1.23T。ABCI 3.0キュー待ち問題。国内全プロバイダにMLプラットフォーム機能なし | ABCI/さくら補完、ISMAP認証、日本語対応、年度予算制度適応。「データ主権+研究加速」 | README.md / gpt54pro_verdict_review.md |
| 2 | **韓国** | KRW 10.1T ($7.3B) AI予算。260,000+ GPU確約。日本と類似の研究文化 | 英語対応MVP → 韓国語ローカライズ | README.md |
| 3 | **シンガポール** | RIE2030 S$37B。ASEANハブ。DC-CFA規制でローカル需要 | NUS/NTU等の英語系大学をターゲット（o3推奨） | gpt54pro_verdict_review.md / README.md |
| 4 | **UK** | £500MソブリンAI基金。EU規制なしで参入しやすい | AIRR互換、英語圏で展開コスト低 | README.md |
| 5 | **EU** | InvestAI EUR 200B。AI Act+GDPRが非EU提供者への参入障壁（逆にAIXSには有利） | 「Sovereign by design -- EU AI Act Ready」。GDPR対応はMoat | README.md |

**米国市場への直接参入は避けるべき。** 300+プロバイダ参入済み、VC$194B（世界の75%）で価格競争には勝てない。[debate_synthesis_final.md]

---

## 9. データの信頼性

### 最も信頼できる数字

| 数字 | 値 | 出典 | 検証ステータス |
|---|---|---|---|
| RunPod ARR | $120M+、500K+開発者 | 公式プレスリリース（2026年1月20日） | Verified |
| CoreWeave 2025売上 | $5.131B | 公式IR | Verified |
| Vast.ai テイクレート | 25%（hosts receive 75%） | 公式FAQ | Verified |
| H100オンデマンド価格 | $1.99-$6.88/hr | 各社公式価格ページ（2026-03-28時点） | Verified |
| SaaS freemium転換率 | 約5% | OpenView PLGベンチマーク（n=450+） | Verified |
| SaaS $10M ARR到達率 | 13% | ChartMogul 2023レポート | Verified |
| METI FY2026予算 | ¥1.23T（AI・半導体4倍増） | Japan Times報道 | Verified |

### 最も不確実な数字

| 数字 | 幅 | 矛盾の理由 |
|---|---|---|
| RunPod粗利率 | 15-25% vs 60-70%（4倍） | 会計定義の違い（net revenue vs gross revenue） [citation_verification.md] |
| 成功確率 | 2.3-12%（5倍） | 前提条件の違い（各段階の条件付き確率の置き方） [citation_verification.md] |
| TAM | $41B-$134B（3倍） | 定義範囲の違い（純粋GPUaaS vs AIインフラ全体） [citation_verification.md] |
| Pro $99プラン粗利 | -10%〜+41% | H100調達単価次第（$2.50/hr vs $4.50/hr） [citation_verification.md] |
| Lambda ARR | $500M+（推定） | Sacra推定のみ、公式未確認 [citation_verification.md] |

### 追加調査が必要な項目

1. **WTP（支払意向）の一次検証。** 研究者50人インタビュー未実施。「AIXSに月2万円以上払うか」の直接データなし [gpt54pro_verdict_review.md]
2. **H100の安定調達単価。** $2.50/hrで調達できるか否かで粗利が-10%〜+41%と逆転。RunPod/Lambdaとの卸契約交渉が必要 [gpt54pro_financial_critique.md]
3. **日本市場の実際のGPU需要量。** ABCI利用者数千人の具体的な不満点とWTP。さくらDOKの実利用者数・利用パターン [analysis_viability_moat.md]
4. **米輸出規制の影響。** 2026/1「Advanced AI Chip Rule」でH100-SXMの国外再販にBISライセンス要。海外展開時にタイムラグ3-6ヶ月 [gpt54pro_verdict_review.md]
5. **コンサルモデルの具体的なデリバリー設計。** Phase 1でコンサルを楔にする場合、どの程度のリソースで何を提供するか。人月商売化を防ぐ仕組み [gpt54pro_reality_check.md]

---

## 10. 参考ファイル一覧

| ファイル | 内容 | 行数 | 読むべき人 |
|---|---|---|---|
| **README.md** | エグゼクティブサマリー、全レポート統合ダイジェスト | ~900 | **全員（最優先）** |
| **debate_synthesis_final.md** | 5エージェント合議最終判定書、成功確率8-12%、10論点の結論 | ~441 | **全員（必読）** |
| **gpt54pro_verdict_review.md** | o3独立検証、成功確率2.3-6%に下方修正、Kill Criteria強化 | ~210 | **全員（必読）** |
| **gpt54pro_reality_check.md** | 5主張のリアリティチェック（粗利、BEP、成功確率、コンサル、PWC） | ~750 | 財務担当、戦略担当 |
| **gpt54pro_financial_critique.md** | RunPod/Modal/CoreWeave/Lambda/Vast.ai実データ、H100ユニットエコノミクス | ~600 | 財務担当 |
| **gpt54pro_price_comparison.md** | 16社x4シナリオGPU価格比較、研究者ペルソナ別年間コスト | ~500 | プロダクト担当 |
| **analysis_financial_model.md** | 保守的財務モデリング（バイアス補正適用）、18ヶ月P&L | ~700 | 財務担当、投資家向け |
| **analysis_viability_moat.md** | 事業成立性分析、ユニットエコノミクス、Moat構築戦略 | ~807 | 戦略担当 |
| **analysis_pricing_gtm.md** | 8ペルソナ定義、5プラン設計、競合価格比較、LTV/CAC | ~841 | プロダクト担当、マーケティング |
| **analysis_kill_criteria_v2.md** | 攻撃的Kill Criteria、YC/AI速度ベンチマーク、失敗事例 | ~250 | **全員（月次判断の基準書）** |
| **analysis_small_team_launches.md** | RunPod/Cursor/Bolt.new等の創業ストーリー | ~400 | 創業者 |
| **analysis_competitive_scenarios.md** | 5競争シナリオ、Microsoft Discovery脅威度9/10、防御戦略 | ~699 | 戦略担当 |
| **critical_review_deep.md** | Kill Analysis 5シナリオ、VC批判7点への反論、Gemini独立分析 | ~827 | 投資家向け |
| **citation_verification.md** | 主要30クレームの出典検証、矛盾データ5件の原因分析 | ~200 | 全員（数字の裏取り） |
