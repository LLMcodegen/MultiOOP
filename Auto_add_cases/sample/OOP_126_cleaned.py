
class CRT:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
    def _private_clockwise_rotation(self, k):
        rotated = self.nums[-k:] + self.nums[:-k]
        return sum((i * num) for i, num in enumerate(rotated))
    def public_clockwise_rotation(self):
        max_value = float('-inf')
        for k in range(self.n):
            current_value = self._private_clockwise_rotation(k)
            if current_value > max_value:
                max_value = current_value
        return max_value

#--------------:
print(CRT([2, 2, 2, 2]).public_clockwise_rotation() == 12)
print(CRT([-1, -2, -3, -4]).public_clockwise_rotation() == -12)
print(CRT([1, -2, 3, -4]).public_clockwise_rotation() == 6)
