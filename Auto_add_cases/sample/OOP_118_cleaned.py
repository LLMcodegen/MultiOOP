
class SAS:
    def __init__(self, matrix, k):
        self.matrix = matrix
        self.k = k
    def _private_Sort_ascending(self):
        flat_list = [item for sublist in self.matrix for item in sublist]
        flat_list.sort()
        return flat_list[self.k - 1]
    def public_Sort_ascending(self):
        return self._private_Sort_ascending()

#--------------:
print(SAS([[1, 3, 5], [2, 4, 6]], 4).public_Sort_ascending() == 4)
print(SAS([[12, 14], [10, 11]], 1).public_Sort_ascending() == 10)
print(SAS([[30, 40], [20, 35]], 2).public_Sort_ascending() == 30)
