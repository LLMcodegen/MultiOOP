class CTNOI:
    def __init__(self):
        pass
    def number_islands(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        island_count = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0' or visited[r][c]:
                return
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1
        return island_count
#--------------:
print(CTNOI().number_islands([["0","1","0"],["1","0","1"],["0","1","0"]]) == 4)
print(CTNOI().number_islands([["1","1","1"],["1","0","1"],["1","1","1"]]) == 1)
print(CTNOI().number_islands([["0","0","0"],["0","1","0"],["0","0","0"]]) == 1)
