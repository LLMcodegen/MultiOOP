
class DPH:
    def __init__(self, matrix):
        self.matrix = matrix
class SN_DPH(DPH):
    def descent_path(self):
        n = len(self.matrix)
        dp = [row[:] for row in self.matrix]
        for i in range(1, n):
            for j in range(n):
                min_above = dp[i - 1][j]
                if j > 0:
                    min_above = min(min_above, dp[i - 1][j - 1])
                if j < n - 1:
                    min_above = min(min_above, dp[i - 1][j + 1])
                dp[i][j] += min_above
        return min(dp[-1])

#--------------:
print(SN_DPH([[1, 2, 3, 4], [5, 6, 7, 8]]).descent_path() == 6)
print(SN_DPH([[1, 2, 3], [13, 14, 15]]).descent_path() == 14)
print(SN_DPH([[1, 2, 3, 4, 5], [11, 12, 13, 14, 15]]).descent_path() == 12)
