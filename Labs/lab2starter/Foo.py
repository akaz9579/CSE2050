class Foo:
    name = ""
    profession = ""
    
    def __init__(self, n, p):
        self.name = n
        self.profession = p


    def speak(obj):
        return f"{obj.name} says hello!"
    
    def __repr__(self):
        return f"Foo({self.name}, {self.profession})"
    
   

    