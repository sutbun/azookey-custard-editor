# SF Symbols Browser prototype

Windows上でSF Symbolsを検索・確認・コピーするための試作です。

## 目的

- Symbol名を高速検索する
- 手元のSVGを一覧表示する
- Symbol名をクリック操作でコピーする
- SwiftUI / JSON向けのコピー形式を用意する
- AppleのSF Symbolsアセット自体はRepositoryへ再配布しない

## 起動

`tools/sf-symbols-browser/index.html` をEdge / Chromeで開きます。

## SVGの読み込み

1. `SVGフォルダを開く` を押す
2. `.svg` ファイルが入ったフォルダを選ぶ
3. ファイル名から拡張子を除いた文字列をSymbol名として登録する
4. 検索欄から絞り込む
5. Symbolカードを選択してコピーする

例: `square.and.arrow.up.svg` → `square.and.arrow.up`

フォルダ内のSVGはブラウザのObject URLとしてローカル表示するだけで、外部へアップロードしません。

## 現在のMVP

- 組み込みの代表的なSymbol名による名前検索
- ユーザー指定SVGフォルダの一括読み込み
- SVGプレビュー
- 部分一致検索
- `.` / `_` / `-` を区切りとして扱う検索
- Symbol名コピー
- `Image(systemName: "...")` コピー
- `"symbol": "..."` コピー
- SVGあり / 名前のみフィルタ
- `/` で検索欄フォーカス
- `Esc` で検索解除

## 次段階

- 大量SVG向け仮想スクロール
- お気に入り / 最近使ったSymbol
- Variantグルーピング（`.fill` など）
- OS availability / deprecated metadata
- カテゴリ
- azooKey Custard Editorとの共通データ層
- 独立Windowsアプリ化（Tauri等）

## 配布方針

SF Symbolsの画像・フォント等のAppleアセットそのものはこのRepositoryへ同梱しません。実アセットはユーザー側で用意し、このブラウザはローカル参照・検索UIとして動作させます。
