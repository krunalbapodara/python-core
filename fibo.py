def fibo(n):
    a = 0
    b = 1
    c = 0
    while c <= n:
        print(a)
        x = a + b
        a = b
        b = x
        c += 1
print(fibo(20))
