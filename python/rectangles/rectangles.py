def rectangles(strings):
    if not strings or len(strings) < 2 or len(strings[0]) < 2:
        return 0
    counter = 0
    for r, row in enumerate(strings):
        for c, cell in enumerate(row):
            if cell != "+":
                continue
            for i in range(c + 1, len(row)):
                if strings[r][i] not in "+-":
                    break
                elif strings[r][i] == "+":
                    for j in range(r + 1, len(strings)):
                        if strings[j][i] not in "|+":
                            break
                        elif strings[j][i] == "+":
                            if strings[j][c] != "+":
                                continue
                            if not all(
                                strings[row_idx][c] in "|+"
                                for row_idx in range(r + 1, j)
                            ):
                                break
                            if not all(
                                strings[j][col_idx] in "-+"
                                for col_idx in range(c + 1, i)
                            ):
                                break
                            counter += 1
    return counter
