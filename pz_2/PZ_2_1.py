#С начала суток прошло N секунд (N — целое). Найти количество полных минут, прошедших с начала последнего часа.

#проверка
try:

         #ввод
          N = int(input("Введите количество секунд ,прошедших с начала суток:"))


          #нахождение полных минут
          minutes_passed = (N // 60)

          print("Количество полных минут, прошедших с начала последнего часа:", minutes_passed)
#проверка
except ValueError:
 print('Что-то пошло не так')