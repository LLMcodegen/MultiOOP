
class FCA:
    def __init__(self, words):
        self.words = words
class SN_FCA(FCA):
    def Form_chain(self):
        words = sorted(self.words, key=len)
        longest_chain = {}
        max_length = 1
        for word in words:
            longest_chain[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in longest_chain:
                    longest_chain[word] = max(longest_chain[word], longest_chain[predecessor] + 1)
            max_length = max(max_length, longest_chain[word])
        return max_length

#--------------:
print(SN_FCA(["a", "aa", "aaa", "aaaa"]).Form_chain() == 4)
print(SN_FCA(["a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", "abcd", "abcde"]).Form_chain() == 5)
print(SN_FCA(["a", "b", "c", "d", "ab", "bc", "cd", "abc", "bcd", "abcd", "abcde", "abcdef"]).Form_chain() == 6)
