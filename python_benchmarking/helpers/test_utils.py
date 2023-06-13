import time

def measure(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Time of {func.__name__} executions: {end-start}")
    return wrapper
    
    