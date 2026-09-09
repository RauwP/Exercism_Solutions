class ConnectGame:
    def __init__(self, board):
        self.board = [row.replace(" ", "") for row in board.split("\n")]

    def _check_winner(self, player):
        directions = [(0, -1), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 0)]
        todo_ls = []
        visited = set()

        if player == "O":
            for col_index, cell_val in enumerate(self.board[0]):
                if cell_val == "O":
                    todo_ls.append((0, col_index))
        else:
            for row_index, row_data in enumerate(self.board):
                if row_data[0] == "X":
                    todo_ls.append((row_index, 0))
        while todo_ls:
            current_r, current_c = todo_ls.pop()
            if (current_r, current_c) in visited:
                continue
            visited.add((current_r, current_c))
            if player == "O" and current_r == len(self.board) - 1:
                return "O"
            if player == "X" and current_c == len(self.board[0]) - 1:
                return "X"
            for r_offset, c_offset in directions:
                next_r = current_r + r_offset
                next_c = current_c + c_offset

                if 0 <= next_r < len(self.board) and 0 <= next_c < len(self.board[0]):
                    if (
                        self.board[next_r][next_c] == player
                        and (next_r, next_c) not in visited
                    ):
                        todo_ls.append((next_r, next_c))
        return False

    def get_winner(self):
        if self._check_winner("O"):
            return "O"
        if self._check_winner("X"):
            return "X"
        return ""
