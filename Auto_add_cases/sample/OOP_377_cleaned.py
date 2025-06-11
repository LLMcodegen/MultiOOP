
class OSR:
    def __init__(self, nums):
        self.nums = nums
class SN_OSR(OSR):
    def __init__(self, nums, firstLen, secondLen):
        super().__init__(nums)
        self.firstLen = firstLen
        self.secondLen = secondLen
    def overlapping_subarray(self):
        n = len(self.nums)
        max_sum = 0
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + self.nums[i]
        for i in range(n):
            if i + self.firstLen <= n:
                first_sum = prefix_sum[i + self.firstLen] - prefix_sum[i]
                for j in range(i + self.firstLen, n):
                    if j + self.secondLen <= n:
                        second_sum = prefix_sum[j + self.secondLen] - prefix_sum[j]
                        max_sum = max(max_sum, first_sum + second_sum)
            if i + self.secondLen <= n:
                second_sum = prefix_sum[i + self.secondLen] - prefix_sum[i]
                for j in range(i + self.secondLen, n):
                    if j + self.firstLen <= n:
                        first_sum = prefix_sum[j + self.firstLen] - prefix_sum[j]
                        max_sum = max(max_sum, first_sum + second_sum)
        return max_sum

#--------------:
print(SN_OSR([1, 2, 3, 4, 5], 3, 1).overlapping_subarray() == 14)
print(SN_OSR([1, 2, 3, 4, 5], 1, 3).overlapping_subarray() == 14)
print(SN_OSR([1, 2, 3, 4, 5], 5, 3).overlapping_subarray() == 0)
