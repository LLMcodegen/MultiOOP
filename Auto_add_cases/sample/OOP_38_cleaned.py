class STEZ:
    def element_setting_zero(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        rows_to_zero = set()
        cols_to_zero = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        for row in rows_to_zero:
            for j in range(n):
                matrix[row][j] = 0
        for col in cols_to_zero:
            for i in range(m):
                matrix[i][col] = 0
        return matrix
#--------------:
#--------------:
print(STEZ().element_setting_zero([[1]]) == [[1]])
print(STEZ().element_setting_zero([[0]]) == [[0]])
print(STEZ().element_setting_zero([[0, 1], [1, 1]]) == [[0, 0], [0, 1]])
