class STFM:
    def string_form(self, num1, num2):
        product = int(num1) * int(num2)
        return str(product)
#--------------:
#--------------:
print(STFM().string_form("7", "11") == "77")
print(STFM().string_form("56", "78") == "4368")
print(STFM().string_form("12345", "6789") == "83810205")
