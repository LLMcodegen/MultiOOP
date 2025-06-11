
class SDC:
    def __init__(self, n):
        self.n = n
class SN_SDC(SDC):
    def __init__(self, n, edges):
        super().__init__(n)
        self.edges = edges
        self.graph = self.build_graph()
    def build_graph(self):
        graph = {i: [] for i in range(self.n)}
        for a, b in self.edges:
            graph[a].append(b)
            graph[b].append(a)
        return graph
    def dfs(self, node, parent, distances):
        for neighbor in self.graph[node]:
            if neighbor != parent:
                distances[neighbor] = distances[node] + 1
                self.dfs(neighbor, node, distances)
    def Sum_distances(self):
        answer = [0] * self.n
        for i in range(self.n):
            distances = [0] * self.n
            distances[i] = 0
            self.dfs(i, -1, distances)
            answer[i] = sum(distances)
        return answer

#--------------:
print(SN_SDC(4, [[0, 1], [1, 2], [2, 3]]).Sum_distances() == [6, 4, 4, 6])
print(SN_SDC(4, [[0, 1], [0, 2], [0, 3]]).Sum_distances() == [3, 5, 5, 5])
print(SN_SDC(5, [[0, 1], [1, 2], [2, 3], [3, 4]]).Sum_distances() == [10, 7, 6, 7, 10])
