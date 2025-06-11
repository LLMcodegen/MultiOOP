
class NSY:
    def __init__(self, nums):
        self.nums = nums
class SN_NSY(NSY):
    def __init__(self, nums, goal):
        super().__init__(nums)
        self.goal = goal
    def Non_subarray(self):
        count = 0
        current_sum = 0
        sum_count = {0: 1}
        for num in self.nums:
            current_sum += num
            if current_sum - self.goal in sum_count:
                count += sum_count[current_sum - self.goal]
            sum_count[current_sum] = sum_count.get(current_sum, 0) + 1
        return count

#--------------:
print(SN_NSY([1, 2, 3, 4, 5], 15).Non_subarray() == 1)
print(SN_NSY([1, 2, 3, 4, 5], 0).Non_subarray() == 0)
print(SN_NSY([0, 1, 0, 1, 0], 2).Non_subarray() == 4)
