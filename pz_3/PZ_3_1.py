#Даны числа x, у. Проверить истинность высказывания:# «Точка с координатами (x, у) лежит в первой или третьей координатной четверти».

#ввод переменных
x=int(input('Введите значение переменной X'))
y=int(input('Введите зачение переменной Y'))

#первая координатная четверть
if y>0 x>0:
else: print("находится в первой")

#третья координатная четверть
if y<0 x<0:
else: print ("находится в третьей")