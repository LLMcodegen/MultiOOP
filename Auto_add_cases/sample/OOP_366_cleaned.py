
class MCG:
    def __init__(self, weights):
        self.weights = weights
class SN_MCG(MCG):
    def __init__(self, weights, days):
        super().__init__(weights)
        self.days = days
    def Minimum_carrying(self):
        def can_ship(capacity):
            days_needed = 1
            current_load = 0
            for weight in self.weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = weight
                else:
                    current_load += weight
            return days_needed <= self.days
        left, right = max(self.weights), sum(self.weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left

#--------------:
print(SN_MCG([1, 2, 3, 4, 5], 4).Minimum_carrying() == 5)
print(SN_MCG([1, 2, 3, 4, 5], 5).Minimum_carrying() == 5)
print(SN_MCG([10, 20, 30, 40, 50], 2).Minimum_carrying() == 90)
