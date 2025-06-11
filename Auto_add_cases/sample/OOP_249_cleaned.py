
class CN:
    def __init__(self, sx, sy, tx, ty):
        self.sx = sx
        self.sy = sy
        self.tx = tx
        self.ty = ty
    def __private_Convert_numbers(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        return False
    def public_Convert_numbers(self):
        return self.__private_Convert_numbers(self.sx, self.sy, self.tx, self.ty)

#--------------:
print(CN(1, 1, 6, 7).public_Convert_numbers() == True)
print(CN(1, 1, 7, 6).public_Convert_numbers() == True)
print(CN(1, 1, 8, 9).public_Convert_numbers() == True)
