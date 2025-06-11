
class SPAR:
    def __init__(self, nums):
        self.nums = nums
    def __private_Subsequences_patterns(self):
        n = len(self.nums)
        if n < 3:
            return False
        min_values = [0] * n
        min_values[0] = self.nums[0]
        for i in range(1, n):
            min_values[i] = min(min_values[i - 1], self.nums[i])
        stack = []
        for j in range(n - 1, -1, -1):
            if self.nums[j] > min_values[j]:
                while stack and stack[-1] <= min_values[j]:
                    stack.pop()
                if stack and stack[-1] < self.nums[j]:
                    return True
                stack.append(self.nums[j])
        return False
    def public_Subsequences_patterns(self):
        return self.__private_Subsequences_patterns()

#--------------:
print(SPAR([4, 1, 3, 2]).public_Subsequences_patterns() == True)
print(SPAR([2, 4, 3, 5, 1]).public_Subsequences_patterns() == True)
print(SPAR([1, 1, 1]).public_Subsequences_patterns() == False)
