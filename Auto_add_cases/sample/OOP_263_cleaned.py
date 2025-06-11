
class MSE:
    def __init__(self, nums):
        self.nums = nums
class SN_MSE(MSE):
    def __init__(self, nums, k):
        super().__init__(nums)
        self.k = k
    def Maximum_score(self):
        n = len(self.nums)
        if n == 0:
            return 0
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + self.nums[i - 1]
        dp = [[0] * (self.k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, min(i, self.k) + 1):
                if j == 1:
                    dp[i][j] = prefix_sum[i] / i
                else:
                    for x in range(j - 1, i):
                        dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix_sum[i] - prefix_sum[x]) / (i - x))
        return dp[n][self.k]

#--------------:
print(SN_MSE([1, 2, 3, 4, 5, 6], 2).Maximum_score() == 9.0)
print(SN_MSE([1, 2, 3, 4, 5, 6], 3).Maximum_score() == 13.5)
print(SN_MSE([1, 2, 3, 4, 5, 6], 4).Maximum_score() == 17.0)
