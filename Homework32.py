# Напишите программу, которая бы "подбрасывала" условную монету
# 100 раз и сообщала, сколько раз выпал орел, а сколько решка

import random

a = 0
b = 100
c = 0 # Орел
d = 0 # Решка
while a != b:
    the_number = random.randint(1, 2)
    a = a + 1
    if the_number == 1:
        c = c + 1
    elif the_number == 2:
        d = d + 1

print("Орел выпал: ", c, " раз!")
print("Решка выпала: ", d, " раза!")

input("\n\nНажмите Enter, чтобы выйти.")
