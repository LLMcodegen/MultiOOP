
class FOR:
    def __init__(self, logs):
        self.logs = logs
class SN_FOR(FOR):
    def Final_order(self):
        letter_logs = []
        number_logs = []
        for log in self.logs:
            if log.split()[1].isdigit():
                number_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + number_logs

#--------------:
print(SN_FOR(["m1 11 12", "n1 act can", "o1 13 14", "p1 act zero"]).Final_order() == ["n1 act can", "p1 act zero", "m1 11 12", "o1 13 14"])
print(SN_FOR(["h1 15 16", "i1 act car", "j1 17 18", "k1 act zoo"]).Final_order() == ["i1 act car", "k1 act zoo", "h1 15 16", "j1 17 18"])
print(SN_FOR(["e1 19 20", "f1 act can", "g1 21 22", "h1 act zero"]).Final_order() == ["f1 act can", "h1 act zero", "e1 19 20", "g1 21 22"])
