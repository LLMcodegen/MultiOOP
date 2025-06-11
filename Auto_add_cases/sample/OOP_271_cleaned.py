
class UCR:
    def __init__(self, s):
        self.s = s
class SN_UCR(UCR):
    def __init__(self, s):
        super().__init__(s)
    def Unique_character(self):
        s = self.s
        index = {}
        n = len(s)
        contribution = 0
        prev_index = [-1] * n
        next_index = [n] * n
        last_occurrence = {}
        for i in range(n):
            char = s[i]
            if char in last_occurrence:
                prev_index[i] = last_occurrence[char]
            last_occurrence[char] = i
        last_occurrence.clear()
        for i in range(n - 1, -1, -1):
            char = s[i]
            if char in last_occurrence:
                next_index[i] = last_occurrence[char]
            last_occurrence[char] = i
        for i in range(n):
            left = i - prev_index[i]
            right = next_index[i] - i
            contribution += left * right
        return contribution

#--------------:
print(SN_UCR("ABCDE").Unique_character() == 35)
print(SN_UCR("AAB").Unique_character() == 6)
print(SN_UCR("ABA").Unique_character() == 8)
