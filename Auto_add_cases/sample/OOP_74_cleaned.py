class FTLS:
    def largest_square(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side
#--------------:
#--------------:
print(FTLS().largest_square([["1", "0"], ["0", "1"]]) == 1)
print(FTLS().largest_square([["1", "1", "0", "0"], ["1", "1", "1", "1"], ["1", "1", "1", "0"]]) == 4)
print(FTLS().largest_square([["0", "0", "0", "0"], ["0", "0", "0", "1"], ["0", "0", "1", "1"], ["0", "1", "1", "1"]]) == 4)
