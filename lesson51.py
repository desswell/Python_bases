# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
"""
import os
for i in range(1, 10):
    os.mkdir(f'dir_{i}')
for i in range(1, 10):
    os.rmdir(f'dir_{i}')
"""
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!
"""
import os
a = os.listdir()
for i in a:
    if os.path.isdir(i):
        print(i)
"""
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS
"""
import os
import shutil

a = os.path.basename(__file__)

b = os.path.join(os.getcwd(), f'copia_{a}')

shutil.copyfile(__file__, b)
"""
while True:
    import os
    import shutil
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('5. Выйти из утилиты')
    a = int(input())
    if a == 1:
        b = input('В какую папку перейти: ')
        os.chdir(b)
        print(f'Вы перешли в папку {b}')
    elif a == 2:
        print(*os.listdir())
    elif a == 3:
        b = input('Какую папку вы хотите удалить? ')
        print(b)
        shutil.rmtree(b)
        print(f'Папка {b} успешно удалена')
    elif a == 4:
        b = input('Введите название папки: ')
        os.mkdir(b)
        print(f'Папка {b} успешно создана')
    elif a == 5:
        break