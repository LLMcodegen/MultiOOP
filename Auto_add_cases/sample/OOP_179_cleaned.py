
from typing import List

class MTD:
    def __init__(self, timePoints: List[str]):
        self.timePoints = timePoints
    def __Minimum_difference(self) -> int:
        minutes_list = []
        for time in self.timePoints:
            hours, minutes = map(int, time.split(":"))
            total_minutes = hours * 60 + minutes
            minutes_list.append(total_minutes)
        minutes_list.sort()
        min_diff = (24 * 60 - minutes_list[-1] + minutes_list[0])
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
        return min_diff
    def public_Minimum_difference(self) -> int:
        return self.__Minimum_difference()

#--------------:
print(MTD(["22:10", "22:15", "22:30"]).public_Minimum_difference() == 5)
print(MTD(["00:00", "01:00", "02:00"]).public_Minimum_difference() == 60)
print(MTD(["23:30", "00:30", "12:30"]).public_Minimum_difference() == 60)
