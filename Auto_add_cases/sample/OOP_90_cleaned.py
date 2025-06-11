
class MCS:
    def __init__(self, nums):
        self.nums = nums
    def _private_Maximum_coins(self):
        nums = self.nums
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(1, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
        return dp[1][n]
    def public_Maximum_coins(self):
        return self._private_Maximum_coins()

#--------------:
print(MCS([3, 1]).public_Maximum_coins() == 6)
print(MCS([2]).public_Maximum_coins() == 2)
print(MCS([5, 5, 5]).public_Maximum_coins() == 155)
