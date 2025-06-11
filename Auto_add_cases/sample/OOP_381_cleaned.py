
class TGT:
    def __init__(self, values):
        self.values = values
class SN_TGT(TGT):
    def triangulation(self):
        n = len(self.values)
        if n < 3:
            return 0
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    score = self.values[i] * self.values[k] * self.values[j]
                    total_score = dp[i][k] + dp[k][j] + score
                    dp[i][j] = min(dp[i][j], total_score)
        return dp[0][n - 1]

#--------------:
print(SN_TGT([1, 2, 3, 4, 5]).triangulation() == 38)
print(SN_TGT([5, 4, 3, 2, 1]).triangulation() == 38)
print(SN_TGT([1, 2, 3, 4, 5, 6]).triangulation() == 68)
