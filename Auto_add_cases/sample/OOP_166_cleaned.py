
class DESI:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def public_Different_expressions(self):
        return self.__private_Different_expressions()
    def __private_Different_expressions(self):
        def backtrack(index, current_sum):
            if index == len(self.nums):
                return 1 if current_sum == self.target else 0
            positive = backtrack(index + 1, current_sum + self.nums[index])
            negative = backtrack(index + 1, current_sum - self.nums[index])
            return positive + negative
        return backtrack(0, 0)

#--------------:
print(DESI([2, 2, 2], 2).public_Different_expressions() == 3)
print(DESI([1, 2, 3, 4], 5).public_Different_expressions() == 0)
print(DESI([1, 1, 1, 1], 4).public_Different_expressions() == 1)
