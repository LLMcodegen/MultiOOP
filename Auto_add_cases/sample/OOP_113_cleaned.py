
class PIT:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def _private_positive_integer(self):
        def mod_exp(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        def array_to_number(arr):
            num = 0
            for digit in arr:
                num = num * 10 + digit
            return num
        mod = 1337
        exponent = array_to_number(self.b)
        return mod_exp(self.a, exponent, mod)

    def public_positive_integer(self):
        return self._private_positive_integer()

#--------------:
print(PIT(2, [3, 4]).public_positive_integer() == 779)
print(PIT(6, [2, 5]).public_positive_integer() == 1007)
print(PIT(8, [2, 2]).public_positive_integer() == 295)
