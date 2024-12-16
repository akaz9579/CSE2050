import time

def time_func(func, *args):

    min_time = float('inf')

    for x in range(10):
        start = time.time()
        func(*args)
        end = time.time()
        t = end - start
        
        if t < min_time:
            min_time = t

    return min_time

def double(x): return x*2

print(time_func(double, ("black", "nigga", "niger", "niggas")))




