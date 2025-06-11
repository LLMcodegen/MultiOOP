class ITBB:
    def Invert_the_binary_bits(self, n):
        binary_str = format(n, '032b')
        reversed_binary_str = binary_str[::-1]
        reversed_int = int(reversed_binary_str, 2)
        return reversed_int
#--------------:
print(ITBB().Invert_the_binary_bits(0b10101010101010101010101010101010) == 1431655765)
print(ITBB().Invert_the_binary_bits(0b01010101010101010101010101010101) == 2863311530)
print(ITBB().Invert_the_binary_bits(0b11110000111100001111000011110000) == 252645135)
