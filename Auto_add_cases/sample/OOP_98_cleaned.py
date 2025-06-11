
class IAN:
    def __init__(self, nums, lower, upper):
        self.nums = nums
        self.lower = lower
        self.upper = upper
    def __private_Interval_and(self):
        count = 0
        n = len(self.nums)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + self.nums[i]
        for i in range(n):
            for j in range(i + 1, n + 1):
                interval_sum = prefix_sums[j] - prefix_sums[i]
                if self.lower <= interval_sum <= self.upper:
                    count += 1
        return count
    def public_Interval_and(self):
        return self.__private_Interval_and()

#--------------:
print(IAN([1, 1, 1, 1], 1, 2).public_Interval_and() == 7)
print(IAN([0, 1, 0, 1, 0], 1, 1).public_Interval_and() == 8)
print(IAN([10, -10, 10], 0, 10).public_Interval_and() == 5)
