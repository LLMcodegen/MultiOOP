
class LSS:
    def __init__(self, nums):
        self.nums = nums
    def __private_Longest_subsequence(self):
        if not self.nums:
            return 0
        n = len(self.nums)
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if self.nums[i] > self.nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif self.nums[i] < self.nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[-1], down[-1])
    def public_Longest_subsequence(self):
        return self.__private_Longest_subsequence()

#--------------:
print(LSS([1, 5, 4, 3, 8, 6]).public_Longest_subsequence() == 5)
print(LSS([2, 2, 1, 4, 3, 5, 6]).public_Longest_subsequence() == 5)
print(LSS([5, 1, 5, 1, 5]).public_Longest_subsequence() == 5)
