
class MRC:
    def __init__(self, n):
        self.n = n
    def __private_Minimum_replacements(self):
        def replacements(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + replacements(num // 2)
            else:
                return 1 + min(replacements(num + 1), replacements(num - 1))
        return replacements(self.n)
    def public_Minimum_replacements(self):
        return self.__private_Minimum_replacements()

#--------------:
print(MRC(99).public_Minimum_replacements() == 9)
print(MRC(4).public_Minimum_replacements() == 2)
print(MRC(3).public_Minimum_replacements() == 2)
