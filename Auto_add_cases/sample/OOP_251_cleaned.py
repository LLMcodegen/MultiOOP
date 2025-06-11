
class NM:
    def __init__(self, board):
        self.board = board
    def __private_Network_Matrix(self, board):
        n = len(board)
        def check_pattern(arr):
            count_ones = sum(arr)
            if count_ones not in {n // 2, (n + 1) // 2}:
                return False
            return True
        def valid_chessboard_pattern(board):
            first_row_pattern = board[0]
            for row in board:
                if not check_pattern(row):
                    return False
            for col in zip(*board):
                if not check_pattern(col):
                    return False
            return True
        def count_moves(arr, n):
            moves_0, moves_1 = 0, 0
            for i in range(n):
                if i % 2 != arr[i]:
                    moves_0 += 1
                if i % 2 == arr[i]:
                    moves_1 += 1
            return min(moves_0, moves_1)
        if not valid_chessboard_pattern(board):
            return -1
        row_moves = count_moves([row[0] for row in board], n)
        col_moves = count_moves([board[0][i] for i in range(n)], n)
        if row_moves % 2 or col_moves % 2:
            return -1
        return (row_moves + col_moves) // 2
    def public_Network_Matrix(self):
        return self.__private_Network_Matrix(self.board)

#--------------:
print(NM([[0, 1, 1], [1, 0, 0], [1, 0, 0]]).public_Network_Matrix() == -1)
print(NM([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]).public_Network_Matrix() == 2)
print(NM([[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1]]).public_Network_Matrix() == 1)
