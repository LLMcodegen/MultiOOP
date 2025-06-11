
class DOE:
    def __init__(self, n, k):
        self.n = n
        self.k = k
    def __private_Dictionary_order(self):
        def count_steps(prefix, n):
            steps = 0
            cur = prefix
            next_prefix = prefix + 1
            while cur <= n:
                steps += min(n + 1, next_prefix) - cur
                cur *= 10
                next_prefix *= 10
            return steps
        current = 1
        k_remaining = self.k - 1
        while k_remaining > 0:
            steps = count_steps(current, self.n)
            if steps <= k_remaining:
                k_remaining -= steps
                current += 1
            else:
                current *= 10
                k_remaining -= 1
        return current
    def public_Dictionary_order(self):
        return self.__private_Dictionary_order()

#--------------:
print(DOE(13, 6).public_Dictionary_order() == 2)
print(DOE(13, 7).public_Dictionary_order() == 3)
print(DOE(13, 8).public_Dictionary_order() == 4)
