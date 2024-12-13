#Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
def calculate(N):
    sum = 0
    i = N
    while i <= 2*N:
        sum += i**2
        i += 1
#возвращение суммы
    return sum

try:
    N = int(input("Введите целое число N: "))
    result = calculate(N)
    print("Сумма равна", result)
#проверка
except ValueError:
    print("Введите целое число, пожалуйста")
