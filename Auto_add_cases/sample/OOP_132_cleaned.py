
class EAY:
    def __init__(self, nums):
        self.nums = nums
    def __private_Equidistant_array(self):
        n = len(self.nums)
        if n < 3:
            return 0 
        count = 0
        current_length = 2
        diff = self.nums[1] - self.nums[0]
        for i in range(2, n):
            if self.nums[i] - self.nums[i-1] == diff:
                current_length += 1
            else:
                if current_length >= 3:
                    count += (current_length - 2) * (current_length - 1) // 2
                diff = self.nums[i] - self.nums[i-1]
                current_length = 2
        if current_length >= 3:
            count += (current_length - 2) * (current_length - 1) // 2
        return count
    def public_Equidistant_array(self):
        return self.__private_Equidistant_array()

#--------------:
print(EAY([10, 20, 30, 40, 50]).public_Equidistant_array() == 6)
print(EAY([2, 4, 6, 8, 10, 12]).public_Equidistant_array() == 10)
print(EAY([1, 4, 7, 10, 13]).public_Equidistant_array() == 6)
