class PFTN:
    def power_function(self, x, n):
        return x ** n
#--------------:
print(PFTN().power_function(2, 1) == 2)
print(PFTN().power_function(8, 3) == 512)
print(PFTN().power_function(9, 2) == 81)
