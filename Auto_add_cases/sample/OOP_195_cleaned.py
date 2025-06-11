
class NOT:
    def __init__(self, nums):
        self.nums = nums
    def __private_Number_of_triples(self):
        count = 0
        n = len(self.nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.nums[i] + self.nums[j] > self.nums[k] and \
                       self.nums[i] + self.nums[k] > self.nums[j] and \
                       self.nums[j] + self.nums[k] > self.nums[i]:
                        count += 1
        return count
    def public_Number_of_triples(self):
        return self.__private_Number_of_triples()

#--------------:
print(NOT([2, 4, 5, 6]).public_Number_of_triples() == 3)
print(NOT([3, 3, 4, 5]).public_Number_of_triples() == 4)
print(NOT([10, 1, 1, 1]).public_Number_of_triples() == 1)
