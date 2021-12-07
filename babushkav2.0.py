def add_s(n):
    count = 0
    a = set ()
    name = dict()
    for i in range (n):
        print('Введите учащегося №', i+1, 'Введите 1, чтобы остановить ввод')
        f = True
        try:
            x = input()
            if x == '1':
                print()
                break
            else:
                #вытаскиваем имя и колво баллов
                b = x.split(' ')
                name[b[1]] = b[2]
                k = list(name)
        except Exception as e:
            print('ошибка')
            f = False

        if f == False:
            add_s(n)
    print(count, end = ' ')
    return (name)
#--------------------------------------
#листы
list_1 = set()
list_2 = set()
list_3 = set()
ind = 0
name = dict()
# #цикл ввода

# while ind < 5:
#     print('Введите 1, чтобы ввести олимпиадников по математике')
#     print('Введите 2, чтобы ввести олимпиадников по русскому')
#     print('Введите 3, чтобы ввести олимпиадников по информатике')
#     print('Введите 4, чтобы распечатать все списки')
#     print('Введите 5, чтобы закончить')
#     print('Введите 6, чтобы вывести количество баллов')
#     ind = int(input())

#     if ind == 1:
#         print('Введите количество учащихся:', end = ' ')
#         n = int(input())
#         list_1=add_s(n)
#     elif ind == 2:
#         print('Введите количество учащихся:', end = ' ')
#         n = int(input())
#         list_2=add_s(n)
#     elif ind == 3:
#         print('Введите количество учащихся:', end = ' ')
#         n = int(input())
#         list_3=add_s(n)
#     elif ind == 4:
#         print('Олипиада по математике: ', *list_1, *list_2, *list_3, sep='\t')
#         a = list_1.union(list_2).union(list_3)
#         print('общее количество участников: ', len(a))
#     elif ind == 5:
#         break
#     elif ind == 6:
#         word = input()
#         if word in name.keys():
#             print(name[word])
#     else:
#         print('ошибка ввода')
print(add_s(2))