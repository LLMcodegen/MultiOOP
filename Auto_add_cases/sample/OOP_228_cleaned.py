
class AD:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    def __private_absolute_difference(self):
        sorted_nums = sorted(self.nums)
        n = len(sorted_nums)
        def count_pairs(mid):
            count = 0
            j = 0
            for i in range(n):
                while j < n and sorted_nums[j] - sorted_nums[i] <= mid:
                    j += 1
                count += j - i - 1
            return count
        left, right = 0, sorted_nums[-1] - sorted_nums[0]
        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) < self.k:
                left = mid + 1
            else:
                right = mid
        return left
    def public_absolute_difference(self):
        return self.__private_absolute_difference()

#--------------:
print(AD([1, 2, 3, 4], 2).public_absolute_difference() == 1)
print(AD([1, 2, 3, 4], 3).public_absolute_difference() == 1)
print(AD([1, 2, 3, 4], 4).public_absolute_difference() == 2)
