# Напишите программу, которая принимала бы текст из пользовательского ввода
# и печатала этот текст на экране наоборот

import random

word = input("Введите слово: ")

new_word = " "
new_word1 = " "
b = word
g = int(len(word))

for i in range(g, 0, -1):
    # new_word1 = new_word1 + b[i]
    print(i)

# while word:
    # position = random.randrange(len(word))
    # new_word = new_word + word[i]
    # word = word[:position] + word[(position + 1):]

# Второй вариант

# word_2 = word
#
# print(word_2[::-1])
#
input("Click Enter to leave")
