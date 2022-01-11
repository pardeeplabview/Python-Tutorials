num = int(input('Enter a number'))
b1 = bool(int(input('Enter 1 or 0')))
count= num
if b1 == True:
    for i in range(num+1):
        for j in range(i):
            print('*',end= ' ')
        print('')
else:
    for i in range(num+1):
        for j in range(count):
            print('*',end= ' ')
        print('')
        count-=1