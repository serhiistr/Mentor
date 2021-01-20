import random

word = input("Enter word: ")

new_word = " "

for i in range(3):
    new_word = new_word + word[i]
    while word:
        position = random.randrange(len(word))
        word = word[:position] + word[(position + 1):]