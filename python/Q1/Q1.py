def solutions(S, C):
    rows = S.strip().split("\n")
    headers = rows[0].split(",")
    if C not in headers:
        raise ValueError("Column Header not found")
    col_idx = headers.index(C)

    max_val = None
    for row in rows[1:]:
        if not row:
            continue
        try:
            val = int(row.split(",")[col_idx])
            if max_val is None or val > max_val:
                max_val = val
        except (IndexError, ValueError):
            continue
    if max_val is None:
        print("No Numbers in column!")
        return None
    return max_val


if __name__ == "__main__":
    S1 = "id,name,age,act.,room,dept.\n1,Jack,a,T,13,8,\n17,Betty,28,F,15,7"
    print(solutions(S1, "age"))
    S2 = "city,temp2,temp\nParis,7,-3\nDubai,4,-4\nPorto,-1,-2"
    print(solutions(S2, "temp"))
    S3 = "area,land\n3722,CN\n6612,RU\n3855,CA\n3797,USA"
    print(solutions(S3, "area"))
