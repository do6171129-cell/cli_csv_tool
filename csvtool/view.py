
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

def render_preview_columns(columns):
    # 4) ヘッダ＆区切り線
    header_cells = [col for col in columns]
    print(" | ".join(header_cells))


def render_preview(columns, rows, limit):
    # 1) 先頭N件だけ対象（rowsは触らない）
    preview_rows = rows[:limit]

    if not preview_rows:
        print("0件")
        return

    # 2) 表示用に「文字列セル配列」へ変換（欠損は "-"）
    display_rows = []
    for row in preview_rows:
        display_cells = []
        for col in columns:
            value = row.get(col)
            if value == "" or value is None:
                display_cells.append("-")
            else:
                display_cells.append(str(value))
        display_rows.append(display_cells)

    # 3) 列幅計算（ヘッダ名の長さ or 各セル長の最大）
    widths = [len(col) for col in columns]
    for i in range(len(display_rows)):
        for j in range(len(columns)):
            widths[j] = max(widths[j], len(display_rows[i][j]))

    # 4) ヘッダ＆区切り線
    header_cells = [col.ljust(widths[j]) for j, col in enumerate(columns)]
    print(" | ".join(header_cells))

    sep_cells = ["-" * w for w in widths]
    print("-+-".join(sep_cells))

    # 5) 本体（数字っぽい文字列は右寄せ、それ以外は左寄せ）
    def is_number_str(s: str) -> bool:
        if s == "-" or s == "":
            return False
        try:
            float(s)  # "12", "12.3", "-5" もOK
            return True
        except ValueError:
            return False

    for cells in display_rows:
        out_cells = []
        for j, cell in enumerate(cells):
            if is_number_str(cell):
                out_cells.append(cell.rjust(widths[j]))
            else:
                out_cells.append(cell.ljust(widths[j]))
        print(" | ".join(out_cells))





