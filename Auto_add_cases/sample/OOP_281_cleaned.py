
class LMN:
    def __init__(self, arr):
        self.arr = arr
class SN_LMN(LMN):
    def Longest_mountain(self):
        n = len(self.arr)
        if n < 3:
            return 0
        longest = 0
        for i in range(1, n - 1):
            if self.arr[i - 1] < self.arr[i] > self.arr[i + 1]:
                left = i - 1
                right = i + 1
                while left > 0 and self.arr[left - 1] < self.arr[left]:
                    left -= 1
                while right < n - 1 and self.arr[right] > self.arr[right + 1]:
                    right += 1
                current_mountain_length = right - left + 1
                longest = max(longest, current_mountain_length)
        return longest if longest >= 3 else 0

#--------------:
print(SN_LMN([2, 1, 4, 7, 3, 2, 5]).Longest_mountain() == 5)
print(SN_LMN([2, 2, 2, 1, 2, 3, 4, 4, 3, 2, 1, 0]).Longest_mountain() == 0)
