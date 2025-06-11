
class CWS:
    def __init__(self, words1):
        self.words1 = words1
class SN_CWS(CWS):
    def __init__(self, words1, words2):
        super().__init__(words1)
        self.words2 = words2
    def Common_Words(self):
        def is_subset(a, b):
            from collections import Counter
            counter_a = Counter(a)
            counter_b = Counter(b)
            return all(counter_b[char] <= counter_a[char] for char in counter_b)
        universal_words = []
        for word_a in self.words1:
            if all(is_subset(word_a, word_b) for word_b in self.words2):
                universal_words.append(word_a)
        return universal_words

#--------------:
print(SN_CWS(["amazon", "apple", "facebook", "google", "leetcode"], ["f", "b"]).Common_Words() == ['facebook'])
print(SN_CWS(["amazon", "apple", "facebook", "google", "leetcode"], ["t", "c"]).Common_Words() == ['leetcode'])
print(SN_CWS(["amazon", "apple", "facebook", "google", "leetcode"], ["a", "p"]).Common_Words() == ['apple'])
