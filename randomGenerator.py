import random

def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def randomizeParam():
    m = random.randint(101, 205)
    c = random.randint(2, m-1)

    while gcd(m, c) != 1 :
        c = random.randint(2, m - 1)

    primfac = primes(m)

    if len(primfac) != 0 :
        tmp = 1
        for item in primfac :
            tmp = lcm(tmp, item)

        if m % 4 == 0:
            tmp *= 4

        a = tmp + 1
    else :
        a = random.randint(1, 10)

    seed = random.randint(1, 5)

    return a, c, m, seed