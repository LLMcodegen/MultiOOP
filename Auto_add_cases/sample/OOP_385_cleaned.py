
class RST:
    def __init__(self, s):
        self.s = s
class SN_RST(RST):
    def Repeated_substring(self):
        s = self.s
        n = len(s)
        longest_substr = ""
        seen = set()
        for l in range(1, n):
            for i in range(n - l + 1):
                substr = s[i:i + l]
                if substr in seen:
                    if len(substr) > len(longest_substr):
                        longest_substr = substr
                else:
                    seen.add(substr)
        return longest_substr

#--------------:
print(SN_RST("abacabad").Repeated_substring() == "aba")
print(SN_RST("xyzxyzxyz").Repeated_substring() == "xyzxyz")
print(SN_RST("abracadabra").Repeated_substring() == "abra")
