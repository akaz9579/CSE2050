from math import sqrt, cos, sin, atan

class Vector:
    """Class for methods that have been factored out from Rectangluar and Polar Vectors"""
    _x = 0
    _y=0
    _ang = 0
    _mag= 0

    def __init__(self, *args):
        """Users should specify rectangular or polar instead"""
        raise NotImplementedError("Specify RectangularVector or PolarVector.")
    
    def __mul__(self, other):
        raise NotImplementedError("Use dot() instead to find dot product")

    def __add__(self, other: 'Vector'):
        newX= self.get_x() + other.get_x()
        newY = self.get_y() + other.get_y()

        newVec = RectangularVector(newX, newY)
        return newVec


    def __eq__(self, other: 'Vector'):
        return round(self.get_x(),3) == round(other.get_x(),3) or round(self.get_y(),3) == round(other.get_y(),3)

    # Define "getters" for x, y, mag, and angle
    def get_x(self):
        """Returns x-component of vector."""
        return round(self._x,3)
    
    def get_y(self):
        return round(self._y,3)

    def get_ang(self):
        return round(self._ang,3)

    def get_mag(self):
        return round(self._mag, 3)

    def rectangular(self):
        return RectangularVector(self._x, self._y)

    def polar(self):
        return PolarVector(self._mag, self._ang)

    def dot(self,other: 'Vector'):
       return round(self.get_x() * other.get_x() + self.get_y() * other.get_y(), 3)


    

    


class RectangularVector(Vector):
    """Rectangular vectors have an x and y component."""
    def __init__(self, x:float, y:float):
        """Creates a new vector with given x- and y- attributes."""
        self._x = x
        self._y = y
        self._ang = atan( self._y/self._x)
        self._mag = sqrt(self._x**2 + self._y**2)
        self._update() # add self._mag and self.

    def _update(self):
        self._x= self._mag*cos(self._ang)
        self._y= self._mag*sin(self._ang) 
        self._ang = atan( self._y/self._x)
        self._mag = sqrt(self._x**2 + self._y**2)

        
    def __repr__(self):
        return f"RectangularVector({self.get_x()}, {self.get_y()})" 
    
    def set_x(self, new_x: float):
        self._x = new_x
        self._ang = atan( self._y/self._x)
        self._mag = sqrt(self._x**2 + self._y**2)
        self._update()

    
    def set_y(self, new_y: float):
        self._y = new_y
        self._ang = atan( self._y/self._x)
        self._mag = sqrt(self._x**2 + self._y**2)
        self._update()



class PolarVector(Vector):

    def __init__(self,mag:float,ang:float):
        self._mag=mag
        self._ang=ang
        self._x= self._mag*cos(self._ang)
        self._y= self._mag*sin(self._ang) 
        self._update()


    
    def __repr__(self):
        return f"PolarVector({self.get_mag()}, {self.get_ang()})"

        

    def _update(self):
        self._ang = atan( self._y/self._x)
        self._mag = sqrt(self._x**2 + self._y**2)
        self._x= self._mag*cos(self._ang)
        self._y= self._mag*sin(self._ang) 
        

    def set_mag(self, new_mag: float):
        self._mag = new_mag
        self._x= self._mag*cos(self._ang)
        self._y= self._mag*sin(self._ang) 
        self._update()  
        
    
    def set_ang(self, new_ang: float):
        self._ang = new_ang
        self._x= self._mag*cos(self._ang)
        self._y= self._mag*sin(self._ang) 
        self._update()

    



