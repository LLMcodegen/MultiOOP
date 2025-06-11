
import heapq
from collections import defaultdict

class NN:
    def __init__(self, times, n, k):
        self.times = times
        self.n = n
        self.k = k
    def __private_network_node(self):
        graph = defaultdict(list)
        for u, v, w in self.times:
            graph[u].append((v, w))
        min_heap = [(0, self.k)]
        distances = {i: float('inf') for i in range(1, self.n + 1)}
        distances[self.k] = 0
        while min_heap:
            current_dist, node = heapq.heappop(min_heap)
            if current_dist > distances[node]:
                continue
            for neighbor, time in graph[node]:
                new_dist = current_dist + time
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))
        max_dist = max(distances.values())
        return max_dist if max_dist != float('inf') else -1
    def public_network_node(self):
        return self.__private_network_node()

#--------------:
print(NN([(1, 2, 1), (1, 3, 4), (2, 3, 2)], 3, 3).public_network_node() == -1)
print(NN([(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)], 5, 1).public_network_node() == 4)
print(NN([(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)], 5, 2).public_network_node() == -1)
