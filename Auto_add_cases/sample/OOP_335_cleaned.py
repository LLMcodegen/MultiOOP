
from itertools import permutations

class ETM:
    def __init__(self, arr):
        self.arr = arr
class SN_ETM(ETM):
    def effective_time(self):
        max_time = ""
        for perm in permutations(self.arr):
            hour = perm[0] * 10 + perm[1]
            minute = perm[2] * 10 + perm[3]
            if hour < 24 and minute < 60:
                time_str = f"{hour:02}:{minute:02}"
                if time_str > max_time:
                    max_time = time_str
        return max_time

#--------------:
print(SN_ETM([1, 2, 3, 4]).effective_time() == "23:41")
print(SN_ETM([2, 2, 5, 9]).effective_time() == "22:59")
print(SN_ETM([9, 9, 9, 9]).effective_time() == "")
