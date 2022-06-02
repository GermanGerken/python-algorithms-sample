import time  # import time for measure time it took to execute function

cache = {}  # Create global Cache


def rec_fib_cached(n):
    assert n >= 0  # check if number not negative
    if n not in cache:
        cache[n] = n if n <= 1 else rec_fib_cached(n - 1) + rec_fib_cached(n - 2)
    return cache[n]


start = time.time()
print(rec_fib_cached(40))
end = time.time()
print(end - start)  # It will take nearly 0.0003 sec to find fib number

#comment line bellow before run
print(rec_fib_cached(8000))  # will cause an error, hit the limit of recursion
