
class LI:
    def __init__(self, nums):
        self.nums = nums
    def __private_Local_inversion(self):
        n = len(self.nums)
        local_inversions = 0
        global_inversions = 0
        for i in range(n - 1):
            if self.nums[i] > self.nums[i + 1]:
                local_inversions += 1
        for i in range(n):
            for j in range(i + 1, n):
                if self.nums[i] > self.nums[j]:
                    global_inversions += 1
        return local_inversions == global_inversions
    def public_Local_inversion(self):
        return self.__private_Local_inversion()

#--------------:
print(LI([1, 0, 3, 2]).public_Local_inversion() == True)
print(LI([3, 2, 1, 0]).public_Local_inversion() == False)
print(LI([0, 3, 2, 1]).public_Local_inversion() == False)
