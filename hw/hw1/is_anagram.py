def is_anagram(a, b):
    """Checks if a and b are anagrams of each other.
     if they are it retuns true, else it will return false """
    x = False
    

    
    if sorted(a) == sorted(b):
        x =  True
    else:
        x = False

    print(x)
    return x




