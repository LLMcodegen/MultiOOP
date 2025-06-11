
class NOO:
    def __init__(self, nums):
        self.nums = nums
    def __Number_occurrences(self):
        low, high = 0, len(self.nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1
            if self.nums[mid] == self.nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return self.nums[low]
    def public_Number_occurrences(self):
        return self.__Number_occurrences()

#--------------:
print(NOO([1, 2, 2, 3, 3, 4, 4, 5, 5]).public_Number_occurrences() == 1)
print(NOO([1, 1, 2, 2, 3, 3, 4, 5, 5]).public_Number_occurrences() == 4)
print(NOO([2, 2, 3, 3, 4, 4, 5, 5, 6]).public_Number_occurrences() == 6)
