def seive_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

# test
if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline().strip())
    primes = seive_of_eratosthenes(N)
    print(" ".join(map(str, primes)))
    # Example usage: python temp/test.py < input.txt
    # where input.txt contains a single integer N