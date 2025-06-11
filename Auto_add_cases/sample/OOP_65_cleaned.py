class RV:
    def Return_value(self, n):
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)
#--------------:
print(RV().Return_value(1) == 0)
print(RV().Return_value(100) == 25)
print(RV().Return_value(3) == 1)