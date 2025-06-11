
class RSI:
    def __init__(self, s):
        self.s = s
    def __private_Result_String(self):
        vowels = "aeiouAEIOU"
        vowel_list = [char for char in self.s if char in vowels]
        reversed_vowel_list = vowel_list[::-1]
        result_string = []
        vowel_index = 0
        for char in self.s:
            if char in vowels:
                result_string.append(reversed_vowel_list[vowel_index])
                vowel_index += 1
            else:
                result_string.append(char)
        return ''.join(result_string)
    def public_Result_String(self):
        return self.__private_Result_String()

#--------------:
print(RSI("vowels reversed").public_Result_String() == "vewels reversod")
print(RSI("python is awesome").public_Result_String() == "pythen os ewasimo")
print(RSI("United States").public_Result_String() == "enated StitUs")
