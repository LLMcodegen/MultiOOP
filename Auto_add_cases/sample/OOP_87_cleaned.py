
class LSQ:
    def __init__(self, nums):
        self.nums = nums
    def __private_Longest_subsequence(self):
        if not self.nums:
            return 0
        dp = [1] * len(self.nums)
        for i in range(1, len(self.nums)):
            for j in range(i):
                if self.nums[i] > self.nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    def public_Longest_subsequence(self):
        return self.__private_Longest_subsequence()

#--------------:
print(LSQ([1, 2, 4, 3, 5, 4, 7, 2]).public_Longest_subsequence() == 5)
print(LSQ([2, 2, 2, 2, 2, 2]).public_Longest_subsequence() == 1)
print(LSQ([10, 22, 9, 33, 21, 50, 41, 60, 80]).public_Longest_subsequence() == 6)
