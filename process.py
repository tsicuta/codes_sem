count = 0
a = set ()
name = [ ]
#Фамилия Имя 10.split()
#[Фамилия, Имя, 10]

#ввод: ФИО баллы  // вывод: №_И_Б
print('Введите учащегося №', 'Введите 1, чтобы остановить ввод')
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
        name = b[0]
        kolvo = b[2]

except Exception as e:
    print('ошибка') #you died, try again?

print(name[0],'_', kolvo, end = '')