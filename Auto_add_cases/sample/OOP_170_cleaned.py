
class NCC:
    def __init__(self, amount, coins):
        self.amount = amount
        self.coins = coins
    def __coin_combinations(self):
        dp = [0] * (self.amount + 1)
        dp[0] = 1
        for coin in self.coins:
            for i in range(coin, self.amount + 1):
                dp[i] += dp[i - coin]
        return dp[self.amount]
    def public_combinations(self):
        return self.__coin_combinations()

#--------------:
print(NCC(5, [1, 2]).public_combinations() == 3)
print(NCC(5, [1, 3]).public_combinations() == 2)
print(NCC(6, [1, 2, 3]).public_combinations() == 7)
