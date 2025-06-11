
class FSG:
    def __init__(self, n):
        self.n = n
class SN_FSG(FSG):
    def Forming_String(self):
        if self.n == 0:
            return 0
        counts = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        transitions = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        for _ in range(2, self.n + 1):
            new_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            for prev_vowel, next_vowels in transitions.items():
                for next_vowel in next_vowels:
                    new_counts[next_vowel] += counts[prev_vowel]
            counts = new_counts
        total = sum(counts.values())
        return total

#--------------:
print(SN_FSG(6).Forming_String() == 129)
print(SN_FSG(7).Forming_String() == 249)
print(SN_FSG(8).Forming_String() == 474)
