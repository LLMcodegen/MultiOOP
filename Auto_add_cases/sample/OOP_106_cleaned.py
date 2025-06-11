
from collections import Counter

class AOER:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    def _private_Any_order(self):
        count = Counter(self.nums)
        top_k = count.most_common(self.k)
        return [item[0] for item in top_k]
    def public_Any_order(self):
        return self._private_Any_order()

#--------------:
print(AOER([6, 5, 5, 6, 7, 7, 7], 3).public_Any_order() == [7, 6, 5])
print(AOER([8, 8, 9, 10, 10, 10, 11], 2).public_Any_order() == [10, 8])
print(AOER([3, 3, 4, 4, 4, 5, 6], 2).public_Any_order() == [4, 3])
