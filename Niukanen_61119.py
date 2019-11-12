#Task 1
a=int(input('Enter the first number \n'))
b=int(input('Enter the second number \n'))
if a > b:
    print('a = ', a, 'is more than b = ', b,)
elif a == b:
    print('Numbers are the same')
else:
    print('b = ', b, 'is more than a = ', a)
    
    
#Task 2
x = int(input('Enter x \n'))
if x > 0:
    sign = 1
elif x==0:
    sign = 0
else:
    sign = -1
print('sign(x) is ',x)


#Task 3
x1 = int(input('Enter the string number for the first cell (1-8) \n')) 
y1 = int(input('Enter the coloumn number for the first cell (1-8) \n'))   
x2 = int(input('Enter the string number for the second cell (1-8) \n'))
y2 = int(input('Enter the coloumn number for the second cell (1-8) \n')) 
if (x1+y1+x2+y2)%2==0:
    print('Yes, they have the same color')
else:
    print('They have different colors')
    

#Task 4
year=int(input('Enter the year number \n'))
if year%4==0 and (year%100!=0 or year%400==0):
    print ('This is the leap year')
else:
    print ('This is not a leap year')
  
    
#Task 5
a = int(input('Enter the firt number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
max = 0
if a>b and c>b:\
    print(b, ' is the lowest number')
elif b>a and c>a:
    print (a, ' is the lowest number')
else:
    print(c, ' is the lowest number')
    
    
#Task 6
a = int(input('Enter the firt number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
if a==b and a==c:
    print('3')
elif a==b or a==c or c==b:
    print ('2')
else:
    print('0')
    
    
#Task 7    
x1 = int(input('Enter the string number for the first cell (1-8) \n')) 
y1 = int(input('Enter the coloumn number for the first cell (1-8) \n'))   
x2 = int(input('Enter the string number for the second cell (1-8) \n'))
y2 = int(input('Enter the coloumn number for the second cell (1-8) \n')) 
if x1==x2 or y1==y2:
    print('Yes')
else:
    print('No')


#Task 8
x1 = int(input('Enter the string number for the first cell (1-8) \n')) 
y1 = int(input('Enter the coloumn number for the first cell (1-8) \n'))   
x2 = int(input('Enter the string number for the second cell (1-8) \n'))
y2 = int(input('Enter the coloumn number for the second cell (1-8) \n')) 
if x1==x2-1 and y1==y2-1 :
    print('Yes')
else:
    print('No')


#Task 9

x1 = int(input('Enter the string number for the first cell (1-8) \n')) 
y1 = int(input('Enter the coloumn number for the first cell (1-8) \n'))   
x2 = int(input('Enter the string number for the second cell (1-8) \n'))
y2 = int(input('Enter the coloumn number for the second cell (1-8) \n')) 
if abs(x1-x2)==abs(y1-y2): #abs - module
    print('Yes')
else:
    print('No')


#Task 10
x1 = int(input('Enter the string number for the first cell (1-8) \n')) 
y1 = int(input('Enter the coloumn number for the first cell (1-8) \n'))   
x2 = int(input('Enter the string number for the second cell (1-8) \n'))
y2 = int(input('Enter the coloumn number for the second cell (1-8) \n')) 
if  (x1==x2 or y1==y2) or abs(x1-x2)==abs(y1-y2) :
    print('Yes')
else:
    print('No')


#Task 11
x1 = int(input('Enter the string number for the first cell (1-8) \n'))
y1 = int(input('Enter the coloumn number for the first cell (1-8) \n'))
x2 = int(input('Enter the string number for the second cell (1-8) \n'))
y2 = int(input('Enter the coloumn number for the second cell (1-8) \n'))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Yes')
else:
    print('No')


#Task 12
n=int(input('Choose length: '))
m=int(input('Choose width: '))
k=int(input('Choose amount lobules: '))
if (n*m) > k and (k%n==0) or (k%m==0):
   print('Yes')
else:
   print('No')


#Задача про Яшу
N = int(input("Введите длину бассейна: "))
M = int(input("Введите ширину бассейна: "))
x = int(input("Введите расстояние от длинного бортика: "))
y = int(input("Введите расстояние от короткого бортика: "))
if x<=N//2 and y<=M//2:
    if x<y:
        print("Минимально он должен проплыть: ", x)
    else:
        print("Минимально он должен проплыть: ", y)
elif x>N//2 and y<M//2:
    if (N-x)<y:
        print("Минимально он должен проплыть: ", N-x)
    else:
        print("Минимально он должен проплыть: ", y)
elif x>N//2 and y>M//2:
    if N-x<M-y:
        print("Минимально он должен проплыть: ", N-x)
    else:
        print("Минимально он должен проплыть: ", M-y)
elif x<N//2 and y>M//2:
    if x<M-y:
        print("Минимально он должен проплыть: ", x)
    else:
        print("Минимально он должен проплыть: ", M-y)  
       

#Задача на ставку
import random
wins = 0
print("Ставочник 2019");print("____"*15)
comp_choice = random.randint(1,50)
game_count = int(input("Сколько раз вы хотите играть? : "))
game_played = 0
while game_played < game_count:
    x = int(input("Введите число от 1 до 50: "));print("")
    game_played += 1
    if x == comp_choice:
       print("Ставка сыграла!")
       input("Введите 1, чтобы продолжить или 2, что закончить: ")
       
    else:
        continue
print('Выбранное ПК число'comp_choice)








