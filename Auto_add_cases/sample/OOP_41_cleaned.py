class CMP:
    def Calculate_Maximum_Profit(self, prices):
        if not prices:
            return 0
        first_buy, first_sell = -float('inf'), 0
        second_buy, second_sell = -float('inf'), 0
        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
        return second_sell
#--------------:
print(CMP().Calculate_Maximum_Profit([1, 2]) == 1)
print(CMP().Calculate_Maximum_Profit([2, 1]) == 0)
print(CMP().Calculate_Maximum_Profit([10, 22, 5, 75, 65, 80]) == 87)