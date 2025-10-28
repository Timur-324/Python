#варианты решения:
# сделать через алгоритм Дейкстры
# использовать рекурсию
# реализовать стэк через кластеры

def calc(expr):
    expr = expr.replace(" ", "")

    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    def eval_simple(s):
        numbers = []
        ops_list = []
        num = ""

        # Разделяем числа и операторы
        for ch in s:
            if ch.isdigit():
                num += ch
            else:
                numbers.append(int(num))
                ops_list.append(ch)
                num = ""
        numbers.append(int(num))


        result = numbers[0]
        for i in range(len(ops_list)):
            result = ops[ops_list[i]](result, numbers[i + 1])
        return result

    # Пока есть скобки решаем то что внутри
    while "(" in expr:
        start = 0
        end = 0
        for i in range(len(expr)):
            if expr[i] == "(":
                start = i
            if expr[i] == ")":
                end = i
                break

        inside = expr[start+1:end]     #то, что внутри скобок
        value = eval_simple(inside)    #подсчёт
        expr = expr.replace("(" + inside + ")", str(value), 1)  #заменяем на результат

    return eval_simple(expr)

print(calc("2 + (3 * 20) - 5"))    