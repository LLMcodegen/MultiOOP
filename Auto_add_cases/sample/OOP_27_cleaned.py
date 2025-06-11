class FDSB:
    def find_subarray(self, nums):
        if not nums:
            return 0
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global
#--------------:
print(FDSB().find_subarray([-2, -3, 4, -1, -2, 1, 5, -3]) == 7)
print(FDSB().find_subarray([1, 2, 3, 4, 5]) == 15)
print(FDSB().find_subarray([-1, 1, -2, 2, -3, 3]) == 3)
