
class RS:
    def __init__(self, dictionary, sentence):
        self.dictionary = dictionary
        self.sentence = sentence
    def __private_Root_substitution(self):
        sorted_dict = sorted(self.dictionary, key=len)
        words = self.sentence.split()
        for i, word in enumerate(words):
            for root in sorted_dict:
                if word.startswith(root):
                    words[i] = root
                    break
        return ' '.join(words)
    def public_Root_substitution(self):
        return self.__private_Root_substitution()

#--------------:
print(RS(["out", "our", "the"], "our house is out there").public_Root_substitution() == "our house is out the")
print(RS(["up", "down"], "going up and down").public_Root_substitution() == "going up and down")
print(RS(["like", "likes", "liking"], "she likes to dance").public_Root_substitution() == "she like to dance")
