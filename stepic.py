'''
# Задачи ко второй неделе https://stepic.org/lesson/Задачи-по-материалам-недели-3369
lis = sorted([int(i) for i in input().split()])
i = 0
out = ''
while i < len(lis):
    if lis.count(lis[i]) > 1:
       out += (str(lis[i]) + ' ')
    i += lis.count(lis[i])
print(out.strip())

###############################################################

sum = 0
sum_sqr = 0
while True:
    i = int(input())
    sum += i
    sum_sqr += (i ** 2)
    if sum == 0:
        print(sum_sqr)
        break

###################################################################

n = int(input())
i = 1
count = 0
out = ''
while count < n:
    for j in range(0, i):
        out += (str(i) + ' ')
        count += 1
        if count == n:
            break
    i += 1
print(out.strip())

####################################################################

lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
else:
    j = 0
    out = ''
    for i in lst:
        if i == x:
            out += (str(j) + ' ')
        j += 1
    print(out.strip())

####################################################################

st = input()
array = []
array_out = []

while st != 'end':
    array.append([int(i) for i in st.split()])
    st = input()

for i in range(len(array) - 1):
    str_out = []
    for j in range(len(array[i]) - 1):
        str_out.append(array[i-1][j] + array[i+1][j] + array[i][j-1] + array[i][j+1])
    j = len(array[len(array) - 1]) - 1
    str_out.append(array[i - 1][j] + array[i + 1][j] + array[i][j - 1] + array[i][0])
    array_out.append(str_out)
i = len(array) - 1
str_out = []
for j in range(len(array[i]) - 1):
    str_out.append(array[i - 1][j] + array[0][j] + array[i][j - 1] + array[i][j + 1])
j = len(array[len(array) - 1]) - 1
str_out.append(array[i - 1][j] + array[0][j] + array[i][j-1] + array[i][0])
array_out.append(str_out)

for i in range(len(array_out)):
    for j in range(len(array_out[i])):
        print(array_out[i][j], end=' ')
    print()

####################################################################

# Заполнение матрицы по спирали по часовой стрелке
n = int(input())
array = [[0 for j in range(n)] for i in range(n)]

# Инициализирум итераторы для внешнего "кольца"
nn = n
num = 1
start = 0
end = n - 1

# Перебираем "кольца" массива
for step in range(n // 2):
# Пробегаем по каждой стороне "кольца" от первой до предпоследней ячейки
    for i in range(start, end):
# Магия с расчётом значения ячейки от её положения и от номера кольца
        array[step][i] = num + i - step
        array[i][n - step - 1] = num + nn + i - 1 - step
        array[n - step - 1][end - i + step] = num + (2 * nn) + i - 2 - step
        array[end - i + step][step] = num + (3 * nn) + i - 3 - step
# Изменяем набор значений для следующего кольца
    num += (4 * nn - 4)
    start += 1
    end -= 1
    nn -= 2

# Для нечётного n заполняем серединку
if n % 2 == 1:
    array[n // 2][n // 2] = n ** 2

# Выводим на экран
for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print()

####################################################################

def f(x):
    if x <= -2:
        ret = 1 - ((x + 2) ** 2)
    elif x <= 2:
        ret = -(x / 2)
    else:
        ret = 1 + ((x - 2) ** 2)
    return ret


print(f(4.5))
print(f(-4.5))
print(f(1))

####################################################################


def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 != 0:
            l.pop(i)
        else:
            l[i] //= 2
            i += 1


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)




words = [i.lower() for i in input().split()]
dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for key, value in dictionary.items():
    print(key, value)


####################################################################

max_count = 0
dictionary = {}
with open('dataset_3363_3.txt', 'r') as inf:
    for line in inf:
        line = line.strip().lower()
        for word in line.split():
            if word in dictionary:
                dictionary[word] += 1
                if dictionary[word] > max_count:
                    max_count = dictionary[word]
            else:
                dictionary[word] = 1

max_len_words = []
for key, value in dictionary.items():
    if value == max_count:
        max_len_words.append(key)

min_word = max_len_words[0]
for i in max_len_words:
    if min_word > i:
        min_word = i

with open('file_out.txt', 'w') as ouf:
    ouf.write(min_word + ' ' + str(max_count))

####################################################################

marks = []
with open('dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        mark = [str(word) for word in line.split(';')]
        marks.append(mark)

math_mark = 0
phys_mark = 0
russ_mark = 0
with open('file_out.txt', 'w') as ouf:
    for mark in marks:
        avg_mark = (float(mark[1]) + float(mark[2]) + float(mark[3])) / 3
        ouf.write(str(avg_mark) + '\n')
        math_mark += float(mark[1])
        phys_mark += float(mark[2])
        russ_mark += float(mark[3])
    ouf.write(str(math_mark / len(marks)) + ' ' + str(phys_mark / len(marks)) + ' ' + str(russ_mark / len(marks)))


####################################################################

import math
r = float(input())
print(2 * r * math.pi)

####################################################################

import sys
for param in range(1, len(sys.argv)):
    print(sys.argv[param], end=' ')

####################################################################

import requests
url = ''
with open('dataset_3378_2.txt', 'r') as inf:
    url = inf.readline().strip()

res = requests.get(url).text.splitlines()
print(len(res))

####################################################################


import requests
url = ''
with open('dataset_3378_3.txt', 'r') as inf:
    url = inf.readline().strip()

count = 1
res = requests.get(url).text.splitlines()
while res[0].find('We') != 0:
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + res[0]
    print(res, url, count)
    count += 1
    res = requests.get(url).text.splitlines()

for i in res:
    print(i)

'''
