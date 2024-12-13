#Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
try:
#ввод N
    N = int(input("Введите целое число N (> 0): "))
#проверка
    if N > 0:
#вычисляем сумму квадратов чисел от N до 2N
        total_sum = sum((i * 2) for i in range(N, 2 * N + 1))
        print("Сумма:", total_sum)
    else:
        print("Введите число больше 0")
except ValueError:
    print("Введите число!")