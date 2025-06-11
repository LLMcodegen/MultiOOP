class BASTI:
    def binary_string(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        sum_int = int_a + int_b
        sum_binary = bin(sum_int)[2:]
        return sum_binary
#--------------:
print(BASTI().binary_string("101010", "1101") == "110111")
print(BASTI().binary_string("1111", "1111") == "11110")
print(BASTI().binary_string("1001", "1010") == "10011")
