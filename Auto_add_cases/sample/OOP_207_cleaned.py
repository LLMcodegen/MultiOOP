
class MPT:
    def __init__(self, s):
        self.s = s
    def __Minimum_Times(self, s):
        n = len(s)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]
    def public_Minimum_Times(self):
        return self.__Minimum_Times(self.s)

#--------------:
print(MPT("abccba").public_Minimum_Times() == 3)
print(MPT("ababa").public_Minimum_Times() == 3)
print(MPT("ababab").public_Minimum_Times() == 4)
