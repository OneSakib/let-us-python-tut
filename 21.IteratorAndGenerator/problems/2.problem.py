def isprime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return True
        for i in range(2, n//2):
            if n % i == 0:
                return False
        else:
            return False
    return False


def generate_primes():
    num = 1
    while True:
        if isprime(num):
            yield num
        num += 1


total = 0
for next_prime in generate_primes():
    if next_prime < 300000:
        total += next_prime
    else:
        print(total)
        exit()
