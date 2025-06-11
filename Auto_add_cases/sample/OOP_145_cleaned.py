
class ISAR:
    def __init__(self, chars):
        self.chars = chars
    def __private_Input_sarray(self):
        s = []
        i = 0
        while i < len(self.chars):
            char = self.chars[i]
            count = 1
            while i + 1 < len(self.chars) and self.chars[i + 1] == char:
                i += 1
                count += 1
            s.append(char)
            if count > 1:
                s.extend(list(str(count)))
            i += 1
        return s
    def public_Input_sarray(self):
        return self.__private_Input_sarray()

#--------------:
print(ISAR(['a', 'b', 'b', 'b', 'a', 'a', 'b', 'b']).public_Input_sarray() == ['a', 'b', '3', 'a', '2', 'b', '2'])
print(ISAR(['x', 'y', 'y', 'y', 'x', 'x']).public_Input_sarray() == ['x', 'y', '3', 'x', '2'])
print(ISAR(['1', '1', '2', '2', '2', '1', '1']).public_Input_sarray() == ['1', '2', '2', '3', '1', '2'])
