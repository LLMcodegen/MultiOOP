
class ED:
    def __init__(self, words):
        self.words = words
    def __private_English_Dictionary(self):
        self.words.sort()
        word_dict = {}
        longest_word = ""
        for word in self.words:
            if len(word) == 1 or word[:-1] in word_dict:
                word_dict[word] = True
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word
    def public_English_Dictionary(self):
        return self.__private_English_Dictionary()

#--------------:
print(ED(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg"]).public_English_Dictionary() == "abcdefg")
print(ED(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh"]).public_English_Dictionary() == "abcdefgh")
print(ED(["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi"]).public_English_Dictionary() == "abcdefghi")
