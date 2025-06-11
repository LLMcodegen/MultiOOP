
from collections import Counter
from math import gcd
from functools import reduce

class SIR:
    def __init__(self, deck):
        self.deck = deck
class SN_SIR(SIR):
    def Same_integer(self):
        count = Counter(self.deck)
        frequencies = list(count.values())
        def find_gcd(num_list):
            return reduce(gcd, num_list)
        overall_gcd = find_gcd(frequencies)
        return overall_gcd >= 2

#--------------:
print(SN_SIR([1, 1, 1, 2, 2, 2, 2]).Same_integer() == False)
print(SN_SIR([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]).Same_integer() == True)
print(SN_SIR([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]).Same_integer() == True)
