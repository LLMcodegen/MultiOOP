
class AP:
    def __init__(self, nums):
        self.nums = nums
    def __private_Add_parentheses(self):
        if len(self.nums) == 1:
            return str(self.nums[0])
        elif len(self.nums) == 2:
            return f"{self.nums[0]}/{self.nums[1]}"
        else:
            return f"{self.nums[0]}/(" + "/".join(map(str, self.nums[1:])) + ")"
    def public_Add_parentheses(self):
        return self.__private_Add_parentheses()

#--------------:
print(AP([1, 2, 3, 4]).public_Add_parentheses() == "1/(2/3/4)")
print(AP([9, 3, 1, 1]).public_Add_parentheses() == "9/(3/1/1)")
print(AP([20, 5]).public_Add_parentheses() == "20/5")
