
class ES:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    def __private_Equal_sum(self):
        total_sum = sum(self.nums)
        if total_sum % self.k != 0:
            return False
        target = total_sum // self.k
        used = [False] * len(self.nums)
        def backtrack(start, k, subset_sum):
            if k == 0:
                return True
            if subset_sum == target:
                return backtrack(0, k - 1, 0)
            for i in range(start, len(self.nums)):
                if not used[i] and subset_sum + self.nums[i] <= target:
                    used[i] = True
                    if backtrack(i + 1, k, subset_sum + self.nums[i]):
                        return True
                    used[i] = False
            return False
        return backtrack(0, self.k, 0)
    def public_Equal_sum(self):
        return self.__private_Equal_sum()

#--------------:
print(ES([1, 1, 1, 1], 1).public_Equal_sum() == True)
print(ES([1, 1, 1, 1], 5).public_Equal_sum() == False)
print(ES([1, 2, 3, 4, 5, 6], 3).public_Equal_sum() == True)
