
class MVE:
    def __init__(self, s1):
        self.s1 = s1
class SN_MVE(MVE):
    def __init__(self, s1, s2):
        super().__init__(s1)
        self.s2 = s2
    def Minimum_value(self):
        if sorted(self.s1) != sorted(self.s2):
            raise ValueError("s1 and s2 are not anagrams")
        swaps = 0
        s1_list = list(self.s1)
        s2_list = list(self.s2)
        for i in range(len(s1_list)):
            if s1_list[i] != s2_list[i]:
                swap_index = s1_list.index(s2_list[i], i)
                s1_list[i], s1_list[swap_index] = s1_list[swap_index], s1_list[i]
                swaps += 1
        return swaps

#--------------:
print(SN_MVE("dcba", "abcd").Minimum_value() == 2)
print(SN_MVE("knead", "nadke").Minimum_value() == 3)
print(SN_MVE("hello", "olleh").Minimum_value() == 3)
