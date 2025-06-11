
from collections import Counter

class ORU:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    def __private_Order_results(self):
        count1 = Counter(self.nums1)
        count2 = Counter(self.nums2)
        result = []
        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))
        return result
    def public_Order_results(self):
        return self.__private_Order_results()

#--------------:
print(ORU([11, 12, 12, 13], [12, 13, 14]).public_Order_results() == [12, 13])
print(ORU([6, 6, 6, 7], [6, 7, 8]).public_Order_results() == [6, 7])
print(ORU([1, 2, 3], [4, 5, 6]).public_Order_results() == [])
