# Напишите программу "Автодиллер", в окно которой пользователь сможет ввести стоимость авто
# без наценок. Программа должна прибавить к ней несколько дополнительных сумм: налог,
# регистрационный сбор, агентский сбор, цену доставки автомобиля до места назначения.
# Пусть налог и регистрационный сбор вычисляются как доля от начальной стоимости, а остальные
# наценки будем считать фиксированными величинами. Выводим на экран полную стоимость автомобиля.

a = float(input("Введите стоимость автомобиля без наценок:\n"))
b = a * 1.1         # tax
c = a * 1.03        # registration fee
d = 1000            # agency fee
k = 1500            # delivery

print("Full coast of the car: ", float("{0:.2f}".format(b + c + d + k)))
print("Hello")