
class ISQE:
    def __init__(self, nums):
        self.nums = nums
    def __private_increasing_subsequence(self):
        def backtrack(start, prev, path, result):
            if len(path) >= 2:
                result.append(path[:])
            for i in range(start, len(self.nums)):
                if self.nums[i] >= prev:
                    path.append(self.nums[i])
                    backtrack(i + 1, self.nums[i], path, result)
                    path.pop()
        result = []
        backtrack(0, float('-inf'), [], result)
        return result
    def public_increasing_subsequence(self):
        return self.__private_increasing_subsequence()

#--------------:
print(ISQE([3, 3, 3]).public_increasing_subsequence() == [[3, 3], [3, 3, 3], [3, 3], [3, 3]])
print(ISQE([1, 1, 2, 2]).public_increasing_subsequence() == [[1, 1], [1, 1, 2], [1, 1, 2, 2], [1, 1, 2], [1, 2], [1, 2, 2], [1, 2], [1, 2], [1, 2, 2], [1, 2], [2, 2]])
print(ISQE([4, 5, 6, 7]).public_increasing_subsequence() == [[4, 5], [4, 5, 6], [4, 5, 6, 7], [4, 5, 7], [4, 6], [4, 6, 7], [4, 7], [5, 6], [5, 6, 7], [5, 7], [6, 7]])
