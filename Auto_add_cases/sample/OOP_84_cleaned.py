
class BOT:
    def __init__(self, num: str, target: int):
        self.num = num
        self.target = target
    def __private_Binary_operator(self, path: str, pos: int, prev_operand: int, current_operand: int, value: int, results: list):
        if pos == len(self.num):
            if value == self.target and current_operand == 0:
                results.append(path)
            return
        for i in range(pos, len(self.num)):
            if i != pos and self.num[pos] == '0':
                break
            current_str = self.num[pos:i + 1]
            current_num = int(current_str)
            if pos == 0:
                self.__private_Binary_operator(current_str, i + 1, current_num, 0, current_num, results)
            else:
                self.__private_Binary_operator(path + "+" + current_str, i + 1, current_num, 0, value + current_num, results)
                self.__private_Binary_operator(path + "-" + current_str, i + 1, -current_num, 0, value - current_num, results)
                self.__private_Binary_operator(path + "*" + current_str, i + 1, prev_operand * current_num, 0, value - prev_operand + (prev_operand * current_num), results)
    def public_Binary_operator(self):
        results = []
        self.__private_Binary_operator("", 0, 0, 0, 0, results)
        return results

#--------------:
print(BOT("222", 8).public_Binary_operator() == ['2*2*2'])
print(BOT("81", 9).public_Binary_operator() == ['8+1'])
print(BOT("567", 30).public_Binary_operator() == [])