
class ROR:
    def __init__(self, nums):
        self.nums = nums
    def __private_Rearranged_order(self):
        for i in range(len(self.nums) - 1):
            if i % 2 == 0:
                if self.nums[i] > self.nums[i + 1]:
                    self.nums[i], self.nums[i + 1] = self.nums[i + 1], self.nums[i]
            else:
                if self.nums[i] < self.nums[i + 1]:
                    self.nums[i], self.nums[i + 1] = self.nums[i + 1], self.nums[i]
        return self.nums
    def public_Rearranged_order(self):
        return self.__private_Rearranged_order()

#--------------:
print(ROR([4, 7, 1, 5, 2, 6]).public_Rearranged_order() == [4, 7, 1, 5, 2, 6])
print(ROR([11, 9, 13, 8, 15, 5]).public_Rearranged_order() == [9, 13, 8, 15, 5, 11])
print(ROR([0, 10, 20, 30, 40, 50]).public_Rearranged_order() == [0, 20, 10, 40, 30, 50])
