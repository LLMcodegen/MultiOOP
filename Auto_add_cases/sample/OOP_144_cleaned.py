
class AFO:
    def __init__(self, nums):
        self.nums = nums
    def __private_Array_form(self):
        n = len(self.nums)
        result = []
        for i in range(n):
            index = abs(self.nums[i]) - 1
            if self.nums[index] < 0:
                result.append(abs(self.nums[i]))
            else:
                self.nums[index] = -self.nums[index]
        return result
    def public_Array_form(self):
        return self.__private_Array_form()

#--------------:
print(AFO([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]).public_Array_form() == [])
print(AFO([1, 1, 1, 2, 2, 2, 3, 3, 3]).public_Array_form() == [1, 1, 2, 2, 3, 3])
print(AFO([3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]).public_Array_form() == [3, 3, 4, 4, 5, 5, 6, 6])
