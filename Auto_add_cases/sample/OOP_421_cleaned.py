from collections import defaultdict

class DMM:
    def __init__(self, s):
        self.s = s
class SN_DMM(DMM):
    def __init__(self, s, pairs):
        super().__init__(s)
        self.pairs = pairs
    def Dictionary_minimum(self):
        def dfs(node, graph, visited, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, graph, visited, component)
        graph = defaultdict(list)
        for a, b in self.pairs:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        components = []
        for node in graph:
            if node not in visited:
                component = []
                dfs(node, graph, visited, component)
                components.append(component)
        s_list = list(self.s)
        for component in components:
            chars = [s_list[i] for i in component]
            chars.sort()
            for i, idx in enumerate(sorted(component)):
                s_list[idx] = chars[i]
        return ''.join(s_list)

#--------------:
print(SN_DMM("dcab", [[0, 3], [1, 2]]).Dictionary_minimum() == "bacd")
print(SN_DMM("dcab", [[0, 3], [1, 2]]).Dictionary_minimum() == "bacd")
print(SN_DMM("cba", []).Dictionary_minimum() == "cba")
