import math
decimal_places = int(input("Введите сколько нужно колличество знаков после запятой: "))
number = round(math.pi, decimal_places)
print(number)