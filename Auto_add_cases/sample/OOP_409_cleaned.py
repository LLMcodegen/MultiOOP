
class SSN:
    def __init__(self, text1):
        self.text1 = text1
class SN_SSN(SSN):
    def __init__(self, text1, text2):
        super().__init__(text1)
        self.text2 = text2
    def Shared_subsequences(self):
        m, n = len(self.text1), len(self.text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.text1[i - 1] == self.text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

#--------------:
print(SN_SSN("abcde", "bd").Shared_subsequences() == 2)
print(SN_SSN("abcde", "bde").Shared_subsequences() == 3)
print(SN_SSN("abcde", "bcd").Shared_subsequences() == 3)
