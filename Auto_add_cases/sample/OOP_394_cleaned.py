from collections import Counter

class LSQ:
    def __init__(self, tiles):
        self.tiles = tiles
class SN_LSQ(LSQ):
    def letter_sequence(self):
        def backtrack(count):
            total_sequences = 0
            for char in count:
                if count[char] > 0:
                    count[char] -= 1
                    total_sequences += 1
                    total_sequences += backtrack(count)
                    count[char] += 1
            return total_sequences
        tile_count = Counter(self.tiles)
        return backtrack(tile_count)

#--------------:
print(SN_LSQ("ABCD").letter_sequence() == 64)
print(SN_LSQ("AABBCCDD").letter_sequence() == 7364)
print(SN_LSQ("AABBCCDDEE").letter_sequence() == 326010)
