
class LSQ:
    def __init__(self, nums):
        self.nums = nums
class SN_LSQ(LSQ):
    def Longest_subsequence(self):
        if not self.nums:
            return 0
        n = len(self.nums)
        dp = {}
        max_length = 1
        for i in range(n):
            for j in range(i):
                diff = self.nums[i] - self.nums[j]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                else:
                    dp[(i, diff)] = 2
                max_length = max(max_length, dp[(i, diff)])
        return max_length

#--------------:
print(SN_LSQ([1, 3, 5, 7, 9]).Longest_subsequence() == 5)
print(SN_LSQ([1, 3, 5, 7, 9, 11]).Longest_subsequence() == 6)
print(SN_LSQ([1, 3, 5, 7, 9, 11, 13]).Longest_subsequence() == 7)
