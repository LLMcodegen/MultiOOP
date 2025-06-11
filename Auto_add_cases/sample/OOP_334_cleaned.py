
class INY:
    def __init__(self, tokens):
        self.tokens = tokens
class SN_INY(INY):
    def __init__(self, tokens, power):
        super().__init__(tokens)
        self.power = power
    def Initial_energy(self):
        self.tokens.sort()
        score = 0
        max_score = 0
        left = 0
        right = len(self.tokens) - 1
        while left <= right:
            if self.power >= self.tokens[left]:
                self.power -= self.tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                self.power += self.tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return max_score

#--------------:
print(SN_INY([10, 20, 30], 0).Initial_energy() == 0)
print(SN_INY([10, 20, 30, 40], 50).Initial_energy() == 2)
print(SN_INY([10, 20, 30, 40], 60).Initial_energy() == 3)
