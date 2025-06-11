
class MSE:
    def __init__(self, nums):
        self.nums = nums
class SN_MSE(MSE):
    def __init__(self, nums, k):
        super().__init__(nums)
        self.k = k
    def Minimum_score(self):
        if not self.nums:
            return 0
        nums = sorted(self.nums)
        n = len(nums)
        k = self.k
        max_num = nums[-1]
        min_num = nums[0]
        result = max_num - min_num
        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i + 1] - k)
            result = min(result, high - low)
        return result

#--------------:
print(SN_MSE([1, 1, 1, 1], 0).Minimum_score() == 0)
print(SN_MSE([5, 5, 5, 5], 2).Minimum_score() == 0)
print(SN_MSE([1, 2, 3, 4, 5], 2).Minimum_score() == 3)
