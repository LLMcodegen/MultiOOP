
class JA:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def __private_Judgment_arrangement(self):
        from collections import Counter
        len_s1, len_s2 = len(self.s1), len(self.s2)
        if len_s1 > len_s2:
            return False
        s1_count = Counter(self.s1)
        window_count = Counter(self.s2[:len_s1])
        if s1_count == window_count:
            return True
        for i in range(len_s1, len_s2):
            window_count[self.s2[i]] += 1
            window_count[self.s2[i - len_s1]] -= 1
            if window_count[self.s2[i - len_s1]] == 0:
                del window_count[self.s2[i - len_s1]]
            if s1_count == window_count:
                return True
        return False
    def public_Judgment_arrangement(self):
        return self.__private_Judgment_arrangement()

#--------------:
print(JA("abc", "ababcb").public_Judgment_arrangement() == True)
print(JA("abcd", "dcbaef").public_Judgment_arrangement() == True)
print(JA("xyz", "abcdef").public_Judgment_arrangement() == False)
