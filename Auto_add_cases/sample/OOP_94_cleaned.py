
class CLS:
    def __init__(self, words):
        self.words = words
    def __private_Common_letters(self):
        max_product = 0
        n = len(self.words)
        for i in range(n):
            for j in range(i + 1, n):
                if not set(self.words[i]) & set(self.words[j]):
                    product = len(self.words[i]) * len(self.words[j])
                    max_product = max(max_product, product)
        return max_product
    def public_Common_letters(self):
        return self.__private_Common_letters()

#--------------:
print(CLS(["abcd", "efg", "hij", "klm"]).public_Common_letters() == 12)
print(CLS(["flower", "tree", "bush", "grass"]).public_Common_letters() == 24)
print(CLS(["apple", "banana", "orange", "grape"]).public_Common_letters() == 0)
