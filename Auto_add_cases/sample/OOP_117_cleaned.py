
class EAC:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def __private_element_association(self, target, memo):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in memo:
            return memo[target]
        count = 0
        for num in self.nums:
            count += self.__private_element_association(target - num, memo)
        memo[target] = count
        return count
    def public_element_association(self):
        memo = {}
        return self.__private_element_association(self.target, memo)

#--------------:
print(EAC([2, 4, 6], 10).public_element_association() == 13)
print(EAC([1, 3, 4], 7).public_element_association() == 15)
print(EAC([1, 2, 3, 4], 10).public_element_association() == 401)
