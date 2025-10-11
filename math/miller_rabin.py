def miller_rabin(n):
    if n < 2: return False
    if n != 2 and n%2==0: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n!=p and n%p == 0:
            return False
        
    base = [2,325,9375,28178,450775,9780504,1795265022] #64bit
    d = (n-1)
    s = 0
    while d%2 == 0:
        d //= 2
        s += 1
    for a in base:
        if a % n == 0:
            continue
        x = pow(a,d,n)
        if x == 1 or x == n-1:continue
        
        composite = True
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                composite = False
                break
        if composite:return False
    return True