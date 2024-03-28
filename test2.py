# Дан список чисел. Определите, сколько в нем встречается различных чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4] 
# Output: 6

# list =[]
# for i in range(1, 10):
#      list.append(i)
#      print(list)
# set = list
# print(set)  == print(set(list)) atunci rindul ulterior este deprisos

# list = [1, 1, 2, 4, 5, 5, 0, 8, 0, -1]
# my_list = []

# Запрашиваем у пользователя ввод элементов списка
# print("Введите элементы списка (для завершения введите пустую строку):")
# while True:
#     user_input = input("Элемент: ")
#     if user_input == "":
#         break  # Выход из цикла при вводе пустой строки
#     my_list.append(int(user_input))  # Преобразуем введенное значение в целое число и добавляем в список

# # Выводим полученный список
# print("Список, введенный с консоли:", my_list)


# print(set(my_list))
# print(len(set(my_list)))

#  SARCINA II
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число
# Input:   [1, 2, 3, 4, 5] k = 3 
# Output:  [4, 5, 1, 2, 3]

# list = [1, 2, 3, 4, 5, 6]
# k = int(input())
# k = k % len(list)

# list_res = []

# for i in range(k):
#     list_res.append(list[len(list) - 1 - i])
    
# print(list_res)

# for i in range(len(list) - k):
#     list_res.append(list[i])
# print(list_res)

# SARCINA III
# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
#          {" V ":" S009 "}, {" VIII ":" S007 "}] - list of dictionaries 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
#      {" V ":" S009 "}, {" VIII ":" S007 "}] 
# set1 = set()
# for i in list:
#     # print(i)
#     for j in i:
#         # print(j)
#         set1.add((i[j]))
# print(set1)

# SARCINA IV
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3] 
# Output: 2 (-1 < 5, 2 < 3)

# list = [0, -1, 5, 2, 3]   
# count = 0
# for i in range(1, len(list)):
#     if list[i] > list[i - 1]:
#         count += 1
# print (count)

# tema de acasa
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# N = int(input())
# list = []
# for i in range(1, N + 1):
#     list.append(i)
# print (list)
# X = int(input())
# count = 0

# for i in list:
#     if i == X:
#         count += 1 
# print (count)
    
#     TEMA DE ACASA II
#    Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#    Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#    В последующих  строках записаны N целых чисел Ai . 
#    Последняя строка содержит число X           
    
# N = int(input())
# list_1 = []

# for i in range(1, N+1):
#     list_1.append(i)
# print(list_1)

# x = int(input())
# с = list_1[0]

# min_diff = N + 1

# for number in list_1:
#     diff = number - x
#     if 0 <= diff < min_diff:
#         min_diff = diff
#         c = number
#         print (c)  
   
# list_1 = [1, 12, 6, 7, 8, 15]   
# k = 11  
# number = 0 # инициализация переменной которая будет хранить ближайший елемент к х
# for i in range(len(list_1)): 
#     if k - list_1[i] < k - number and k - list_1[i] >= 0:
#         number = i
# print(list_1[number]) 

# number = 0 if list_1[0] <= k else len(list_1) - 1

# for i in range(len(list_1)):
#     if list_1[i] == k:
#         number = i
#         break
#     elif list_1[i] < k and k - list_1[i] < k - list_1[number]:
#         number = i
#     elif list_1[i] > k and list_1[i] - k < list_1[number] - k:
#         number = i

# print(list_1[number])
# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11
# number = 0  # Инициализация переменной, которая будет хранить индекс ближайшего элемента к k

# for i in range(1, len(list_1)):
#     if abs(k - list_1[i]) < abs(k - list_1[number]):
#         number = i

# print(list_1[number])



# points_ru = {1:"АВЕИНОРСТ", 2:"ДКЛМПУ", 3:"БГЁЬЯ", 4:"ЙЫ", 5:"ЖЗХЦЧ", 8:"ШЭЮ", 10:"ФЩЪ"}
# points_en = {1:"AEIOULNSTR", 2:"DG", 3:"BCMP", 4:"FHVWY", 5:"K", 8:"JX", 10:"QZ"}

# word = "ноутбук"

# if word[0].lower() in points_ru:
#         sum = 0
#         for letter in word:
#             for key, value in points_ru.items():
#                 if letter.upper() in value:
#                     sum += key

#         print(sum)

# elif word[0].lower() in points_en:
#         sum = 0
#         for letter in word:
#             for key, value in points_en.items():
#                 if letter.upper() in value:
#                     sum += key
#         print(sum)
    
# points_ru = {"АВЕИНОРСТ":1, "ДКЛМПУ":2, "БГЁЬЯ":3, "ЙЫ": 4, "ЖЗХЦЧ":5, "ШЭЮ":8, "ФЩЪ":10}
# points_en = {"AEIOULNSTR":1, "DG":2, "BCMP":3, "FHVWY":4, "K":5, "JX":8, "QZ":10}

# word = "ноутбук"
# word_upper = word[0].upper()  # Приводим первую букву слова к нижнему регистру для сравнения

# if word_upper in points_ru:
#     total_score = 0
#     for letter in word:
#         for key, value in points_ru.items():
#             if letter.upper() in key:
#                 total_score += value
#                 break
#     print("Сумма очков для слова '{}' на русском языке: {}".format(word, total_score))

# elif word_upper in points_en:
#     total_score = 0
#     for letter in word:
#         for key, value in points_en.items():
#             if letter.upper() in key:
#                 total_score += value
#                 break
#     print("Сумма очков для слова '{}' на английском языке: {}".format(word, total_score))

# else:
#     print("Ошибка: Начальная буква '{}' не определена в словарях.".format(word_upper))
    
# points_ru = {"АВЕИНОРСТ":1, "ДКЛМПУ":2, "БГЁЬЯ":3, "ЙЫ": 4, "ЖЗХЦЧ":5, "ШЭЮ":8, "ФЩЪ":10}
#  points_en = {"AEIOULNSTR":1, "DG":2, "BCMP":3, "FHVWY":4, "K":5, "JX":8, "QZ":10}

# k = "ноутбук"
#  k_lower = k[0].lower()  # Приводим первую букву слова к нижнему регистру для сравнения

#  # Определяем, принадлежит ли начальная буква слова русскому или английскому алфавиту
#  if any(k_lower in key.lower() for key in points_ru):
#      total_score = 0
#      for letter in k:
#         for key, value in points_ru.items():
#             if letter.upper() in key:
#                 total_score += value
#                 break
#      print(total_score)

#  elif any(k_lower in key.lower() for key in points_en):
#     total_score = 0
#     for letter in k:
#         for key, value in points_en.items():
#             if letter.upper() in key:
#                 total_score += value
#                 break
#     print(total_score)

#  else:
#     print("Ошибка: Начальная буква '{}' не определена в словарях.".format(word_lower))

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_ru:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)


# word = k.upper()
# count = 0
# for i in word:
#     if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_ru:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
            
    