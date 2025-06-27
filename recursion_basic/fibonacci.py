def fib(N):
    if N<=1:
        return N

    a = fib(N-1)
    b = fib(N-2)
    return a+b


print(fib(4))