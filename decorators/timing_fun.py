import time

def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        res = func(*args , **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start}")
        return res
    return wrapper

@timer
def examplefun(n):
    time.sleep(n)

examplefun(2)