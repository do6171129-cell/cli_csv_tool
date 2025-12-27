import csv

def export_csv(rows: list[dict], path: str, columns=None):
    if rows == []:
        raise ValueError("no rows to export")

    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)