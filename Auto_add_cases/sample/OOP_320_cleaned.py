
class ASG:
    def __init__(self, nums):
        self.nums = nums
class SN_ASG(ASG):
    def Array_sorting(self):
        evens = [num for num in self.nums if num % 2 == 0]
        odds = [num for num in self.nums if num % 2 != 0]
        sorted_array = [0] * len(self.nums)
        sorted_array[::2] = evens
        sorted_array[1::2] = odds
        return sorted_array

#--------------:
print(SN_ASG([1, 2, 3, 4]).Array_sorting() == [2, 1, 4, 3])
print(SN_ASG([1, 6]).Array_sorting() == [6, 1])
print(SN_ASG([1, 2, 6]).Array_sorting() == [2, 1, 6])
