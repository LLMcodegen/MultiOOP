
class ARS:
    def __init__(self, rooms):
        self.rooms = rooms
class SN_ARS(ARS):
    def All_rooms(self):
        n = len(self.rooms)
        visited = [False] * n
        stack = [0]
        while stack:
            room = stack.pop()
            if not visited[room]:
                visited[room] = True
                for key in self.rooms[room]:
                    if not visited[key]:
                        stack.append(key)
        return all(visited)

#--------------:
print(SN_ARS([[1], [2], [3], [4], [0]]).All_rooms() == True)
print(SN_ARS([[1], [2], [3], [4], [5], []]).All_rooms() == True)
print(SN_ARS([[1], [2], [3], [4], [5], [0]]).All_rooms() == True)
