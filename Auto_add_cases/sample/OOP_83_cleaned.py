
class MQT:
    def __init__(self, n):
        self.n = n
    def __private_Minimum_quantity(self):
        if self.n <= 0:
            return 0
        dp = [float('inf')] * (self.n + 1)
        dp[0] = 0
        squares = [i * i for i in range(1, int(self.n**0.5) + 1)]
        for i in range(1, self.n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[self.n]
    def public_Minimum_quantity(self):
        return self.__private_Minimum_quantity()

#--------------:
print(MQT(6).public_Minimum_quantity() == 3)
print(MQT(7).public_Minimum_quantity() == 4)
print(MQT(8).public_Minimum_quantity() == 2)
