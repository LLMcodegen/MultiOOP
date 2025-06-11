
class MOT:
    def __init__(self, nums):
        self.nums = nums
class SN_MOT(MOT):
    def Minimum_operations(self):
        self.nums.sort()
        operations = 0
        for i in range(1, len(self.nums)):
            if self.nums[i] <= self.nums[i - 1]:
                operations += (self.nums[i - 1] + 1) - self.nums[i]
                self.nums[i] = self.nums[i - 1] + 1
        return operations

#--------------:
print(SN_MOT([4, 4, 4, 4, 4]).Minimum_operations() == 10)
print(SN_MOT([5, 5, 5, 5, 5, 5]).Minimum_operations() == 15)
print(SN_MOT([6, 6, 6, 6, 6, 6, 6]).Minimum_operations() == 21)
