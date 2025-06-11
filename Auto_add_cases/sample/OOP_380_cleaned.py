
class SGD:
    def __init__(self, blocked):
        self.blocked = blocked
class SN_SGD(SGD):
    def __init__(self, blocked, source, target):
        super().__init__(blocked)
        self.source = source
        self.target = target
    def Source_grid(self):
        BLOCKED = set(map(tuple, self.blocked))
        LIMIT = 20000
        def is_escape_possible(start, end):
            visited = set()
            queue = [tuple(start)]
            visited.add(tuple(start))
            for _ in range(LIMIT):
                if not queue:
                    break
                x, y = queue.pop(0)
                if (x, y) == tuple(end):
                    return True
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in BLOCKED and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            else:
                return True
            return False
        return is_escape_possible(self.source, self.target) and is_escape_possible(self.target, self.source)

#--------------:
print(SN_SGD([[2, 2], [3, 3], [4, 4]], [0, 0], [5, 5]).Source_grid() == True)
print(SN_SGD([[2, 2], [3, 3], [4, 4], [5, 5]], [0, 0], [6, 6]).Source_grid() == True)
print(SN_SGD([[3, 3], [4, 4], [5, 5], [6, 6]], [0, 0], [7, 7]).Source_grid() == True)
