
class MI:
    def __init__(self, n):
        self.n = n
    def __private_Minimum_integer(self):
        from itertools import permutations
        str_n = str(self.n)
        length = len(str_n)
        perms = permutations(str_n)
        greater_numbers = {int(''.join(p)) for p in perms if int(''.join(p)) > self.n}
        if not greater_numbers:
            return -1
        return min(greater_numbers)
    def public_Minimum_integer(self):
        return self.__private_Minimum_integer()

#--------------:
print(MI(124).public_Minimum_integer() == 142)
print(MI(213).public_Minimum_integer() == 231)
print(MI(100).public_Minimum_integer() == -1)
