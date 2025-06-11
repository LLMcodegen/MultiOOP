class DABA:
    def Digits_bitwise(self, left: int, right: int) -> int:
        shift_count = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift_count += 1
        return left << shift_count
#--------------:
print(DABA().Digits_bitwise(2, 3) == 2)
print(DABA().Digits_bitwise(25, 30) == 24)
print(DABA().Digits_bitwise(60, 65) == 0)
