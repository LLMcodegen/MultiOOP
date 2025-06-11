
class LS:
    def __init__(self, s, dictionary):
        self.s = s
        self.dictionary = dictionary
    def __private_Longest_string(self):
        def is_subsequence(word, s):
            it = iter(s)
            return all(char in it for char in word)
        longest_string = ""
        for word in self.dictionary:
            if is_subsequence(word, self.s):
                if len(word) > len(longest_string) or (len(word) == len(longest_string) and word < longest_string):
                    longest_string = word
        return longest_string
    def public_Longest_string(self):
        return self.__private_Longest_string()

#--------------:
print(LS("abpcplea", ["pple", "ple", "p"]).public_Longest_string() == "pple")
print(LS("aabbcc", ["abc", "a", "b", "c"]).public_Longest_string() == "abc")
print(LS("hello", ["he", "hello", "hell"]).public_Longest_string() == "hello")
