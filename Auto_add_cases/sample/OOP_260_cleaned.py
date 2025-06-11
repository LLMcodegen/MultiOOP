
class SND:
    def __init__(self, graph):
        self.graph = graph
class SN_SND(SND):
    def __init__(self, graph):
        super().__init__(graph)
    def secure_node(self):
        n = len(self.graph)
        safe = [False] * n
        graph = self.graph
        def dfs(node, visited):
            if safe[node]:
                return True
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor, visited):
                    return False
            visited.remove(node)
            safe[node] = True
            return True
        for i in range(n):
            dfs(i, set())
        return [i for i in range(n) if safe[i]]

#--------------:
print(SN_SND([[1], [2], [3], []]).secure_node() == [0, 1, 2, 3])
print(SN_SND([[1, 2], [2, 3], [5], [0], [5], [], []]).secure_node() == [2, 4, 5, 6])
print(SN_SND([[1], [2], [0]]).secure_node() == [])