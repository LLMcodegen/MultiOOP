
class NDE:
    def __init__(self, n):
        self.n = n
    def __private_Numbers_different(self):
        def has_unique_digits(x):
            return len(set(str(x))) == len(str(x))
        count = 0
        for x in range(10**self.n):
            if has_unique_digits(x):
                count += 1
        return count
    def public_Numbers_different(self):
        return self.__private_Numbers_different()

#--------------:
print(NDE(0).public_Numbers_different() == 1)
print(NDE(1).public_Numbers_different() == 10)
print(NDE(7).public_Numbers_different() == 712891)