
class ROE:
    def __init__(self, nums):
        self.nums = nums
    def __private_relative_order(self):
        non_zero_index = 0
        for i in range(len(self.nums)):
            if self.nums[i] != 0:
                self.nums[non_zero_index], self.nums[i] = self.nums[i], self.nums[non_zero_index]
                non_zero_index += 1
        return self.nums
    def public_relative_order(self):
        return self.__private_relative_order()

#--------------:
print(ROE([7, 8, 0, 0, 9, 0]).public_relative_order() == [7, 8, 9, 0, 0, 0])
print(ROE([0, 0, 0, 0, 0]).public_relative_order() == [0, 0, 0, 0, 0])
print(ROE([1, 2, 3, 4, 0]).public_relative_order() == [1, 2, 3, 4, 0])
