
class PPN:
    def __init__(self, n):
        self.n = n
class SN_PPN(PPN):
    def __init__(self, n, minProfit, group, profit):
        super().__init__(n)
        self.minProfit = minProfit
        self.group = group
        self.profit = profit
    def Profit_Plan(self):
        MOD = 10**9 + 7
        dp = [[0] * (self.n + 1) for _ in range(self.minProfit + 1)]
        dp[0][0] = 1  
        for p, g in zip(self.profit, self.group):
            for i in range(self.minProfit, -1, -1):
                for j in range(self.n - g, -1, -1):
                    dp[min(i + p, self.minProfit)][j + g] += dp[i][j]
                    dp[min(i + p, self.minProfit)][j + g] %= MOD 
        return sum(dp[self.minProfit]) % MOD

#--------------:
print(SN_PPN(10, 5, [2, 3, 5], [10, 11, 12]).Profit_Plan() == 7)
print(SN_PPN(10, 5, [2, 3, 5], [13, 14, 15]).Profit_Plan() == 7)
print(SN_PPN(10, 5, [2, 3, 5], [16, 17, 18]).Profit_Plan() == 7)
