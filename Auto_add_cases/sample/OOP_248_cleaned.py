
class GNR:
    def __init__(self, n, k):
        self.n = n
        self.k = k
    def __private_Given_number_rows(self) -> int:
        if self.n == 1:
            return 0
        mid = 2**(self.n - 1) // 2
        if self.k <= mid:
            return GNR(self.n - 1, self.k).__private_Given_number_rows()
        else:
            return 1 - GNR(self.n - 1, self.k - mid).__private_Given_number_rows()
    def public_Given_number_rows(self) -> int:
        return self.__private_Given_number_rows()

#--------------:
print(GNR(3, 3).public_Given_number_rows() == 1)
print(GNR(3, 4).public_Given_number_rows() == 0)
print(GNR(4, 1).public_Given_number_rows() == 0)