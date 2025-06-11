class NLAR:
    def new_length_removal(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
#--------------:
#--------------:
print(NLAR().new_length_removal([10, 20, 30], 10) == 2)
print(NLAR().new_length_removal([100, 200, 300, 100, 400], 100) == 3)
print(NLAR().new_length_removal([1, 2, 3, 4, 5], 2) == 4)
