
class CGS:
    def __init__(self, graph):
        self.graph = graph
class SN_CGS(CGS):
    def Cat_games(self):
        from functools import lru_cache
        DRAW = 0
        MOUSE_WIN = 1
        CAT_WIN = 2
        n = len(self.graph)
        @lru_cache(None)
        def search(mouse, cat, turn):
            if turn > 2 * n * n:
                return DRAW
            if mouse == 0:
                return MOUSE_WIN
            if cat == mouse:
                return CAT_WIN
            if turn % 2 == 0:
                result = CAT_WIN
                for next_mouse in self.graph[mouse]:
                    res = search(next_mouse, cat, turn + 1)
                    if res == MOUSE_WIN:
                        return MOUSE_WIN
                    elif res == DRAW:
                        result = DRAW
                return result
            else:
                result = MOUSE_WIN
                for next_cat in self.graph[cat]:
                    if next_cat == 0:
                        continue
                    res = search(mouse, next_cat, turn + 1)
                    if res == CAT_WIN:
                        return CAT_WIN
                    elif res == DRAW:
                        result = DRAW
                return result
        return search(1, 2, 0)

#--------------:
print(SN_CGS([[1,4],[0,2],[1,3],[2,4],[0,3,5],[4,6],[5]]).Cat_games() == 1)
print(SN_CGS([[1,4],[0,2],[1,3],[2,4],[0,3,5],[4,6],[5,7],[6]]).Cat_games() == 1)
print(SN_CGS([[1,4],[0,2],[1,3],[2,4],[0,3,5],[4,6],[5,7],[6,8],[7]]).Cat_games() == 1)
