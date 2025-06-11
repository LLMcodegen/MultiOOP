
class CS:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    def _private_Continuous_subarray(self):
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}
        for num in self.nums:
            prefix_sum += num
            if prefix_sum - self.k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - self.k]
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
        return count
    def public_Continuous_subarray(self):
        return self._private_Continuous_subarray()

#--------------:
print(CS([-1, -1, 1, 1], 0).public_Continuous_subarray() == 2)
print(CS([5, 5, 5], 10).public_Continuous_subarray() == 2)
print(CS([1, 2, 3, 4], 7).public_Continuous_subarray() == 1)
