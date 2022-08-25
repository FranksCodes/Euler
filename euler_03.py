#Print factors and prime factors of a given number.
print('Welcome! Input a number and the program will tell you its factors and prime factors.')
num=input('Input a number:')
n=int(num)
lstf=[]
lstp=[]

#print factors of input number in a list
for fac in range(1, n):
    if n%fac == 0:
        lstf.append(fac)
print('The factors of', num, 'are:\n', lstf)

#select prime factors from list of factors
for x in lstf:
    #skip 0-2
    if x <= 2:
        continue
    #divide list members by all number from 2 to half their value
    for d in range(2, x//2+1):
        #test if number in x is divisible by d
        if x%d == 0:
            break
    #add non-divisible numbers to lstp
    else:
        lstp.append(x)
print('The prime factors of', num, 'are:\n', lstp)
