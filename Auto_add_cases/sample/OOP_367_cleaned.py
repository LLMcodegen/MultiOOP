
class RNS:
    def __init__(self, n):
        self.n = n
class SN_RNS(RNS):
    def __init__(self, n):
        super().__init__(n)
    def Repeating_numbers(self):
        def has_repeating_digits(num):
            str_num = str(num)
            return len(set(str_num)) != len(str_num)
        count = 0
        for i in range(1, self.n + 1):
            if has_repeating_digits(i):
                count += 1
        return count

#--------------:
print(SN_RNS(300).Repeating_numbers() == 66)
print(SN_RNS(150).Repeating_numbers() == 27)
print(SN_RNS(250).Repeating_numbers() == 55)
