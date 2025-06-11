
class BTT:
    def __init__(self, nums):
        self.nums = nums
class SN_BTT(BTT):
    def Bitwise_triplet(self):
        count = 0
        n = len(self.nums)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (self.nums[i] & self.nums[j] & self.nums[k]) == 0:
                        count += 1
        return count

#--------------:
print(SN_BTT([10, 11, 12]).Bitwise_triplet() == 0)
print(SN_BTT([13, 14, 15]).Bitwise_triplet() == 0)
print(SN_BTT([16, 17, 18]).Bitwise_triplet() == 0)
