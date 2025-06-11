
class SCT:
    def __init__(self, values):
        self.values = values
class SN_SCT(SCT):
    def Sightseeing_combination(self):
        max_score = 0
        max_i = self.values[0] + 0
        for j in range(1, len(self.values)):
            current_score = max_i + self.values[j] - j
            max_score = max(max_score, current_score)
            max_i = max(max_i, self.values[j] + j)
        return max_score

#--------------:
print(SN_SCT([5, 4, 3, 2, 1]).Sightseeing_combination() == 8)
print(SN_SCT([1, 2, 3, 4, 5]).Sightseeing_combination() == 8)
print(SN_SCT([10, 1, 1, 1, 1]).Sightseeing_combination() == 10)
