def add_s(n):
    count = 0
    a = set ()
    name = [ ]
    for i in range (n):
        print('Введите учащегося №', i+1, 'Введите 1, чтобы остановить ввод')
        f = True
        try:
            x = input()
            if x == '1':
                print()
                break
            else:
                #забиваем список
                set.add (a, x)

                #вытаскиваем имя и колво баллов
                b = x.split(' ')
                print(b)
                name = b[0]
                kolvo = b[2]
        except Exception as e:
            print('ошибка')
            f = False
        if f == False:
            add_s(n)

    print(count)
    print(*a, sep=', ')
    return (a)

#листы
list_1 = set()
list_2 = set()
list_3 = set()
ind = 0
#цикл ввода

while ind < 5:
    print('Введите 1, чтобы ввести олимпиадников по математике')
    print('Введите 2, чтобы ввести олимпиадников по русскому')
    print('Введите 3, чтобы ввести олимпиадников по информатике')
    print('Введите 4, чтобы распечатать все списки')
    print('Введите 5, чтобы закончить')
    ind = int(input())

    if ind == 1:
        print('Введите количество учащихся:', end = ' ')
        n = int(input())
        list_1=add_s(n)
    elif ind == 2:
        print('Введите количество учащихся:', end = ' ')
        n = int(input())
        list_2=add_s(n)
    elif ind == 3:
        print('Введите количество учащихся:', end = ' ')
        n = int(input())
        list_3=add_s(n)
    elif ind == 4:
        print('Олипиада по математике: ', *list_1, *list_2, *list_3, sep='\t')
        a = list_1.union(list_2).union(list_3)
        print('общее количество участников: ', len(a))
    elif ind == 5:
        break
    else:
        print('ошибка ввода')

