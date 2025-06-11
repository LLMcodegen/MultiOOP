
class FDSB:
    def __init__(self, nums):
        self.nums = nums
class SN_FDSB(FDSB):
    def __init__(self, nums, left, right):
        super().__init__(nums)
        self.left = left
        self.right = right
    def find_subarray(self):
        count = 0
        n = len(self.nums)
        for i in range(n):
            max_val = float('-inf')
            for j in range(i, n):
                max_val = max(max_val, self.nums[j])
                if self.left <= max_val <= self.right:
                    count += 1
                elif max_val > self.right:
                    break
        return count

#--------------:
print(SN_FDSB([1, 2, 3], 1, 1).find_subarray() == 1)
print(SN_FDSB([1, 2, 3], 3, 3).find_subarray() == 3)
print(SN_FDSB([1, 2, 3], 4, 5).find_subarray() == 0)
