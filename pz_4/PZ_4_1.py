#Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
def calculate(N):
# Инициализация переменной
    sum = 0
    i = N
# Цикл while, который выполняется, пока i меньше или равно 2*N
    while i <= 2*N:
        sum += i**2
        i += 1
# возвращение суммы
    return sum
#проверка
try:

    N = int(input("Введите целое число N: "))
    result = calculate(N)
    print("Сумма равна", result)
except ValueError:
    print("Введите целое число!")