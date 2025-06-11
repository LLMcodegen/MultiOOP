
class MPS:
    def __init__(self, s):
        self.s = s
class SN_MPS(MPS):
    def Minimum_parentheses(self):
        left_needed = 0
        right_needed = 0
        for char in self.s:
            if char == '(':
                left_needed += 1
            elif char == ')':
                if left_needed > 0:
                    left_needed -= 1
                else:
                    right_needed += 1
        return left_needed + right_needed

#--------------:
print(SN_MPS("))(").Minimum_parentheses() == 3)
print(SN_MPS("((())").Minimum_parentheses() == 1)
print(SN_MPS("()()").Minimum_parentheses() == 0)
