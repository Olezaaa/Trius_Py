# Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада
# увеличивается на P процентов от имеющейся суммы (P — вещественное число, 0< P
# <25). По данному P определить, через сколько месяцев размер вклада превысит 1100
# руб., и вывести найденное количество месяцев K (целое число) и итоговый размер
# вклада S (вещественное число).

def calculate(P):
    deposit = 1000
# Счетчик месяцев для отслеживания времени
    months = 0
# Цикл продолжается, пока депозит меньше 1100
    while deposit < 1100:
# Расчет нового значения депозита с учетом процентной ставки P
        deposit += deposit * (P / 100)
        months += 1
# Возврат количества месяцев и конечного значения депозита
        return months, deposit

try:
# Запрос процентной ставки
    P = float(input("Введите процент P (0 < P < 25): "))
    if 0< P < 25:
# Вызов функции calculate и получение результатов
        months, final_deposit = calculate(P)
# Вывод результатов
        print("Через", months, "месяцев размер вклада превысит 1100 руб")
        print("Итоговый размер вклада будет составлять", final_deposit, "руб")
    else:
        print("Введите число от 0 до 25")
#проверка
except ValueError:
    print("Введите число: ")