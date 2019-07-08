def place_queen(row, cols, result):
    if row == 8:
        result.append(list(cols))
    for col in range(8):
        if is_valid(row, col, cols):
            cols[row] = col
            place_queen(row + 1, cols, result)


def is_valid(row, col, cols):
    for row1 in range(row):
        col1 = cols[row1]
        if col1 == col:
            return False

        col_distance = abs(col1 - col)
        row_distance = abs(row1 - row)

        if col_distance == row_distance:
            return False

    return True


res = []
place_queen(0, [None] * 8, res)

for i, r in enumerate(res):
    print(i, ':', r)
