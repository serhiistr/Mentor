# Создайте программу, которая будет выводить список слов в случайном порядке.
# На экране должны печататься без повторений все слова из представленного списка

import random

WORD = ["мир", "дом", "машина", "дерево", "колесо", "небо", "солнце"]

# WORD1 = []

while WORD:
    a = random.choice(WORD)
    if a in WORD:
        WORD.remove(a)
    print(WORD)

# for i in WORD:
#     print(i, end=" ")

