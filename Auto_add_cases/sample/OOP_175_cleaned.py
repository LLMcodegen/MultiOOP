
# import random
# class RS:
#     def __init__(self, w):
#         self.w = w
#     def __private_Return_Subscript(self):
#         total_weight = sum(self.w)
#         probabilities = [weight / total_weight for weight in self.w]
#         return random.choices(range(len(self.w)), probabilities)[0]
#     def public_Return_Subscript(self):
#         return self.__private_Return_Subscript()
    

import random
class RS:
    def __init__(self, w):
        self.w = w
    def __private_Return_Subscript(self):
        total = sum(self.w)
        if total == 0:
            raise ValueError("Sum of weights must be greater than 0.")
        probabilities = [weight / total for weight in self.w]
        return random.choices(range(len(self.w)), weights=probabilities, k=1)[0]
    def public_Return_Subscript(self):
        return self.__private_Return_Subscript()


#--------------:
print(RS([10, 0, 1]).public_Return_Subscript() == 0)
print(RS([0.1, 0.3, 0.6]).public_Return_Subscript() == 2)