class RTICW:
    def rotate_image_clockwise(self, matrix):
        n = len(matrix)
        if n == 0:
            return matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix
#--------------:
print(RTICW().rotate_image_clockwise([[1, 3, 5], [7, 9, 11], [13, 15, 17]]) == [[13, 7, 1], [15, 9, 3], [17, 11, 5]])
print(RTICW().rotate_image_clockwise([[2, 4, 8], [16, 32, 64], [128, 256, 512]]) == [[128, 16, 2], [256, 32, 4], [512, 64, 8]])
print(RTICW().rotate_image_clockwise([[0, 0, 0], [1, 2, 3], [4, 5, 6]]) == [[4, 1, 0], [5, 2, 0], [6, 3, 0]])# New Test cases
print(RTICW().rotate_image_clockwise([[1]]) == [[1]])  # Single element matrix
print(RTICW().rotate_image_clockwise([[1, 2], [3, 4]]) == [[3, 1], [4, 2]])  # 2x2 matrix
print(RTICW().rotate_image_clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])  # 4x4 matrix
