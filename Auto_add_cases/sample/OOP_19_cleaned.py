class TSPI:
    def smallest_positive_integer(self, nums):
        num_set = set(nums)
        smallest_positive = 1
        while smallest_positive in num_set:
            smallest_positive += 1
        return smallest_positive
#--------------:
print(TSPI().smallest_positive_integer([1, 2, 5, 7, 11]) == 3)  # 3
print(TSPI().smallest_positive_integer([10, 20, 30]) == 1)  # 1
print(TSPI().smallest_positive_integer([1, 2, 3, 7, 8, 9]) == 4)  # 4