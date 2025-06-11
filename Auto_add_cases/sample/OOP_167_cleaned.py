
class DTVL:
    def __init__(self, mat):
        self.mat = mat
    def __private_Diagonal_traversal(self):
        if not self.mat or not self.mat[0]:
            return []
        m, n = len(self.mat), len(self.mat[0])
        result = []
        for sum_index in range(m + n - 1):
            if sum_index % 2 == 0:
                row = min(sum_index, m - 1)
                col = max(0, sum_index - m + 1)
                while row >= 0 and col < n:
                    result.append(self.mat[row][col])
                    row -= 1
                    col += 1
            else:
                col = min(sum_index, n - 1)
                row = max(0, sum_index - n + 1)
                while col >= 0 and row < m:
                    result.append(self.mat[row][col])
                    row += 1
                    col -= 1
        return result
    def public_Diagonal_traversal(self):
        return self.__private_Diagonal_traversal()

#--------------:
print(DTVL([[1, 2], [3, 4], [5, 6]]).public_Diagonal_traversal() == [1, 2, 3, 5, 4, 6])
print(DTVL([[1, 2, 3, 4]]).public_Diagonal_traversal() == [1, 2, 3, 4])
print(DTVL([[1], [2], [3], [4]]).public_Diagonal_traversal() == [1, 2, 3, 4])
