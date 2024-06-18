def check_prime(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def numrange(x, y):
    for i in range(x, y + 1):
        yield i


x1 = int(input('enter a number: '))
x2 = int(input('enter a number: '))
it = numrange(x1, x2)
for i in it:
    if check_prime(i):
        print('primes', i)