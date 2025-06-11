
class FAR:
    def __init__(self, arr):
        self.arr = arr
class SN_FAR(FAR):
    def __init__(self, arr):
        super().__init__(arr)
    def Final_Answer(self):
        unique_results = set()
        for i in range(len(self.arr)):
            current_or = 0
            for j in range(i, len(self.arr)):
                current_or |= self.arr[j]
                unique_results.add(current_or)
        return len(unique_results)

#--------------:
print(SN_FAR([3, 3, 3]).Final_Answer() == 1)
print(SN_FAR([4, 4, 4]).Final_Answer() == 1)
print(SN_FAR([5, 5, 5]).Final_Answer() == 1)
