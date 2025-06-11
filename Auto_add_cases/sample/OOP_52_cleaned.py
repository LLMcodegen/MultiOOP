class RWO:
    def Reverse_Word_Order(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string
#--------------:
print(RWO().Reverse_Word_Order("Artificial intelligence will shape the future") == "future the shape will intelligence Artificial")
print(RWO().Reverse_Word_Order("Never stop exploring new opportunities") == "opportunities new exploring stop Never")
print(RWO().Reverse_Word_Order("Learning to code is a valuable skill") == "skill valuable a is code to Learning")
