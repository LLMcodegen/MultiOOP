
class PM:
    def __init__(self, order, s):
        self.order = order
        self.s = s
    def __private_Permutation_matching(self):
        frequency_map = {}
        for char in self.s:
            if char in frequency_map:
                frequency_map[char] += 1
            else:
                frequency_map[char] = 1
        result = []
        for char in self.order:
            if char in frequency_map:
                result.append(char * frequency_map[char])
                del frequency_map[char]
        for char, count in frequency_map.items():
            result.append(char * count)
        return ''.join(result)
    def public_Permutation_matching(self):
        return self.__private_Permutation_matching()

#--------------:
print(PM("xyz", "abcdef").public_Permutation_matching() == "abcdef")
print(PM("xyz", "xyzxyz").public_Permutation_matching() == "xxyyzz")
print(PM("xyz", "abcxyz").public_Permutation_matching() == "xyzabc")
