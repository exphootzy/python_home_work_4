#  В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
from random import randint

n=(int(input("Введите число для n элементов для первого множества: ")))
list_one =set([randint(1, 10) for x in range(1, n+1)])
print(list_one)

n_bushes = int(input('Введите количество кустов черники: '))
arr = list()
for i in range(n_bushes):
    a =int(input('Введите количество ягод на кусте: '))
    arr.append(a)

arr_count = list()
for i in range(len(arr)):
       arr_count.append(arr[i-2] + arr[i-1] + arr[i])
print(max(arr_count))