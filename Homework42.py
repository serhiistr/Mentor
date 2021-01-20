# Напишите программу, которая принимала бы текст из пользовательского ввода
# и печатала этот текст на экране наоборот

import random

word = input("Введите слово: ")
a = word

new_word = " "

while word:
    # for i in range(3):
    #     new_word = new_word + word[i]
    position = random.randrange(len(word))
    word = word[:position] + word[(position + 1):]
print("new_word")

# Второй вариант

# word_2 = word
#
# print(word_2[::-1])
#
input("Click Enter to leave")
