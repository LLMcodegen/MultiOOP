
from collections import defaultdict

class GPG:
    def __init__(self, n):
        self.n = n
class SN_GPG(GPG):
    def __init__(self, n, dislikes):
        super().__init__(n)
        self.dislikes = dislikes
    def grouping(self):
        graph = defaultdict(list)
        for a, b in self.dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color = [-1] * (self.n + 1)
        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    return False
            return True
        for i in range(1, self.n + 1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

#--------------:
print(SN_GPG(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]).grouping() == True)
print(SN_GPG(6, [[1, 2], [3, 4], [5, 6]]).grouping() == True)
print(SN_GPG(7, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]).grouping() == False)
