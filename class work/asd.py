# def my_def(first_name, lastname):
#     print('Hi!', first_name, lastname)
#
#
# a = input('Введи имя: ')
# b = input('Введи фамилию: ')
# my_def(a, b)


# def my_sum(a, b):
#      if a > b:
#          return a + b
#      else:
#          return a - b
#
#
# num1 = int(input('Введи 1 число'))
# num2 = int(input('Введи 2 число'))
# print('Результат = ', my_sum(num1, num2))





# def my_sum(a, b):
#         return a + b, a * b
#
#
#
# num1 = int(input('Введи 1 число'))
# num2 = int(input('Введи 2 число'))
# s, d = my_sum(num1, num2)
# print('Результат суммы = ', s)
# print('Результат суммы = ', d)


var1 = ('Global')


def foo():
    var1 = 'local'
    var2 = 'local2'
    print(var1)


print(var1)
print(var2)
foo()
