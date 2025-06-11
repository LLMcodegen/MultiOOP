
class RL:
    def __init__(self, s: str):
        self.s = s
    def __private_Return_length(self) -> int:
        n = len(self.s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if self.s[i] == self.s[j] and length == 2:
                    dp[i][j] = 2
                elif self.s[i] == self.s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]

    def public_Return_length(self) -> int:
        return self.__private_Return_length()

#--------------:
print(RL("banana").public_Return_length() == 5)
print(RL("abcbda").public_Return_length() == 5)
print(RL("madam").public_Return_length() == 5)
