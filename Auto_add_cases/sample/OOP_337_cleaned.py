
from collections import Counter

class RSF:
    def __init__(self, arr):
        self.arr = arr
class SN_RSF(RSF):
    def Reorganization_satisfaction(self):
        arr = self.arr
        if len(arr) % 2 != 0:
            return False
        count = Counter(arr)
        keys = sorted(count.keys(), key=abs)
        for x in keys:
            if count[x] == 0:
                continue
            if count[2 * x] < count[x]:
                return False
            count[2 * x] -= count[x]
        return True

#--------------:
print(SN_RSF([1, 2, 4, 8, 16]).Reorganization_satisfaction() == False)
print(SN_RSF([1, 2, 4, 8, 16, 32]).Reorganization_satisfaction() == True)
print(SN_RSF([1, 2, 4, 8, 16, 32, 64]).Reorganization_satisfaction() == False)
