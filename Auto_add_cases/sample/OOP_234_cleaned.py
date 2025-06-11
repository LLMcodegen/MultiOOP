
from collections import Counter

class MN:
    def __init__(self, nums):
        self.nums = nums
    def __private_Maximum_number(self):
        if not self.nums:
            return 0
        count = Counter(self.nums)
        unique_nums = sorted(count.keys())
        prev_take, prev_skip = 0, 0
        prev_num = None
        for num in unique_nums:
            take = prev_skip + num * count[num]
            skip = max(prev_take, prev_skip)
            if prev_num is None or num == prev_num + 1:
                prev_take, prev_skip = take, skip
            else:
                prev_take, prev_skip = max(prev_take, prev_skip) + num * count[num], max(prev_take, prev_skip)
            prev_num = num
        return max(prev_take, prev_skip)
    def public_Maximum_number(self):
        return self.__private_Maximum_number()

#--------------:
print(MN([1, 2, 2, 3, 3, 4]).public_Maximum_number() == 8)
print(MN([1, 2, 3, 4, 5, 6]).public_Maximum_number() == 12)
print(MN([1, 1, 2, 2, 3, 3]).public_Maximum_number() == 8)
