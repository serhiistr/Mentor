def fact(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    return fact(x-1)*x


def factor(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    return factor(x-1)*x


a = int(input("Enter a number: "))

while a >= 0:
    print(fact(a))
    print(factor(a))
    a = int(input("Enter a number: "))



