
from itertools import combinations
from math import gcd
from functools import lru_cache

class EMT:
    def __init__(self, nums):
        self.nums = nums
class SN_EMT(EMT):
    def __init__(self, nums):
        super().__init__(nums)
    def Element_Movement(self):
        total_sum = sum(self.nums)
        n = len(self.nums)
        if n < 2:
            return False
        @lru_cache(None)
        def possible(size, target_sum):
            if size == 0:
                return target_sum == 0
            if size > n or target_sum < 0:
                return False
            for i in range(n):
                if possible(size - 1, target_sum - self.nums[i]):
                    return True
            return False
        for subset_size in range(1, n // 2 + 1):
            if total_sum * subset_size % n == 0:
                target_sum = total_sum * subset_size // n
                if possible(subset_size, target_sum):
                    return True
        return False

#--------------:
print(SN_EMT([1, 2, 3, 4, 5, 6]).Element_Movement() == True)
print(SN_EMT([1, 2, 3, 4, 5, 6, 7]).Element_Movement() == True)
print(SN_EMT([1, 2, 3, 4, 5, 6, 7, 8, 9]).Element_Movement() == True)
