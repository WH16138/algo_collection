# =======================================
# Euler's Totient Function (φ function)
# ---------------------------------------
# Description:
#   For a given positive integer n, the Euler's Totient function φ(n)
#   returns the count of integers from 1 to n that are coprime with n.
#
#   This implementation uses the formula:
#     φ(n) = n × Π (1 - 1/p) for each distinct prime factor p of n
#
# Time Complexity:
#   - Sieve of Eratosthenes: O(√n log log √n)
#   - Factorization and phi computation: O(√n)
#   => Overall: O(√n log log n)
#
# Constraints:
#   - Efficient for n up to around 10^12
#   - Requires enough memory to store primes up to √n
# =======================================

def sieve_of_eratosthenes(limit):
    """
    Generates all prime numbers up to 'limit' using the Sieve of Eratosthenes.
    Returns:
        A list of prime numbers ≤ limit.
    """
    prime = [1] * (limit + 1)
    prime[0] = prime[1] = 0  # 0 and 1 are not prime
    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = 0
        p += 1
    return [i for i, is_prime in enumerate(prime) if is_prime]

def euler_phi(n):
    """
    Computes Euler's Totient Function φ(n).
    Args:
        n (int): The input integer (n ≥ 1)
    Returns:
        int: The value of φ(n)
    """
    result = 1
    for p in sieve_of_eratosthenes(int(n**0.5) + 1):
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            result *= p**a - p**(a - 1)
    if n > 1:
        # n is a remaining prime factor larger than √original_n
        result *= n - 1
    return result

# =======================================
# Example Usage
# =======================================

if __name__ == "__main__":
    # Example 1
    print("φ(9) =", euler_phi(9))    # Output: 6
    # Explanation: 1, 2, 4, 5, 7, 8 are coprime with 9

    # Example 2
    print("φ(36) =", euler_phi(36))  # Output: 12
    # Prime factors of 36: 2^2 × 3^2
    # φ(36) = (2^2 - 2^1) × (3^2 - 3^1) = 4 - 2 = 2 × (9 - 3 = 6) = 12

    # Example 3
    print("φ(1000000000039) =", euler_phi(1000000000039))
    # If n is a prime, φ(n) = n - 1
