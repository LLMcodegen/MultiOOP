
from typing import List
from collections import defaultdict, deque

class PFS:
    def __init__(self, n: int):
        self.n = n
class SN_PFS(PFS):
    def __init__(self, n: int, paths: List[List[int]]):
        super().__init__(n)
        self.paths = paths
    def Planted_flowers(self) -> List[int]:
        graph = defaultdict(list)
        for x, y in self.paths:
            graph[x].append(y)
            graph[y].append(x)
        result = [0] * self.n
        for i in range(1, self.n + 1):
            used_flowers = {result[neigh - 1] for neigh in graph[i]}
            for flower in range(1, 5):
                if flower not in used_flowers:
                    result[i - 1] = flower
                    break
        return result

#--------------:
print(SN_PFS(4, [[1,2], [2,3], [3,4]]).Planted_flowers() == [1,2,1,2])
print(SN_PFS(4, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]).Planted_flowers() == [1,2,3,4])
print(SN_PFS(3, []).Planted_flowers() == [1,1,1])