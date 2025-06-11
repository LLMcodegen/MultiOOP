
class EDC:
    def __init__(self, words: list):
        self.words = words
    def private_Excluding_Duplicates(self) -> list:
        word_set = set(self.words)
        result = []
        def can_form(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and (suffix in word_set or can_form(suffix)):
                    return True
            return False
        for word in self.words:
            word_set.remove(word)
            if can_form(word):
                result.append(word)
            word_set.add(word)
        return result
    def public_Excluding_Duplicates(self) -> list:
        return self.private_Excluding_Duplicates()

#--------------:
print(EDC(["rat", "cat", "catrat"]).public_Excluding_Duplicates() == ['catrat'])
print(EDC(["blue", "berry", "blueberry"]).public_Excluding_Duplicates() == ['blueberry'])
print(EDC(["a", "b", "ab", "abc"]).public_Excluding_Duplicates() == ['ab'])
