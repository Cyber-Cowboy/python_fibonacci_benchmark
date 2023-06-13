import sys
from helpers.test_utils import measure
from helpers.test_casees import slow_fibonacci, cache_fibonacci, oop_fibonacci, itterative_fibonacci, chad_fibonacci


@measure
def benchmark_a_slow_fibonacci(x, n):
    for i in range(x):
        slow_fibonacci(n)

@measure
def benchmark_a_cache_fibonacci(x, n):
    for i in range(x):
        cache_fibonacci(n)

@measure
def benchmark_an_oop_fibonacci(x, n):
    for i in range(x):
        oop_fibonacci(n)

@measure
def benchmark_an_itterative_fibonacci(x, n):
    for i in range(x):
        itterative_fibonacci(n)

@measure
def benchmark_a_chad_fibonacci(x, n):
    for i in range(x):
        chad_fibonacci(n)


if __name__ == "__main__":
    print(f"Current Python version is: {sys.version}")
    benchmark_a_slow_fibonacci(10**2, 30)
    benchmark_a_cache_fibonacci(10**6, 30)
    benchmark_an_oop_fibonacci(10**6, 30)
    benchmark_an_itterative_fibonacci(10**7, 30)
    benchmark_a_chad_fibonacci(10**7, 30)