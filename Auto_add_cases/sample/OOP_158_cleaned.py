
class EMSP:
    def __init__(self, matchsticks):
        self.matchsticks = matchsticks
    def _private_Each_matchstick(self):
        total_length = sum(self.matchsticks)
        if total_length % 4 != 0:
            return False
        side_length = total_length // 4
        return self._can_form_square(side_length, [0] * 4, self.matchsticks, 0)
    def _can_form_square(self, side_length, sides, matchsticks, index):
        if index == len(matchsticks):
            return all(side == side_length for side in sides)
        for i in range(4):
            if sides[i] + matchsticks[index] <= side_length:
                sides[i] += matchsticks[index]
                if self._can_form_square(side_length, sides, matchsticks, index + 1):
                    return True
                sides[i] -= matchsticks[index]
        return False
    def public_Each_matchstick(self):
        return self._private_Each_matchstick()

#--------------:
print(EMSP([1, 1, 1, 1, 1, 1, 1, 1]).public_Each_matchstick() == True)
print(EMSP([8, 8, 8, 8]).public_Each_matchstick() == True)
print(EMSP([1, 1, 1, 1, 1, 5]).public_Each_matchstick() == False)
