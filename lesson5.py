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
import os
import shutil
print('1. Перейти в папку')
print('2. Перейти в папку')
print('3. Перейти в папку')
print('4. Перейти в папку')
