
class PLH:
    def __init__(self, nums):
        self.nums = nums
class SN_PLH(PLH):
    def Packet_Length(self):
        n = len(self.nums)
        left_max = [0] * n
        right_min = [0] * n
        left_max[0] = self.nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], self.nums[i])
        right_min[n - 1] = self.nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], self.nums[i])
        for i in range(n - 1):
            if left_max[i] <= right_min[i + 1]:
                return i + 1
        return n

#--------------:
print(SN_PLH([50, 40, 30, 20, 10]).Packet_Length() == 5)
print(SN_PLH([1, 3, 2, 4, 3, 5]).Packet_Length() == 1)
print(SN_PLH([1, 3, 2, 4, 3, 5, 6]).Packet_Length() == 1)
