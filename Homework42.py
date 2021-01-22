# Напишите программу, которая принимала бы текст из пользовательского ввода
# и печатала этот текст на экране наоборот

word = input("Введите слово: ")

new_word = ""

for i in range(-1, -len(word) - 1, -1):
    new_word = new_word + word[i]
print(new_word)

# Второй вариант

# word_2 = word
#
# print(word_2[::-1])
#
input("Click Enter to leave")
