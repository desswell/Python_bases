#author = 'Ким Алексей Максимович'
#ez_1
"""
def ur(a):
    a = a.split('.')
    c = int(input())
    global d, p
    b = a[1][:c]
    u = a[0][:c]
    d = ''
    p = 0
    o = 0
    if a[0] == '0':
        x = list(a[1])
        g = int(x[c])
        if g >= 5:
            p = 1
    else:
        d = ''
        if c > len(a[1]):
            b += (c - len(a[1]))*'0'
        elif c < len(a[1]):
            x = list(a[1])
            g = int(x[c])
            y = list(a[0])
            if g >= 5:
                if c == 0:
                    u = 1
                    o = 1
                else:
                    x[c-1] = str(int(x[c-1]) + 1)
                    b = ''.join(x)[:c]
        elif c == len(a[1]):
             a[1] += '0'
        if c != 0:
            d = a[0] + '.' + b
        elif c == 0 and o != 1:
            d = a[0]
        elif o == 1:
            d = int(a[0]) + u
    if d == '':
        d = 0
a = input()
ur(a)
if p == 1:
    print(p)
else:
    print(d)
"""
#ez_2
"""
def lot(a, t, f):
    b = a[0:2]
    c = a[3:5]
    for i in range(len(b)):
        f += int(b[i])
    for i in range(len(c)):
        t += int(c[i])
    return f, t
f = 0
t = 0
lot(input(), t, f)
if f == t:
    print('WIN')
else:
    print('lose')
"""
#normal_1
"""
def fib(n, m):
    if n == 1:
        print(1)
        print(1)
    if n == 2:
        print(1)
    fib2 = 1
    fib1 = 1
    i = 2
    while i < m:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        if i >= n:
            print(fib_sum)
n = int(input())
m = int(input())
if n <= m:
    fib(n, m)
else:
    print('Ошибка')
"""
#2
"""
def sor(a, b):
    for i in range(len(a)):
        b.append(min(a))
        a.remove(min(a))
a = [1, 3, 5, 1, -1]
b = []
sor(a, b)
print(b)
"""
#3
"""
def fil(a, c, y):
    for i in range(len(a)):
        if a[i] == c:
            y.append(a[i])
a = ['1', '2', '1', '2']
c = input()
y = []
fil(a, c, y)
print(y)
"""
#4
"""
import math
a = input().split(';')
b = input().split(';')
c = input().split(';')
d = input().split(';')
r1 = math.sqrt(math.fabs((int(b[0]) - int(a[0]))**2 + (int(b[1]) - int(a[1]))**2))
r2 = math.sqrt(math.fabs((int(c[0]) - int(b[0]))**2 + (int(c[1]) - int(b[1]))**2))
r3 = math.sqrt(math.fabs((int(d[0]) - int(c[0]))**2 + (int(d[1]) - int(c[1]))**2))
r4 = math.sqrt(math.fabs((int(a[0]) - int(d[0]))**2 + (int(a[1]) - int(d[1]))**2))
if r1 == r3 and r2 == r4:
    print('Это параллелограмм')
else:
    print('Это не параллелограмм')
"""
#1hard
"""
def NOD(nod, r1, r2, t0, y1):
    r1 = t0
    r2 = y1
    while r1 != 0 and r2 != 0:
        if r1 > r2:
            r1 = r1 % r2
        else:
            r2 = r2 % r1
    nod = r1 + r2
    return nod
nod = 0
r1 = 0
r2 = 0
nod1 = 0
a = input()
a = a.split(' ')
if '/' in a[0] and '/' in a[2]:
    b = a[0].split('/')
    c = a[2].split('/')
    p = 1
elif '/' in a[1]:
    b = a[1].split('/')
    c = a[3].split('/')
    p = 2
    n1 = int(a[0])
elif '/' in a[3]:
    b = a[0].split('/')
    c = a[3].split('/')
    p = 1
    n1 = int(a[2])
if len(a) == 5:
    if '/' in a[1] and '/' in a[4]:
        b = a[1].split('/')
        c = a[4].split('/')
        p = 2
        n1 = int(a[0]) + int(a[3])
t1 = int(b[0])
t2 = int(c[0])
y1 = int(b[1])
if b[1] != c[1]:
    y1 *= int(c[1]) #знам
    t1 *= int(c[1])
    t2 *= int(b[1])
if a[p] == "+":
    t0 = t1 + t2 #числитель
    n = t0 // y1  # целая часть
    if n > 0:
        t0 -= (t0 // y1) * y1
        if t0 == 0:
            print(f'{n + n1}')
        else:
            while nod1 != 1:
                nod1 = NOD(nod, r1, r2, t0, y1)
                t0 //= nod1
                y1 //= nod1
            print(f'{n + n1} {t0}/{y1}')
    else:
        while nod1 != 1:
            nod1 = NOD(nod, r1, r2, t0, y1)
            t0 //= nod1
            y1 //= nod1
        print(f'{t0}/{y1}')
else:
    t0 = t1 - t2
    if t0 == 0:
        print(0)
    else:
        n = t0 // y1  # целая часть
        if n > 0:
            t0 -= (t0 // y1) * y1
            if t0 == 0:
                print(f'{n + n1}')
            else:
                while nod1 != 1:
                    nod1 = NOD(nod, r1, r2, t0, y1)
                    t0 //= nod1
                    y1 //= nod1
                print(f'{n + n1} {t0}/{y1}')
        else:
            while nod1 != 1:
                nod1 = NOD(nod, r1, r2, t0, y1)
                t0 //= nod1
                y1 //= nod1
            print(f'{t0}/{y1}')
"""
#2              #Как бы вы не перемешивали файл с работниками и часами, все равно программа будет работать) P.S не забудьте поменять название файла к которы1 будете считывать
"""
import os
a = []
q = 0
ya = 0
b = []
y = 1
o = 0
l = -1
y1 = 1
path = os.path.join('workers.txt')
path1 = os.path.join('hours.txt')
f = open(path, 'r', encoding='UTF-8')
f1 = open(path1, 'r', encoding='UTF-8')
h = f.readlines()
h1 = f1.readlines()
for i in range(len(h) - 1):
    if ya == 1:
        ya = 0
        q = 0
    a = h[i + 1].split(' ')
    a = list(filter(None, a))
    b = h1[i + 1].split(' ')
    b = list(filter(None, b))
    if a[0] != b[0] or a[1] != b[1]:
        q = 0
        q -= l
        while ya != 1:
            b = h1[i + q].split(' ')
            b = list(filter(None, b))
            if a[0] == b[0] and a[1] == b[1]:
                ya = 1
            q += 1
            l += 1
    if i == len(h) - 2:
        k = 0
    else:
        a[4] = a[4][:-1]
    if i == len(h) - 1:
        k = 0
    else:
        b[2] = b[2][:-1]
    if b[2] <= a[4]:
        zp = int(a[2])*int(b[2]) / int(a[4])
    else:
        zp = int(a[2]) + (int(b[2]) - int(a[4])) / int(a[4])*int(a[2])
    print(f'{a[0]} {a[1]} зарплата: {zp}')
f.close()
f1.close()
"""
#3
"""
import os
def write(o):
    for i in range(len(h)):
        if alp[o] == h[i][0]:
            f1.write(h[i])
            f1.write(' ')
    o += 1
    return o
u = 0
o = 0
a = 0
path = os.path.join('fruits')
f = open(path, 'r', encoding='UTF-8')
h = f.readlines()
h = list(filter(None, h))
for i in range(len(h)):
    h[i] = h[i][:-1]
h = list(filter(None, h))
alp = list(map(chr, range(ord('А'), ord('Я')+1)))
for t in range(len(alp)):
    f1 = open('fruits_' + str(alp[o]), 'w')
    o = write(o)
    f1.close()
f.close()
"""