def unique_string(s):
    
    i = s[0]
    for x in s[1:]:
        if i == x:
           return False
        i=s[x]

    
    return True

print(unique_string("aaa"))
