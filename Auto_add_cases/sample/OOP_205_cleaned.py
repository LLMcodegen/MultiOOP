
class FPV:
    def __init__(self, arr, k, x):
        self.arr = arr
        self.k = k
        self.x = x
    def __private_Find_Proximity_Values(self):
        sorted_arr = sorted(self.arr, key=lambda num: (abs(num - self.x), num))
        return sorted(sorted_arr[:self.k])
    def public_Find_Proximity_Values(self):
        return self.__private_Find_Proximity_Values()

#--------------:
print(FPV([-10, -5, 0, 5, 10], 2, 3).public_Find_Proximity_Values() == [0, 5])
print(FPV([2, 4, 6, 8, 10], 5, 7).public_Find_Proximity_Values() == [2, 4, 6, 8, 10])
print(FPV([1, 4, 6, 8, 10], 4, 7).public_Find_Proximity_Values() == [4, 6, 8, 10])
