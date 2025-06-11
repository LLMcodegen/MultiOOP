
class ERS:
    def __init__(self, num):
        self.num = num
    def __private_rep(self):
        if self.num == 0:
            return "Zero"
        def one(num):
            switcher = {
                1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
            }
            return switcher.get(num, "")
        def two_less_than_20(num):
            switcher = {
                10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
            }
            return switcher.get(num, "")
        def ten(num):
            switcher = {
                2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty",
                7: "Seventy", 8: "Eighty", 9: "Ninety"
            }
            return switcher.get(num, "")
        def two(num):
            if not num:
                return ""
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_than_20(num)
            else:
                tens = num // 10
                rest = num % 10
                return ten(tens) + (" " + one(rest) if rest else "")
        def three(num):
            hundred = num // 100
            rest = num % 100
            if hundred and rest:
                return one(hundred) + " Hundred " + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + " Hundred"
        billion = self.num // 1000000000
        million = (self.num - billion * 1000000000) // 1000000
        thousand = (self.num - billion * 1000000000 - million * 1000000) // 1000
        remainder = self.num % 1000
        result = ""
        if billion:
            result += three(billion) + " Billion "
        if million:
            result += three(million) + " Million "
        if thousand:
            result += three(thousand) + " Thousand "
        if remainder:
            result += three(remainder)
        return result.strip()
    def public_rep(self):
        return self.__private_rep()

#--------------:
print(ERS(204).public_rep() == "Two Hundred Four")
print(ERS(999).public_rep() == "Nine Hundred Ninety Nine")
print(ERS(1000).public_rep() == "One Thousand")
