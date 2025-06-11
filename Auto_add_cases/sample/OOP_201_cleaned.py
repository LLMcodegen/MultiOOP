
class LPC:
    def __init__(self, pairs):
        self.pairs = pairs
    def __private_Longest_pair_chain(self):
        if not self.pairs:
            return 0
        self.pairs.sort(key=lambda x: x[1])
        longest_chain_length = 1
        current_end = self.pairs[0][1]
        for i in range(1, len(self.pairs)):
            if self.pairs[i][0] > current_end:
                longest_chain_length += 1
                current_end = self.pairs[i][1]
        return longest_chain_length
    def public_Longest_pair_chain(self):
        return self.__private_Longest_pair_chain()


#--------------:
print(LPC([[1, 2], [2, 3], [4, 5], [6, 7]]).public_Longest_pair_chain() == 3)
print(LPC([[10, 20], [15, 25], [20, 30], [25, 35]]).public_Longest_pair_chain() == 2)