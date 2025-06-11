class IRSID:
    def sequences_DNA(self, s):
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        return list(repeated)
#--------------:
print(IRSID().sequences_DNA("CGTACGTACGTACTGACGTACGTA") == [])
print(IRSID().sequences_DNA("CCCCCCCCCCGGGGGGGGGGCCCCCCCCCC") == ['CCCCCCCCCC'])
print(IRSID().sequences_DNA("ACGTACGTACACGTACGTAC") == ['ACGTACGTAC'])