# Даны числа x, у. Проверить истинность высказывания:
# «Точка с координатами (x, у) лежит в первой или третьей координатной четверти».
# Проверка
try:
    # ввод переменных
    x = int(input('Введите значение переменной X:'))
    y = int(input('Введите значение переменной Y:'))

    #координатная четверть
    if y > 0 and x > 0 or y < 0 and x < 0:
        print("Находится в первой или третье координатной четверти")
    else:
        print("Не находится в первой или третьей координатной четверти")

    #проверка
except ValueError:
    print("что-то пошло не так")

