---
description: Hallmark - AI生成に見えないUIを作成するデザインスキル
---

# Hallmark ワークフロー

Hallmark は AI コーディングアシスタント用のデザインスキルで、生成された UI が「作られた」ように見え、「生成された」ように見えないようにします。

## 使用方法

Hallmark にはデフォルトの動作と3つの明示的な動詞があります。

| 呼び出し | 動作 |
| --- | --- |
| *(デフォルト)* | 新しいものをデザイン・ビルドするようユーザーが要求。以下のデザインフローに従う。 |
| `hallmark audit <target>` | ターゲットを読み、アンチパターンリストに対してスコアリングし、ランク付けされたパンチリストを返す。**編集しない。** |
| `hallmark redesign <target> [--mood <name>]` | ターゲットのコンテンツと意図を取り、既存の実装境界内で視覚構造を再デザインする（ユーザーが完全な再構築を明示的に確認しない限り）。新しいセクションリズム、新しい見出し配置、新しいコンポーネントボイス。既存のルート、コンポーネント所有権、コピー意図、ブランド、情報アーキテクチャを保持。 |
| `hallmark study <screenshot \| URL>` | ユーザーが気に入っているデザインのスクリーンショットを貼り付けた、**または**ライブページの URL を貼り付けた。**DNA**（マクロ構造、アーキタイプ、タイプペアリング、カラーアンカー）を抽出し、診断レポートを生成。抽出された DNA を使用してユーザーのコンテンツを再構築するか、DNA のポータブルな `design.md` を生成する。 |

## デザインフロー（デフォルト）

### 0. 事前スキャン

プロジェクトに既にコードがある場合、Hallmark はユーザーに何かを尋ねる前に**まず読む**必要があります。

**6つのシグナルソースを順番にスキャン:**

1. **`design.md`** - プロジェクトルートにある場合、これはプロジェクトのロックされたデザインシステムです。最初に読み、他のすべてを上書きします。
2. **フォントスタック** - `package.json`、HTML、`tailwind.config` など
3. **パレット** - OKLCH/HSL/hex 値、Tailwind 設定、トークンファイル
4. **マイクロインタラクションスタンス** - framer-motion、gsap などの依存関係
5. **スペーシングスケール** - Tailwind 設定、CSS カスタムプロパティ
6. **フレームワーク** - Next.js、Astro、Vue、Svelte、Remix、またはバニラ HTML

### 1. デザインコンテキストゲート

コードを書く前に以下の3つを知る必要があります:

1. **オーディエンス** - 誰がこれを使うか？彼らは何を知っているか？
2. **ユースケース** - このインターフェースが行う単一の仕事は何か？
3. **トーン** - 極端なものを選ぶ - editorial, brutalist, soft, utilitarian, luxury, playful, technical, austere

**常に尋ねる - 回答はオプションです。**

### 2. マクロ構造を最初に選択

視覚ルールセットをロードする前に、[`references/macrostructures.md`](.windsurf/.hallmark/references/macrostructures.md) のスリムなインデックスを読み、21の名前付きマクロ構造から1つを選択します。

**多様化ルール（必須）:**

1. ターゲットコードベースで既存の `/* Hallmark · macrostructure: <name> · ... */` スタンプを探す。見つかった場合、選択は異なるマクロ構造でなければならない。
2. このセッションでユーザーに対して他の Hallmark 出力を生成した場合、選択は最後のものと異なるマクロ構造でなければならない。
3. **Specimen マクロ構造はもはやデフォルトではない。**

**テーマ多様化ルール（必須）:**

連続する2つの Hallmark 出力は、以下の3つの軸の少なくとも1つで異なる必要があります:

- **ペーパーバンド** - ダーク (L < 30%) / ミッド (30-85%) / ライト (> 85%)
- **ディスプレイスタイル** - italic-serif / roman-serif / geometric-sans / mono / display-condensed-italic / display-heavy / system-native / risograph-bold
- **アクセント色相** - ウォーム (赤/オレンジ/アンバー) / クール (青/インディゴ/シアン) / ニュートラル / クロマティックその他

### 2.5. プロジェクトメモリを確認

プロジェクトに `.hallmark/log.json` ファイルがある場合、マクロ構造やテーマを選択する前に読みます。最後の3-5エントリを使用して多様化を決定します。

### 2.6. テーマルート

研究された DNA、カタログ、またはカスタムのいずれかを選択します。

**カタログ（デフォルト）** - 22の名前付きテーマ（Specimen, Atelier, Brutal, Salon, Newsprint, Linen, Studio, Manifesto, Terminal, Midnight, Almanac, Garden, Quiet, Riso, Sport, Bloom, Coral, Violet, Aurora, Halo, Plume, Editorial）

**カスタム** - このブリーフに合わせた OKLCH パレット + フリーフォントペアリング

### 3. コンポーネントクックブックからアーキタイプを選択

[`references/component-cookbook.md`](.windsurf/.hallmark/references/component-cookbook.md) のスリムなインデックスを読み、ナビゲーションアーキタイプ（N1-N10）とフッターアーキタイプ（Ft1-Ft8）を選択します。

**デフォルトで N1 と Ft3 を避ける。** これらは最も認識されやすい AI 指紋です。

### 4. スロップテストを実行

[`references/slop-test.md`](.windsurf/.hallmark/references/slop-test.md) をロードし、65のゲートを実行します。

### 5. 出力を生成

選択されたマクロ構造、テーマ、アーキタイプに従って UI を生成します。

### 6. スタンプを追加

CSS コメントの先頭に以下のスタンプを追加します:

```css
/* Hallmark · macrostructure: <name> · theme: <name> · nav: N<N> · footer: Ft<Ft>
 * audience: <audience> · use: <use> · tone: <tone>
 * pre-emit critique: P<1-5> H<1-5> E<1-5> S<1-5> R<1-5> V<1-5>
 */
```

### 7. プロジェクトメモリを更新

`.hallmark/log.json` に新しいエントリを追加します。

## 参考ファイル

主要な参考ファイルは `.windsurf/.hallmark/references/` にあります:

- `macrostructures.md` - 21のマクロ構造インデックス
- `macrostructures/` - 各マクロ構造の詳細
- `component-cookbook.md` - ナビゲーション、フッター、セクションヘッドなどのアーキタイプ
- `components/` - 各コンポーネントアーキタイプの詳細
- `slop-test.md` - 65のスロップテストゲート
- `anti-patterns.md` - 避けるべきアンチパターン
- `genres/` - editorial, modern-minimal, atmospheric, playful のジャンルルール
- `study.md` - デザイン DNA 抽出のプロトコル
- `custom-theme.md` - カスタムテーマ構築のプロトコル

## ライセンス

MIT。使用、フォーク、配布は自由です。
