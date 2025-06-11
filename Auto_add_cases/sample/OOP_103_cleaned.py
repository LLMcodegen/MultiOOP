
class USI:
    def __init__(self, words):
        self.words = words
    def __private_Unique_String(self):
        def is_palindrome(s):
            return s == s[::-1]
        palindrome_pairs = []
        unique_words = set(self.words)
        word_index_map = {word: i for i, word in enumerate(self.words)}
        for i, word in enumerate(self.words):
            reversed_word = word[::-1]
            if reversed_word in unique_words and word_index_map[reversed_word] != i:
                palindrome_pairs.append([i, word_index_map[reversed_word]])
            if word and is_palindrome(word) and "" in unique_words:
                palindrome_pairs.append([i, word_index_map[""]])
                palindrome_pairs.append([word_index_map[""], i])
            for j in range(1, len(word)):
                prefix, suffix = word[:j], word[j:]
                reversed_prefix, reversed_suffix = prefix[::-1], suffix[::-1]
                if is_palindrome(prefix) and reversed_suffix in unique_words:
                    palindrome_pairs.append([word_index_map[reversed_suffix], i])
                if is_palindrome(suffix) and reversed_prefix in unique_words:
                    palindrome_pairs.append([i, word_index_map[reversed_prefix]])
        return palindrome_pairs
    def public_Unique_String(self):
        return self.__private_Unique_String()

#--------------:
print(USI(["madam", "madam", "d"]).public_Unique_String() == [[0, 1]])
print(USI(["bob", "bobcat", "cat"]).public_Unique_String() == [])
print(USI(["abcba", "abba", "abc", "cba"]).public_Unique_String() == [[2, 3], [3, 2]])
