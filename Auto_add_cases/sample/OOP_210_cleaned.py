
class LIS:
    def __init__(self, nums):
        self.nums = nums
    def __lo_in_sub(self):
        if not self.nums:
            return 0
        n = len(self.nums)
        dp = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if self.nums[i] > self.nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        longest = max(dp)
        return sum(count[i] for i in range(n) if dp[i] == longest)
    def public_lo_in_sub(self):
        return self.__lo_in_sub()

#--------------:
print(LIS([5, 6, 7, 8, 9]).public_lo_in_sub() == 1)
print(LIS([4, 3, 2, 1]).public_lo_in_sub() == 4)
print(LIS([1, 5, 3, 4, 2]).public_lo_in_sub() == 1)
