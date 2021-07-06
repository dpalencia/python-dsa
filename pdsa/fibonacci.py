# Fibonacci numbers. Recursive method and dynamic programming method
import unittest

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)


fib_list = {0: 0, 1 : 1}
def fibonacci_dynamic(i):
    if i == 0 or i == 1:
        return fib_list[i]
    else:
        if not i in fib_list:
            fib_list[i] = fibonacci_dynamic(i - 1) + fibonacci_dynamic(i - 2)
        return fib_list[i]

def fibonacci_three_var(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    c = a + b
    # We want to repeat 49 times
    for repeat in range(2, n):
        a = b
        b = c
        c = a + b
    return c

if __name__ == "__main__":
    unittest.main()