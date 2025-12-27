# CLI CSV Tool

Pythonで作成した **CSV操作用CLIツール** です。  
CSVデータに対して、**プレビュー / フィルタ / ソート / エクスポート** などの基本操作を  
**CLI上で安全に実行**できます。

---

## 🎯 目的

- CSV操作を題材にした **状態管理・責務分離設計** の実践
- **Session / 純関数 / UI** の役割分離を意識した設計練習
- 就職活動向けの **小さく完結した成果物** を作ること

---

## 🛠 使用技術

- **Python 3.x**
- **標準ライブラリのみ**
  - `csv`
  - `pathlib`
  - `json`

---

## 📁 ディレクトリ構成

```text
csvtool/
├─ session.py      # CSVの状態管理（original_rows / current_rows）
├─ filtering.py    # フィルタ処理（純関数）
├─ sorting.py      # ソート処理（純関数）
├─ exporting.py    # CSVエクスポート（純関数）
├─ view.py         # 表示専用（UI補助）
├─ config.py       # 前回使用パスの保存
main.py            # メニュー・入力・例外処理

```

## 🧠 設計方針
# CSVSession

- CSVの 状態のみ を保持

- UI や ファイルI/O の詳細を知らない

- original_rows と current_rows を分離

# 処理系（filter / sort / export）

- 純関数として実装

- 状態を持たず、入力 → 出力のみを扱う

# UI（main）

- ユーザー入力

- 再入力制御

- 例外処理とメッセージ表示を担当

# データ構造の分離

- columns（列定義） と rows（行データ） を分離

- CSVのヘッダ行とデータ行が 混在しない構造

- 行データは常に list[dict] として扱える

---

## ✅ 機能一覧

- CSVロード

- プレビュー表示（先頭N件）

- 列一覧表示

- 件数表示

- フィルタ（完全一致）

- ソート（昇順 / 降順）

- リセット

- CSVエクスポート

## 🚀 実行方法
```text
python main.py
```

## 📝 補足

- エクスポートは「保存先ファイルが存在しない場合」でも作成されます（open(path, "w")）

- エクスポート対象が0件の場合は ValueError を出してUIでメッセージ表示します
