import random
znak = list()
stroka=1
m = []
n = []
a = open("input2.txt","r+")
f= open("output2.txt", "w+")
print( "Введите количество игр, которые вы хотите сыграть за один раз (до 50)")
print('Компьютер <===> Вы', file = f)
for znak in a:
    while znak:
        znak.replace('Ножницы','2')
        znak.replace('Бумага','3')
        znak.replace('Камень','1')    
        print(znak, file = f)
        '''Kd = random.randi(1, 3)
        if Kd == 1:
            Kd = u'Камень'
        elif Kd == 2:
            Kd = u'Ножницы'
        elif Kd == 3:
            Kd = u'Бумага'
        if Kd == znak:
            m = Kd + '===>' + znak + 'Ничья'
            print(m, file = f)
            
        m = Kd + '===>' + znak
        print(m, file = f)
        
        stroka +=1'''
        break
    


a.close()
f.close()
