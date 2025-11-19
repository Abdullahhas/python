import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]

        res = func(*args)
        cache_value[args] = res
        return res
    return wrapper

@cache
def long_running_fun (a , b):
    time.sleep(4)
    return a + b


print(long_running_fun(2,3))
print(long_running_fun(2,3))