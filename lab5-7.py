def precedence(operator):

    if operator == '^':
        return 3

    elif operator == '*' or operator == '/':
        return 2

    elif operator == '+' or operator == '-':
        return 1

    return 0


stack = []
postfix = ""

expression = input("Enter infix expression: ")

for ch in expression:

    if ch.isalnum():
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':

        while stack and stack[-1] != '(':
            postfix += stack.pop()

        if stack:
            stack.pop()

    else:

        while (stack and
               stack[-1] != '(' and
               precedence(stack[-1]) >= precedence(ch)):

            postfix += stack.pop()

        stack.append(ch)


while stack:
    postfix += stack.pop()


print("Postfix expression:", postfix)
