class TMDBAE:
    def adjacent_elements(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i] - nums[i - 1])
        return max_diff
#--------------:
print(TMDBAE().adjacent_elements([8, 1, 6, 4, 9, 2]) == 2)
print(TMDBAE().adjacent_elements([3, 3, 3, 3]) == 0)
print(TMDBAE().adjacent_elements([5, 1, 9, 3, 7]) == 2)
