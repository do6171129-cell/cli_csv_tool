from csvtool.session import CSVSession
from csvtool.view import CSVView
from csvtool.config import save_config, load_config

PREVIEW_LIMIT = 5

def handle_choice(choice: str, session: CSVSession) -> bool:

    if choice == "0":
        return True

    elif choice == "1":
        path = input("CSVパス： ").strip()
        try:
            session.load(path)
        except Exception as e:
            print(f"読み込み失敗：{e}")
            return False

        save_config(path)
        print("読み込み成功")
        return False

    elif choice == "2":
        for row in session.current_rows[:PREVIEW_LIMIT]:
            print(row)
        return False

    elif choice == "3":
        print(", ".join(session.columns))
        return False

    elif choice == "4":
        while True:
            column = input("列名： ").strip()
            value = input("値： ").strip()
            op = "eq"

            cond = {
                "op": op,
                "col": column,
                "value": value
            }
            try:
                session.filter(cond)
                break
            except ValueError as e:
                # 「列が存在しない」系だけ、再入力ループにする
                msg = str(e)
                if msg.startswith("column not found:"):
                    print(f"存在しない列名です: {column}")
                    continue
                # それ以外（op未対応など）は想定外なので上に投げる
                raise

        print(f"フィルター後の件数: {len(session.current_rows)}")
        print("フィルターした結果：（{PREVIEW_LIMIT}件まで)")
        for row in session.current_rows[:PREVIEW_LIMIT]:
            print(row)

    elif choice == "5":
        while True:
            col = input("列名： ").strip()
            order_number = input("1:昇順、2：降順： ").strip()
            order = ""

            if order_number == "1":
                order = "asc"
            elif order_number == "2":
                order = "desc"

            spec = {
                "col": col,
                "order": order
            }

            try:
                session.sort(spec)
                break
            except ValueError as e:
                # 「列が存在しない」系だけ、再入力ループにする
                msg = str(e)
                if msg.startswith("column not found:"):
                    print(f"存在しない列名です: {col}")
                    continue
                # それ以外（op未対応など）は想定外なので上に投げる
                raise

        print(f"ソートした結果:{PREVIEW_LIMIT}件まで")
        for row in session.current_rows[:PREVIEW_LIMIT]:
            print(row)


    elif choice == "6":
        print(session.count())
        return False

    elif choice == "7":
        path = input("保存先パスを入力してください: ").strip()
        try:
            session.export(path)
            print(f"exportしました: {path}")
            print(f"件数: {session.count()}")
        except RuntimeError as e:
            print(e)
        except ValueError:
            print("エクスポート対象が0件です。")
        except OSError as e:
            print(f"ファイル書き込みに失敗: {e}")

    elif choice == "8":
        session.reset()

        print("resetしました。")

        for row in session.current_rows[:PREVIEW_LIMIT]:
            print(row)
        return False

    else:
        print("その番号は無いよ（0〜8）")
    return False




def main():
    last_path = load_config()
    session = CSVSession()
    csvview = CSVView()

    if last_path is not None:
        yn = input("前回のcsvを開きますか？(y/n)").strip().lower()
        if yn == "y":
            try:
                session.load(last_path)
            except Exception as e:
                print(f"読み込み失敗：{e}")

    while True:
        csvview.show_menu()
        choice = input("数字を入力してください：").strip()

        if not session.is_loaded() and choice not in ("1", "0"):
            print("先にロードしてください")
            continue

        exit_flag = handle_choice(choice, session)
        if exit_flag:
            break




if __name__ == '__main__':
    main()

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
