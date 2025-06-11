
class SIL:
    def __init__(self, intervals):
        self.intervals = intervals
    def __private_Set_intervals(self):
        if not self.intervals:
            return 0
        self.intervals.sort(key=lambda x: x[1])
        end = self.intervals[0][1]
        count = 0
        for i in range(1, len(self.intervals)):
            if self.intervals[i][0] < end:
                count += 1
            else:
                end = self.intervals[i][1]
        return count
    def public_Set_intervals(self):
        return self.__private_Set_intervals()

#--------------:
print(SIL([[1, 3], [2, 4], [5, 7], [6, 8]]).public_Set_intervals() == 2)
print(SIL([[1, 2], [2, 3], [2, 4], [3, 5]]).public_Set_intervals() == 1)
print(SIL([[1, 10], [2, 8], [3, 6], [7, 9]]).public_Set_intervals() == 2)
