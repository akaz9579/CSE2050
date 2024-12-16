def factorial(n):
    """Returns the nth factorial"""
    # n! = 1*2*3*4*..*n
    product = 1
    for number in range(1, n+1):
        product *= number
    return product
    #O(1) memory overhead

def factorial_recr(n):
    """Returns the nth factorial"""
    return 1 if n==0 else n * factorial_recr(n-1)
    # O(n) memory overhead
    if n == 0:
        return 1
    else:
        return factorial_recr(n-1) * n
    




factorial_recr(4)

if __name__ == '__main__':
    sols = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720}

    for key in sols:
        assert factorial(key) == sols[key]
        assert factorial_recr(key) == sols[key]

    print("all good")