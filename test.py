# n = int(input())
# m = int(input())

# print((m + n - 1)//n)

# a = int(input())
# b = int(input())
# c = int(input())

# s1 = (a + 1)//2
# s2 = (b + 1)//2
# s3 = (c + 1)//2
# print(s1 + s2 + s3) 

# i = int(input())
# j = int(input())

# if i == j:
#     print(-1)
# else:
#     print(i + j - 1)

# a = int(input())

# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('yes')
# else:
#     print('no')

# a = int(input())
# sum = 0
# for i in a: sum
# x = a % 10
# a = a / 10
# sum += x 

# factorial n (1*2*3*4...*n)
 # n = int(input())
# i = 1 scetcik tsicla
# result = 1

# while i <= n:
#     result *= i
#     i += 1

# print(result)

#  numarul Fibonaci
# n = int(input())
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2

# while n0 <= n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = -1
# print(i)

# n = int(input())
# max = 0
# k = 0

# for i in range(n):
#     x = int(input())
#     if x > 0:
#         k += 1
#     else:
#         if k > max:
#             max = k
#         k = 0
# print(max)

# n = int(input())
# max = 0
# min = 3001

# for i in range(n):
#     x = int(input())
#     if x > max:
#         max = x
#     if x < min:
#         min = x
# print(max, min)

# coins = [0, 1, 0, 1, 1, 0]
# count_0 = 0
# count_1 = 0

# for i in range(len(coins)):
#     if coins[i] == 1:
#         count_0 += 1
#     else:
#          count_1 += 1

# print(count_0 if count_0 < count_1 else count_1)
# from math import sqrt
# s = int(input())
# p = int(input())
# if s * s - 4 * p >= 0:
#     y1 =  int((s + sqrt( s * s - 4 * p)) / 2) 
#     y2 = int((s - sqrt( s * s - 4 * p)) / 2)
#     x1 = int(s - y1)
#     x2 = int(s - y2)
#     if 0 <  x1 < 1000 and 0 < y1 < 1000:
#         print(x1, y1)
#     if 0 <  x2 < 1000 and 0 < y2 < 1000:
#         print(x2, y2)
# else: 

#     print('introduceti alte numere')

# N = int(input())
# k = 0
# a = 2
# while a**k <= N:
#     print(a**k)
#     k += 1
