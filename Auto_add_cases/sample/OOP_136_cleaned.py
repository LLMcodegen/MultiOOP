
class DOR:
    def __init__(self, s):
        self.s = s
    def __private_Disordered_order(self):
        count = {}
        for char in self.s:
            count[char] = count.get(char, 0) + 1
        digits = [0] * 10
        digits[0] = count.get('z', 0)
        digits[2] = count.get('w', 0)
        digits[4] = count.get('u', 0)
        digits[6] = count.get('x', 0)
        digits[8] = count.get('g', 0)
        digits[1] = count.get('o', 0) - digits[0] - digits[2] - digits[4]
        digits[3] = count.get('h', 0) - digits[8]
        digits[5] = count.get('f', 0) - digits[4]
        digits[7] = count.get('s', 0) - digits[6]
        digits[9] = count.get('i', 0) - digits[5] - digits[6] - digits[8]
        result = []
        for i in range(10):
            result.extend([str(i)] * digits[i])
        return ''.join(sorted(result))
    def public_Disordered_order(self):
        return self.__private_Disordered_order()

#--------------:
print(DOR("twosixfourzero").public_Disordered_order() == "0246")
print(DOR("eightthree").public_Disordered_order() == "38")
print(DOR("eightfivefourzero").public_Disordered_order() == "0458")
