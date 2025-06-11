
class IAA:
    def __init__(self, nums):
        self.nums = nums
    def __private_Integer_array(self):
        n = len(self.nums)
        counts = [0] * n
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if self.nums[j] < self.nums[i]:
                    count += 1
            counts[i] = count
        return counts
    def public_Integer_array(self):
        return self.__private_Integer_array()

#--------------:
print(IAA([4, 3, 2, 1]).public_Integer_array() == [3, 2, 1, 0])
print(IAA([6, 2, 7, 5, 1]).public_Integer_array() == [3, 1, 2, 1, 0])
print(IAA([2, 8, 1, 4, 7]).public_Integer_array() == [1, 3, 0, 0, 0])
