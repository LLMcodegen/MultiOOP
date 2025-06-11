
class PAL:
    def __init__(self, n):
        self.n = n
class SN_PAL(PAL):
    def __init__(self, n, goal, k):
        super().__init__(n)
        self.goal = goal
        self.k = k
    def PlayList(self):
        n, goal, k = self.n, self.goal, self.k
        mod = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                dp[i][j] = dp[i - 1][j - 1] * (n - (j - 1)) % mod
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod
        return dp[goal][n]

#--------------:
print(SN_PAL(3, 4, 2).PlayList() == 6)
print(SN_PAL(3, 4, 3).PlayList() == 0)
print(SN_PAL(4, 5, 1).PlayList() == 144)
