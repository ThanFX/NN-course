import numpy as np

'''
# Создали массив 4х3 из двух единичных, преобразовали в вертикальный вектор
mat = (np.eye(3, 4) * 2) + (np.eye(3, 4, 1))
mat = mat.reshape((12, 1))
print(mat)
'''

'''
# Считали размерность массива и сам массив (2 раза). Вывели X*транспонированный Y (или предупредение при несовпадении размерностей)
a_shape = tuple(map(int, input().split()))
A = np.fromiter(map(int, input().split()), np.int).reshape(a_shape)
b_shape = tuple(map(int, input().split()))
B = np.fromiter(map(int, input().split()), np.int).reshape(b_shape)

if a_shape[1] != b_shape[1]:
    print("matrix shapes do not match")
else:
    print(A.dot(B.T))
'''

'''
# Сформировали массив из csv, вывели среднее по столбцам
from urllib.request import urlopen
f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')

sbux = np.loadtxt(f, skiprows=1, delimiter=",")
print(sbux.mean(axis=0))
'''

'''
# Расчёт коэффициентов линейной регрессии матричным способом
# (единичный первый столбец нужен для свободного коэффициента)

y = np.array([[60], [50], [75]])
x = np.array([[1, 10], [1, 7], [1, 12]])
b = (np.linalg.inv(x.T.dot(x))).dot(x.T.dot(y))

print((np.linalg.inv(x.T.dot(x))).dot(x.T.dot(y)))
print()
print()
'''

import urllib
from urllib import request

f = urllib.request.urlopen("https://stepic.org/media/attachments/lesson/16462/boston_houses.csv")  # open file from URL
x = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

y = x.copy()[..., 0:1]
x[..., 0:1] = 1
b = (np.linalg.inv(x.T.dot(x))).dot(x.T.dot(y))

for beta in b:
    print(*beta, end=' ')
