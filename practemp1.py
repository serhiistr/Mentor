# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".

a, b = map(int, input("Enter two numbers through a space: ").split())
c = input("Введите операцию, которую хотите выполнить: ")


def arithmetic(a, b, c):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    elif c == "*":
        return a*b
    elif c == "/":
        return a/b
    else:
        return "неизвестна операция"


print(arithmetic(a, b, c))
