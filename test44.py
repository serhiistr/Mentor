# Анализатор текста
# Демонстрирует работу функции len() и оператора in

message = input("Enter text: ")
print("\nThe length entered text is: ", len(message))
print("\nMost common consonant. 'т'.")

if "т" in message:
    print("встречается в вашем тексте")
else:
    print("не встречается в вашем тексте")

input("\n\n Click Enter to leave.")
