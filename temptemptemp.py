a = "Striukovskyi Serhii"

print(a.split())

a = "1, 2, 3, 4, 5"

print(a.split())

s = ['43', '54', '32', '65']
print('+'.join(s))
print(''.join([str(i) for i in s]))


a = [-1, -2, -3, 4, 5]
b = list(map(abs, a))
c = [ abs(i) for i in a]
print(b, c)


def f(x):
    return x**2
b = list(map(f, a))
print(b)

a = ['hello', 'hi', 'good morning']
b = list(map(str.upper, a))
#map используют не только с фукциями (str и другие) но и с методами (upper и другие)
print(b)
