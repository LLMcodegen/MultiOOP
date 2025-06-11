class CWSO:
    def clockwise_spiral_order(self, matrix):
        if not matrix or not matrix[0]:
            return []
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
#--------------:
#--------------:
print(CWSO().clockwise_spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
print(CWSO().clockwise_spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3])
print(CWSO().clockwise_spiral_order([[2, 5, 8], [4, 0, -1]]) == [2, 5, 8, -1, 0, 4])
