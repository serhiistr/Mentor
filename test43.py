# Считалка
# Демонстрирует использование функции range()

print("Count: ")
for i in range(10):
    print(i, end=" ")

print("\n\nLet's list multiples of five: ")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCount in reverse order: ")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nClick Enter to leave.\n")