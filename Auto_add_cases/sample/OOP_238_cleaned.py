
class SP:
    def __init__(self, s):
        self.s = s
    def __private_String_partitioning(self):
        last_occurrence = {char: idx for idx, char in enumerate(self.s)}
        partitions = []
        start = 0
        max_end = 0
        for i, char in enumerate(self.s):
            max_end = max(max_end, last_occurrence[char])
            if i == max_end:
                partitions.append(i - start + 1)
                start = i + 1
        return partitions
    def public_String_partitioning(self):
        return self.__private_String_partitioning()

#--------------:
print(SP("abacdc").public_String_partitioning() == [3, 3])
print(SP("abacdce").public_String_partitioning() == [3, 3, 1])
print(SP("abacdcef").public_String_partitioning() == [3, 3, 1, 1])
