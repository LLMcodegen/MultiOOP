
class MS:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    def __private_Maximum_subarray(self):
        n = len(self.nums)
        if n < 3 * self.k:
            return []
        subarray_sums = [0] * (n - self.k + 1)
        curr_sum = sum(self.nums[:self.k])
        subarray_sums[0] = curr_sum
        for i in range(1, n - self.k + 1):
            curr_sum += self.nums[i + self.k - 1] - self.nums[i - 1]
            subarray_sums[i] = curr_sum
        left = [0] * len(subarray_sums)
        right = [0] * len(subarray_sums)
        best_left_idx = 0
        for i in range(len(subarray_sums)):
            if subarray_sums[i] > subarray_sums[best_left_idx]:
                best_left_idx = i
            left[i] = best_left_idx
        best_right_idx = len(subarray_sums) - 1
        for i in range(len(subarray_sums) - 1, -1, -1):
            if subarray_sums[i] >= subarray_sums[best_right_idx]:
                best_right_idx = i
            right[i] = best_right_idx
        max_sum = 0
        result = []
        for mid in range(self.k, len(subarray_sums) - self.k):
            left_idx = left[mid - self.k]
            right_idx = right[mid + self.k]
            total_sum = subarray_sums[left_idx] + subarray_sums[mid] + subarray_sums[right_idx]
            if total_sum > max_sum:
                max_sum = total_sum
                result = [left_idx, mid, right_idx]
        return result
    def public_Maximum_subarray(self):
        return self.__private_Maximum_subarray()

#--------------:
print(MS([1, 2, 3, 4, 5, 6, 7, 8, 9], 3).public_Maximum_subarray() == [0, 3, 6])
print(MS([1, 2, 3, 4, 5, 6, 7, 8, 9], 2).public_Maximum_subarray() == [3, 5, 7])
print(MS([1, 2, 3, 4, 5, 6, 7, 8, 9], 1).public_Maximum_subarray() == [6, 7, 8])
