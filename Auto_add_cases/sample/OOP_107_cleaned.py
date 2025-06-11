
class TIE:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    def __private_Their_intersection(self):
        return list(set(self.nums1) & set(self.nums2))
    def public_Their_intersection(self):
        return self.__private_Their_intersection()

#--------------:
print(TIE([11, 12, 13], [14, 15, 16]).public_Their_intersection() == [])
print(TIE([1, 1, 1], [1, 2, 3]).public_Their_intersection() == [1])
print(TIE([1, 2, 3, 4], [3, 4, 5, 6]).public_Their_intersection() == [3, 4])
