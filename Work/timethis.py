import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time}")
        return func_result

    return wrapper
