class ITOC:
    def Invert_outcome(self, x: int) -> int:
        if not (-2**31 <= x <= 2**31 - 1):
            raise ValueError("Input is not a 32-bit signed integer")
        str_x = str(x)
        if str_x[0] == '-':
            reversed_str_x = '-' + str_x[:0:-1]
        else:
            reversed_str_x = str_x[::-1]
        reversed_x = int(reversed_str_x)
        if not (-2**31 <= reversed_x <= 2**31 - 1):
            return 0
        return reversed_x
#--------------:
print(ITOC().Invert_outcome(-2147483648) == 0)
print(ITOC().Invert_outcome(1001) == 1001)