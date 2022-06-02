import time  # import time for measure time it took to execute function


def iter_fib(n):
    assert n >= 0  # check if number not negative
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


start = time.time()
print(iter_fib(40))
end = time.time()
print(end - start)  # It will take nearly 0.0001 sec to find fib number

start = time.time()
print(iter_fib(8000))
end = time.time()
print(end - start)  # It will take nearly 0.002 sec to find fib number
