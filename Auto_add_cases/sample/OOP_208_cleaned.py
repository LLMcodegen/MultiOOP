
class NDC:
    def __init__(self, nums):
        self.nums = nums
    def __private_Non_decreasing_column(self):
        n = len(self.nums)
        count = 0
        for i in range(1, n):
            if self.nums[i] < self.nums[i - 1]:
                count += 1
                if count > 1:
                    return False
                if i >= 2 and self.nums[i] < self.nums[i - 2]:
                    self.nums[i] = self.nums[i - 1]
                else:
                    self.nums[i - 1] = self.nums[i]
        return True
    def public_Non_decreasing_column(self):
        return self.__private_Non_decreasing_column()

#--------------:
print(NDC([10, 5, 7]).public_Non_decreasing_column() == True)
print(NDC([1, 5, 3, 4]).public_Non_decreasing_column() == True)
print(NDC([1, 3, 2, 4]).public_Non_decreasing_column() == True)