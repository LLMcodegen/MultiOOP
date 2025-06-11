
import heapq

class GS:
    def __init__(self, grid):
        self.grid = grid
    def __private_Grid_swimming(self) -> int:
        n = len(self.grid)
        def can_swim(t):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited = set()
            heap = [(self.grid[0][0], 0, 0)]
            while heap:
                height, x, y = heapq.heappop(heap)
                if x == n - 1 and y == n - 1:
                    return True
                visited.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        if self.grid[nx][ny] <= t:
                            heapq.heappush(heap, (self.grid[nx][ny], nx, ny))
            return False
        left, right = self.grid[0][0], max(max(row) for row in self.grid)
        while left < right:
            mid = (left + right) // 2
            if can_swim(mid):
                right = mid
            else:
                left = mid + 1  
        return left
    def public_Grid_swimming(self) -> int:
        return self.__private_Grid_swimming()

#--------------:
print(GS([[0, 2], [2, 3]]).public_Grid_swimming() == 3)
print(GS([[0, 3, 2], [3, 4, 5], [6, 7, 8]]).public_Grid_swimming() == 8)
print(GS([[0, 4, 1], [1, 3, 2], [2, 1, 0]]).public_Grid_swimming() == 2)
