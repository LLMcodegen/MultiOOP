
class LSU:
    def __init__(self, nums):
        self.nums = nums
    def __private_Longest_subsequence(self):
        if len(self.nums) < 3:
            return False
        min1 = float('inf')
        min2 = float('inf')
        for num in self.nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        return False
    def public_Longest_subsequence(self):
        return self.__private_Longest_subsequence()

#--------------:

print(LSU([11, 12, 8, 6, 10]).public_Longest_subsequence() == False)
print(LSU([1, 2, 3]).public_Longest_subsequence() == True)
print(LSU([2, 3]).public_Longest_subsequence() == False)
