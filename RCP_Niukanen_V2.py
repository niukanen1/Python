"""
1 - Rock / Камень
2 - Scissors / Ножницы
3 - Paper / Бумага
"""
import random
he = ['r', 's', 'p']
t = int(input('Enter attemps \n'))
d = l = w = 0
for i in range (t):
    y = str(input('Rock - r   \nScissors - s   \nPaper - p \nChoose: '))
    a=random.choice(he) 
    print(a, 'vs', y)
    if a==y:
        print ('Draw!')
        d+=1
#Rock vs Scissors        
    elif y=='r' and a=='s':
         print ('You won!')
         w+=1
#Scissors vs Paper
    elif y=='s' and a=='p':
        print ('You won!')
        w+=1
#Paper vs Rock
    elif y=='p' and a=='r':
         print ('You won!')
         w+=1
    else:
        print('Loser')
        l+=1
    t-=1
print('Victories:' +str(w), '\nDraws:' +str(d), '\nFailure:' +str(l)) 
