
from collections import deque

class GS:
    def __init__(self, start, end, bank):
        self.start = start
        self.end = end
        self.bank = bank
    def _private_gene_sequence(self):
        def is_one_mutation_away(seq1, seq2):
            return sum(1 for a, b in zip(seq1, seq2) if a != b) == 1
        queue = deque([(self.start, 0)])
        visited = set([self.start])
        while queue:
            current_seq, mutations = queue.popleft()
            if current_seq == self.end:
                return mutations
            for next_seq in self.bank:
                if next_seq not in visited and is_one_mutation_away(current_seq, next_seq):
                    visited.add(next_seq)
                    queue.append((next_seq, mutations + 1))
        return -1
    def public_gene_sequence(self):
        return self._private_gene_sequence()

#--------------:
print(GS("A", "B", ["B"]).public_gene_sequence() == 1)
print(GS("A", "C", ["B", "C"]).public_gene_sequence() == 1)
print(GS("GATTACA", "GATTTCA", ["GATTACC", "GATTTCC", "GATTTCA"]).public_gene_sequence() == 1)
