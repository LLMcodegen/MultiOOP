class CE:
    def Calculating_Expressions(self, tokens):
        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop() 
                if token == '+':
                    stack.append(left_operand + right_operand)
                elif token == '-':
                    stack.append(left_operand - right_operand)
                elif token == '*':
                    stack.append(left_operand * right_operand)
                elif token == '/':
                    stack.append(int(left_operand / right_operand))
        return stack[0]
#--------------:
print(CE().Calculating_Expressions(["4", "3", "-", "5", "2", "*", "+"]) == 11)
print(CE().Calculating_Expressions(["7", "8", "3", "/", "+"]) == 9)
print(CE().Calculating_Expressions(["2", "3", "11", "+", "5", "-", "*"]) == 18)
