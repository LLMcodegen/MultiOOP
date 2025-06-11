
class ECG:
    def __init__(self, words):
        self.words = words
class SN_ECG(ECG):
    def efficient_coding(self):
        words = sorted(self.words, key=lambda x: -len(x))
        encoded_string = ""
        for word in words:
            if word + '#' not in encoded_string:
                encoded_string += word + '#'
        return len(encoded_string)

#--------------:
print(SN_ECG(["abc", "ab", "a"]).efficient_coding() == 9)
print(SN_ECG(["abc", "def", "ghi"]).efficient_coding() == 12)
print(SN_ECG(["abc", "def", "ghi", "jkl"]).efficient_coding() == 16)
