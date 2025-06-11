class AC:
    def Array_conditions(self, nums, indexDiff, valueDiff):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + indexDiff + 1, n)):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False
#--------------:
print(AC().Array_conditions([5, 10, 15, 20], 2, 4) == False)
print(AC().Array_conditions([7, 11, 9, 15], 1, 3) == True)
print(AC().Array_conditions([20, 30, 40, 50], 1, 8) == False)
