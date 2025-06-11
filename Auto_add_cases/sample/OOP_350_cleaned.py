from collections import defaultdict

class SET:
    def __init__(self, nums):
        self.nums = nums
class SN_SET(SET):
    def __init__(self, nums, k):
        super().__init__(nums)
        self.k = k
    def Sum_Elements(self):
        count = 0
        prefix_sum = 0
        prefix_sum_mod = defaultdict(int)
        prefix_sum_mod[0] = 1
        for num in self.nums:
            prefix_sum = (prefix_sum + num) % self.k
            count += prefix_sum_mod[prefix_sum]
            prefix_sum_mod[prefix_sum] += 1
        return count

#--------------:
print(SN_SET([1, 2, 3, 4, 5], 1).Sum_Elements() == 15)
print(SN_SET([1, 2, 3, 4, 5], 6).Sum_Elements() == 2)
print(SN_SET([1, 2, 3, 4, 5], 7).Sum_Elements() == 2)
