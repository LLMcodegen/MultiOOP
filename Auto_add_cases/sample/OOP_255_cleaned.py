
class NW:
    def __init__(self, s, words):
        self.s = s
        self.words = words
    def __private_Number_words(self):
        def is_subsequence(word, s):
            it = iter(s)
            return all(char in it for char in word)
        count = 0
        for word in self.words:
            if is_subsequence(word, self.s):
                count += 1
        return count
    def public_Number_words(self):
        return self.__private_Number_words()

#--------------:
print(NW("abcde", ["abcde"]).public_Number_words() == 1)
print(NW("abcde", ["a", "bb", "cc", "dd", "ee"]).public_Number_words() == 1)
print(NW("abcde", ["aa", "bb", "cc", "dd", "ee"]).public_Number_words() == 0)
