
class SSG:
    def __init__(self, s):
        self.s = s
class SN_SSG(SSG):
    def __init__(self, s, k):
        super().__init__(s)
        self.k = k
    def Smallest_string(self):
        if self.k == 1:
            s = self.s
            min_s = s
            for i in range(len(s)):
                rotated = s[i:] + s[:i]
                if rotated < min_s:
                    min_s = rotated
            return min_s
        else:
            return ''.join(sorted(self.s))

#--------------:
print(SN_SSG("bca", 1).Smallest_string() == "abc")
print(SN_SSG("bca", 2).Smallest_string() == "abc")
print(SN_SSG("bca", 3).Smallest_string() == "abc")
