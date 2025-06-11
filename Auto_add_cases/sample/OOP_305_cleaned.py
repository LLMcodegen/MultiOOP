
class SWS:
    def __init__(self, nums):
        self.nums = nums
class SN_SWS(SWS):
    def Sum_widths(self):
        total_width = 0
        n = len(self.nums)
        self.nums.sort()
        for i in range(n):
            max_contrib = self.nums[i] * (1 << i)
            min_contrib = self.nums[i] * (1 << (n - i - 1))
            total_width += max_contrib - min_contrib
        return total_width

#--------------:
print(SN_SWS([2, 3, 1]).Sum_widths() == 6)
print(SN_SWS([4, 1, 3, 2]).Sum_widths() == 23)
print(SN_SWS([1, 4, 2, 3]).Sum_widths() == 23)
