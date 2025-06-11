
class FTM:
    def __init__(self, s):
        self.s = s
class SN_FTM(FTM):
    def Flip_Times(self):
        flips = 0
        ones = 0
        for c in self.s:
            if c == '0':
                if ones > 0:
                    flips += 1
            else:
                ones += 1
            flips = min(flips, ones)
        return flips

#--------------:
print(SN_FTM("010101").Flip_Times() == 2)
print(SN_FTM("101010").Flip_Times() == 3)
print(SN_FTM("001111").Flip_Times() == 0)