
from collections import Counter

class MT:
    def __init__(self, words, k):
        self.words = words
        self.k = k
    def __private_Most_times(self):
        word_count = Counter(self.words)
        return [word for word, count in word_count.most_common(self.k)]
    def public_Most_times(self):
        return self.__private_Most_times()


print(MT(["apple", "banana", "apple", "orange", "banana", "apple"], 2).public_Most_times() == ['apple', 'banana'])
print(MT(["cat", "dog", "fish", "bird"], 3).public_Most_times() == ['cat', 'dog', 'fish'])
print(MT(["sun", "moon", "sun"], 5).public_Most_times() == ['sun', 'moon'])
