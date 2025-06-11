
from collections import deque

class TTH:
    def __init__(self, graph):
        self.graph = graph
class SN_TTH(TTH):
    def The_length(self):
        n = len(self.graph)
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        visited = {(i, 1 << i) for i in range(n)}
        target_mask = (1 << n) - 1
        while queue:
            node, visited_mask, distance = queue.popleft()
            if visited_mask == target_mask:
                return distance
            for neighbor in self.graph[node]:
                new_visited_mask = visited_mask | (1 << neighbor)
                if (neighbor, new_visited_mask) not in visited:
                    visited.add((neighbor, new_visited_mask))
                    queue.append((neighbor, new_visited_mask, distance + 1))
        return -1

#--------------:
print(SN_TTH([[1,2,3],[0],[0],[0]]).The_length() == 4)
print(SN_TTH([[1],[0,2],[1,3],[2]]).The_length() == 3)