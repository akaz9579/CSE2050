###################
# START RECORDING #
###################


#recursive way
def sum_k(k):
    """Returns the sum of the first k ints"""
    result = 0
    if k > 0:
            result = k + sum_k(k-1)

    return result
    
    #return (k/2_*(k+1)) just this line, its o(1)

sum_k(10)



if __name__ == '__main__':
    sols = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15, 6:21, 7:28, 8:36, 9:45, 10:55}

    for key in sols:
        assert sum_k(key) == sols[key]

    print("all good!")