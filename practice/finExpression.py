# postfix evaluation
class Expression:
    def __init__(self):
        self.expr = '57*43-6/9%+'
        self.len = len(self.expr)
        self.stack = []
        self.expression = ''
        self.sym = None
        
    def eval_postfix(self):
        for i in range(self.len):
            print(self.expr[i], end = ' ')
            if self.getSymtype(self.expr[i]) == 'operand':
                self.stack.append(int(self.expr[i]))
            else:
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                if self.expr[i] == '+':
                    self.stack.append(op1 + op2)
                elif self.expr[i] == '-':
                    self.stack.append(op2 - op1)
                elif self.expr[i] == '/':
                    self.stack.append(op2 // op1)
                elif self.expr[i] == '*':
                    self.stack.append(op1 * op2)
                elif self.expr[i] == '%':
                    self.stack.append(op2 % op1)
            print(self.stack)
        return self.stack[0]

    def getSymtype(self, sym):
        self.sym = sym
        if self.sym.isdigit():
            return 'operand'
        else:
            pass
        
    def infix_postfix(self, expr):
        for token in expr:
            print(token)
            if self.getSymtype(token) == 'operand':
                self.expression += token
            else: # operator
                if self.precedence(token) == None:
                    if token == '(':
                        self.stack.insert(0, token)
                    else:
                        c = self.stack.pop()
                        while c != '(':
                            self.expression += c
                else:
                    if len(self.stack) == 0 or \
                        self.precedence(token) > self.precedence(self.stack[0]):
                        self.stack.insert(0,token)
                    elif self.precedence(token) <= self.precedence(self.stack[0]):
                        self.expression += self.stack.pop()
                
        print(self.expression)
        
    def precedence(self, op):
        if op == '+' or op == '-':
            return 0
        elif op == '*' or op == '/':
            return 1
        else:
            return None

expr = '9/(3+6-5)*7*(6-4)'  
e = Expression()
e.infix_postfix(expr)