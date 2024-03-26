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
       
    
    