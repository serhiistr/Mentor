# Доработайте программу "Анаграммы" так, чтобы к каждому слову полагалась подсказка. Игрок должен
# получать право на подсказку в том случае, если у него нет никаких предположений. Разрабоайте систему
# начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех,
# кто запросил подсказку

import random

WORDS = ("hello", "house", "car")

word = random.choice(WORDS)
correct = word

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble = jumble + word[position]
    word = word[:position] + word[(position + 1):]

print(
    """
            Добро пожаловать в игру 'Анаграммы'
        Надо переставить буквы так, чтобы получилось осмысленное слово.
        Если Вы не угадаете слово с 3-ей попытки, я дам вам подсказку, но Вы 
        потеряете одно очко. За каждую попытку Вам начисляется одно очко.
        Выигрывает тот игрок, который наберет наименьшее количество очков.
        (Для выхода нажмите Enter, не вводя своей версии)
    """)

print("Вот анаграмма: ", jumble)

a = 0
b = 1

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != " ":
    a = a + 1
    print("К сожалению, вы неправы.")
    if a == 3:
        print("Я могу дать Вам подсказку, для продолжения игры. Если согласны, введите Yes, если не согласны введите No")
        c = input()
        if c == "Yes":
            print("Я даю вам подсказку. Оно может иметь несколько этажей ")
        else:
            print("Игра окончена ", input("Click Enter to leave"))
    guess = input("Попробуйте отгадать исходное слово: ")
    b = b + 1

if guess == correct:
    print("Да, именно так! Вы отгадали!\n")
    print("Вы набрали ", b, "очков")

print("Спасибо за игру.")

input("Click Enter to leave")
