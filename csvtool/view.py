
class CSVView:
    def __init__(self):
        pass

    def show_menu(self):
        print("=== CSV TOOL ===")
        print("1: CSVを読み込む（ファイル選択）")
        print("2: 先頭N行プレビュー表示（フィルタを適用した）")
        print("3: 列（カラム）一覧を表示")
        print("4: フィルタ（条件で絞り込み）")
        print("5: ソート（列で並べ替え）")
        print("6: 選択中のデータ件数を表示")
        print("7: CSVとしてエクスポート（保存）")
        print("8: フィルタ/ソートをリセット（元データに戻す）")
        print("0: 終了")
