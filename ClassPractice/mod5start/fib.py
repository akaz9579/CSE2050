def fib(k):
    """Returns the nth fibonacci number"""
    if k == 0:
        return 0
    elif k ==1:
        return 1
    else:
        return fib(k-1)+ fib(k-2)



if __name__ == '__main__':
    sols = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55}

    for key in sols:
        assert fib(key) == sols[key]
    print("all good!")