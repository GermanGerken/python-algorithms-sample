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


def euclid_gcd(a, b):
    assert a >= 0 and b >= 0
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

print(test(euclid_gcd))