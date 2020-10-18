import math

class Point:
    def info(self):
        return "I have 0 sides, Sum of Angles is 0"

class Line:
    def __init__(self,l=0):
        self.l = l  
    def length(self):
        return self.l
    def info(self):
        return "I have 1 side, Sum of Angles is 180"

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    def area(self):
        area = math.pi*(self.radius**2)
        return area
    def perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter
    def info(self):
        return "I have 1 side, Sum of Angles is 360"

class Triangle:
    def __init__(self, a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a+self.b+self.c)/2
        area = math.sqrt((s-self.a)*(s-self.b)*(s-self.c))
        return area
    def perimeter(self):
        s = (self.a+self.b+self.c)/2
        if((s-self.a) != 0 and (s-self.b) != 0 and (s-self.c)!=0):
            return s*2
        else:
            return 0

    def info(self):
        return "I have 3 sides, Sum of Angles is 180"
        
class Quadrilateral:
    def __init__(self, sides = 4, sumOfAngles = 360):
        self.sides = sides
        self.sumOfAngles = sumOfAngles
    def info(self):
        return "I have 4 sides, Sum of Angles is 360"

class square(Quadrilateral):
    def __init__(self, s=0):
        self.s = s
    def area(self):
        return self.s**2
    def perimeter(self):
        return 4*self.s
    
class rectangle(Quadrilateral):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b
    def perimeter(self):
        return 2*(self.a + self.b)

sq = square(1)
print(sq.info())
print('sq perimeter: ',sq.perimeter())
print('sq area: ', sq.area())

tr = Triangle(1,1,1)
print(tr.info())
print('tr perimeter: ',tr.perimeter())
print('tr area: ', tr.area())

tr = Triangle(2,1,1)
print(tr.info())
print('tr perimeter: ',tr.perimeter())
print('tr area: ', tr.area())

cr = Circle(2)
print(cr.info())
print('cr perimeter: ',cr.perimeter())
print('cr area: ', cr.area())

line = Line(2)
print('line length',line.length())

