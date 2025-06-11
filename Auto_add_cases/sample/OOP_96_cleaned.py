
class TAU:
    def __init__(self, coins, amount):
        self.coins = coins
        self.amount = amount
    def __private_Total_amount(self):
        dp = [float('inf')] * (self.amount + 1)
        dp[0] = 0
        for coin in self.coins:
            for i in range(coin, self.amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[self.amount] if dp[self.amount] != float('inf') else -1
    def public_Total_amount(self):
        return self.__private_Total_amount()

#--------------:
print(TAU([1, 4, 5], 8).public_Total_amount() == 2)
print(TAU([2, 5, 10], 27).public_Total_amount() == 4)
print(TAU([5, 7, 1], 18).public_Total_amount() == 4)
