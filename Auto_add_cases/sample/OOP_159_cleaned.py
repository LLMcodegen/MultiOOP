
class MSBS:
    def __init__(self, strs, m, n):
        self.strs = strs
        self.m = m
        self.n = n
    def public_Maximum_subset(self):
        return self.__private_Maximum_subset()
    def __private_Maximum_subset(self):
        dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for s in self.strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(self.m, zeros - 1, -1):
                for j in range(self.n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[self.m][self.n]

#--------------:
print(MSBS(["111", "11", "0", "00"], 3, 2).public_Maximum_subset() == 3)
print(MSBS(["0", "1", "10", "01"], 2, 2).public_Maximum_subset() == 3)
print(MSBS(["11100", "10101", "001", "10"], 5, 3).public_Maximum_subset() == 2)
