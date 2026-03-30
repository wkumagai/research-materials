# Kill Criteria徹底検証：「6ヶ月で有料10人未満→ピボット」は2025-2026年のAIスタートアップとして悠長すぎるか？

**結論：Yes。致命的に遅い。**

現在のAIスタートアップの速度感では、6ヶ月で有料10人は**「既に死んでいる」と同義**である。以下、データに基づき論証する。

---

## 1. AIスタートアップの速度ベンチマーク

### 1.1 Tier 1：歴史的速度記録

| 企業 | ローンチ | $1M ARR | $10M ARR | $100M ARR | 備考 |
|---|---|---|---|---|---|
| **Cursor** | 2023年4月 | 2023年11月（7ヶ月） | 2024年中頃（~14ヶ月） | 2024年10月（18ヶ月） | $1B ARRまで24ヶ月。史上最速のSaaS。マーケティング費用ゼロ。コンバージョン率36% |
| **Bolt.new** | 2024年10月3日 | **1週間** | **4週間** | — | $20M ARR 8週間、$40M ARR 5ヶ月。Tweet1本でローンチ |
| **Lovable** | 2025年1月 | **1週間** | 2025年1月末（~4週間） | 2025年7月（8ヶ月） | $200M ARR 11ヶ月。800万ユーザー（2025年末） |
| **ChatGPT** | 2022年11月 | — | — | — | 5日で100万ユーザー、2ヶ月で1億ユーザー。消費者アプリ史上最速 |
| **DeepSeek R1** | 2025年1月20日 | — | — | — | 数週間で3,000万DAU。ウェブトラフィック2,800%増 |
| **Cognition (Devin)** | 2024年 | 2024年9月 | ~2025年初頭 | — | $1M→$73M ARRを9ヶ月で。73倍成長 |
| **ElevenLabs** | 2023年 | — | — | 2025年4月（~20ヶ月） | $200M 10ヶ月後、$330M 5ヶ月後。Twilioが同額に8年かかった |
| **Midjourney** | 2022年 | — | — | 2023年（~12ヶ月） | $500M ARR（2025年5月）。外部資金調達ゼロ。社員40-50人 |

### 1.2 Tier 2：インフラ/GPU系

| 企業 | 創業 | $1M ARR | $120M ARR | 備考 |
|---|---|---|---|---|
| **RunPod** | 2022年 | 9ヶ月（ブートストラップ） | 2026年1月（~3.5年） | Redditの投稿から開始。50万開発者。NDR 120% |

### 1.3 新しい「正常」

- **2025年のStripe Atlasデータ**: 最初の6ヶ月で$100Kに到達するスタートアップが2024年比56%増加。到達速度も11%高速化（108日 vs 121日）
- **TechCrunch（2026年2月）**: $10M ARRを3ヶ月で達成するスタートアップの数が2024年比で2倍
- **AI-nativeスタートアップ**: 6ヶ月で$1M ARR到達確率が従来の3倍、12ヶ月で$10M ARR到達確率が8倍
- **2025年の新規スタートアップの20%**: 30日以内に最初の有料顧客を獲得

---

## 2. YC W24/S24/W25バッチデータ

### 2.1 バッチ構成

| バッチ | 企業数 | AI比率 | 特記事項 |
|---|---|---|---|
| **W24** | 260社 | 50-67% | 27,000件の応募から選抜 |
| **S24** | 255社 | 67% | AI企業が3分の2 |
| **Fall 2024** | — | 87% | AI企業が圧倒的多数 |
| **Spring 2025** | 144社 | 50%+がエージェントAI | エージェントAIが主流に |
| **S25** | 169社 | 88% | AI-nativeが標準 |
| **W26** | ~200社 | — | **14社が$1M ARRをデモデイで達成**（過去最高） |

### 2.2 デモデイ時点の収益ベンチマーク

**YCの3ヶ月バッチ期間中の成績：**

| ティア | 割合 | ARR | 備考 |
|---|---|---|---|
| **トップティア** | 5-10% | $150K-$500K ARR | ラウンド即完売。$25-40M Valuation |
| **ミッドティア** | 60% | $36K-$60K ARR（$3-5K MRR） | パイロット段階が多い |
| **ボトムティア** | 30% | $0（LOIまたはパイプラインのみ） | $15-20M Cap |
| **W26トップ** | 7%（14/200社） | **$1M+ ARR** | バッチ期間中に達成。過去最高記録 |

**重要な変化（Garry Tan談、2025年3月）：**
> "YCスタートアップは週次収益成長率10-20%を達成している。歴史的な2-4%と比較すると5倍速い"

- W25では4分の1の企業が$100K MRR超を達成（以前は$20-30K MRRで例外的だった）
- Fall 2024はバッチ期間中に平均3倍の収益成長を達成した初のバッチ
- **25%のYCスタートアップはコードの95%がAI生成**

### 2.3 「6ヶ月で有料10人」はYC基準でどうか？

**完全に不合格。**

- YCのバッチ期間はたった3ヶ月
- その3ヶ月で、**ボトムティア（30%）でさえ**LOIやパイプラインを持つ
- ミッドティア（60%）は$3-5K MRRを達成
- 有料10人は月$200（$20/月×10人）= **$2.4K ARR**
- これはYCの**3ヶ月バッチ終了時のボトム30%以下**

---

## 3. 「遅すぎて死んだ」AIスタートアップの事例

### 3.1 競合に先を越されたケース

| 企業 | 何が起きたか | 教訓 |
|---|---|---|
| **Jasper AI** | 2022年に$1.5B Unicorn。2023年のChatGPT/Claude登場で差別化喪失。収益$120M→$35M（53%減）。CEO交代、レイオフ。Valuation 20%カット | **AIラッパーは12ヶ月以内にコモディティ化する** |
| **Inflection AI (Pi)** | $4B評価。Pi chatbot市場シェア獲得失敗。2024年3月、MSがほぼ全員を吸収。CEOのMustafa SuleymanがMS入り | **消費者向けチャットボットの窓は数ヶ月で閉じた** |
| **Character.AI** | Googleに$2.7Bライセンス取引で創業者流出。収益化に常に苦戦。自社モデル開発を断念 | **ユニットエコノミクスなき成長は売却以外の出口がない** |
| **Adept AI** | Amazonに人材吸収。ソフトウェアタスク自動化の約束を実現できず | **デモとプロダクトのギャップが致命的** |
| **CodeParrot** | YC出身。Figma→コード変換。GitHub Copilot/Replitの拡張で差別化喪失。MRR最高$1.5K。複数回ピボットも失敗 | **大手の機能追加スピードに勝てない** |
| **Tune AI (旧Nimblebox)** | MLプラットフォーム→GenAIプラットフォームにピボット。クラウド各社が類似ツーリングを低コスト提供。無料ユーザーばかりで収益化失敗 | **インフラコストvs無料ユーザーの罠** |
| **Stability AI** | $100M+調達。キー人材流出（Stable Diffusion開発者3名離脱）。AWSの支払い不能報道。CEO交代 | **莫大な資金もバーンレート管理なしでは意味がない** |
| **Builder.ai** | MS支援。$1.2B評価。$445M消費。「AI開発」が実際はオフショア人力作業だった。破産申請 | **AIの嘘は致命的** |

### 3.2 AI Wrapperの大量死

- 2024年：14,000+の新AIスタートアップがローンチ
- 2025年：3,800社がシャットダウン（27%）
- 2026年初頭：さらに1,800社が閉鎖（追加13%）
- **合計：24ヶ月以内に40%が死亡**
- AIスタートアップの失敗率は90%（従来テック企業の70%より大幅に高い）
- **中央値寿命：18ヶ月**

### 3.3 共通パターン：なぜ「遅い」が致命的か

1. **コモディティ化速度**: OpenAI/Anthropic/Googleが四半期ごとに機能を追加。今日の差別化は来四半期のコモディティ
2. **GPUコスト競争**: H100の時間単価は$6.98→$1.49に急落（2024-2026年）。マージンが消える速度が速い
3. **人材流動性**: 大手の「疑似買収」（MS-Inflection、Google-Character.AI、Amazon-Adept）で小規模チームは常に人材流出リスク
4. **資金調達の窓**: 2025年Q1にAIスタートアップ資金調達が23%急落。「どうやって稼ぐのか？」が問われる時代に突入

---

## 4. 攻撃的なKill Criteria提案

### 前提

- AI/GPUインフラまたはAIアプリケーション領域のスタートアップ
- 2-3人の創業チーム
- プロダクトは開発可能な状態（技術的な不確実性は限定的）

### Week 1-2（ローンチ前/直後）

| 項目 | 定量目標 | 根拠 | 未達の判断 |
|---|---|---|---|
| **ランディングページ公開** | ウェイトリスト100人以上 | Bolt.new/LovableはTweet1本で爆発。ウェイトリストが集まらない=問題の選択が間違っている可能性 | 問題の再定義を検討。ターゲット顧客との会話を20件実施 |
| **初期プロトタイプ** | 動作するMVPが存在 | 2025年のYCスタートアップの25%はコード95%がAI生成。MVP作成は週単位の作業 | チームの技術力に問題。即座に評価 |
| **初期ユーザーテスト** | 5人以上が実際に使用 | RunPodはReddit投稿で無料アクセスを提供しフィードバック獲得 | **継続**：まだ早い。ただし興味の低さを記録 |

### Month 1（ローンチ後4週間）

| 項目 | 定量目標 | 根拠 | 未達の判断 |
|---|---|---|---|
| **最初の有料顧客** | **1人以上**（金額不問） | 2025年の新規スタートアップの20%は30日以内に初課金。Bolt.new/Lovableは1週間で$1M ARR | 未達→**強い警告シグナル**。誰も$1も払わないなら、問題設定が間違っている。2週間で改善なければピボット検討開始 |
| **アクティブユーザー** | 無料含め50人以上が週次で使用 | — | 未達→マーケティング/チャネルの問題か、プロダクトの問題かを切り分け |
| **ユーザーフィードバック** | NPS調査実施、Detractorの理由把握 | — | 実施しない→盲目的な開発。即座に実施 |
| **MRR** | $500+（理想は$1K+） | YCミッドティアはバッチ3ヶ月で$3-5K MRR到達 | **継続判断**：成長トレンドが上向きなら継続。フラットなら危険 |

### Month 2（ローンチ後8週間）

| 項目 | 定量目標 | 根拠 | 未達の判断 |
|---|---|---|---|
| **有料顧客数** | **20人以上** | Bolt.newは8週間で$20M ARR。これは異常値だが、20人の有料は最低ライン | 未達→**ピボット準備開始**。既存顧客10人にインタビュー。何が足りないかを特定 |
| **MRR** | $2K+（理想は$5K+） | YCボトムティアですらLOIがある段階。$2Kは最低限の市場シグナル | 未達→**仮説の根本的見直し**。2週間でピボット方向を決定 |
| **週次成長率** | 15%以上 | Garry Tan: YCスタートアップは10-20%/週。15%未満は下位 | 10%未満→**赤信号**。チャーンが成長を食っている可能性 |
| **リテンション** | Week 1→Week 4の継続率30%以上 | — | 20%未満→プロダクトが解決する問題が弱い |

### Month 3（ローンチ後12週間）—— **最初の重大判断ポイント**

| 項目 | 定量目標 | 根拠 | 未達の判断 |
|---|---|---|---|
| **有料顧客数** | **50人以上** | YCバッチは3ヶ月。トップ10%は$150K-$500K ARR。50人×$20/月=$12K ARRはミッドティアの下限 | 未達→**ピボットまたは撤退を真剣に検討**。「もう3ヶ月あれば」は危険な思考 |
| **MRR** | $5K+（理想は$10K+） | YCミッドティア=$3-5K MRR。3ヶ月で$5K未達はボトム30%圏 | $3K未満→**ピボット実行**。$1K未満→**撤退検討** |
| **NDR（Net Dollar Retention）** | 100%以上 | 既存顧客が拡大利用しているか。RunPodのNDR 120%が世界クラスの基準 | 80%未満→顧客が離脱している。プロダクトに根本的問題 |
| **オーガニック成長比率** | 50%以上が口コミ/検索経由 | Cursor: マーケティング費用ゼロで$100M ARR。プロダクトが良ければ広告不要 | 全成長が有料広告依存→ユニットエコノミクスが成立しない |
| **チャーン率** | 月次10%未満 | a16z: 「持続的成長は超高速成長より重要」。チャーンが高い成長は砂上の楼閣 | 15%以上→**プロダクト再設計が必要** |

### Month 6（ローンチ後24週間）—— **最終判断ポイント**

| 項目 | 定量目標 | 根拠 | 未達の判断 |
|---|---|---|---|
| **有料顧客数** | **200人以上** | Lovableは6ヶ月で$50M ARR（異常値）。200人は保守的だがPMFの最低証明 | 100人未満→**ピボットまたは撤退**。50人未満→**即撤退** |
| **MRR** | $20K+（理想は$50K+） | $20K MRR = $240K ARR。AI-nativeなら6ヶ月で$1M ARR到達確率は従来の3倍。$240Kは下位 | $10K未満→**撤退**。$10-20K→最後の30日で方向転換。改善なければ撤退 |
| **ARR** | $100K+（理想は$500K+） | Cursor: 7ヶ月で$1M ARR。ElevenLabs: 20ヶ月で$100M ARR。$100Kは最低ライン | $50K未満→**撤退確定** |
| **成長率** | 月次20%以上 | — | 10%未満が3ヶ月連続→市場の天井に到達。ピボット必須 |
| **バーンマルチプル** | 3x以下 | Net Burn ÷ Net New ARR。Cognition: バーン$20M未満で$73M ARR | 5x以上→資金効率が悪すぎる。10x以上→即座にコスト構造を見直し |

---

## 5. 元の基準との比較

| 基準 | 元の「6ヶ月で有料10人」 | 提案する攻撃的基準 | 差異 |
|---|---|---|---|
| **Month 1** | （基準なし） | 有料1人+, MRR $500+ | 早期の市場シグナル検出 |
| **Month 2** | （基準なし） | 有料20人+, MRR $2K+ | ピボット判断の前倒し |
| **Month 3** | （基準なし） | 有料50人+, MRR $5K+ | YCバッチ終了時のミッドティア基準 |
| **Month 6** | 有料10人 | **有料200人+, MRR $20K+** | **20倍の顧客数、40倍以上のMRR** |

### なぜ元の基準が危険か

1. **6ヶ月間フィードバックなし**: Month 1-5に判断基準がないため、間違った方向に5ヶ月走り続けるリスク
2. **有料10人は統計的に無意味**: 友人・知人10人で達成可能。市場からのシグナルではない
3. **MRR基準がない**: 10人×$1/月でも「達成」。収益規模の基準が欠如
4. **競合の速度を無視**: Bolt.newが1週間で$1M ARRを出す世界で、6ヶ月で$200は「プロダクトが存在しない」と同義
5. **AI中央値寿命は18ヶ月**: 6ヶ月でPMFの兆候がなければ、残り12ヶ月で逆転する確率は極めて低い

---

## 6. GPU/インフラスタートアップ特有の考慮事項

GPU/インフラは消費者向けアプリと速度感が異なるため、補正が必要：

| 要素 | 消費者向けアプリ | GPU/インフラ | 補正理由 |
|---|---|---|---|
| 初回課金まで | 1-2週間 | 2-4週間 | 技術的インテグレーションが必要 |
| PMFシグナル | $1M ARR（3ヶ月） | $100K ARR（3ヶ月） | 顧客単価が高い代わりに顧客数が少ない |
| Month 6目標 | $500K+ ARR | $200K+ ARR | ただしNDR 110%以上が必須 |
| チャーン | 月次10%未満 | 月次5%未満 | インフラは切り替えコストが高い。チャーンが高い=致命的品質問題 |

**GPU市場特有のリスク:**
- H100価格が$6.98→$1.49/hrに急落（2024-2026年）
- CoreWeave, Lambda, RunPod, VAST.aiとの価格競争
- 「差別化なきGPUリセラー」は利益が蒸発する
- **Month 3で差別化要因（独自機能/特定ワークロード最適化/地域特化）が明確でなければピボット**

---

## 7. 最終提言：改訂版Kill Criteria Decision Tree

```
Week 2: ウェイトリスト100人未満？
  → ターゲット顧客20人にインタビュー。問題の再定義。

Month 1: 有料顧客0人？
  → 強い警告。2週間の集中スプリント。
  → それでも0人 → ピボット方向の探索開始。

Month 2: 有料20人未満 or MRR $2K未満？
  → ピボット準備。既存顧客全員にインタビュー。
  → 週次成長率10%未満 → ピボット実行。

Month 3: 有料50人未満 or MRR $5K未満？
  → ピボットまたは撤退を決定。「もう少し」は禁句。
  → MRR $1K未満 → 即撤退。

Month 6: 有料200人未満 or MRR $20K未満？
  → 撤退。この時点でPMFがないなら、ない。
  → MRR $10K未満 → 即撤退。リソースの浪費。
```

**最も重要な原則：**

> 2025-2026年のAIスタートアップにおいて、「6ヶ月後に判断する」こと自体が最大のリスクである。判断は**毎週**行い、**Month 3が最初の本気のGo/No-Go**であるべきだ。Bolt.newもLovableもCursorも、6ヶ月時点では既に数千万ドルのARRに到達していた。あなたのスタートアップがMonth 3で50人の有料顧客すら持てないなら、それは市場からの明確な「No」である。

---

## Sources

- [Cursor at $100M ARR - Sacra](https://sacra.com/research/cursor-at-100m-arr/)
- [Cursor Hit $1B ARR in 24 Months - SaaStr](https://www.saastr.com/cursor-hit-1b-arr-in-17-months-the-fastest-b2b-to-scale-ever-and-its-not-even-close/)
- [How Bolt.new hit $40M ARR in 5 months - Growth Unhinged](https://www.growthunhinged.com/p/boltnew-growth-journey)
- [Bolt.new ARR at $4M in just 4 weeks](https://www.arr.club/signal/bolt-new-arr-at-4m-in-just-4-weeks)
- [Bolt.new at $40M ARR - Sacra](https://sacra.com/research/bolt-new-at-40m-arr/)
- [Lovable: How an AI Coding Tool Reached $100M ARR in 8 Months](https://medium.com/@takafumi.endo/lovable-case-study-how-an-ai-coding-tool-reached-17m-arr-in-90-days-f4816e7b3f2b)
- [Lovable nearing 8 million users - TechCrunch](https://techcrunch.com/2025/11/10/lovable-says-its-nearing-8-million-users-as-the-year-old-ai-coding-startup-eyes-more-corporate-employees/)
- [How Lovable Hit $100M Revenue in 8 Months - Latka](https://getlatka.com/blog/lovable-revenue-valuation/)
- [Perplexity AI crosses $100M ARR](https://americanbazaaronline.com/2025/03/27/perplexity-ai-crosses-100-million-in-annualized-revenue-says-aravind-srinivas-461224/)
- [RunPod AI Cloud Surpasses $120M ARR](https://www.runpod.io/press/runpod-ai-cloud-surpasses-120m-in-arr)
- [RunPod $120M ARR - TechCrunch](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
- [DeepSeek AI Statistics 2026](https://www.demandsage.com/deepseek-statistics/)
- [ChatGPT Statistics - Notta](https://www.notta.ai/en/blog/chatgpt-statistics)
- [ElevenLabs $330M ARR - TechCrunch](https://techcrunch.com/2026/01/13/elevenlabs-ceo-says-the-voice-ai-startup-crossed-330-million-arr-last-year/)
- [ElevenLabs $330M ARR in 24 Months - SaaStr](https://www.saastr.com/elevenlabs-just-hit-330m-arr-it-took-twilio-8-years-to-get-there/)
- [Cognition Funding & Growth](https://cognition.ai/blog/funding-growth-and-the-next-frontier-of-ai-coding-agents)
- [Cognition $400M Raise at $10.2B - TechCrunch](https://techcrunch.com/2025/09/08/cognition-ai-defies-turbulence-with-a-400m-raise-at-10-2b-valuation/)
- [Midjourney Bootstraps to $200M Revenue](https://www.sramanamitra.com/2025/03/12/ultralight-startup-midjourney-bootstraps-to-200m-in-revenue/)
- [Midjourney $500M ARR with 40 people](https://signalhub.substack.com/p/midjourney-arr-at-500m-with-40-people)
- [50% of YC W24 Is Built With AI - Crunchbase](https://news.crunchbase.com/venture/yc-winter-batch-2024-ai-startup-seed-funding/)
- [YC S25 Batch Profile - Catalaize](https://catalaize.substack.com/p/y-combinator-s25-batch-profile-and)
- [$1 Million By Demo Day - Tremendous](https://tremendous.blog/2026/03/25/what-the-best-yc-companies-look-like-at-demo-day/)
- [Benchmarks for Valuation at YC - Tremendous](https://tremendous.blog/2024/11/26/benchmarks-for-valuation-and-traction-at-y-combinator/)
- [YC Startups Growing 5X Faster - Garry Tan / Mixergy](https://mixergy.com/interviews/garry-tan-y-combinator-startups-growing-5x-faster-heres-what-changed/)
- [YC Startups Fastest Growing in History - CNBC](https://www.cnbc.com/2025/03/15/y-combinator-startups-are-fastest-growing-in-fund-history-because-of-ai.html)
- [More startups hitting $10M ARR in 3 months - TechCrunch](https://techcrunch.com/2026/02/24/more-startups-are-hitting-10m-arr-in-3-months-than-ever-before/)
- [AI Startups That Shut Down in 2025 - Tech Startups](https://techstartups.com/2025/12/09/top-ai-startups-that-shut-down-in-2025-what-founders-can-learn/)
- [Biggest Startup Failures of 2025](https://www.wearefounders.uk/top-10-startup-failures-of-2025-so-far/)
- [End of the AI Wrapper Era](https://medium.com/@opiaaustin/the-end-of-the-ai-wrapper-era-ae3692837ad7)
- [Jasper Cuts Internal Valuation](https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/)
- [Jasper - Contrary Research](https://research.contrary.com/company/jasper)
- [Google Character.AI Acquihire - Fortune](https://fortune.com/2024/08/02/google-character-ai-founders-microsoft-inflection-amazon-adept/)
- [Inflection AI Pi - IEEE Spectrum](https://spectrum.ieee.org/inflection-ai-pi)
- [Stability AI Chronicle - Turing Post](https://www.turingpost.com/p/stabilityai)
- [GPU Clouds Growing 1,000% YoY - Sacra](https://sacra.com/research/gpu-clouds-growing/)
- [Stripe Atlas Startups 2025 Year in Review](https://stripe.com/blog/stripe-atlas-startups-in-2025-year-in-review)
- [Mastering PMF for AI Founders - Bessemer](https://www.bvp.com/atlas/mastering-product-market-fit-a-detailed-playbook-for-ai-founders)
- [State of Consumer AI 2025 - a16z](https://a16z.com/state-of-consumer-ai-2025-product-hits-misses-and-whats-next/)
- [SaaS Growth Report 2025 - ChartMogul](https://chartmogul.com/reports/saas-growth-the-odds-of-making-it/)
