# creare lists (spischi)
# list_1 = []  # list e gol
# list_1 = list()  # functia list - crearea de list gol
# print (list_1)
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] # print (*list_1) nu vrem paranteze patrate, virgule, este o lista de valori
# for i in list_1:
    # print (i)
# print(len(list_1))
# print(list_1[3])
# print(list_1[-1]) # indexarea de la urma
# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)


# functii in list
# (1) .append (adaugam un element)
# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# (2) .pop() (excluderea ultimului element din list)
# list_1 = [12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(list_1)
# a = list_1.pop()
# print(a)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)

# (3) .pop(i) (excluderea elementului concret din list)
# list_1 = [12, 13, 14, 15, 16, 17]
# print(list_1.pop(0)) # se exclude list[0] = 12
# print(list_1)
# print(list_1.pop(3)) # se exclude list[3] = 16
# print(list_1)

#(4) .insert(i, a) adaugare de elemente la pozitia dorita: index - i, element - a
# list_1 = [1, 2, 3, 4, 5, 6]
# print(list_1.insert(2, 11))
# print(list_1)

# srezi
#list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list_1[0])
# print(list_1[1])
# print(list_1[len(list_1)-1]) # =  print (list_1[-1])
# print (list_1[-1])
# print(list_1[-5])
# print(list_1[:])
# print(list_1[:2]) # de 0 pina la [2]
# print (list_1[len(list_1)-2:])  # de la [-2] pna la urma, daca nu este indicata cifra dupa :
# print(list_1[8:])
# print(list_1[2:9])
# print(list_1[6:-1])
# print (list_1[0: len(list_1):6]) # = print(list_1[::6]) # de la 0 pe lungimea str cu pasul 6 (adica fiecarea a 6-le element)
# print(list_1[::6])

# cortej - tuple
# t = ()
# print(type(t))

# t = (1, 2, 3, 4, 5,)
# print(type(t))

# v = [1, 2, 3, 4, 5]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# # raspacovka corteja
# a,b,c,d,e = v
# print(a, b, c, d, e)

#ASAMANARI DEOSEBIRI LIST TUPLE

#asemanari
#t = (1, 2, 3, 4, 5,)☻
#print(t[1])
#for i in t: print (i)
#for i in range(len(t)): print (t[i])

# DICTIONARE
# d = {}
# d = dict()
# d['q'] = 'qwerty'
# print(d) # {'q': qwerty'} in dictionary d sub cheie q se afla element qwerty

# d['w'] = 'wwerty'
# print(d)
# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→' } # cheie up, down, right, left, 
#print(dictionary)
# print (dictionary['left'])
# print (dictionary['right'])
# print (dictionary['up'])
# dictionary['left'] = '<='
# print (dictionary['left'])
#print (dictionary['type']) # type = nu este o astfel de cheie, este gresala
# dictionary[123] = 247649
# print(dictionary) # putem adauga ori ce type de colectie sau elemente
# del dictionary['down'] # delete element
# print (dictionary) 
#for item in dictionary:
    #print(item)
    #print(dictionary[item])
    #print ('{}: {}' .format(item, dictionary[item])) # identificarea dictionary prin cheie [item] si valoare     
    #print(dictionary[item])
# print (dictionary.items()) # list of tuples: dict_items([('up', '↑'), ('down', '↓'), ('left', '←'), ('right', '→')])
# for(a, b) in dictionary.items():
#     print (a, b) # raspacovcha dictionary a = item, b = dictionary[a]

# MNOJESTVA SETS
# colors = {'red', 'green', 'blue'} 
# print(colors)
#colors.add('red') # adaugam 
# colors.add('gray')
# print(colors)
# colors.remove('red') # excludem 
# print(colors)
# colors.discard('red') # verificam daca elementul exista in set, excludem daca este, trecem peste daca nu este
# print(colors)
# colors.clear() # excludem toate elemente din set
# print(colors)

# q = set() # crearea de set

# OPERATII CU SETS
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = a
# print(c)
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)
# i = a.intersection(b)# i = { 2, 5, 8}
# print(i)
# d1 = a.difference(b) # d1 = {1, 3}
# # print(d1)
# d2 = b.difference(a) # d2 = {13,21}
# # print(d2)
# q = a.union(b).difference(a.intersection(b)) 
# q = u.difference(i)
# print(q) # q =

# FRONZENSET SETS
# a = {1, 3, 6, 10}
# b = frozenset(a)
# print(b)

# LIST COMPREHENSION
#list_1 = [exp for item in iterable] = crearea de list
#list_1 = ['none' for item in range(5)] = crearea list
# list_1 = []
# list_1 = list()
# for i in range(5):
#     list_1.append ('none')
#     print(list_1)
#list_2 = [exp for item in iterable (if conditional)] выборка по заданому условию

# list = []
# for i in range(1, 101):
#     list.append(i)
#     print(list)
# list = [i for i in range(1, 101)]

# print(list)
# list = [i for i in range(1, 101) if i % 2 == 0]

# print(list)
# list = [(i, i) for i in range(1, 101) if i % 2 == 0] - crearea de tuple in cadrul list
# print(list)

# list = [(i, i*i) for i in range(1, 101) if i % 2 == 0]
# print(list)

# list = [(i*2, i-2) for i in range(1, 101) if i % 2 == 0]

# print(list)


