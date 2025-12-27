
def apply_filter(rows: list[dict], cond: dict) -> list[dict]:
    op = cond.get("op")
    col = cond.get("col")
    value = cond.get("value")

    if op == "eq":
        return filter_eq(rows, col, value)

    raise ValueError(f"unsupported filter op: {op}")


def filter_eq(rows: list[dict], column: str, value: str) -> list[dict]:
    if not rows:
        return []

    # 列チェック（どの行にも無いならエラー）
    if not any(column in row for row in rows):
        raise ValueError(f"column not found: {column}")

    # 絞り込み（その行に列が無い場合は不一致扱い＝落ちる）
    return [row for row in rows if row.get(column) == value]

