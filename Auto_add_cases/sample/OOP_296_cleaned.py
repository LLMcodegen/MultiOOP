
import math

class MSD:
    def __init__(self, piles):
        self.piles = piles
class SN_MSD(MSD):
    def __init__(self, piles, h):
        super().__init__(piles)
        self.h = h
    def Minimum_Speed(self):
        def can_eat_all(speed):
            time_taken = 0
            for pile in self.piles:
                time_taken += math.ceil(pile / speed)
            return time_taken <= self.h
        left, right = 1, max(self.piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1
        return left

#--------------:
print(SN_MSD([30, 11, 23, 4, 20], 9).Minimum_Speed() == 12)
print(SN_MSD([30, 11, 23, 4, 20], 10).Minimum_Speed() == 11)
print(SN_MSD([30, 11, 23, 4, 20], 11).Minimum_Speed() == 10)
