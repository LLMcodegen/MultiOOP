
import heapq
from collections import Counter

class RL:
    def __init__(self, s: str):
        self.s = s
    def __private_Rearrange_letters(self) -> str:
        char_count = Counter(self.s)
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        prev_char, prev_count = None, 0
        result = []
        while max_heap or prev_count:
            if prev_count < 0:
                if not max_heap:
                    return ""
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            prev_char, prev_count = char, count + 1
        return "".join(result)
    def public_Rearrange_letters(self) -> str:
        return self.__private_Rearrange_letters()

#--------------:
print(RL("aaaabbbcc").public_Rearrange_letters() == "ababacabc")
print(RL("aaabbc").public_Rearrange_letters() == "ababac")
print(RL("aaabbbccc").public_Rearrange_letters() == "abcabcabc")
