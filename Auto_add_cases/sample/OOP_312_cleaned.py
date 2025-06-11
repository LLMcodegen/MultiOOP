
class AOR:
    def __init__(self, nums):
        self.nums = nums
class SN_AOR(AOR):
    def ascend_order(self):
        self.nums.sort()
        return self.nums

#--------------:
print(SN_AOR([100, 200, 300, 400, 500]).ascend_order() == [100, 200, 300, 400, 500])
print(SN_AOR([-5, -4, -3, -2, -1, 0]).ascend_order() == [-5, -4, -3, -2, -1, 0])
print(SN_AOR([3, 3, 3, 3, 3]).ascend_order() == [3, 3, 3, 3, 3])
