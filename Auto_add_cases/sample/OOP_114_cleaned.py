
import heapq

class DAG:
    def __init__(self, nums1, nums2, k):
        self.nums1 = nums1
        self.nums2 = nums2
        self.k = k
    def __private_decreasing_arrangement(self):
        if not self.nums1 or not self.nums2:
            return []
        min_heap = []
        result = []
        n1, n2 = len(self.nums1), len(self.nums2)
        for i in range(min(self.k, n1)):
            heapq.heappush(min_heap, (self.nums1[i] + self.nums2[0], i, 0))
        while self.k > 0 and min_heap:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append((self.nums1[i], self.nums2[j]))
            self.k -= 1
            if j + 1 < n2:
                heapq.heappush(min_heap, (self.nums1[i] + self.nums2[j + 1], i, j + 1))
        return result
    def public_decreasing_arrangement(self):
        return self.__private_decreasing_arrangement()

#--------------:
print(DAG([2, 4], [5, 6], 1).public_decreasing_arrangement() == [(2, 5)])
print(DAG([10, 20], [15, 25], 3).public_decreasing_arrangement() == [(10, 15), (10, 25), (20, 15)])
print(DAG([7, 8, 9], [1, 2], 5).public_decreasing_arrangement() == [(7, 1), (7, 2), (8, 1), (8, 2), (9, 1)])
