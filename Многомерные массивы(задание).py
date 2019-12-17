
#11111111111111
import numpy as np
n = int(input('Strings: '))
m = int(input('Elements: '))
a = np.random.randint(1,10, size = (n, m))
print(a)
max = a [0][0]
for i in range (n):
    for j in range (m):
        if a[i][j] > max:
            max = a[i][j]
            b_i, b_j = i, j
print(b_i,b_j)

#222222222222
n = int(input('Matrix: '))
b_a = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or (n-j==i+1):
            b_a[i][j] = '*'
        elif i == n//2:
            b_a[i][j] = '*'
        elif j == n//2:
            b_a[i][j] = '*'
for i in range (len(b_a)):
    print()
    for j in range (len(b_a)):
       print(b_a[i][j], end = ' ')

#######33333333
n, m =[int(i) for i in input().split()]
a = [['*'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2 == 0:
            a[i][j] = '.'
for i in range (n):
    print()
    for j in range (m):
        print(a[i][j], end = ' ')

#44444444444444444
n = int(input('Matrix: '))
b_a = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        c=0
        while c < n:
            if (i+c == j) or (i-c == j):
                b_a[i][j] = c
            c+=1
for i in range (n):
    print()
    for j in range (n):
       print(b_a[i][j], end = ' ')

#####55555555555
n = int(input('Matrix: '))
a = [['0'] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for i in a:
    for j in i:
        print(j, end=' ')
    print()


###666666666666666666666
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
n, m = [int(i) for i in input('Elements and Strings').split()]
a = [[int(j) for j in input('el').split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(a, i, j)
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))

