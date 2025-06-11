
class ML:
    def __init__(self, strs):
        self.strs = strs
    def __private_Maximum_length(self):
        def is_subsequence(s1, s2):
            it = iter(s2)
            return all(c in it for c in s1)
        strs_sorted = sorted(self.strs, key=len, reverse=True)
        for i, s1 in enumerate(strs_sorted):
            if all(not is_subsequence(s1, s2) for j, s2 in enumerate(strs_sorted) if i != j):
                return len(s1)
        return -1
    def public_Maximum_length(self):
        return self.__private_Maximum_length()

#--------------:
print(ML(["a", "aa", "aaa"]).public_Maximum_length() == 3)
print(ML(["test", "t", "te"]).public_Maximum_length() == 4)
print(ML(["unique", "sequence", "test"]).public_Maximum_length() == 8)
