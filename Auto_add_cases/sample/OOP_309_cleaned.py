
from itertools import permutations

class EAT:
    def __init__(self, s):
        self.s = s
class SN_EAT(EAT):
    def Effective_arrangement(self):
        n = len(self.s)
        count = 0
        for perm in permutations(range(n + 1)):
            valid = True
            for i in range(n):
                if self.s[i] == 'D' and perm[i] <= perm[i + 1]:
                    valid = False
                    break
                elif self.s[i] == 'I' and perm[i] >= perm[i + 1]:
                    valid = False
                    break
            if valid:
                count += 1
        return count

#--------------:
print(SN_EAT("ID").Effective_arrangement() == 2)
print(SN_EAT("II").Effective_arrangement() == 1)
print(SN_EAT("DIDI").Effective_arrangement() == 16)
