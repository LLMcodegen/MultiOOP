
class POE:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    def __private_Product_of_elements(self):
        count = 0
        product = 1
        left = 0
        for right in range(len(self.nums)):
            product *= self.nums[right]
            while product >= self.k and left <= right:
                product //= self.nums[left]
                left += 1
            count += right - left + 1
        return count
    def public_Product_of_elements(self):
        return self.__private_Product_of_elements()

#--------------:
print(POE([10, 2, 2], 50).public_Product_of_elements() == 6)
print(POE([10, 5, 2, 6], 10).public_Product_of_elements() == 3)
print(POE([10, 5, 2, 6], 1).public_Product_of_elements() == 0)
