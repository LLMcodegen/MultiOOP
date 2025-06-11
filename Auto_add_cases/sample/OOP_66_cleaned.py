class DIIII:
    def isomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_to_t_mapping = {}
        t_mapped = set()
        for char_s, char_t in zip(s, t):
            if char_s in s_to_t_mapping:
                if s_to_t_mapping[char_s] != char_t:
                    return False
            else:
                if char_t in t_mapped:
                    return False
                s_to_t_mapping[char_s] = char_t
                t_mapped.add(char_t)
        return True
#--------------:
print(DIIII().isomorphic("abab", "cdcd") == True)
print(DIIII().isomorphic("abcd", "efgh") == True)
print(DIIII().isomorphic("abcd", "eeff") == False)
