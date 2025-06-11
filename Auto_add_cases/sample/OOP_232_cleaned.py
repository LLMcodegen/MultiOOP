
class MI:
    def __init__(self, n):
        self.n = n
    def __private_monotonic_increase(self):
        digits = [int(d) for d in str(self.n)]
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                for j in range(i, len(digits)):
                    digits[j] = 9
        return int(''.join(map(str, digits)))
    def public_monotonic_increase(self):
        return self.__private_monotonic_increase()

#--------------:
print(MI(10).public_monotonic_increase() == 9)
print(MI(999).public_monotonic_increase() == 999)
print(MI(12321).public_monotonic_increase() == 12299)
