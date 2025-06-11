
class AST:
    def __init__(self, nums1, nums2, nums3, nums4):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums3 = nums3
        self.nums4 = nums4
    def __private_Array_stlength(self):
        n = len(self.nums1)
        count = 0
        sum_dict = {}
        for i in range(n):
            for j in range(n):
                sum_val = self.nums1[i] + self.nums2[j]
                if sum_val in sum_dict:
                    sum_dict[sum_val] += 1
                else:
                    sum_dict[sum_val] = 1
        for k in range(n):
            for l in range(n):
                target = -(self.nums3[k] + self.nums4[l])
                if target in sum_dict:
                    count += sum_dict[target]
        return count
    def public_Array_stlength(self):
        return self.__private_Array_stlength()

#--------------:
print(AST([0, 0], [0, 0], [0, 0], [0, 0]).public_Array_stlength() == 16)
print(AST([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]).public_Array_stlength() == 0)
print(AST([1, -1], [2, -2], [-1, 1], [-2, 2]).public_Array_stlength() == 4)
