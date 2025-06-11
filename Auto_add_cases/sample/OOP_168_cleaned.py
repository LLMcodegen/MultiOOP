
class ATSA:
    def __init__(self, nums):
        self.nums = nums
    def __private_Array_traversal(self):
        n = len(self.nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            while stack and self.nums[stack[-1]] < self.nums[i % n]:
                result[stack.pop()] = self.nums[i % n]
            if i < n:
                stack.append(i)
        return result
    def public_Array_traversal(self):
        return self.__private_Array_traversal()

#--------------:
print(ATSA([1, 3, 2, 4]).public_Array_traversal() == [3, 4, 4, -1])
print(ATSA([6, 5, 4, 3, 2, 1]).public_Array_traversal() == [-1, 6, 6, 6, 6, 6])
print(ATSA([2, 4, 3, 5, 1]).public_Array_traversal() == [4, 5, 5, -1, 2])
