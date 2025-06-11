
class NAR:
    def __init__(self, nums):
        self.nums = nums
    def __private_Number_array(self):
        n = len(self.nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(self.nums)
        return total_sum - actual_sum
    def public_Number_array(self):
        return self.__private_Number_array()

#--------------:
print(NAR([0, 1, 2, 3, 4, 6, 7, 8, 9]).public_Number_array() == 5)
print(NAR([0, 1, 2, 3, 4, 5, 7, 8, 9]).public_Number_array() == 6)
print(NAR([0, 1, 2, 3, 4, 5, 6, 8, 9]).public_Number_array() == 7)
