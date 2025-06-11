
class ETG:
    def __init__(self, s: str):
        self.s = s
class SN_ETG(ETG):
    def __init__(self, s: str, n: int):
        super().__init__(s)
        self.n = n
    def Each_integer(self) -> bool:
        for i in range(1, self.n + 1):
            binary_representation = bin(i)[2:]
            if binary_representation not in self.s:
                return False
        return True

#--------------:
print(SN_ETG("110111", 6).Each_integer() == False)
print(SN_ETG("110111", 7).Each_integer() == False)
print(SN_ETG("110111", 8).Each_integer() == False)
