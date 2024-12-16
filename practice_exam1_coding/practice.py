def has_same_letters(str1, str2):
    s1 = set(str1)
    s2 = set(str2)

    
    if s1 == s2 or s2 == s1:
        return True
    else:
        return False
    
print(has_same_letters("reheat", "theater"))
print(has_same_letters("reheat", "there"))

#O(n)

class Animal:
    name = ""
    sound = ""
    species = ""

    def __init__(self, name, sound, species):
        self.name = name 
        self.sound = sound
        self.species = species

class Dog(Animal):
    is_good_boy = True 

    def __init__(self, name, sound, species):
        super().__init__(name, sound, species)
        
    def good_boy(self, bool):
        self.is_good_boy = bool
        return bool
    
class Cat(Animal):

    def __init__(self, name, sound, species):
        super().__init__(name, sound, species)
    



