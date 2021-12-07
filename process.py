count = 0
a = set ()
name = dict()
#Фамилия Имя 10.split()
#[Фамилия, Имя, 10]
count +=1
#ввод: ФИО баллы  // вывод: №_И_Б
print('Введите учащегося №', count, 'Введите 1, чтобы остановить ввод')
try:
    x = input()
    if x == '1':
        print()
    else:
        #забиваем список
        set.add (a, x)

        #вытаскиваем имя и колво баллов
        b = x.split(' ')
        print(b)
        name[b[0]] = b[2]

except Exception as e:
    print('ошибка') #you died, try again?

print(count, '_', name, end = '')