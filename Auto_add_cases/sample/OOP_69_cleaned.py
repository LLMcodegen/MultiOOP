import heapq
class RTLE:
    def largest_element(self, nums, k):
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
#--------------:
#--------------:
print(RTLE().largest_element([10, 9, 8, 7, 6, 5], 6) == 5)
print(RTLE().largest_element([1, 2, 3, 4, 5, 6], 4) == 3)
print(RTLE().largest_element([1, 1, 2, 2, 3, 3], 2) == 3)
