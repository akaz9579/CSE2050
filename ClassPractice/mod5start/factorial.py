def factorialRecursive(n):
    """Returns the nth factorial"""
    result = 1
    if n > 0:
        result = n * factorialRecursive(n-1)
    return result

def factorialIterative(n):
    """Returns the nth factorial"""
    x =1
    for n in range(1,n+1):
        x *= n
    
    return x



if __name__ == '__main__':
    sols = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720}

    for key in sols:
        assert factorialIterative(key) == sols[key]

    print("all good!")