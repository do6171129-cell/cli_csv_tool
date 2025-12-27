CLI CSV Tool

Pythonで作成した CSV操作用CLIツール です。
CSVデータに対して、プレビュー・フィルタ・ソート・エクスポートなどの基本操作をCLI上で行えます。

目的

CSV操作を題材にした 状態管理・責務分離設計 の実践

純関数と状態クラスの分離を意識した設計練習

就職活動向けの 小さく完結した成果物

使用技術

Python 3.x

標準ライブラリのみ

csv

pathlib

json

ディレクトリ構成
csvtool/
├─ session.py      # CSVの状態管理（original / current）
├─ filtering.py    # フィルタ処理（純関数）
├─ sorting.py      # ソート処理（純関数）
├─ exporting.py    # CSVエクスポート（純関数）
├─ view.py         # 表示専用
├─ config.py       # 前回パス保存
main.py            # メニュー・入力・例外処理

設計方針

Session

CSVの状態のみを保持

UIやI/Oの詳細を知らない

処理系

フィルタ・ソート・エクスポートは純関数として実装

UI(main)

入力・再入力・例外処理を担当

CSVの列定義（columns）と行データ（rows）を分離し、
意味の異なるデータが混在しない構造にしている

機能一覧

CSVロード

プレビュー表示（先頭N件）

列一覧表示

件数表示

フィルタ（完全一致）

ソート（昇順 / 降順）

リセット

CSVエクスポート

実行方法
python main.py


メニューに従って操作してください。
