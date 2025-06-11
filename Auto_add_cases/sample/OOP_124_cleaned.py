
class VED:
    def __init__(self, data):
        self.data = data
    def _private_Valid_encoding(self):
        def get_byte_count(byte):
            if byte & 0x80 == 0:
                return 1
            elif byte & 0xE0 == 0xC0:
                return 2
            elif byte & 0xF0 == 0xE0:
                return 3
            elif byte & 0xF8 == 0xF0:
                return 4
            else:
                return -1
        i = 0
        while i < len(self.data):
            byte_count = get_byte_count(self.data[i])
            if byte_count == -1:
                return False
            if i + byte_count > len(self.data):
                return False
            for j in range(1, byte_count):
                if self.data[i + j] & 0xC0 != 0x80:
                    return False
            i += byte_count
        return True

    def public_Valid_encoding(self):
        return self._private_Valid_encoding()

#--------------:
print(VED([0b11000010, 0b11000010]).public_Valid_encoding() == False)
print(VED([0b11100010, 0b10000010]).public_Valid_encoding() == False)
print(VED([0b11110000, 0b10000010]).public_Valid_encoding() == False)
