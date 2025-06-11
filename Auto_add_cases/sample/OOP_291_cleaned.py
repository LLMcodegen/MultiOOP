
class SEY:
    def __init__(self, nums):
        self.nums = nums
class SN_SEY(SEY):
    def __init__(self, nums, k):
        super().__init__(nums)
        self.k = k
    def Shortest_empty(self):
        n = len(self.nums)
        min_length = n + 1
        current_sum = 0
        left = 0
        for right in range(n):
            current_sum += self.nums[right]
            while current_sum >= self.k:
                min_length = min(min_length, right - left + 1)
                current_sum -= self.nums[left]
                left += 1
        return min_length if min_length != n + 1 else -1

#--------------:
print(SN_SEY([1, 2, 3, 4, 5], 10).Shortest_empty() == 3)
print(SN_SEY([1, 2, 3, 4, 5], 5).Shortest_empty() == 1)
print(SN_SEY([1, 2, 3, 4, 5], 1).Shortest_empty() == 1)
