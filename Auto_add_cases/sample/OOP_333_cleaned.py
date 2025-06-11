
class RSN:
    def __init__(self, stones):
        self.stones = stones
class SN_RSN(RSN):
    def Removed_stones(self):
        def dfs(x, y, visited, rows, cols):
            visited.add((x, y))
            for ny in rows[x]:
                if (x, ny) not in visited:
                    dfs(x, ny, visited, rows, cols)
            for nx in cols[y]:
                if (nx, y) not in visited:
                    dfs(nx, y, visited, rows, cols)
        rows = {}
        cols = {}
        for x, y in self.stones:
            if x not in rows:
                rows[x] = []
            if y not in cols:
                cols[y] = []
            rows[x].append(y)
            cols[y].append(x)
        visited = set()
        components = 0
        for x, y in self.stones:
            if (x, y) not in visited:
                dfs(x, y, visited, rows, cols)
                components += 1
        return len(self.stones) - components

#--------------:
print(SN_RSN([[0,0],[1,1],[2,2],[3,3],[4,4]]).Removed_stones() == 0)
print(SN_RSN([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]).Removed_stones() == 0)
print(SN_RSN([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]).Removed_stones() == 0)
