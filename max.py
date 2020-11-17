length = input('How many numbers you want to add for comparision ? ')
nList = []
for i in range(0,length):
    x = input('Enter number {} - '.format(i+1))
    nList.append(x)

max = nList[0]
min = nList[0]
for n in nList:
    #maximum
    if(n > max):
        max = n
    
    #minimum
    if(n < min):
        min = n

print('{} is maximum and {} is minimum out of {}'.format(max,min,nList))