import stack_array

class PostfixFormatException(Exception):
    pass

def infix_to_postfix(input_str):
    x = input_str.split(" ")
    stack = stack_array.Stack(len(x))
    ex = ""
    for i in x: #Operators
        print(i, stack.items, ex)
        if is_operator(i):
            #print(i, stack.items)
            if (stack.is_empty() == False) and ((stack.items[0] != ")") and (stack.items[0] != "(")):
                while (precedence(stack.items[0]) >= precedence(i) and (stack.items[0] != "**")) or ((precedence(stack.items[0]) > precedence(i)) and (stack.items[0] == "**")):
                    ex += stack.pop() + " "
            stack.push(i)
        elif i == "(": #Opening Parenthesis
            stack.push(i)
        elif i == ")": #Closing Parenthesis
            c = None
            while c != "(":
                c = stack.pop()
                if (c != "(") and (c != ")"):
                    ex += c + " "
        else: #Values
            ex += i + " "
    for i in range(stack.size()):
        ex += stack.pop() + " "
    exx = ex[0:-1]
    return exx

def is_operator(i):
    return (i == "*") or (i == "/") or (i == "+") or (i == "-") or (i == "**") or (i == "<<") or (i == ">>")

def postfix_eval(input_str):
    if len(input_str) == 0:
        raise PostfixFormatException("Insufficient operands")
    x = input_str.split(" ")
    stack = stack_array.Stack(len(x))
    for i in x: #Operators
        if is_operator(i):
            if (stack.items[0] == None) or (stack.items[1] == None):
                raise PostfixFormatException("Insufficient operands")
            if i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.push(int(b) - int(a))
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.push(int(b) + int(a))
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.push(int(b) * int(a))
            elif i == "**":
                a = stack.pop()
                b = stack.pop()
                stack.push(int(b) ** int(a))
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                if int(a) == 0:
                    raise ValueError()
                stack.push(int(int(b) / int(a)))
            elif i == "<<":
                a = stack.pop()
                b = stack.pop()
                if (type(a) == type(3.5)) or (type(b) == type(3.5)):
                    raise PostfixFormatException("Illegal bit shift operand")
                stack.push(int(b) << int(a))
            elif i == ">>":
                a = stack.pop()
                b = stack.pop()
                if (type(a) == type(3.5)) or (type(b) == type(3.5)):
                    raise PostfixFormatException("Illegal bit shift operand")
                stack.push(int(b) >> int(a))
        else: #Values
            try:
                stack.push(int(i))
            except ValueError:
                try:
                    stack.push(float(i))
                except ValueError:
                    raise PostfixFormatException("Invalid token")
    if (stack.size() > 1):
        raise PostfixFormatException("Too many operands")
    return stack.pop()
    
def prefix_to_postfix(input_str):
    input_str = rev_str(input_str)
    x = input_str.split(" ")
    stack = stack_array.Stack(len(x))
    ex = ""
    for i in x: #Operators
        if is_operator(i):
            a = stack.pop()
            b = stack.pop()
            stack.push(a + " " + b + " " + i)
        else: #Values
            stack.push(i)
    for i in range(stack.size()):
        ex += stack.pop() + " "
    exx = ex[0:-1]
    return exx
    
def rev_str(string):
    new = ""
    for n in range(len(string)):
        new += string[-(n+1)]
    return new

def precedence(a):
    order = ["-", "+", "/", "*", "**", ">>", "<<"]
    for n in range(len(order)):
        if order[n] == a:
            return (n // 2)
