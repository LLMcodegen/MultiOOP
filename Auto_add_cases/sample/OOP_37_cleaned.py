class TAFER:
    def trans_fomer(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]
#--------------:
print(TAFER().trans_fomer("abcdef", "azced") == 3)
print(TAFER().trans_fomer("sunday", "saturday") == 3)
print(TAFER().trans_fomer("giraffe", "griffin") == 4)
