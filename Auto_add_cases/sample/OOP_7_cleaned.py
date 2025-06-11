class PDIT:
    def Palindromic_integer(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]
#--------------:
print(PDIT().Palindromic_integer(1) == True)
print(PDIT().Palindromic_integer(11) == True)