
class NOS:
    def __init__(self, s):
        self.s = s
    def __private_Number_of_sequences(self):
        mod = 10**9 + 7
        n = len(self.s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if self.s[i] == self.s[j]:
                    l, r = i + 1, j - 1
                    while l <= r and self.s[l] != self.s[i]:
                        l += 1
                    while l <= r and self.s[r] != self.s[j]:
                        r -= 1
                    if l > r:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif l == r:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[l + 1][r - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                dp[i][j] = (dp[i][j] + mod) % mod
        return dp[0][n - 1]
    def public_Number_of_sequences(self):
        return self.__private_Number_of_sequences()

#--------------:
print(NOS("abba").public_Number_of_sequences() == 6)
print(NOS("xyyx").public_Number_of_sequences() == 6)
print(NOS("xxyyxx").public_Number_of_sequences() == 10)
