
class SSA:
    def __init__(self, arr):
        self.arr = arr
class SN_SSA(SSA):
    def __init__(self, arr, k):
        super().__init__(arr)
        self.k = k
    def Sum_subarrays(self):
        modified_arr = self.arr * self.k
        max_sum = float('-inf')
        current_sum = 0
        for num in modified_arr:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum if max_sum > 0 else 0

#--------------:
print(SN_SSA([-1, 2, -1], 4).Sum_subarrays() == 2)
print(SN_SSA([1, 2, 3, 4], 2).Sum_subarrays() == 20)
print(SN_SSA([1, -2, 3, -4, 5], 2).Sum_subarrays() == 8)
