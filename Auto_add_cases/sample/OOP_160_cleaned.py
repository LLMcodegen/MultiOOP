
class ANUB:
    def __init__(self, nums):
        self.nums = nums
    def __private_Any_numbers(self):
        def hamming_distance(x, y):
            return bin(x ^ y).count('1')
        total_distance = 0
        n = len(self.nums)
        for i in range(n):
            for j in range(i + 1, n):
                total_distance += hamming_distance(self.nums[i], self.nums[j])
        return total_distance
    def public_Any_numbers(self):
        return self.__private_Any_numbers()


#--------------:
print(ANUB([10, 15, 20]).public_Any_numbers() == 10)
print(ANUB([5, 6]).public_Any_numbers() == 2)
print(ANUB([7, 8, 9]).public_Any_numbers() == 8)
