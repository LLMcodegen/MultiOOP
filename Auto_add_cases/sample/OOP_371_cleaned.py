
class NGY:
    def __init__(self, n):
        self.n = n
class SN_NGY(NGY):
    def negabinary(self):
        if self.n == 0:
            return "0"
        result = []
        n = self.n
        while n != 0:
            n, remainder = divmod(n, -2)
            if remainder < 0:
                remainder += 2
                n += 1
            result.append(str(remainder))
        return ''.join(reversed(result))

#--------------:
print(SN_NGY(7).negabinary() == "11011")
print(SN_NGY(8).negabinary() == "11000")
print(SN_NGY(9).negabinary() == "11001")
