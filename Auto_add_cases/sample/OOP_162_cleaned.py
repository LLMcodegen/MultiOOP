
class MSRI:
    def __init__(self, n):
        self.n = n
    def _private_Magic_String(self):
        if self.n == 0:
            return 0 
        s = [1, 2, 2]
        index = 2
        while len(s) < self.n:
            next_val = 2 if s[-1] == 1 else 1
            s.extend([next_val] * s[index])
            index += 1
        return s[:self.n].count(1)

    def public_Magic_String(self):
        return self._private_Magic_String()

#--------------:
print(MSRI(5).public_Magic_String() == 3)
print(MSRI(6).public_Magic_String() == 3)
print(MSRI(7).public_Magic_String() == 4)