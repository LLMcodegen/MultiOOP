
from itertools import permutations
import math

class SAT:
    def __init__(self, A):
        self.A = A
class SN_SAT(SAT):
    def is_perfect_square(self, num):
        return int(math.isqrt(num)) ** 2 == num
    def Square_arrangement(self):
        count = 0
        unique_permutations = set(permutations(self.A))
        for perm in unique_permutations:
            valid = True
            for i in range(len(perm) - 1):
                if not self.is_perfect_square(perm[i] + perm[i + 1]):
                    valid = False
                    break
            if valid:
                count += 1       
        return count

#--------------:
print(SN_SAT([1, 2, 3]).Square_arrangement() == 0)
print(SN_SAT([9, 16, 25]).Square_arrangement() == 0)
print(SN_SAT([1, 4, 9]).Square_arrangement() == 0)
