
class SSB:
    def __init__(self, nums):
        self.nums = nums
    def __private_split_subset(self):
        total_sum = sum(self.nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        n = len(self.nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= self.nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - self.nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][target]

    def public_split_subset(self):
        return self.__private_split_subset()

#--------------:
print(SSB([10, 20, 30, 40]).public_split_subset() == True)
print(SSB([1, 5, 11, 5, 2]).public_split_subset() == True)
print(SSB([5, 2, 7, 6]).public_split_subset() == False)
