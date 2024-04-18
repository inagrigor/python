# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы 
# используется множество раз и вы не хотите ничего сломать): 
# transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
# или любой другой список transormed_values = list(map(transformation, values)) 
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation. 
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
# а нужно получить его как есть. Напишите такое лямбда-выражение transformation, чтобы transformed_values 
# получился копией values.

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('True')
# else: print('False')

# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию f ind_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
# по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
# зато искусственные спутники были были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: 
# сначала вычислить самую большую площадь эллипса, 
# а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна 

import math


# def find_farthest_orbit(list_of_orbits):
#     #   Вычисляем площади эллипсов для каждой орбиты
#     list_1 = [i for i in list_of_orbits if i[0] != i[1]] 
#     areas = [math.pi * a * b for a, b in list_1]
#  # Находим орбиту с самой большой площадью
#     farthest_orbit_index = max(range(len(areas)), key=lambda i: areas[i])
#     #  Возвращаем полуоси эллипса самой далекой планеты
#     return list_1[farthest_orbit_index]
    
# orbits = [(10, 5), (8, 6), (12, 4), (6, 6)]  # Пример списка орбит
# farthest_orbit = find_farthest_orbit(orbits)
# print("Полуоси эллипса самой далекой планеты:", farthest_orbit)


# from math import pi
# def find_farthest_orbit(list_of_orbits):
#     list1 = [i for i in list_of_orbits if i [0] != i[1]]
#     list_s = [(pi * i[0] * i[1]) for i in list1]
#     max_s = list_s.index(max(list_s)) function index = return index
    
#     return list_s[max_s]

# orbits = [(10, 5), (8, 6), (12, 4), (6, 6)] 
# print (find_farthest_orbit(orbits))

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют 
# одинаковое значение некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику. 
# Ввод: 
# values = [0, 2, 10, 6] 
#     if same_by(lambda x: x % 2, values): 
#         print(‘same’) 
#     else: print(‘different’)
    
# def same_by(characteristic, objects):
#     # Проверка для пустого списка объектов
#     if not objects:
#         return True
    
#     # Характеристика первого объекта
#     first_characteristic = characteristic(objects[0])
    
#     # Проверка характеристики для остальных объектов
#     for obj in objects[1:]:
#         if characteristic(obj) != first_characteristic:
#             return False
    
#     return True

# # Пример использования:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# def same_by(characteristic, objects):
#     result = True # результат работы функции
#     list1 = [characteristic(x) for x in objects]
#     for i in range(len(list1) - 1):
#         if list1[i] != list1[i + 1]:
#             result = False
#     return result

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента 
# функцию, вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, 
# у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.


# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     if num_rows <= 2 and num_columns <= 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#         return
#     for i in range(num_rows + 1):
#         for j in range(num_columns + 1):
#             element = operation(i, j)
#             print(element, end = ' ' if j < num_columns else "")
#         print()


# def print_operation_table(operation, num_rows=9, num_columns=9):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 if j != num_columns :
#                     result.append(f'{operation(i, j)} ')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')
#         print(''.join([str(i) for i in result[:len(result) - 1]]
        
        
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: 
#     Количество фраз должно быть больше одной!.

# Пример
# На входе:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:
# Парам пам-пам

# def count_vowels(word):
#     # Функция для подсчета гласных букв в слове
#     vowels = 'aeiouаеёиоуыэюя'
#     return sum(1 for char in word if char.lower() in vowels)

# def check_rhythm(stroka):
#     # Разделяем строку на фразы
#     phrases = stroka.split()
    
#     # Проверяем, что количество фраз больше одной
#     if len(phrases) <= 1:
#         return "Количество фраз должно быть больше одной!"
    
#     # Проверяем ритм для каждой фразы
#     for phrase in phrases:
#         words = phrase.split('-')  # Разделяем фразу на слова
#         vowels_count = [count_vowels(word) for word in words]  # Подсчитываем количество гласных в каждом слове
#         if len(set(vowels_count)) != 1:  # Если количество гласных в словах не одинаковое
#             return "Пам парам"
    
#     # Если ритм во всех фразах одинаковый
#     return "Парам пам-пам"

# # Пример использования:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# print(check_rhythm(stroka))

# def check_rhythm(stroka):
 
#     phrases = stroka.split()
#     if len(phrases) <= 1:
#         return "Количество фраз должно быть больше одной!"
#     vowels_count = [count_vowels(phrase) for phrase in phrases]
#     if len(set(vowels_count)) == 1:
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"
# def count_vowels(phrase):
#     vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ" 
#     # return sum(1 for char in phrase if char.lower() in vowels)
#     count = 0
#     for char in phrase:
#         lower_case_char = char.lower()
#         if lower_case_char in vowels:
#             count =+1
#             return count
    
# # Пример использования:

# # Пример использования:
# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# print(check_rhythm(stroka))

# f len(phrases) < 2:
#  print('Количество фраз должно быть больше одной!')
# else:
#  countVowels = []

#  for i in phrases:
#   countVowels.append(len([x for x in i if x.lower() in vowels]))

#  if countVowels.count(countVowels[0]) == len(countVowels):
#   print('Парам пам-пам')
#  else:
#   print('Пам парам')

