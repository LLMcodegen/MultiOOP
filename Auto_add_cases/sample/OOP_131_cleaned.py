
class CSR:
    def __init__(self, nums, m):
        self.nums = nums
        self.m = m
    def __private_Continuous_subarray(self):
        def can_split(max_sum):
            count = 1
            current_sum = 0
            for num in self.nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
            return count <= self.m
        left, right = max(self.nums), sum(self.nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left
    def public_Continuous_subarray(self):
        return self.__private_Continuous_subarray()

#--------------:
print(CSR([2, 3, 5, 7, 11], 2).public_Continuous_subarray() == 17)
print(CSR([10, 5, 7, 8], 3).public_Continuous_subarray() == 12)
print(CSR([100, 200, 300, 400], 2).public_Continuous_subarray() == 600)
