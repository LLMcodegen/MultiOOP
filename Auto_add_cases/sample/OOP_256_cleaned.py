
class NI:
    def __init__(self, k):
        self.k = k
    def __private_nonnegative_integer(self):
        def count_trailing_zeros(n):
            count = 0
            while n >= 5:
                n //= 5
                count += n
            return count
        low, high = 0, 5 * self.k
        while low <= high:
            mid = (low + high) // 2
            if count_trailing_zeros(mid) < self.k:
                low = mid + 1
            else:
                high = mid - 1
        count = 0
        for x in range(low, low + 5):
            if count_trailing_zeros(x) == self.k:
                count += 1
        return count
    def public_nonnegative_integer(self):
        return self.__private_nonnegative_integer()

#--------------:
print(NI(4).public_nonnegative_integer() == 5)
print(NI(6).public_nonnegative_integer() == 5)
print(NI(7).public_nonnegative_integer() == 5)
