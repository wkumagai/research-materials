# 少人数スタートアップのローンチ前準備 調査レポート

> 調査日: 2026-03-10
> 対象: 1-5人チームで初期立ち上げに成功したAI/クラウド系スタートアップ6社

---

## 1. RunPod（GPU Cloud）

### 創業者の経歴
- **Zhen Lu**（CEO）と **Pardeep Singh** の2人で創業
- 両者ともComcastのソフトウェアエンジニア出身
- 副業でEthereum（ETH）マイニングをニュージャージーの自宅地下室で運用

### ローンチ前の準備
- **準備期間**: 約3-4ヶ月（2021年末〜2022年初頭）
- Ethereumの「Proof of Stake」移行（The Merge）によりマイニングが非採算化する前に、GPUリグをAIサーバーに転用する計画を立案
- GPU上でのソフトウェア開発体験が「ゴミ」（原文: "hot garbage"）だと感じたことが動機
- 既存のクリプトマイニング用GPUリグをAIワークロード用にアップグレード

### 初期GPU調達
- **台数**: 地下室のマイニングリグ数台からスタート（正確な台数は非公開）
- **調達方法**: 完全に自費（ブートストラップ）
- **初期投資額**: 約$50,000（マイニング用に$15K投入済み + AI用に追加$10K + その他ハードウェア）
- 外部資金調達なし、借入もなし

### 初期資金
- **完全ブートストラップ** — 約2年間、外部資金ゼロで運営
- 無料ティアは一切提供せず、最低限の利益が出る価格設定で自走
- **シード資金**: $20M（2024年5月、Intel CapitalとDell Technologies Capital共同リード）
  - これはブートストラップで$24M以上の売上を達成した後

### 最初のReddit投稿
- **時期**: 2022年初頭
- **内容**: AI関連のsubredditに投稿。「フィードバックと引き換えにAIサーバーへの無料アクセスを提供」
- 複数のAI関連サブレディットに投稿（マーケティング経験がなかったため、Redditが唯一の手段）
- VCのRadhika Malik（Dell Technologies Capital）がこのReddit投稿を見つけてコンタクト

### 最初の有料ユーザー獲得
- Reddit投稿後、無料フィードバック期間を経て有料ユーザーを獲得
- **約9ヶ月で$1M売上**に到達し、Comcastを退職

### ローンチ1ヶ月後
- 具体的な1ヶ月後のユーザー数/MRRは非公開
- ただし、9ヶ月で$1Mということは、月平均約$111K（初月はそれ以下と推定）
- 現在（2026年1月時点）: **$120M ARR**、50万人以上の開発者

### 特筆すべき点
- Hugging Face共同創業者のJulien Chaumondがユーザーとして使っており、サポートチャット経由でエンジェル投資家に
- 無借金経営を貫いた

**Sources:**
- [RunPod Origin Story](https://www.runpod.io/blog/founder-series-1-origin-story)
- [TechCrunch: RunPod $120M ARR](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
- [RunPod Seed Funding](https://www.businesswire.com/news/home/20240508053225/en/RunPod-Raises-$20M-in-Seed-Funding-Co-led-by-Intel-Capital-and-Dell-Technologies-Capital)
- [We Are Founders: RunPod Story](https://www.wearefounders.uk/how-runpod-turned-failed-crypto-rigs-into-a-leading-ai-hosting-platform/)

---

## 2. Cursor（AI Code Editor / Anysphere）

### 創業チームの経歴
4人全員がMIT（コンピュータサイエンス・数学）のクラスメート:

| 名前 | 役職 | 経歴 |
|------|------|------|
| Michael Truell | CEO | USA Computing Olympiad決勝進出、14歳でプログラミングゲーム開発、Google・Two Sigma・Octantでインターン |
| Sualeh Asif | CPO | パキスタン出身、国際数学オリンピック代表、IBMで神経機械翻訳 |
| Arvid Lunnemark | - | 国際情報オリンピックメダリスト、Stripe・Jane Street・QuantCo |
| Aman Sanger | - | 医療AI・エンタープライズML、Google・Bridgewater Associates・You.com |

### Anysphere設立前
- 全員MIT在学中に出会い、AIによるプログラミング変革のビジョンを共有
- 各自がGoogle、Stripe、Bridgewater等のトップ企業でインターン経験

### 最初のプロトタイプ
- **2022年1月**: Anysphere法人設立
- **2022年4月**: $400Kのプレシード資金調達、開発開始
- **2022年後半**: 複数のテストフェーズを経て内部イテレーション
- **2023年3月**: Cursor一般公開

### ベータ版の規模
- **2023年中**: 約10,000人のアーリーテスター
- **2023年末**: 30,000 DAU（日次アクティブユーザー）

### 初期シード資金
- **プレシード**: $400K（2022年4月）
- **シード**: $8M（2023年10月、OpenAI Startup Fundリード）
  - エンジェル: 元GitHub CEOのNat Friedman、Dropbox共同創業者Arash Ferdowsi
- OpenAIアクセラレーターを卒業

### VS Code forkの技術選択
- **理由**: VS Codeの拡張API（Extension API）は、AIが必要とする深いシステムレベル統合（コードベース全体の認識、ターミナル操作、複数ファイルリファクタリング）に対応できない
- VS Codeは後方互換性を維持する必要があり、根本的なアーキテクチャ変更が不可能
- forkにより、VS Codeの馴染みのあるUIを維持しつつ、AI機能をネイティブに統合可能

### 最初の有料ユーザー獲得
- 2023年3月ローンチ後、**2023年中に$1M売上**に到達
- マーケティング支出ゼロで達成
- **20ヶ月で$100M ARR**（2025年1月）

### 現在の規模（2025年末）
- 100万+ DAU、50,000以上の企業利用
- 前年比9,900% ARR成長
- **評価額$29.3B**（Series D: $2.3B調達、Accel・Coatue共同リード）
- ARR $1B超

**Sources:**
- [Contrary Research: Cursor](https://research.contrary.com/company/cursor)
- [Cursor Founders Story](https://www.wearefounders.uk/cursor-founders-the-mit-team-behind-the-400-million-ai-code-editor-revolution/)
- [Wikipedia: Anysphere](https://en.wikipedia.org/wiki/Anysphere)
- [TechCrunch: Anysphere Seed](https://techcrunch.com/2023/10/11/anysphere-raises-8m-from-openai-to-build-an-ai-powered-ide/)
- [SaaStr: Cursor $1B ARR](https://www.saastr.com/cursor-hit-1b-arr-in-17-months-the-fastest-b2b-to-scale-ever-and-its-not-even-close/)

---

## 3. Bolt.new（AI Web Builder / StackBlitz）

### StackBlitz自体のチーム規模
- **創業者**: Eric Simons（CEO）、Albert Pai（CTO）— 2017年創業
- シカゴ出身、ティーンエイジャー時代に出会い一緒にコーディング開始
- 2011年にClassConnect（教育スタートアップ）をImagine K12アクセラレーターで立ち上げ
- **コア技術**: WebContainers（ブラウザ内でNode.jsを動作させるランタイム）— 開発に**7年以上**

### Bolt.newの開発
- **開発人数**: 小規模チーム（StackBlitz内部プロジェクト）
- **開発期間**: **約90日間**（2024年7月〜10月）
  - 2024年2月: 最初のプロトタイプ作成 → モデル性能不足で棚上げ
  - 2024年6月: Anthropic Claude 3.5 Sonnetへの早期アクセスを取得 → これが突破口
  - 2024年7月: 本格開発コミット
  - 2024年10月3日: ローンチ
- ローンチ時のStackBlitzチーム: 約12-15人のエンジニア

### ローンチ前のテスター
- **正式なベータテスター群は設けず** — ローンチ日に直接一般公開
- StackBlitzの既存ユーザーベース（200万MAU以上）が潜在的なアーリーアダプター

### Twitter/Xでのバイラル戦略
- **戦略**: マーケティング予算ゼロ、**ツイート1本のみ**でローンチ
- ユーザーがデモ動画をTwitter、Reddit、YouTube、TikTokに投稿 → オーガニックバイラル
- 創業者Eric Simonsが積極的にTwitterで反応

### $1M ARR到達の経緯
- **ローンチ初日**: $60K ARR追加
- **2日目**: $80K ARR追加
- **1週間後**: 約$1M ARR
- **30日後**: **$4M ARR**
- **2ヶ月後**: **$20M ARR**
- **5ヶ月後**: **$40M ARR**
- 15人のエンジニアリングチームで達成

### 成功の鍵
1. WebContainersという7年の技術蓄積（ブラウザ内でフルスタック開発環境）
2. Claude 3.5 Sonnetの登場タイミング（モデル性能が閾値を超えた）
3. 無料ティア + バイラルデモ（ユーザーが作ったアプリのスクリーンショットがSNSで拡散）

**Sources:**
- [PostHog: How bolt.new works](https://newsletter.posthog.com/p/from-0-to-40m-arr-inside-the-tech)
- [Contrary Research: Bolt](https://research.contrary.com/company/bolt)
- [Lenny's Newsletter: Inside Bolt](https://www.lennysnewsletter.com/p/inside-bolt-eric-simons)
- [Evil Martians: Bolt.new + StackBlitz](https://evilmartians.com/chronicles/bolt-new-from-stackblitz-how-they-surfed-the-ai-wave-with-no-wipeouts)
- [Product Growth: Bolt.new](https://www.productgrowth.blog/p/how-bolt-new-hacked-its-growth)

---

## 4. Lovable（旧GPT Engineer）

### 創業者
- **Anton Osika**（CEO、26歳）— スウェーデン出身、KTH工科大学
- **Fabian Hedin**（CTO）— Stephen Hawkingのコンピュータインターフェースを開発、元SpaceXエンジニアと車椅子技術に従事

### GitHub starsの実績
- 2023年春にGPT Engineerをオープンソースで公開
- GitHub史上最速で成長したリポジトリの1つ: **52,000+ stars**
- これにより強力なコミュニティと認知度を構築

### OSSからSaaSへの転換プロセス

| 時期 | 出来事 |
|------|--------|
| 2023年春 | GPT Engineer OSS公開 → 52K stars |
| 2023年11月 | Lovable（当時GPT Engineer App）設立 |
| 2024年春-夏 | **2回のローンチ失敗**（ユーザーニーズの検証失敗、ブランド不一致） |
| 2024年10月 | プレシード$7.5M調達（Hummingbird、byFoundersリード） |
| 2024年11月 | 「Lovable」にリブランド、Product Hunt #1 & Hacker News #1 |
| 2024年12月 | $1M ARR突破（2週間で） |
| 2025年1月末 | $10M ARR（2ヶ月） |
| 2025年2月 | $17M ARR、50万ユーザー、3万有料顧客 |
| 2025年7月 | $100M ARR（8ヶ月） |

### ローンチ時のチーム人数と資金
- **チーム**: 約15人（ローンチ時）
- **プレシード**: $7.5M（2024年10月）— Hummingbird、byFoundersリード
- チームメンバーに国際情報オリンピック金メダリスト含む

### $1M ARR到達の経緯
1. OSSで300,000人のアドボケイト（支持者）コミュニティを構築済み
2. 2回の失敗から学び、プロダクトとブランドを根本的に再設計
3. Product Hunt #1で爆発的な初動
4. **2週間で$1M ARR、3,000有料顧客**

### 重要な教訓
- OSSで「信頼」と「コミュニティ」を先に構築 → SaaS転換時のCAC（顧客獲得コスト）が極めて低い
- 最初の2回は失敗しており、3回目で成功（失敗を恐れない反復が重要）
- 「GPT Engineer」というブランドが実際の機能を過小評価させていた → リブランドが転機

**Sources:**
- [Inc: Anton Osika](https://www.inc.com/chloe-aiello/5-things-to-know-about-anton-osika-co-founder-of-the-vibe-coding-unicorn-lovable/91223446)
- [Lenny's Newsletter: Building Lovable](https://www.lennysnewsletter.com/p/building-lovable-anton-osika)
- [Contrary Research: Lovable](https://research.contrary.com/company/lovable)
- [TechCrunch: Lovable $100M ARR](https://techcrunch.com/2025/07/23/eight-months-in-swedish-unicorn-lovable-crosses-the-100m-arr-milestone/)
- [Wikipedia: Lovable](https://en.wikipedia.org/wiki/Lovable_(company))
- [Catalaize: Lovable Growth](https://catalaize.substack.com/p/lovables-path-from-open-source-to)

---

## 5. Replicate（ML Model Hosting）

### 創業者の経歴
- **Ben Firshman**（CEO）— **Fig（後のDocker Compose）の作者**。Docker社でオープンソースプロダクトをリード、Docker Machine/Docker Toolboxを出荷
- **Andreas Jansson** — Spotifyの機械学習エンジニア出身

### 初期の技術的準備
- **2020年7月**: 最初のコード（当初「Keepsake」という名前のML向けバージョン管理ライブラリ）
- **2020年11月**: 「Replicate」にリネーム、正式発表
- コア技術: **Cog** — MLモデルを標準的なDockerコンテナ形式にパッケージングするオープンソースツール
  - Firshmanの Docker Compose の経験が直接活きた設計
  - 「MLモデルのデプロイ体験をDocker並みに簡単にする」というビジョン

### 最初のモデルホスティング
- **2021年初頭**: OpenAIがCLIPをリリース → CLIP + GANの組み合わせでDiscordコミュニティが爆発
- **PixRay**がReplicate上で最初の人気モデルの1つに
- **2022年8月**: Stable Diffusion リリースにより、トラフィックが急増 → ここが本格的なPMFの瞬間

### HuggingFaceとの差別化
| 観点 | HuggingFace | Replicate |
|------|-------------|-----------|
| 主な用途 | モデルの発見・共有・トレーニング | モデルをAPIとして即座にデプロイ |
| 対象 | ML研究者・エンジニア | アプリ開発者（MLの専門知識不要） |
| インフラ | ユーザーが管理 | サーバーレスで自動管理 |
| 差別化 | トランスフォーマーライブラリの充実 | 1行のAPIコールで推論実行 |

### 資金調達
- **シード**: $5.3M
- **Series A**: $12.5M（2023年2月、a16zリード）— Y Combinator、Sequoia参加
- **Series B**: $40M（2023年6月、a16zリード）— Nvidia NVentures参加
- **合計**: $57.8M
- **2025年11月**: **Cloudflareに買収**（金額非公開）

### 規模
- 50,000以上のプロダクション対応モデル
- 37人のチーム（2024年時点）

**Sources:**
- [Latent Space: Ben Firshman](https://www.latent.space/p/replicate)
- [Sequoia: Replicate Spotlight](https://sequoiacap.com/article/replicate-spotlight/)
- [TechCrunch: Replicate](https://techcrunch.com/2023/02/21/replicate-wants-to-take-the-pain-out-of-running-and-hosting-ml-models/)
- [a16z: Investing in Replicate](https://a16z.com/announcement/investing-in-replicate/)
- [Cloudflare: Acquisition](https://www.cloudflare.com/press/press-releases/2025/cloudflare-to-acquire-replicate-to-build-the-most-seamless-ai-cloud-for-developers/)

---

## 6. Vast.ai（GPU Marketplace）

### 創業者の経歴
- **Jake Cannell** — MLエンジニア・GPUプログラマー
  - 2010年からLessWrongでAI・計算に関するエッセイを発表
  - 2015年の論文「The Brain as a Universal Learning Machine」でAlphaGoを予測、深層学習によるスケーリングを提唱
- **Christian Horne** — 同じくLessWrongコミュニティ出身
  - 「計算スケーリング仮説がAI支配権に直結する」という信念を共有

### マーケットプレイスのコールドスタート問題
- **解決方法**:
  1. **2年間のプラットフォーム構築** — ホストオンボーディング、検索インターフェース、価格エンジン、Docker管理を全てエンドツーエンドで開発
  2. **ソフトローンチ**: プレスリリースではなく、**友人・家族 + Reddit + Hacker News**に投稿
  3. 「消費者GPUはエンタープライズハードウェアよりはるかに安い」という経済的インセンティブでホストを誘引
  4. 開発者には「ハイパースケーラーより安い」という価格優位性を提供

### 最初のGPUホスト
- 初期のインディペンデントホスト（個人でGPUを持つ人々）をReddit/HNコミュニティから獲得
- マイニングリグの転用ユーザーが自然にホスト側として参入

### 資金・規模
- **資金調達**: $4M（DRW Holdings、Nazare）
- **創業年**: 2016年（一部ソースでは2018年）
- **現在**: 350以上の独立ホスト、17,000+ GPU、前年比310%成長（2024年）
- チーム: 11-50人

**Sources:**
- [Vast.ai About](https://vast.ai/about)
- [Hacker News: Vast.ai](https://news.ycombinator.com/item?id=30736459)
- [AI Magazine: Jake Cannell](https://aimagazine.com/executive/jake-cannell)
- [Crunchbase: Vast.ai](https://www.crunchbase.com/organization/vastai)

---

## 共通パターン分析

### 成功した6社の比較表

| 項目 | RunPod | Cursor | Bolt.new | Lovable | Replicate | Vast.ai |
|------|--------|--------|----------|---------|-----------|---------|
| 創業人数 | 2人 | 4人 | 2人(+既存チーム) | 2人 | 2人 | 2人 |
| 準備期間 | 3-4ヶ月 | 12ヶ月 | 3ヶ月(+7年の技術蓄積) | 12ヶ月(OSS期間含む) | 6ヶ月 | 24ヶ月 |
| 初期資金 | $50K(自費) | $400K(プレシード) | 既存会社の資金 | $7.5M(プレシード) | YC標準 | 不明(少額) |
| $1M ARR到達 | 9ヶ月 | ~12ヶ月 | **1週間** | **2週間** | ~24ヶ月 | 不明 |
| 初期獲得チャネル | Reddit | 口コミ+OpenAI | Twitter 1ツイート | Product Hunt/HN | Discordコミュニティ | Reddit/HN |
| 技術的差別化 | DX重視のGPU管理 | VS Code fork + AI統合 | WebContainers | OSS→SaaS | Cog(Docker for ML) | P2P GPU経済性 |

### 抽出された共通パターン

#### 1. 「技術の蓄積」が爆発的成長の前提条件
- Bolt.new: WebContainersに7年 → 90日で$40M ARR
- Replicate: Docker Composeの経験 → Cogを自然に設計
- Cursor: 競技プログラミング+トップ企業経験 → 高品質なAI統合

#### 2. コミュニティ先行型ローンチ
- 6社中5社がReddit、Hacker News、Discordのいずれかでローンチ
- 広告費ゼロが標準（Cursorはマーケティング支出なしで$100M ARR）
- 「使って見せる」デモがバイラルの核

#### 3. 「タイミング」が資金より重要
- RunPod: ETHマイニング終了 → GPU供給過剰のタイミング
- Bolt.new: Claude 3.5 Sonnet登場 → 初めて使えるコード生成
- Lovable: 「Vibe Coding」トレンドの波

#### 4. 2人のコア創業者パターン
- 6社中5社が2人創業（Cursorのみ4人）
- 典型: 1人がプロダクト/技術、1人がインフラ/ビジネス

#### 5. 失敗は計画の一部
- Lovable: 2回の失敗ローンチ → 3回目で成功
- RunPod: クリプトマイニングの失敗 → AIへのピボット
- Bolt.new: 2024年2月にプロトタイプ棚上げ → 6月に再挑戦

---

## 少人数で成功するスタートアップのローンチ前チェックリスト

### 3ヶ月前（基盤構築）

- [ ] **コアチーム確定**: 2-4人、全員がコードを書ける（非技術co-founderは不要）
- [ ] **技術的優位性の特定**: 既存スキル・経験から生まれる「unfair advantage」を明確化
  - 例: Docker経験→Cog、マイニングGPU→RunPod、WebContainers→Bolt.new
- [ ] **ターゲットコミュニティの特定**: Reddit、HN、Discord等でターゲットユーザーがいる場所を特定
- [ ] **20人以上のカスタマーディスカバリー**: 実際のペインポイントを確認（自分の仮説の検証ではない）
- [ ] **技術プロトタイプ着手**: MVPのコア機能1つに絞る
- [ ] **資金計画**: 最低$10K-$50K（自費 or プレシード）、6ヶ月の滑走路

### 1ヶ月前（MVP完成・テスト）

- [ ] **MVPの動作確認**: コア機能が1つ確実に動く状態
- [ ] **10-50人のアルファテスター確保**: ターゲットコミュニティから直接リクルート
- [ ] **フィードバックループ構築**: Discord/Slackで即座にユーザーと対話できる体制
- [ ] **価格設定決定**: 初日から有料（RunPodの教訓: 無料ティアは不要）
- [ ] **ランディングページ準備**: 30秒で価値が伝わるデモ/スクリーンショット
- [ ] **決済インフラ整備**: Stripe等で即座に課金開始できる状態

### 1週間前（ローンチ準備）

- [ ] **ローンチ投稿の準備**: Reddit/HN/Product Hunt用の投稿文を作成
  - 核心は「何を解決するか」であり「どう作ったか」ではない
- [ ] **デモ動画作成**: 30-60秒の短いデモ（Bolt.newのバイラルはユーザーのデモ動画から）
- [ ] **サポート体制**: 創業者自身がチャット対応（RunPodのHugging Face投資家はサポートチャット経由）
- [ ] **インフラのスケーリング準備**: バイラルした場合のサーバー/APIの拡張計画
- [ ] **メトリクス計測**: DAU、有料転換率、MRRを初日からトラッキング

### 資金の最低ライン

| シナリオ | 最低資金 | 例 |
|----------|----------|-----|
| 完全ブートストラップ（ハードウェア不要） | $5K-$10K | ソフトウェアSaaSのMVP |
| ハードウェア必要（GPU等） | $30K-$50K | RunPod |
| プレシード調達 | $200K-$500K | Cursor ($400K) |
| OSSコミュニティ先行 | $0（開発コストのみ） | Lovable (GPT Engineer OSS) |

### チーム構成の最適パターン

**推奨: 2-3人**
- **Person 1**: フルスタックエンジニア（プロダクト構築のリード）
- **Person 2**: インフラ/バックエンドエンジニア（スケーリング・信頼性）
- **Person 3（任意）**: ML/AIエンジニアまたはデザイナー

**重要な属性:**
- 全員がコードを書ける
- 少なくとも1人がターゲットコミュニティのドメイン知識を持つ
- 「ユーザーとの直接対話」を全員が担当する覚悟

### 最初のユーザー獲得チャネル（優先度順）

1. **Reddit** — ターゲットのsubredditに「フィードバック求む」投稿（RunPod方式）
2. **Hacker News (Show HN)** — 技術的に興味深いプロダクト向け
3. **Product Hunt** — コンシューマー寄りのプロダクト向け（Lovable: #1獲得）
4. **Twitter/X** — デモ動画のバイラル（Bolt.new: ツイート1本で$1M ARR）
5. **Discord** — ニッチコミュニティでの口コミ（Replicate: CLIP/GANコミュニティ）
6. **OSS公開** — 長期戦略として（Lovable: 52K stars → 30万人のアドボケイト）

### ローンチ初週のアクション

| 日 | アクション |
|----|-----------|
| Day 0 | ローンチ投稿（Reddit/HN/PH + Twitter）。創業者が全コメントに返信 |
| Day 1 | フィードバック集約。致命的バグの即日修正。2番目のプラットフォームにも投稿 |
| Day 2-3 | 最初の有料ユーザーとの1on1会話。利用パターン分析 |
| Day 4-5 | フィードバックに基づく緊急改善（1-2機能追加または修正） |
| Day 6-7 | 週次メトリクスの振り返り。翌週の優先順位決定。コミュニティへの進捗共有 |

---

## AIXSの3人チームが真似すべきこと

### 前提
- AIXSはGPUクラウド/AIインフラ領域のスタートアップ
- 3人チーム
- RunPod、Vast.ai、Replicate が最も近い参考事例

### Week 1-2: 基盤整備

| 項目 | やること | 参考事例 |
|------|----------|----------|
| ポジショニング | 「AIXSが解決する具体的なペイン」を1文で定義 | RunPod: "GPU上の開発体験がゴミ" |
| コミュニティ調査 | r/MachineLearning, r/LocalLLaMA, r/StableDiffusion等でユーザーの不満を100件収集 | RunPod: Reddit発祥 |
| 技術的優位性の文書化 | AIXSだけが持つ「unfair advantage」を明確に定義 | Replicate: Docker Compose経験→Cog |
| 競合分析 | RunPod/Vast.ai/Lambda/CoreWeaveの弱点リスト作成 | 全社: ニッチを攻めた |

### Week 3-4: MVP開発

| 項目 | やること | 参考事例 |
|------|----------|----------|
| コア機能1つに絞る | 「これだけは他社より圧倒的に良い」機能を1つ | Bolt.new: ブラウザ内フルスタック開発 |
| 有料プランの設計 | 初日から課金。無料ティアは不要 | RunPod: 無料ティアなしで成長 |
| 決済・インフラ整備 | Stripe統合、利用量ベース課金の実装 | - |
| 10人のアルファテスター | Reddit/Discordで「無料アクセス↔フィードバック」 | RunPod: まさにこの方法 |

### Week 5-6: ソフトローンチ

| 項目 | やること | 参考事例 |
|------|----------|----------|
| Reddit投稿 | AI関連subredditに「Show HN」スタイルの投稿 | RunPod: Reddit投稿が$120M ARRの起点 |
| デモ動画作成 | 30秒で価値が伝わるスクリーンキャスト | Bolt.new: ユーザーデモがバイラル |
| サポート直接対応 | 創業者がチャット/Discord/メールで全対応 | RunPod: サポートチャット経由で投資家獲得 |
| メトリクス開始 | DAU、有料転換率、チャーン率のトラッキング | - |

### Week 7-8: 改善・拡大

| 項目 | やること | 参考事例 |
|------|----------|----------|
| フィードバック反映 | 最も要望の多い機能を1-2個追加 | Cursor: ユーザーの声を即座に反映 |
| Hacker News投稿 | Show HNで技術的な深堀り記事と共に投稿 | Vast.ai: HN投稿で初期ユーザー獲得 |
| OSSコンポーネント検討 | CLIツール等をOSS化してコミュニティ構築 | Lovable: OSS→52K stars→SaaS |
| 投資家への可視性 | 成長メトリクスをTwitter/ブログで公開 | RunPod: Reddit投稿をVCが発見 |

### AIXSが絶対にやるべき3つのこと

1. **Day 1から課金する**: RunPodの最大の教訓は「無料ティアなし」。利益が出なくても、コストをカバーする価格設定で開始。これにより「本当に払う気があるユーザー」だけが集まり、フィードバックの質が上がる

2. **Reddit/HNで「フィードバック求む」ローンチ**: マーケティング予算は$0で良い。6社中5社がコミュニティ投稿でローンチ。投稿の核心は「自分たちが何を解決するか」。広告よりも、創業者が全コメントに返信する方が効果的

3. **1つの「unfair advantage」に全集中**: RunPodは「GPU開発体験」、Bolt.newは「ブラウザ内フルスタック」、Replicateは「1行APIコール」。AIXSは「他社が真似できない1つの強み」を明確にし、MVPのコア機能をそこに集中させる

### AIXSがやってはいけないこと

- **機能を増やしすぎない**: MVP段階で複数機能は不要（Bolt.newは1機能で$40M ARR）
- **マーケティングに金をかけない**: 6社全てがオーガニック成長（広告費$0）
- **VC資金がないことを言い訳にしない**: RunPodは$50Kの自費で2年間ブートストラップ
- **完璧を目指さない**: Lovableは2回失敗してから成功。早く出して早く学ぶ

---

*本レポートは2026年3月10日時点のWeb検索結果に基づく。各社の数値は公開情報・報道に基づくため、実際の数値と異なる可能性がある。*
