def productFib(prod):
    current_value = 0
    x = 0
    fib1 = fib2 = 0

    while current_value < prod:
        x += 1
        fib1 = fib(x)
        fib2 = fib(x + 1)
        current_value = fib1 * fib2

    if current_value == prod:
        return [fib1, fib2, True]

    return [fib1, fib2, False]


def fib(n):
    a,b = 1,1

    for i in range(n-1):
        a,b = b,a+b

    return a
