import time  # import time for measure time it took to execute function


def rec_fib(n):
    assert n >= 0  # check if number not negative
    return n if n <= 1 else rec_fib(n - 1) + rec_fib(n - 2)  # returning fib number counted from recursion


start = time.time()
print(rec_fib(40))
end = time.time()
print(end - start)  # It will take nearly 22 sec to find fib number
