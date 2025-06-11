
class BPS:
    def __init__(self, S):
        self.S = S
class SN_BPS(BPS):
    def __init__(self, S):
        super().__init__(S)
    def Balanced_parentheses(self):
        def score_of_string(s, start, end):
            if start + 1 == end:
                return 1
            balance = 0
            for i in range(start, end):
                if s[i] == '(':
                    balance += 1
                elif s[i] == ')':
                    balance -= 1
                if balance == 0:
                    if i == start + 1:
                        return 1 + score_of_string(s, i + 1, end)
                    else:
                        return 2 * score_of_string(s, start + 1, i) + score_of_string(s, i + 1, end)
            return 0
        return score_of_string(self.S, 0, len(self.S))

#--------------:
print(SN_BPS("((()))").Balanced_parentheses() == 4)
print(SN_BPS("(()(()))").Balanced_parentheses() == 6)
print(SN_BPS("((())())").Balanced_parentheses() == 6)
