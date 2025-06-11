class RTN:
    def Hamming_weight(self, binary_str):
        n = int(binary_str, 2)
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
#--------------:
print(RTN().Hamming_weight('00000000000000001000000000000000') == 1)
print(RTN().Hamming_weight('00000000000000001111111111111111') == 16)
print(RTN().Hamming_weight('11111111111111111111111111111111') == 32)
