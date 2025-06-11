
class NOS:
    def __init__(self, k):
        self.k = k
class SN_NOS(NOS):
    def __init__(self, k, n):
        super().__init__(k)
        self.n = n
    def number_operations(self):
        dp = [[0] * (self.n + 1) for _ in range(self.k + 1)]
        for j in range(1, self.n + 1):
            dp[1][j] = j
        for i in range(2, self.k + 1):
            for j in range(1, self.n + 1):
                dp[i][j] = float('inf')
                for x in range(1, j + 1):
                    result = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                    dp[i][j] = min(dp[i][j], result)
        return dp[self.k][self.n]

#--------------:
print(SN_NOS(2, 2).number_operations() == 2)
print(SN_NOS(2, 3).number_operations() == 2)
print(SN_NOS(2, 4).number_operations() == 3)
