
class PO:
    def __init__(self, graph):
        self.graph = graph
class SN_PO(PO):
    def __init__(self, graph):
        super().__init__(graph)
    def Path_output(self):
        def dfs(node, path):
            if node == len(self.graph) - 1:
                paths.append(path)
                return
            for neighbor in self.graph[node]:
                dfs(neighbor, path + [neighbor])
        paths = []
        dfs(0, [0])
        return paths

#--------------:
print(SN_PO([[1], [2], [3], []]).Path_output() == [[0, 1, 2, 3]])
print(SN_PO([[1, 2], [3], [3], []]).Path_output() == [[0, 1, 3], [0, 2, 3]])
print(SN_PO([[1, 2], [3], [3], [4], []]).Path_output() == [[0, 1, 3, 4], [0, 2, 3, 4]])