# Напишите программу, которая принимала бы текст из пользовательского ввода
# и печатала этот текст на экране наоборот

import random

word = input("Введите слово: ")

word_1 = word

new_word = " "

while word_1:
    for i in range(-len(word), 0, 1):
        new_word = new_word + word[i]
    position = random.randrange(len(word_1))
    word1 = word_1[:position] + word_1[(position + 1):]

print(new_word)

input("Click Enter to leave")