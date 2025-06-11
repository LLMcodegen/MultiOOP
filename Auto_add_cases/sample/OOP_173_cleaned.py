
class AL:
    def __init__(self, nums):
        self.nums = nums
    def __private_Array_length(self):
        nums = [x if x == 1 else -1 for x in self.nums]
        sum_map = {0: -1}
        max_length = 0
        cumulative_sum = 0
        for i, num in enumerate(nums):
            cumulative_sum += num
            if cumulative_sum in sum_map:
                max_length = max(max_length, i - sum_map[cumulative_sum])
            else:
                sum_map[cumulative_sum] = i
        return max_length
    def public_Array_length(self):
        return self.__private_Array_length()

#--------------:
print(AL([0, 1, 1, 0, 1, 0, 0, 1]).public_Array_length() == 8)
print(AL([1, 1, 1, 1, 1]).public_Array_length() == 0)
print(AL([0, 0, 0, 1, 1, 1, 0]).public_Array_length() == 6)
