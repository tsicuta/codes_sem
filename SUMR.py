import random
a = [random.randint(100, 1000) for i in range (1,11)]
print (a)
print()

a = list('pyton')
print (a)
print()

a = list(input())
print (a)
print()

a = [random.randint(-10, 10) for i in range (1,21)]
print(a)
s = 0
count_plus = 0
count_min = 0
for i in range (1,20):
    s = s + int(a[i])
    if (int(a[i]) > 0):
        count_plus += int(a[i])
    elif (int(a[i]) < 0):
        count_min += int(a[i])
print ('Сумма всех чисел: ', s) 
print ('Сумма чисел меньше 0: ', count_min)
print ('Сумма чисел больше 0: ', count_plus)
print()

a = [random.randint(-10, 10) for i in range (1,21)]
print (a)
f = 0
for i in range (1,20):
    if int(a[i]) == i:
        f += int(a[i])
print ('Сумма чисел равных своему порядковому номеру: ', f)

