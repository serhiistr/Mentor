# Проигранное сражение
# Демонстрирует тот самый ненавистный нам бесконечный цикл
print("Вашего героя окружила огромная армия троллей.")
print("Смрадными зелеными трупами врагов устланы все окрестные поля.")
print("Одинокий герой достает меч из ножен, готовясь к последней битве в своей жизни.\n")
healthe = 10
trolls = 0
damage = 3
while healthe >= 0:
    trolls += 1
    healthe -= damage
    print("Взмахнум мечем, Ваш герой истребляет злобного тролля, "
          "но сам получает повреждение на", damage, "очков.\n")
print("Ваш герой доблестно сражался и убил", trolls, "троллей.")
print("Но увы! Он упал на поле боя.")
input("Нажмите Enter, чтобы выйти")
