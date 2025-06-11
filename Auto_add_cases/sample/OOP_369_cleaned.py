
class MIR:
    def __init__(self, k):
        self.k = k
class SN_MIR(MIR):
    def Minimum_integer(self):
        remainder = 1 % self.k
        length = 1
        remainders_seen = set()
        remainders_seen.add(remainder)
        while True:
            if remainder == 0:
                return length
            remainder = (remainder * 10 + 1) % self.k
            length += 1
            if remainder in remainders_seen:
                return -1
            remainders_seen.add(remainder)

#--------------:
print(SN_MIR(6).Minimum_integer() == -1)
print(SN_MIR(7).Minimum_integer() == 6)
print(SN_MIR(8).Minimum_integer() == -1)
