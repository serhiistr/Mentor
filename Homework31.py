# Напишите программу - симулятор пирожка с "сюрпризом", - которая бы при запуске
# отображала один из пяти различных "сюрпризов", выбранных случайно.

import random

print("Привет. У меня есь пирожки с капустой, картошкой, яблоком, вишней, смородиной")
input("Загадай какой пирожок из предложеных я тебе предложу и нажми Enter")

the_number = random.randint(1, 5)

if the_number == 1:
    print("\nПирожок с капустой")
elif the_number == 2:
    print("\nПирожок с картошкой")
elif the_number == 3:
    print("\nПирожок с яблоком")
elif the_number == 4:
    print("\nПирожок с вишней")
elif the_number == 5:
    print("\nПирожок с смородиной")

input("\n\nНажмите Enter, чтобы выйти")