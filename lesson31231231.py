'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''
'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
'''
class Worker():
    def __init__(self, fio,  oklad, zp):
        self.fio = fio
        self._income = {
           'oklad': str(oklad),
           'zp': str(zp),
        }


class Position(Worker):
    def __init__(self, fio, oklad, zp, procent):
        Worker.__init__(self, fio, oklad, zp)
        self.procent = int(procent)

    @property
    def proc(self):
        return int(int(self._income['oklad']) + (self.procent / 100) * int(self._income['oklad']))

    @property
    def salary_with_add(self):
        return self.proc + int(self._income['zp'])

    @property
    def get_full_name(self):
        return self.fio


position1 = Position('Алексей', 10000, 500000, 10)
print(position1.salary_with_add)
'''
'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''
"""
import math
class Trey:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a = round(math.sqrt(int(math.fabs(((x2 - x1)**2) + ((y2 - y1)**2)))), 2)
        self.b = round(math.sqrt(int(math.fabs(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))), 2)
        self.c = round(math.sqrt(int(math.fabs(((x1 - x3) ** 2) + ((y1 - y3) ** 2)))), 2)
    def per(self):
        self.per = (self.a + self.b + self.c)
        return per
    def plo(self):
        self.pol = self.per / 2
        self.plo = round(math.sqrt(self.pol * (self.pol - self.a) * (self.pol - self.b) * (self.pol - self.c)), 2)
        return plo
    def visot(self):
        self.plo *= 2
        self.visot = round((self.plo) / self.c, 2)
        return visot
tri = Trey()
print(f'длина стороны {tri.a} {tri.b} {tri.c}')
print(f'периметр треугольника {tri.per}')
print(f'длина площадь {tri.plo}')
print(f'длина высота {tri.visot}')
"""