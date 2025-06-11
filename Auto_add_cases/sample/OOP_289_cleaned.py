
from math import gcd

class RNE:
    def __init__(self, p):
        self.p = p
class SN_RNE(RNE):
    def __init__(self, p, q):
        super().__init__(p)
        self.q = q
    def Receiver_number(self):
        p = self.p
        q = self.q
        n = p - q
        current_gcd = gcd(p, n)
        lcm = (p * n) // current_gcd
        m_prime = lcm // p
        n_prime = lcm // n
        if m_prime % 2 == 1:
            if n_prime % 2 == 1:
                return 0
            else:
                return 2
        else:
            if n_prime % 2 == 1:
                return 1
            else:
                return -1

#--------------:
print(SN_RNE(7, 3).Receiver_number() == 1)
print(SN_RNE(8, 4).Receiver_number() == 2)
print(SN_RNE(9, 4).Receiver_number() == 0)
