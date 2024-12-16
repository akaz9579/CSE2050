import string
import os

def count_letters(data):
    """This function counts how often each character appears in a data file or string."""
    
    #path = /User/amankazi/CSE2050/hw
    
    dic = {}
    text = ""  
    
    try:
        with open(data, "r") as file:
            text = file.read()
    except (FileNotFoundError, IsADirectoryError, IOError, FileExistsError):
        text = data
    
    text = text.lower()
    
    for letter in text:
        if letter in string.ascii_lowercase:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
    
    return dic  

