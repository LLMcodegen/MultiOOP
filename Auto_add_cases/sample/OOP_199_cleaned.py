
class JI:
    def __init__(self, c):
        self.c = c
    def __private_Judging_integers(self):
        for a in range(int(self.c**0.5) + 1):
            b_squared = self.c - a**2
            b = int(b_squared**0.5)
            if a**2 + b**2 == self.c:
                return True
        return False
    def public_Judging_integers(self):
        return self.__private_Judging_integers()

#--------------:
print(JI(6).public_Judging_integers() == False)
print(JI(8).public_Judging_integers() == True)
print(JI(9).public_Judging_integers() == True)
