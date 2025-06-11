
from collections import deque, defaultdict

class AAR:
    def __init__(self, n):
        self.n = n
class SN_AAR(AAR):
    def __init__(self, n, redEdges, blueEdges):
        super().__init__(n)
        self.red_edges = redEdges
        self.blue_edges = blueEdges
    def Alternating_appearance(self):
        graph = defaultdict(list)
        for u, v in self.red_edges:
            graph[u].append((v, 'red'))
        for u, v in self.blue_edges:
            graph[u].append((v, 'blue'))
        answer = [-1] * self.n
        queue = deque([(0, 'red', 0), (0, 'blue', 0)])
        visited = set()
        while queue:
            node, color, dist = queue.popleft()
            if answer[node] == -1:
                answer[node] = dist
            next_color = 'blue' if color == 'red' else 'red'
            for neighbor, edge_color in graph[node]:
                if edge_color == next_color and (neighbor, edge_color) not in visited:
                    visited.add((neighbor, edge_color))
                    queue.append((neighbor, edge_color, dist + 1))
        return answer

#--------------:
print(SN_AAR(3, [[0, 1], [0, 2]], [[1, 0]]).Alternating_appearance() == [0, 1, 1])
print(SN_AAR(4, [[0, 1], [2, 3]], [[1, 2], [3, 0]]).Alternating_appearance() == [0, 1, 2, 3])
print(SN_AAR(2, [], [[0, 1]]).Alternating_appearance() == [0, 1])
