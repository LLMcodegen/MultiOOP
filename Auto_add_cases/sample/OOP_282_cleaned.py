
class RRG:
    def __init__(self, hand):
        self.hand = hand
class SN_RRG(RRG):
    def __init__(self, hand, groupSize):
        super().__init__(hand)
        self.groupSize = groupSize
    def rearrange(self):
        if self.groupSize == 0:
            return False
        if len(self.hand) % self.groupSize != 0:
            return False
        self.hand.sort()
        card_counts = {}
        for card in self.hand:
            card_counts[card] = card_counts.get(card, 0) + 1
        for card in self.hand:
            if card_counts[card] > 0:
                for i in range(self.groupSize):
                    if card + i not in card_counts or card_counts[card + i] == 0:
                        return False
                    card_counts[card + i] -= 1
        return True

#--------------:
print(SN_RRG([1, 2, 3, 4, 5, 6], 5).rearrange() == False)
print(SN_RRG([1, 2, 3, 4, 5, 6, 7, 8, 9], 3).rearrange() == True)
print(SN_RRG([1, 2, 3, 4, 5, 6, 7, 8, 9], 4).rearrange() == False)
