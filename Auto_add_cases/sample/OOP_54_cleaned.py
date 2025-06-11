class PE:
    def Peak_elements(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
#--------------:
print(PE().Peak_elements([0, 10, 5, 2]) == 1)
print(PE().Peak_elements([3, 2, 1, 2, 3, 1]) == 4)
print(PE().Peak_elements([1, 100, 50, 20, 10, 200, 300]) == 1)
