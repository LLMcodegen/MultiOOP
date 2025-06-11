
class SAN:
    def __init__(self, s):
        self.s = s
class SN_SAN(SAN):
    def __init__(self, s, shifts):
        super().__init__(s)
        self.shifts = shifts
    def Shift_application(self):
        n = len(self.s)
        shifted_s = list(self.s)
        total_shift = 0
        for i in range(n - 1, -1, -1):
            total_shift += self.shifts[i]
            total_shift %= 26
            shifted_s[i] = chr((ord(self.s[i]) - ord('a') + total_shift) % 26 + ord('a'))
        return ''.join(shifted_s)

#--------------:
print(SN_SAN("abc", [26, 26, 26]).Shift_application() == "abc")
print(SN_SAN("abc", [25, 25, 25]).Shift_application() == "xzb")
print(SN_SAN("abc", [27, 27, 27]).Shift_application() == "ddd")
