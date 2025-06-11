
class ANB:
    def __init__(self, s):
        self.s = s
    def _private_Accumulated_number(self):
        n = len(self.s)
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = self.s[:i], self.s[i:j]
                if (num1.startswith('0') and num1 != '0') or (num2.startswith('0') and num2 != '0'):
                    continue
                while j < n:
                    num3 = str(int(num1) + int(num2))
                    if not self.s.startswith(num3, j):
                        break
                    num1, num2 = num2, num3
                    j += len(num3)
                if j == n:
                    return True
        return False
    def public_Accumulated_number(self):
        return self._private_Accumulated_number()

#--------------:
print(ANB("891891712").public_Accumulated_number() == False)
print(ANB("123581321").public_Accumulated_number() == True)
print(ANB("199100199299").public_Accumulated_number() == True)
