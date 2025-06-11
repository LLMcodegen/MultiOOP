
from fractions import Fraction

class SNR:
    def __init__(self, s):
        self.s = s
class SN_SNR(SNR):
    def __init__(self, s, t):
        super().__init__(s)
        self.t = t
    def Same_number(self):
        def parse_number(s):
            if '.' in s:
                integer_part_str, decimal_part_str = s.split('.', 1)
            else:
                integer_part_str, decimal_part_str = s, ''
            integer_part = int(integer_part_str) if integer_part_str else 0

            if '(' in decimal_part_str:
                non_repeating_part_str, repeating_part_str = decimal_part_str.split('(')
                repeating_part_str = repeating_part_str.rstrip(')')
            else:
                non_repeating_part_str, repeating_part_str = decimal_part_str, ''
            non_repeating_part_str = non_repeating_part_str or ''
            repeating_part_str = repeating_part_str or ''
            if repeating_part_str:
                non_repeating_len = len(non_repeating_part_str)
                repeating_len = len(repeating_part_str)
                if non_repeating_part_str:
                    numerator = int(non_repeating_part_str + repeating_part_str) - int(non_repeating_part_str)
                else:
                    numerator = int(repeating_part_str)
                denominator = (10 ** (non_repeating_len + repeating_len) - 10 ** non_repeating_len)
            else:
                if non_repeating_part_str:
                    numerator = int(non_repeating_part_str)
                    denominator = 10 ** len(non_repeating_part_str)
                else:
                    numerator = 0
                    denominator = 1
            fraction_part = Fraction(numerator, denominator)
            total_fraction = Fraction(integer_part) + fraction_part
            return total_fraction
        fraction_s = parse_number(self.s)
        fraction_t = parse_number(self.t)
        return fraction_s == fraction_t

#--------------:
print(SN_SNR("12", "12").Same_number() == True)
print(SN_SNR("0.5", "0.50").Same_number() == True)