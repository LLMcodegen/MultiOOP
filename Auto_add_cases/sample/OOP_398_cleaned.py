
from itertools import product

class SSI:
    def __init__(self, str1: str):
        self.str1 = str1
class SN_SSI(SSI):
    def __init__(self, str1: str, str2: str):
        super().__init__(str1)
        self.str2 = str2
    def Shortest_string(self):
        m, n = len(self.str1), len(self.str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif self.str1[i - 1] == self.str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        i, j = m, n
        result = []
        while i > 0 and j > 0:
            if self.str1[i - 1] == self.str2[j - 1]:
                result.append(self.str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                result.append(self.str1[i - 1])
                i -= 1
            else:
                result.append(self.str2[j - 1])
                j -= 1
        while i > 0:
            result.append(self.str1[i - 1])
            i -= 1
        while j > 0:
            result.append(self.str2[j - 1])
            j -= 1
        return ''.join(reversed(result))

#--------------:
print(SN_SSI("abc", "def").Shortest_string() == "abcdef")
print(SN_SSI("dynamic", "programming").Shortest_string() == "dynprogrammicng")
print(SN_SSI("shortest", "supersequence").Shortest_string() == "shortuperstequence")
