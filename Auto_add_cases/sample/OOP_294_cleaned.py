
class MAS:
    def __init__(self, nums1):
        self.nums1 = nums1
class SN_MAS(MAS):
    def __init__(self, nums1, nums2):
        super().__init__(nums1)
        self.nums2 = nums2

    def Maximizing_Advantages(self):
        from sortedcontainers import SortedList
        sorted_nums1 = SortedList(self.nums1)
        result = []
        for num in self.nums2:
            idx = sorted_nums1.bisect_right(num)
            if idx < len(sorted_nums1):
                result.append(sorted_nums1.pop(idx))
            else:
                result.append(sorted_nums1.pop(0))    
        return result

#--------------:
print(SN_MAS([1, 2, 3], [2, 2, 2]).Maximizing_Advantages() == [3, 1, 2])
print(SN_MAS([1, 2, 3], [1, 3, 2]).Maximizing_Advantages() == [2, 1, 3])
print(SN_MAS([1, 2, 3], [2, 1, 3]).Maximizing_Advantages() == [3, 2, 1])
