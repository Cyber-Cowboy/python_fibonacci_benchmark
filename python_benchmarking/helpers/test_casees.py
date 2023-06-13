import numpy as np

def slow_fibonacci(n):
    if n in (1,2):
        return 1
    return slow_fibonacci(n-2) + slow_fibonacci(n-1)

def cache_fibonacci(n):
    cache ={0:0, 1:1}
    def inner_fibonacci(n):
        if n in cache:
             return cache[n]
        cache[n] = inner_fibonacci(n - 1) + inner_fibonacci(n - 2)  # Recursive case
        return cache[n]
    return inner_fibonacci(n)

def oop_fibonacci(n):
    class Fibonacci:
        def __init__(self):
            self.cache = [0, 1]

        def __call__(self, n):
            # Validate the value of n
            if not (isinstance(n, int) and n >= 0):
                raise ValueError(f'Positive integer number expected, got "{n}"')

            # Check for computed Fibonacci numbers
            if n < len(self.cache):
                return self.cache[n]
            else:
                # Compute and cache the requested Fibonacci number
                fib_number = self(n - 1) + self(n - 2)
                self.cache.append(fib_number)

            return self.cache[n]
    return Fibonacci()(n)

def itterative_fibonacci(n):
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number

def chad_fibonacci(n):
    phi = (1 + 5**.5) / 2
    psi = (1 - 5**.5) / 2
    return (phi**n - psi**n) / 5**.5