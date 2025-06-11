
class EE:
    def __init__(self, nums1):
        self.nums1 = nums1
class SN_EE(EE):
    def __init__(self, nums1, nums2):
        super().__init__(nums1)
        self.nums2 = nums2
    def Exchange_Elements(self):
        n = len(self.nums1)
        keep = [float('inf')] * n
        swap = [float('inf')] * n
        keep[0] = 0
        swap[0] = 1
        for i in range(1, n):
            if self.nums1[i] > self.nums1[i - 1] and self.nums2[i] > self.nums2[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if self.nums1[i] > self.nums2[i - 1] and self.nums2[i] > self.nums1[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        return min(keep[-1], swap[-1])

#--------------:
print(SN_EE([1, 2, 5, 4], [1, 2, 3, 7]).Exchange_Elements() == 1)
print(SN_EE([1, 4, 5, 4], [1, 2, 3, 7]).Exchange_Elements() == 1)