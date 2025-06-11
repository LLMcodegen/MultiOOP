
class MRU:
    def __init__(self, nums):
        self.nums = nums
    def __private_Maximum_result(self):
        max_result = 0
        n = len(self.nums)
        for i in range(n):
            for j in range(i, n):
                max_result = max(max_result, self.nums[i] ^ self.nums[j])
        return max_result
    def public_Maximum_result(self):
        return self.__private_Maximum_result()

#--------------:
print(MRU([4, 5, 6, 7]).public_Maximum_result() == 3)
print(MRU([12, 34, 56, 78]).public_Maximum_result() == 118)
print(MRU([20, 40, 60, 80]).public_Maximum_result() == 120)
