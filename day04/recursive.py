def calc(n):
    result = 0
    print(n)
    if n / 2 > 1:
        result = calc(n/2)
    return result


#print(calc(100))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


# print(fact(5))

def fibo(n1, n2):
    if n1 == 0:
        print(n1)
        print(n2)
    n3 = n1 + n2
    print(n3)
    if n3 < 100:
        fibo(n2, n3)

fibo(0,1)
