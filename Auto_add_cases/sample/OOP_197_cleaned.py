
class ROP:
    def __init__(self, n, k):
        self.n = n
        self.k = k
    def __private_Reverse_order_pair(self):
        dp = [[0 for _ in range(self.k + 1)] for _ in range(self.n + 1)]
        dp[0][0] = 1
        for i in range(1, self.n + 1):
            for j in range(self.k + 1):
                dp[i][j] = dp[i - 1][j]
                for x in range(1, min(j + 1, i)):
                    dp[i][j] += dp[i - 1][j - x]
        return dp[self.n][self.k]
    def public_Reverse_order_pair(self):
        return self.__private_Reverse_order_pair()

#--------------:
print(ROP(3, 2).public_Reverse_order_pair() == 2)
print(ROP(4, 0).public_Reverse_order_pair() == 1)
print(ROP(4, 1).public_Reverse_order_pair() == 3)
