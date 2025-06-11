
class SNE:
    def __init__(self, n, primes):
        self.n = n
        self.primes = primes
    def __private_Super_Number(self):
        ugly = [1]
        indices = [0] * len(self.primes)
        next_multiples = self.primes.copy()
        for _ in range(1, self.n):
            next_ugly = min(next_multiples)
            ugly.append(next_ugly)
            for i in range(len(self.primes)):
                if next_ugly == next_multiples[i]:
                    indices[i] += 1
                    next_multiples[i] = ugly[indices[i]] * self.primes[i]
        return ugly[-1]
    def public_Super_Number(self):
        return self.__private_Super_Number()

#--------------:
print(SNE(25, [5, 7, 11]).public_Super_Number() == 1715)
print(SNE(30, [3, 5, 13]).public_Super_Number() == 845)
print(SNE(18, [2, 11, 17]).public_Super_Number() == 176)
