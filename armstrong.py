def checkArmstrong(n):
    length = 0
    temp = n
    while temp > 0:
        temp = temp//10
        length += 1
    
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10

    if(sum == n):
        print('{} is armstrong'.format(n))
    else:
        print('{} is not armstrong'.format(n))
    pass

n = input('Enter number to check armstrong')
print(checkArmstrong(n))