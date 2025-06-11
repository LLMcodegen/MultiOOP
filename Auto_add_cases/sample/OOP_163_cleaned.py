
import math

class MBS:
    def __init__(self, n):
        self.n = int(n)
    def __private_Minimum_base(self):
        n = self.n
        max_m = int(math.log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n**(1/m))
            if (k**(m+1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)
    def public_Minimum_base(self):
        return self.__private_Minimum_base()

#--------------:
print(MBS("6").public_Minimum_base() == "5")
print(MBS("7").public_Minimum_base() == "2")
print(MBS("8").public_Minimum_base() == "7")
