
class MS:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
    def __private_Minimum_Steps(self):
        m, n = len(self.word1), len(self.word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.word1[i - 1] == self.word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]
    def public_Minimum_Steps(self):
        return self.__private_Minimum_Steps()

#--------------:
print(MS("abc", "def").public_Minimum_Steps() == 3)
print(MS("hello", "halo").public_Minimum_Steps() == 2)
print(MS("geek", "gesek").public_Minimum_Steps() == 1)
