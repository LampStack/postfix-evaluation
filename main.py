class postfix :
    stack = list()
    postfix = ''

    def __init__(self, postfix) -> None:
        if postfix[0].isdigit() :
            self.postfix = postfix.split(',')
        else :
            self.postfix = postfix.split(',')[::-1]

    def calculator(self) -> int:
        for char in self.postfix :
            if char.isdigit():
                self.stack.append(int(char))
            else :
                a = self.stack.pop()
                b = self.stack.pop()
                match char :
                    case '+' :
                        self.stack.append(b + a)
                    case '-' :
                        self.stack.append(b - a)
                    case '*' :
                        self.stack.append(b * a)
                    case '/' :
                        self.stack.append(b / a)
                    case '^' :
                        self.stack.append(b ** a)
        return self.stack.pop()


result = postfix('5,3,+,4,/').calculator()
print(result)
