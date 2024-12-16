class Animal:
    name = ""
    species = ""
    sound = "hi"
 
    def __init__(self, n, sp="animal", so="hi"):
        self.name = n
        self.species = sp
        self.sound = so

    def speak(self):
        return f"{self.name}, a {self.species}, says {self.sound}!"


    def __repr__(self):
        return f"Animal({self.name}, {self.species}, {self.sound})"




class Dog(Animal):
    is_good_boy = 0

    def __init__(self, n, sp="dog", so="ruff", goodBoy=True):
       super().__init__(n,sp,so)
       self.is_good_boy = goodBoy
    
    def __repr__(self):
        return f"Dog({self.name})"
       



class Cat(Animal):
    

    def __init__(self, n, sp="cat", so="meow",):
       super().__init__(n,sp,so)

    def __repr__(self):
        return f"Cat({self.name}, {self.species}, {self.sound})"
       
