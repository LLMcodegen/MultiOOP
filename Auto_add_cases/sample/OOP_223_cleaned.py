
class DC:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def __private_Delete_Characters(self):
        m, n = len(self.s1), len(self.s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(self.s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        sum_ascii_s1 = sum(ord(c) for c in self.s1)
        sum_ascii_s2 = sum(ord(c) for c in self.s2)
        return sum_ascii_s1 + sum_ascii_s2 - 2 * dp[m][n]
    def public_Delete_Characters(self):
        return self.__private_Delete_Characters()

#--------------:
print(DC("a", "a").public_Delete_Characters() == 0)
print(DC("ab", "ba").public_Delete_Characters() == 194)
print(DC("ab", "ab").public_Delete_Characters() == 0)
