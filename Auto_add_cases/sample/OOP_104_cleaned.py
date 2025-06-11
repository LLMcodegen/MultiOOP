
class PMM:
    def __init__(self, n):
        self.n = n
    def __private_Product_maximization(self):
        def maximize_product(n):
            if n == 2:
                return 1
            if n == 3:
                return 2
            if n == 4:
                return 4
            product = 1
            while n > 4:
                product *= 3
                n -= 3
            product *= n
            return product
        return maximize_product(self.n)
    def public_Product_maximization(self):
        return self.__private_Product_maximization()

#--------------:
print(PMM(11).public_Product_maximization() == 54)
print(PMM(12).public_Product_maximization() == 81)
print(PMM(13).public_Product_maximization() == 108)
