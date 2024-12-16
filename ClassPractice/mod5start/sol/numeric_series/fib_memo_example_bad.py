def fib(k, solved):
    if k in solved:
        return solved[k]
    
    solved[k] = fib(k-1, solved) + fib(k-2, solved)

    return solved[k]

fib(5, {0:0, 1:0})