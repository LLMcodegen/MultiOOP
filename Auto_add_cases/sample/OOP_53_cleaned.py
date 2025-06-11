class NCS:
    def non_empty_subarray(self, nums):
        if not nums:
            return 0
        max_prod = min_prod = result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            result = max(result, max_prod)
        return result
#--------------:
print(NCS().non_empty_subarray([2, 3, -2, 4, -1]) == 48)
print(NCS().non_empty_subarray([-4, -3, -2, -1, 0]) == 24)
print(NCS().non_empty_subarray([1, 2, 3, 4, 5]) == 120)
