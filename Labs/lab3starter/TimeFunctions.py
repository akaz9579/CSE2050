import time

def time_function(func, args, n_trials = 10):
    """Returns amount of time it takes for a function to run"""
    

    start = time.time()
    func(args)
    end = time.time()
    min_run = end-start

    for i in range(n_trials-1):
        start = time.time()
        func(args) 
        end = time.time() 
        total_Time = end-start
       
        if total_Time < min_run:
            min_run = total_Time

    return min_run
    
    

def time_function_flexible(func, args, n_trials = 10):
    """Add your own docstring here"""

    start = time.time()
    func(*args)
    end = time.time()
    min_run = end-start

    for i in range(n_trials-1):
        start = time.time()
        func(*args) 
        end = time.time() 
        total_Time = end-start
       
        if total_Time < min_run:
            min_run = total_Time

    return min_run



if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    def foo(f, args): return f(*args)

    def add_2_nums(p1, p2): return p1 + p2

    def add_3_nums(p1, p2, p3): return p1+p2+p3
    
    def add_4_nums(p1, p2, p3,p4): return p1+p2+p3+p4


    #L1 =  [i for i in range(10**5)]
    #t1 = time_function(test_func, L1)

   # L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    #t2 = time_function(test_func, L2)

    f1 = foo(add_2_nums, (3, 4))
    f2 = foo(add_4_nums, (3, 4, 5,3))
    
    print(f2)

   # print("t(L1) = {:.3g} ms".format(t1*1000))
   # print("t(L2) = {:.3g} ms".format(t2*1000))


