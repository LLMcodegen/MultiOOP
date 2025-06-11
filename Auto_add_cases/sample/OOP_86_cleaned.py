
class NDC:
    def __init__(self, nums):
        self.nums = nums
    def __private_Number_duplicates(self):
        tortoise = self.nums[0]
        hare = self.nums[0]
        while True:
            tortoise = self.nums[tortoise]
            hare = self.nums[self.nums[hare]]
            if tortoise == hare:
                break
        tortoise = self.nums[0]
        while tortoise != hare:
            tortoise = self.nums[tortoise]
            hare = self.nums[hare]
        return tortoise
    def public_Number_duplicates(self):
        return self.__private_Number_duplicates()
    
#--------------:
print(NDC([1, 3, 4, 2, 2]).public_Number_duplicates() == 2)
print(NDC([3, 1, 3, 4, 2]).public_Number_duplicates() == 3)