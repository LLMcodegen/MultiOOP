
class BC:
    def __init__(self, bits):
        self.bits = bits
    def __private_Bit_character(self):
        i = 0
        while i < len(self.bits) - 1:
            if self.bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == len(self.bits) - 1
    def public_Bit_character(self):
        return self.__private_Bit_character()

#--------------:
print(BC([1, 0, 1, 0]).public_Bit_character() == False)
print(BC([0, 1, 0]).public_Bit_character() == False)
print(BC([1, 0, 0, 0]).public_Bit_character() == True)
