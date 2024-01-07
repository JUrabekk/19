("Напишите функцию arithmetic_operation(operation), которая принимает символ одной из четырех арифметических операций, а возвращает функцию двух аргументов для соответствующей операции")

def matem_operand(op):
    if op == '+':
        return lambda x, y: x + y
    elif op == '-':
        return lambda x, y: x - y
    elif op == '*':
        return lambda x, y: x * y
    elif op == '/':
        return lambda x, y: x / y
    else:
        return lambda x, y: print('Error!')


operation = matem_operand('+')
print(operation(1, 4))