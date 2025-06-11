class WDLH:
    def __init__(self):
        pass
    def word_length(self, s: str) -> int:
        s = s.strip()
        words = s.split()
        if words:
            return len(words[-1])
        else:
            return 0
#--------------:
print(WDLH().word_length(" ") == 0)
print(WDLH().word_length("This is a test sentence") == 8)
print(WDLH().word_length("Python programming language") == 8)
