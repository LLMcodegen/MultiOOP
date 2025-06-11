
class NDT:
    def __init__(self, nums, n):
        self.nums = nums
        self.n = n
    def __private_Number_digits(self):
        missing = 1
        added_count = 0
        i = 0
        while missing <= self.n:
            if i < len(self.nums) and self.nums[i] <= missing:
                missing += self.nums[i]
                i += 1
            else:
                missing += missing
                added_count += 1
        return added_count
    def public_Number_digits(self):
        return self.__private_Number_digits()

#--------------:

print(NDT([1, 2, 3, 8], 10).public_Number_digits() == 1)
print(NDT([1, 5, 11], 25).public_Number_digits() == 3)
print(NDT([1, 4, 7], 15).public_Number_digits() == 2)
