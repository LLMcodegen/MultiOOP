
class MFI:
    def __init__(self, nums):
        self.nums = nums
class SN_MFI(MFI):
    def __init__(self, nums, K):
        super().__init__(nums)
        self.K = K
    def Min_Flip(self):
        flips = 0
        flip_count = 0
        flip_effect = [0] * len(self.nums)
        for i in range(len(self.nums)):
            if i >= self.K:
                flip_count -= flip_effect[i - self.K]
            if (self.nums[i] + flip_count) % 2 == 0:
                if i + self.K > len(self.nums):
                    return -1
                flips += 1
                flip_count += 1
                flip_effect[i] = 1
        return flips

#--------------:
print(SN_MFI([0, 1, 0, 1, 1, 0, 0, 1], 7).Min_Flip() == -1)
print(SN_MFI([0, 1, 0, 1, 1, 0, 0, 1], 8).Min_Flip() == -1)
print(SN_MFI([0, 1, 0, 1, 1, 0, 0, 1], 1).Min_Flip() == 4)
