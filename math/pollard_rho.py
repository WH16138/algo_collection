import random
import math

def pollard_rho(n):
    if n%2==0:return 2

    def f(x,c,n):return (x**2+c) % n
    
    while True:
        y = random.randrange(1,n)
        c = random.randrange(1,n)

        m = 128
        r = 1
        q, g = 1, 1

        x = y
        y = (y*y+c) % n
        while g == 1:
            x = y
            for i in range(1,r):y = f(y,c,n)
            k = 0
            while k < r and g == 1:
                ys = y
                lim = min(m, r-k)
                for i in range(1,lim):
                    y = f(y,c,n)
                    q = (q*abs(x-y))%n
                g = math.gcd(q,n)
                k += lim
            r *= 2

        if g == n:
            g = 1
            while g == 1:
                ys = f(ys,c,n)
                g = math.gcd(abs(x-ys), n)
        
        if g > 1 and g < n:
            return g