
class EqualArrayOperations:
    def __init__(self, nums):
        self.nums = nums
    def __private_One_operation(self):
        sorted_nums = sorted(self.nums)
        median = sorted_nums[len(sorted_nums) // 2]
        operations = sum(abs(num - median) for num in self.nums)
        return operations
    def public_One_operation(self):
        return self.__private_One_operation()

#--------------:
print(EqualArrayOperations([7, 8, 9]).public_One_operation() == 2)
print(EqualArrayOperations([4, 4, 4, 4]).public_One_operation() == 0)
print(EqualArrayOperations([10, 20, 30]).public_One_operation() == 20)
