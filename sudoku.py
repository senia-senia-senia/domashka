import random
flag = 1
while flag == 1:
    f= open("output2.txt", "w")
    i = 0
#Формирование таблицы кодировок
    x = ['Камень' , 'Ножницы' , 'Бумага']
    while i < 3:
            c = '+' + '-' + '+' + 8* '-' + '+'
            print(c)
            print("|%1s|%7s |"%(i,x[i]))
            print(c)
            i +=1
    print('Вам предоставлены кодирови 3-х элементов данной игры. Выберите одну из них, чтобы сразиться с программой')
#Ввод игроком своей кодировки
    T = True
    while T == True:
        try:
            vvod = input()
            vvod = int(vvod)
            while T == True:
                if (vvod <2 ) and (vvod > 0  ):
                   pass 
                else:
                    print('Неверная кодировка!')
                break
        except ValueError:
            print('Вероятно вы ввели неправильную кодировку, попробуйте ещё разок!')
        
        

    Kd = random.randint(0, 2) 
    result = 0

    if ((vvod == 0)and(Kd== 1))or ((vvod == 1)and(Kd==2)) or ((vvod ==2)and(Kd==0)):
        result = 'Вы победили'
    elif ((vvod ==1)and(Kd==0)) or((vvod ==2)and(Kd==1)) or ((vvod ==0)and(Kd==2)):
        result = 'Вы проиграли'
    elif Kd==vvod:
        result = 'Вы сыиграли в ничью'

#Замена Кодировок на игровые слова
    if Kd == 0:
        Kd = 'Камень'
    elif Kd == 1:
        Kd = 'Ножницы'
    elif Kd == 2:
        Kd = 'Бумага'

    if vvod == 0:
        vvod = 'Камень'
    elif vvod == 1:
        vvod = 'Ножницы'
    elif vvod == 2:
        vvod = 'Бумага'

#Вывод результата в файл
    print(vvod, '<<<>>>', Kd, file = f)
    print(result, file = f)

    f.close()

    print('Результат игры ищите в папке "output2.txt"')
    print("Вы хотите еще раз запустить программу? (y/n)")
    mmm = True
    while mmm == True:
        h = input()                                             
        if h == 'y':
            mmm = False
        elif h == 'n':
            mmm = False
            flag = 0
        elif (h != 'y') and (h != 'n'):
            print("Вы ввели неверное значение! Пробуйте еще раз!")
