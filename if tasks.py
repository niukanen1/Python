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
a = int(input('Enter the year number')
if a%4== 0 :
    print('This is the leap year')
else:
    print ('TH')
