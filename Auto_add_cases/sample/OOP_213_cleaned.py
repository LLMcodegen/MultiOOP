
from itertools import permutations
from itertools import product

class ME:
    def __init__(self, cards):
        self.cards = cards
    def __private_mathematical_expression(self):
        def apply_operation(a, b, operator):
            if operator == '+':
                return a + b
            elif operator == '-':
                return a - b
            elif operator == '*':
                return a * b
            elif operator == '/' and b != 0:
                return a / b
            return None
        def check(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24) < 1e-6
            for i in range(len(cards)):
                for j in range(len(cards)):
                    if i != j:
                        remaining_cards = [cards[k] for k in range(len(cards)) if k != i and k != j]
                        for operator in ['+', '-', '*', '/']:
                            result = apply_operation(cards[i], cards[j], operator)
                            if result is not None:
                                if check(remaining_cards + [result]):
                                    return True
            return False
        for perm in permutations(self.cards):
            if check(list(perm)):
                return True
        return False
    def public_mathematical_expression(self):
        return self.__private_mathematical_expression()

#--------------:
print(ME([1, 3, 4, 6]).public_mathematical_expression() == True)
print(ME([2, 3, 8, 9]).public_mathematical_expression() == True)
print(ME([1, 2, 3, 4]).public_mathematical_expression() == True)
