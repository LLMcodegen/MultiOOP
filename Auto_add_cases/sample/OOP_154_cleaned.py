
class PIGE:
    def __init__(self, maxChoosableInteger, desiredTotal):
        self.maxChoosableInteger = maxChoosableInteger
        self.desiredTotal = desiredTotal
    def _private_Public_integer(self, maxChoosableInteger, desiredTotal, usedNumbers, memo):
        if desiredTotal <= 0:
            return False
        if str(usedNumbers) in memo:
            return memo[str(usedNumbers)]
        for i in range(1, maxChoosableInteger + 1):
            if not (usedNumbers & (1 << i)):
                if not self._private_Public_integer(maxChoosableInteger, desiredTotal - i, usedNumbers | (1 << i), memo):
                    memo[str(usedNumbers)] = True
                    return True
        memo[str(usedNumbers)] = False
        return False
    def public_Public_integer(self):
        if self.maxChoosableInteger >= self.desiredTotal:
            return True
        if (self.maxChoosableInteger * (self.maxChoosableInteger + 1)) // 2 < self.desiredTotal:
            return False
        return self._private_Public_integer(self.maxChoosableInteger, self.desiredTotal, 0, {})

#--------------:
print(PIGE(15, 30).public_Public_integer() == True)
print(PIGE(8, 36).public_Public_integer() == False)
print(PIGE(6, 21).public_Public_integer() == False)
