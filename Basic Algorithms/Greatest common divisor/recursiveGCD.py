import random


def test(func, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert func(a, a) == func(a, 0) == a
        assert func(b, b) == func(b, 0) == b
        assert func(a, 1) == func(b, 1) == 1
        d = func(a, b)
        assert a % d == b % d == 0


def rec_gcd(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return rec_gcd(a % b, b)
    elif b >= a:
        return rec_gcd(a, b % a)

print(test(rec_gcd))