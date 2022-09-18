from math import atan2
def add_rational_and_complex(r,c):
    return ComplexRI(r.numer/r.denom + c.real, c.image)
def mul_rational_and_complex(r,c):
    return ComplexMA(r.numer/r.denom * c.manitude , c.angle)
def add_complex_and_rational(c,r):
    return add_rational_and_complex(r,c)
def mul_complex_and_rational(c,r):
    return mul_rational_and_complex(r,c)
def make_add(n):
    def add(k):
        return n + k
    return add
def rational_to_complex(r):
    return ComplexRI(r.numer/r.denom, 0)


class Adder():
    def __init__(self,n):
        self.will_add = n

    def __call__(self,k):
        return self.will_add + k
class Number:
    def __add__(self,other):
        x,y = self.coerce(other)
        return x.add(y)
    def __mul__(self,other):
        x,y = self.coerce(other)
        return x.mul(y)
    def coerce(self, other):
        flag = (self.type_flag,other.type_flag)
        flag1 = (other.type_flag, self.type_flag)
        if flag in self.trans:
            return self.to_coerce(other), other
        elif flag1 in self.trans:
            return self, other.to_coerce(self)
        elif flag[0]== flag[1]:
            return self, other
    def to_coerce(self,other):
        return self.trans[(self.type_flag, other.type_flag)](self)
    trans = {('rat','com'): rational_to_complex}

    
            
class Complex(Number):
    type_flag= 'com'
    def add(self, other):
        return ComplexRI(self.real + other.real, self.image + other.image)
    def mul(self,other):
        manitude = self.manitude * other.manitude
        return ComplexMA(manitude, self.angle + other.angle)

class ComplexRI(Complex):
    def __init__(self,real,image):
        self.real = real
        self.image = image
    @property
    def manitude(self):
        return (self.real**2 + self.image **2)**0.5
    @property
    def angle(self):
        return atan2(self.image, self.real)
    def __repr__(self):
        return 'ComplexRI({0},{1})'.format(self.real, self.image)
from math import sin,cos,pi
class ComplexMA(Complex):
    def __init__(self,manitude, angle):
        self.manitude = manitude
        self.angle = angle
    @property
    def real(self):
        return self.manitude * cos(self.angle)
    @property
    def image(self):
        return self.manitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0},{1}*pi)'.format(self.manitude, self.angle/pi)

from math import gcd
class rational(Number):
    type_flag = 'rat'
    def __init__(self,numer,denom):
        factor = gcd(numer,denom)
        self.numer = numer//factor
        self.denom = denom//factor

    def __add__(self, other):
        nx,ny = self.numer, other.numer
        dx,dy = self.denom, other.denom
        return rational(nx*dy + ny*dx, dx*dy)
    def __mul__(self, other):
        nx,ny = self.numer, other.numer
        dx,dy = self.denom, other.denom
        return rational(nx*ny, dx*dy)
    def __repr__(self):
        return 'rational({0}/{1})'.format(self.numer, self.denom)

a = ComplexRI(1.5,0)
b = rational(3,1)
print(a+b)

