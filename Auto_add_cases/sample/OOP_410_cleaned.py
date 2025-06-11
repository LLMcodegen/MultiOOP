
class JAR:
    def __init__(self, nums):
        self.nums = nums
class SN_JAR(JAR):
    def jagged_array(self):
        nums = self.nums
        n = len(nums)
        res = [0, 0]
        for k in [0, 1]:
            moves = 0
            for i in range(n):
                left = nums[i - 1] if i - 1 >= 0 else float('inf')
                right = nums[i + 1] if i + 1 < n else float('inf')
                min_adjacent = min(left, right)
                if i % 2 == k:
                    if nums[i] >= min_adjacent:
                        decrease = nums[i] - (min_adjacent - 1)
                        moves += decrease
                else:
                    pass
            res[k] = moves
        return min(res)

#--------------:
print(SN_JAR([5, 1, 5, 1, 5]).jagged_array() == 0)
print(SN_JAR([1, 5, 1, 5, 1, 5]).jagged_array() == 0)
print(SN_JAR([5, 1, 5, 1, 5, 1]).jagged_array() == 0)
