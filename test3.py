# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()
# string = input()
# print(string)
# string = string.split(',')
# print(string) # egal cu row 10-11a
# string = input().split()
# print(string) 
# res = {}
# for i in string:
#     if i in res:
#         print(f'{i}_{res[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     res[i] = res.get(i, 0) + 1

# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним 
# или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore 
# I'm sure that the shells are sea shore shells 
# Output: 13
# string = input().split()
# set_1 = set()
# for i in string:
#     set_1.add(i.lower())
# print(len(set_1))
   
#    “Задана последовательность неотрицательных целых чисел. 
#    Требуется определить значение наибольшего элемента последовательности, которая завершается первым 
#    встретившимся нулем (число 0 не входит в последовательность)”.

# n = int(input())
# max = n
# while n!= 0:
#     n = int(input())
#     if n > max:
#         max = n

# print(max)

#  TEMA DE ACASA
#    Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#    Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
#    Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#    Затем пользователь вводит сами элементы множеств.  
# input:11 6 
# input:2 4 6 8 10 12 10 8 6 4 2 
# input:3 6 9 12 15 18 
# output:6 12

# var = '11 6'
# var2 = '2 4 6 8 10 12 10 8 6 4 2' 
# var3 = '3 6 9 12 15 18'
# set1 = set(map(int, var2.split()))
# set2 = set(map(int, var3.split()))


# sorted_value = sorted(set1.intersection(set2))

# res = ' '.join(map(str, sorted_value))
# print(res)

# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')

# n_bushes = int(input('Введите количество кустов черники: '))
# arr = list()
# for i in range(n_bushes):
#     a =int(input('Введите количество ягод на кусте: '))
#     arr.append(a)

# arr_count = list()
# for i in range(len(arr)):
#        arr_count.append(arr[i-2] + arr[i-1] + arr[i])
# print(max(arr_count))
def max_berry_count(arr):
    max_berries = -1
    
    # Пройдемся по каждому кусту в списке arr
    for i in range(len(arr)):
        # Рассчитаем максимальное количество ягод, которое можно собрать
        # с использованием собирающего модуля, находясь перед текущим кустом
        berries = arr[i] + arr[(i - 1) % len(arr)] + arr[(i + 1) % len(arr)]
        
        # Обновим максимальное количество ягод, если текущее количество больше
        max_berries = max(max_berries, berries)
    
    return max_berries

# Пример использования
arr = [5, 8, 6, 4, 9, 2, 7, 3]
print(max_berry_count(arr))  # Ожидаемый результат: 19
