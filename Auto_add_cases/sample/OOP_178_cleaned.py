
import re

class SOP:
    def __init__(self, num1: str, num2: str):
        self.num1 = self._parse_complex(num1)
        self.num2 = self._parse_complex(num2)
    def _parse_complex(self, num_str: str):
        match = re.match(r'([+-]?\d+)\+([+-]?\d+)i', num_str)
        if match:
            real = int(match.group(1))
            imag = int(match.group(2))
            return complex(real, imag)
        else:
            raise ValueError("Invalid complex number format. Use 'a+bi' format.")
    def __String_product(self):
        product = self.num1 * self.num2
        real_part = int(product.real)
        imag_part = int(product.imag)
        result_str = f"{real_part}+{imag_part}i"
        return result_str
    def public_String_product(self):
        return self.__String_product()

#--------------:
print(SOP("1+0i", "0+1i").public_String_product() == "0+1i")
print(SOP("4+5i", "-1+2i").public_String_product() == "-14+3i")
print(SOP("2+3i", "1+1i").public_String_product() == "-1+5i")
