
class ILT:
    def __init__(self, firstList):
        self.firstList = firstList
class SN_ILT(ILT):
    def __init__(self, firstList, secondList):
        super().__init__(firstList)
        self.secondList = secondList
    def Interval_List(self):
        intersection = []
        i = j = 0
        while i < len(self.firstList) and j < len(self.secondList):
            start_i, end_i = self.firstList[i]
            start_j, end_j = self.secondList[j]
            if end_i >= start_j and end_j >= start_i:
                intersection.append([max(start_i, start_j), min(end_i, end_j)])
            if end_i < end_j:
                i += 1
            else:
                j += 1
        return intersection

#--------------:
print(SN_ILT([[1, 3], [5, 7]], [[4, 8], [9, 11]]).Interval_List() == [[5, 7]])
print(SN_ILT([[1, 3], [5, 7]], [[3, 7], [8, 10]]).Interval_List() == [[3, 3], [5, 7]])
print(SN_ILT([[1, 3], [5, 7]], [[2, 8], [9, 11]]).Interval_List() == [[2, 3], [5, 7]])
