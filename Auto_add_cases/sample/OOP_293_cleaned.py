
class NRG:
    def __init__(self, n):
        self.n = n
class SN_NRG(NRG):
    def __init__(self, n):
        super().__init__(n)
    def Number_Reordering(self):
        from itertools import permutations
        str_n = str(self.n)
        for perm in permutations(str_n):
            if perm[0] == '0':
                continue
            num = int(''.join(perm))
            if (num & (num - 1) == 0) and num != 0:
                return True
        return False

#--------------:
print(SN_NRG(4).Number_Reordering() == True)
print(SN_NRG(5).Number_Reordering() == False)
print(SN_NRG(6).Number_Reordering() == False)
