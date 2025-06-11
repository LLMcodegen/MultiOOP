
from collections import deque

class SPB:
    def __init__(self, board):
        self.board = board
    def __private_Solving_puzzle_board(self) -> int:
        target = [[1, 2, 3], [4, 5, 0]]
        target_str = '123450'
        start_str = ''.join(str(num) for row in self.board for num in row)
        if start_str == target_str:
            return 0
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(start_str, start_str.index('0'), 0)])  # (state, index of '0', depth)
        visited = {start_str}
        while queue:
            current, zero_idx, depth = queue.popleft()
            zero_row, zero_col = divmod(zero_idx, 3)
            for move_row, move_col in moves:
                new_row, new_col = zero_row + move_row, zero_col + move_col
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    new_zero_idx = new_row * 3 + new_col
                    new_board = list(current)
                    new_board[zero_idx], new_board[new_zero_idx] = new_board[new_zero_idx], new_board[zero_idx]
                    new_board_str = ''.join(new_board)
                    if new_board_str == target_str:
                        return depth + 1
                    if new_board_str not in visited:
                        visited.add(new_board_str)
                        queue.append((new_board_str, new_zero_idx, depth + 1))
        return -1
    def public_Solving_puzzle_board(self) -> int:
        return self.__private_Solving_puzzle_board()

#--------------:
print(SPB([[1, 3, 5], [4, 2, 0]]).public_Solving_puzzle_board() == 4)
print(SPB([[1, 3, 5], [4, 0, 2]]).public_Solving_puzzle_board() == 5)
print(SPB([[1, 3, 5], [0, 4, 2]]).public_Solving_puzzle_board() == 6)
