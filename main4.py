# def calk1(a):
#     return a + a

# def calk2(a):
#     return a * a

# def math(op, x): # op - operation = calk1 adica op are lincul la calk1, sau calk2
#     print(op(x))
    
# math(calk1, 5)

# def calk1(a,b):
#     return a+b

# def calk2(a,b):
#     return a*b

# def math(op, x, y): # op - operation = calk1 adica op are lincul la calk1, sau calk2
#      print(op (x, y))
    
# math(calk2, 5, 45)


# Lambda functie

# def math(op, x, y): # op - operation = calk1 adica op are lincul la calk1, sau calk2
#      print(op (x, y))
# calk1 = lambda a, b: a + b # == def calk1(a,b): return(a+b)
# math(calk1, 5, 45)
# math(lambda a, b: a + b, 5, 45) IMPOTRANT lambda functie  in calitate de argument in functia math

# В списке хранятся числа.Нужно выбратьтолько чётные числа исоставить список пар (число; квадрат числа). 
# Пример: 1 2 3 5 8 15 23 38 Получить: [(2, 4), (8, 64), (38, 1444)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
        
# print(res)

# def select (f, col): #определяется функция select, которая принимает два аргумента: f - функцию 
#     # и col - коллекцию (например, список). Эта функция применяет функцию f к каждому элементу к
#     # оллекции col и возвращает список результатов.
#     return [f(x) for x in col] # Возвращаем список, в котором каждый элемент получен применением функции
# #f к элементам коллекции col.
# def where(f, col):
#     return[x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data) # Вызываем функцию select, передавая ей функцию int и список data.
# # Функция int используется для преобразования каждого элемента списка data в целое число. 
# # Результат сохраняем в переменной res.
# print(res)
# res = where(lambda x: x % 2 == 0, res) # Вызываем функцию where, передавая ей лямбда-функцию, которая проверяет, 
# #является ли число четным, и список res, полученный на предыдущем шаге. Результат сохраняем в переменной res.
# print(res)
# res = list(select(lambda x: (x, x**2), res)) # Вызываем функцию select с лямбда-функцией, которая возвращает кортеж 
# #из числа и его квадрата, и списком res, полученным на предыдущем шаге. 
# # Результат преобразуем в список и сохраняем в переменной res, используется функция list(), чтобы преобразовать 
# # результат в список, так как функция select возвращает список генераторов.
# print(res)

# Functia map

#  C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. 
#  Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

# data = '12 13 10 32 45 52 5 67'
# data = list(map(int, data.split()))
# print (data)



# def where(f, col):
#     return[x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data) 
# print(res)
# res = where(lambda x: x % 2 == 0, res) 
# print(res)
# res = list(map(lambda x: (x, x**2), res)) 
# print(res)

# function filter()

# data = [5, 15, 65, 36, 45, 66, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data) 
# res = filter(lambda x: x % 2 == 0, res) 
# res = list(map(lambda x: (x, x**2), res)) 
# print(res)

# mode file

# colors = ['red', 'green', 'blue'] 
# data = open('file.txt', 'a') Мы открываем файл с именем 'file.txt' в режиме добавления ('a'). 
# Это означает, что если файл уже существует, мы будем добавлять новые данные в конец файла, 
# а если файла нет, он будет создан. Мы сохраняем этот файл в переменной data.
# data.writelines(colors) Мы записываем содержимое списка colors в файл, 
# который мы только что открыли. Функция writelines() записывает каждый элемент списка в отдельной строке файла.
# data.close()

# with open('file.txt', 'w') as data: #Мы открываем файл с именем 'file.txt' в режиме записи ('w'). 
#     # Ключевое слово with используется для создания контекстного менеджера, который автоматически 
#     # закроет файл после выполнения блока кода внутри него. Мы сохраняем файл в переменной data.
#     data.write('line 1\n') # Мы записываем строку 'line 1\n' в файл data. Здесь '\n' представляет 
#     #собой символ новой строки, который добавляет пустую строку после каждой строки текста.
#     data.write('line 3\n') # Мы записываем строку 'line 3\n' в файл data. Эта строка будет добавлена 
#     #после строки 'line 1\n'.
    
# print(56) #  Мы выводим число 56. Этот код не связан с работой с файлами и будет просто выводить 
# # число 56 на экран.

# path = 'file.txt' # 
# data = open('file.txt', 'r')
# for line in data:# Мы начинаем цикл, чтобы прочитать файл построчно. Каждая строка файла будет присвоена 
# переменной line и будет обработана внутри цикла.
#     print(line)
# data.close()
