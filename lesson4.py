#1_ez
"""
a = [1, 2, 0, 1, 3]
a = [el ** 2 for el in a]
print(a)
"""
#2
"""
a = ['apple', 'orange', 'mango']
b = ['pineapple', 'apple', 'mango']
c = [a[i] for i in range(len(a)) for j in range(len(a)) if a[i] == b[j]]
print(c)
"""
#3
"""
a = [1, 2, 4, 6, 2, 6, 8]
b = [i for i in a if i > 0 and i % 3 == 0 and i % 4 != 0]
print(b[0])
"""
#1normal
"""
import re


result = [i[0] for i in re.findall(r'([a-z]+)[A-Z]+|[A-Z]+([a-z]+)', 'mtMmEZUOmcqG')]
print(result)
"""
#2
"""
import random


with open('newfile.txt', 'w+', encoding='utf-8') as file:
    for i in range(2500):
        print(random.randint(1, 9), file=file, end='')


with open('newfile.txt', 'a+', encoding='utf-8') as file:
    file.seek(0)

    num_str = ''

    for line in file:
        num_str = line

    str_max = ''
    str_1 = ''

    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            str_1 += num_str[i]
        else:
            if num_str[i] == num_str[i - 1] and i != 0:
                str_1 += num_str[i]

            if len(str_max) < len(str_1):
                str_max = str_1
            str_1 = ''


    print('', file=file)
    print(str_max, file=file)
"""