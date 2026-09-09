"""def spiral_matrix(size):
if size == 0:
    return []
if size == 1:
    return [[1]]
upper_new_row = []
lower_new_row = []
for index in range(1, size + 1):
    upper_new_row.append(index)
    lower_new_row.append(size * 3 - 1 - index)
size_minus_two_mat = spiral_matrix(size - 2)
for index in range(0, size - 2):
    for jindex in range(0, size - 2):
        size_minus_two_mat[index][jindex] += size * 4 - 4
    (size_minus_two_mat[index]).append(size + index + 1)
    (size_minus_two_mat[index]).insert(0, size * 4 - index - 4)
size_minus_two_mat.insert(0, upper_new_row)
size_minus_two_mat.append(lower_new_row)
return size_minus_two_mat
"""


def spiral_matrix(size):
    if size == 0:
        return []

    mat = [[0] * size for _ in range(size)]
    i, j = 0, 0

    # State vectors: (di, dj) represent direction
    # Right: (0, 1), Down: (1, 0), Left: (0, -1), Up: (-1, 0)
    di, dj = 0, 1

    for running_num in range(1, size**2 + 1):
        mat[i][j] = running_num

        # Propose the next step
        next_i, next_j = i + di, j + dj

        # Check if the proposed step hits a wall or an already-filled number
        if not (0 <= next_i < size and 0 <= next_j < size and mat[next_i][next_j] == 0):
            # If it does, rotate 90 degrees right using a classic FSM state swap
            di, dj = dj, -di

            # Recalculate next step with the new direction
            next_i, next_j = i + di, j + dj

        # Commit the step
        i, j = next_i, next_j

    return mat
