'''
# Сумма введённых эелементов. Первое введённое число - количество элементов для суммирования
print(sum(int(input()) for i in range(int(input()))))
'''
###################################################################################
'''
# Количество уникальных объектов в списке
objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]
individ = []
for obj in objects:
    in_ind = False
    for ind in individ:
        if id(obj) == id(ind):
            in_ind = True
            break
    if not in_ind:
        individ.append(obj)
print(len(individ))
'''
###################################################################################
'''
# Наибольшее кратное 5 число от введённого
def closest_mod_5(x):
    while(True):
        if x % 5 == 0:
            return x
        else:
            x += 1
'''
###################################################################################
'''
# Вывод количества сочетаний из n по k
def c(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)

n, k = map(int, input().split())
print(c(n, k))
'''
###################################################################################
'''
# Реализация пространств имён
namespaces = {
    'global': {
        'parent': "",
        'vars': []
    }
}


def create_sp(name_sp, parent):
    namespaces[name_sp] = {}
    namespaces[name_sp]['parent'] = parent
    namespaces[name_sp]['vars'] = []


def add_var(name_sp, var):
    namespaces[name_sp]['vars'].append(var)


def get_nsp(name_sp, var):
    name_cur_sp = name_sp
    while True:
        if name_cur_sp == '':
            return None
        elif var in namespaces[name_cur_sp]['vars']:
            return name_cur_sp
        else:
            name_cur_sp = namespaces[name_cur_sp]['parent']

n = int(input())
for i in range(n):
    cmd, name, arg = input().split()
    if cmd == "create":
        create_sp(name, arg)
    if cmd == "add":
        add_var(name, arg)
    if cmd == "get":
        print(get_nsp(name, arg))
    print(namespaces)
'''
###################################################################################
'''
# Реализация класса денежной копилки
class MoneyBox:
    def __init__(self, capasity):
        self.capasity = capasity
        self.money = 0

    def can_add(self, v):
        if (self.capasity - self.money) >= v:
            return True
        else:
            return False

    def add(self, v):
        self.money += v
'''
###################################################################################
'''
class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *args):
        self.data.extend(args)
        while len(self.data) >= 5:
            sum = 0
            for i in range(5):
                sum += self.data.pop(0)
            print(sum)

    def get_current_part(self):
        return self.data
'''
###################################################################################
'''
class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())

    def sub(self):
        # операция вычитания
        self.append(self.pop() - self.pop())

    def mul(self):
        # операция умножения
        self.append(self.pop() * self.pop())

    def div(self):
        # операция целочисленного деления
        self.append(self.pop() // self.pop())
'''
###################################################################################
'''
import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, var):
        super(LoggableList, self).append(var)
        self.log(var)
'''
###################################################################################
# '''
def is_pr_parent(parent, child):
    return parent in classes[child]


def is_parent(parent, child):
    return False

classes = {'B ': ['A'], 'C ': ['A'], 'A': [], 'D ': ['B', 'C']}
'''
n = int(input())
for i in range(n):
    class_str = input().split(':')
    classes[class_str[0]] = []
    if len(class_str) > 1:
        classes[class_str[0]].extend(class_str[1].split())
    else:
        classes[class_str[0]].extend('')
print(classes)
'''
q = int(input())
for i in range(q):
    query = input().split()
    print(is_parent(query[0], query[1]))
# '''