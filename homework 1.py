#1
a = int(input())
while a > 0:
        print(a%10, ' ')
        a = a // 10

#2
a = int(input())
b = int(input())

c = a
a = b
b = c

print (a, ' ', b)

#3
a = int(input())

if a >= 18:
        print('Доступ разрешен')
else:
        print('Извините, пользование данным ресурсом только с 18 лет')

#normal1

a = int(input())
m = 0

while a > 0:
        if a%10 > m:
                m = a%10
        a = a // 10
print(m)

#2
a = int(input())
b = int(input())

a, b = b, a

print(a, ' ', b)

#3

import math

a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4*a*c
if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(x1, ' ', x2)
elif d == 0:
        print (-b / 2*a)
elif d < 0:
        print('Нет корней')

#hard1
a = float('inf')
print(a==a**2)
print(a==a*2)
print (a > 999999)