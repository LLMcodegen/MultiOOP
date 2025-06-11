from collections import defaultdict
import heapq
        
class MSR:
    def __init__(self, values):
        self.values = values
class SN_MSR(MSR):
    def __init__(self, values, labels, numWanted, useLimit):
        super().__init__(values)
        self.labels = labels
        self.numWanted = numWanted
        self.useLimit = useLimit
    def Maximum_score(self):
        items = list(zip(self.values, self.labels))
        items.sort(key=lambda x: -x[0])
        label_count = defaultdict(int)
        selected_values = []
        for value, label in items:
            if len(selected_values) < self.numWanted and label_count[label] < self.useLimit:
                heapq.heappush(selected_values, value)
                label_count[label] += 1
                if len(selected_values) > self.numWanted:
                    heapq.heappop(selected_values)
        return sum(selected_values)

#--------------:
print(SN_MSR([1, 4, 3, 2, 6, 1], [1, 1, 2, 2, 3, 3], 4, 1).Maximum_score() == 13)
print(SN_MSR([5, 1, 3, 2, 6, 1], [1, 1, 2, 2, 3, 3], 5, 1).Maximum_score() == 14)
print(SN_MSR([5, 4, 1, 2, 6, 1], [1, 1, 2, 2, 3, 3], 6, 1).Maximum_score() == 13)
