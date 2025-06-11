
class SS:
    def __init__(self, nums):
        self.nums = nums
    def __private_Shortest_subarray(self):
        nums = self.nums
        n = len(nums)
        if n <= 1:
            return 0
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        subarray_min = min(nums[left:right + 1])
        subarray_max = max(nums[left:right + 1])
        while left > 0 and nums[left - 1] > subarray_min:
            left -= 1
        while right < n - 1 and nums[right + 1] < subarray_max:
            right += 1
        return right - left + 1
    def public_Shortest_subarray(self):
        return self.__private_Shortest_subarray()

#--------------:
print(SS([10, 11, 12, 13, 14, 15, 9]).public_Shortest_subarray() == 7)
print(SS([1, 2, 3, 5, 4]).public_Shortest_subarray() == 2)
print(SS([5, 6, 7, 8, 9, 10, 11]).public_Shortest_subarray() == 0)
