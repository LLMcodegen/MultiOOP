
class AA:
    def __init__(self, n):
        self.n = n
    def __private_Alternating_appearance(self):
        binary_representation = bin(self.n)[2:]
        for i in range(len(binary_representation) - 1):
            if binary_representation[i] == binary_representation[i + 1]:
                return False
        return True
    def public_Alternating_appearance(self):
        return self.__private_Alternating_appearance()

#--------------:
print(AA(13).public_Alternating_appearance() == False)
print(AA(14).public_Alternating_appearance() == False)
print(AA(15).public_Alternating_appearance() == False)
