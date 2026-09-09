def spiral_matrix(size):
    mat = [[0] * size for _ in range(size)]
    up_n_down, left_n_right = (
        -1,
        0,
    )
    i, j = 0, 0
    u_size_v, u_size_h, l_size_v, l_size_h = size, size, 0, 0
    running_num = 1
    while True:
        mat[i][j] = running_num
        if l_size_h <= i < u_size_h and l_size_v <= j < u_size_v:
            running_num += 1
            if left_n_right == 0:
                i += 1
            if left_n_right == 1:
                i -= 1
            if up_n_down == 0:
                j += 1
            if up_n_down == 1:
                j -= 1
        else:
            if left_n_right == 0:
                left_n_right = -1
                up_n_down = 0
            if left_n_right == 1:
                left_n_right = -1
                up_n_down = 1
            if up_n_down == 0:
                up_n_down = -1
                left_n_right = 1
            if up_n_down == 1:
                up_n_down = -1
                left_n_right = 0
            if running_num == size**2:
                break
    return mat
