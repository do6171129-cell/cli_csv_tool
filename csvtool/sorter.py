
def apply_sort(rows:list[dict], spec:dict)-> list[dict]:
    order = spec["order"]
    col = spec["col"]

    if rows == []:
        return rows

    #列チェック（どの行にも無いならエラー）
    if not any(col in row for row in rows):
        raise ValueError(f"column not found: {col}")

    if order == "asc":
        return sorted(rows, key=lambda x: x[col])
    elif order == "desc":
        return sorted(rows, key=lambda x: x[col], reverse=True)
    else:
        raise  ValueError(f"unsupported filter order: {order}")





