
class DSG:
    def __init__(self, S):
        self.S = S
class SN_DSG(DSG):
    def __init__(self, S, K):
        super().__init__(S)
        self.K = K
    def Decode_String(self):
        S = self.S
        K = self.K
        length = 0
        for c in S:
            if c.isdigit():
                length *= int(c)
            else:
                length += 1
        for i in range(len(S) - 1, -1, -1):
            c = S[i]
            if c.isdigit():
                length //= int(c)
                K %= length
            else:
                if K == 0 or K == length:
                    return c
                length -= 1
        return ""

#--------------:
print(SN_DSG("abcd5", 8).Decode_String() == "d")
print(SN_DSG("g5h2i3", 12).Decode_String() == "h")
print(SN_DSG("wxyz4", 7).Decode_String() == "y")
