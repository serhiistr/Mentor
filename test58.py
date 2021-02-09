# Распределенные ссылки

mike = ["белая рубакшка", "комбинезон", "пиджак"]
mr_dawson = mike
honey = mike

print(mike)
print(mr_dawson)
print(mike)

honey[2] = "красный свитер"
# Изменения внесенные через одну из трех переменных, будут оттображаться
# в списке, на который они ссылаются.
print(honey)
print(mike)
print(mr_dawson)