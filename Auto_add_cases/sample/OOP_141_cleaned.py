
class SIN:
    def __init__(self, s, p):
        self.s = s
        self.p = p
    def __private_start_index(self):
        from collections import Counter
        len_s, len_p = len(self.s), len(self.p)
        if len_p > len_s:
            return []
        p_counter = Counter(self.p)
        s_counter = Counter(self.s[:len_p])
        result = []
        if p_counter == s_counter:
            result.append(0)
        for i in range(1, len_s - len_p + 1):
            s_counter[self.s[i - 1]] -= 1
            if s_counter[self.s[i - 1]] == 0:
                del s_counter[self.s[i - 1]]
            s_counter[self.s[i + len_p - 1]] += 1
            if p_counter == s_counter:
                result.append(i)
        return result
    def public_start_index(self):
        return self.__private_start_index()

#--------------:
print(SIN("", "abc").public_start_index() == [])
print(SIN("short", "longerpattern").public_start_index() == [])
print(SIN("abcdefgh", "fgh").public_start_index() == [5])
