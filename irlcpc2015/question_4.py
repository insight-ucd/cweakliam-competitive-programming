def is_prime(n):
    if n < 2:
        return False

    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def gen_primes_lteq(n):
    return filter(is_prime, range(n + 1))


list_101s = [101]

def gen_101s():
    i = 0
    while True:
        if i < len(list_101s):
            yield list_101s[i]
            i += 1
        else:
            list_101s.append(list_101s[-1] * 100 + 1)


def num_digits(n):
    return len(str(n))


def w(p):
    for n in gen_101s():
        if n % p == 0:
            return num_digits(n)

def ans(n):
    return len([p for p in gen_primes_lteq(n) if p not in [2, 5] and w(p) == p - 2])

print ans(int(raw_input()))

