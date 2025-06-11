
from collections import defaultdict

class ESQ:
    def __init__(self, nums):
        self.nums = nums
    def __private_Equidistant_subsequence(self):
        nums = self.nums
        n = len(nums)
        total = 0
        dp = [defaultdict(int) for _ in range(n)] 
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                dp[i][diff] += count + 1
                total += count
        return total
    def public_Equidistant_subsequence(self):
        return self.__private_Equidistant_subsequence()

#--------------:
print(ESQ([3, 6, 9, 12]).public_Equidistant_subsequence() == 3)
print(ESQ([1, 3, 3, 5]).public_Equidistant_subsequence() == 2)
print(ESQ([2, 2, 2, 2]).public_Equidistant_subsequence() == 5)
