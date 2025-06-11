
import heapq

class MS:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
    def __private_Minimum_score(self):
        heap = []
        for j in range(1, len(self.arr)):
            heapq.heappush(heap, (self.arr[0] / self.arr[j], 0, j))
        for _ in range(self.k - 1):
            _, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, (self.arr[i + 1] / self.arr[j], i + 1, j))
        _, i, j = heapq.heappop(heap)
        return [self.arr[i], self.arr[j]]
    def public_Minimum_score(self):
        return self.__private_Minimum_score()


print(MS([1, 2, 3, 5], 3).public_Minimum_score() == [2, 5])
print(MS([1, 2, 3, 5], 1).public_Minimum_score() == [1, 5])
print(MS([1, 2, 3, 5, 7, 11], 4).public_Minimum_score() == [1, 5])
