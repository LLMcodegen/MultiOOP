
class EIT:
    def __init__(self, instructions):
        self.instructions = instructions
class SN_EIT(EIT):
    def __init__(self, instructions):
        super().__init__(instructions)
    def Execute_instructions(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direction = 0
        visited = {(x, y, direction)}
        for _ in range(4):
            for instruction in self.instructions:
                if instruction == 'G':
                    x += directions[direction][0]
                    y += directions[direction][1]
                elif instruction == 'L':
                    direction = (direction - 1) % 4
                elif instruction == 'R':
                    direction = (direction + 1) % 4
                if (x, y, direction) in visited:
                    return True
                visited.add((x, y, direction))
        return False

#--------------:
print(SN_EIT("GRGRGRG").Execute_instructions() == True)
print(SN_EIT("GRGRGRGR").Execute_instructions() == True)
print(SN_EIT("GRGRGRGRG").Execute_instructions() == True)
