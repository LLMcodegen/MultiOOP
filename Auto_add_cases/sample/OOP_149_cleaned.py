
class EEL:
    def __init__(self, nums):
        self.nums = nums
    def __private_Element_equality(self):
        min_element = min(self.nums)
        operations = sum(num - min_element for num in self.nums)
        return operations
    def public_Element_equality(self):
        return self.__private_Element_equality()

#--------------:
print(EEL([2, 2, 2, 5]).public_Element_equality() == 3)
print(EEL([10, 20, 30]).public_Element_equality() == 30)
print(EEL([1, 4, 4, 4, 1]).public_Element_equality() == 9)
