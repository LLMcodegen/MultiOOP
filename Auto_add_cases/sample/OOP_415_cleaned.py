
class LAM:
    def __init__(self, s):
        self.s = s
class SN_LAM(LAM):
    def Lexicographic_arrangement(self):
        substrings = [self.s[i:j] for i in range(len(self.s)) for j in range(i + 1, len(self.s) + 1)]
        substrings.sort()
        return substrings[-1]

#--------------:
print(SN_LAM("zzz").Lexicographic_arrangement() == "zzz")
print(SN_LAM("abac").Lexicographic_arrangement() == "c")
print(SN_LAM("aab").Lexicographic_arrangement() == "b")
