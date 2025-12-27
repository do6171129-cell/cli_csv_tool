import csv

def load_csv(path: str) -> tuple[list[dict[str, str]], list[str]]:
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        columns = reader.fieldnames

        if columns is None:
            raise ValueError("ヘッダー（列名）が見つかりません")

        return rows, columns


