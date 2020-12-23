from file_loading import load_file_readlines


def shunting_yard(exp):
    output = []
    operator = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    exp = exp.replace(' ', '')

    for symbol in exp:
        if symbol in numbers:
            output.append(int(symbol))
        else:
            if symbol == ')':
                done = False
                while not done:
                    operator_pop = operator.pop()
                    if operator_pop == '(':
                        done = True
                    else:
                        output.append(operator_pop)
            else:
                if operator and symbol == '+':
                    if operator[-1] == '+':
                        output.append(operator.pop())
                        operator.append(symbol)
                    elif operator[-1] == '*':
                        operator.append(symbol)
                    else:
                        operator.append(symbol)
                elif operator and symbol == '*':
                    if operator[-1] == '+' or operator[-1] == '*':
                        output.append(operator.pop())
                        operator.append(symbol)
                    else:
                        operator.append(symbol)
                else:
                    operator.append(symbol)

    while operator:
        output.append(operator.pop())

    print(output)

    return output


def reverse_polish_notation_handling(exp):
    stack = []

    for symbol in exp:
        if symbol == '+':
            a = stack.pop()
            b = stack.pop()
            c = a + b
            stack.append(c)
        elif symbol == '*':
            a = stack.pop()
            b = stack.pop()
            c = a * b
            stack.append(c)
        else:
            stack.append(symbol)

    return stack[0]

def operation_order():
    homework_file = 'input.txt'
    # homework_file = "tetst.txt"
    homework = load_file_readlines(homework_file)
    homework_answers = []

    for expression in homework:
        postfix_expression = shunting_yard(expression)
        answer = reverse_polish_notation_handling(postfix_expression)
        homework_answers.append(answer)

    print(sum(homework_answers))

if __name__ == '__main__':
    operation_order()
