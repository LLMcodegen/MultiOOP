
from fractions import Fraction

class MS:
    def __init__(self, expression):
        self.expression = expression
    def _private_Minimal_Score(self):
        parts = self.expression.replace('-', '+-').split('+')
        result = Fraction(0, 1)
        for part in parts:
            if part:
                result += Fraction(part)
        return result
    def public_Minimal_Score(self):
        minimal_score = self._private_Minimal_Score()
        return f"{minimal_score.numerator}/{minimal_score.denominator}"

#--------------:
print(MS("4/7+2/14-1/7").public_Minimal_Score() == "4/7")
print(MS("5/4-2/4+1/2").public_Minimal_Score() == "5/4")