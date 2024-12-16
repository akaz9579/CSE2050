import math
class Point:
    x = 0.0
    y=0.0

    def __init__(self,x:float,y:float) :
        self.x = x
        self.y= y

    def __eq__(self, other):
         return other.x==self.x and other.y==self.y
    
    def dist_from_origin(self):
        return (self.x**2 + self.y**2)**(.5)

p1 = Point(3,5)

print( p1.dist_from_origin())

    
    