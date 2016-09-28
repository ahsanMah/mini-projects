# from time import clock start_time = clock()
import timing
import math
from decimal import Decimal

'''
 This function is used to detrmine erquality for floats and is given in Python's documentation. A similar function has been formally implemented in Python 3.5
 
 Source: https://www.python.org/dev/peps/pep-0485/#proposed-implementation
 '''
def isclose(a, b, rel_tol=1e-9, abs_tol=1e-10):
    # print "abs:", abs(a-b)
    # rel = rel_tol*max(abs(a),abs(b))
    # print rel
    # print max(rel,abs_tol) 

    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        for x,y in zip  (self.coordinates,v.coordinates):
            if not isclose(x,y):
                return False
        return True

    def __add__(self,v):
        # return map(lambda x,y: x+y,self.coordinates,v.coordinates)
        return Vector(map(intAdd,self.coordinates,v.coordinates))

    def __sub__(self,v):
        return Vector(map(intSub,self.coordinates,v.coordinates))

    def __mul__(self,scalar):
        # arr = []
        # for val in self.coordinates:
        #     arr.append(scalar * val)
        
        new_coordinates = [(scalar)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __rmul__(self,scalar):
        return (self * scalar)

    def magnitude(self):
        sum = 0

        for x in self.coordinates:
            sum += x**2  #same as x*x
        
        return (math.sqrt(sum))
        # return sum([x**2 for x in self.coordinates])


    def normalize(self):
        try:
            multiplier = (1)/self.magnitude()
            return (self * multiplier)
        except ZeroDivisionError:
            raise Exception ("Cannot normalize zero vector")

    def dotProduct(self,v):
        try:
            # return sum(map(lambda x,y: x*y, self.coordinates,v.coordinates))
            return sum([x*y for x,y in zip(self.coordinates,v.coordinates)])
        except TypeError:
            raise Exception("Cannot find dot product of different sized vectors")

    def calcAngle(self,v, in_degrees=False):
        try:
            rhs = self.normalize()
            lhs = v.normalize()
            angle = math.acos(rhs.dotProduct(lhs)) 
            if in_degrees:
                return math.degrees(angle)
            else:
                return angle
        except Exception as e:
            raise e

    def isPar(self, v):
        zero_vector = Vector([0]*len(self.coordinates)) #creates a  vector from an array of 0s of size len(self)
        
        if self == zero_vector or v == zero_vector:
            return True

        self_unit = self.normalize()
        v_unit = v.normalize()

        return self_unit == v_unit or self_unit == (-1) * v_unit
        
    def isOrth(self,v):
        return isclose(self.dotProduct(v),(0))


def intAdd (n1,n2):
    # simple addition of two integers
        return n1 + n2

def intSub (n1,n2):
    # integer subtraction
        return n1 - n2

def quiz1():
    v1 = Vector([8.218,-9.341])
    v2 = Vector([-1.129,2.111])
    v3 = Vector([7.119,8.215])
    v4 = Vector([-8.223,0.878])
    v5 = Vector([1.671,-1.012,-0.318])
    print (v1+v2)
    print (v3-v4)
    print (7.41*v5)

def quiz2():
    v1 = Vector([-.221,7.437])
    v2 = Vector([8.813,-1.331,-6.247])
    v3 = Vector([5.581,-2.136])
    v4 = Vector([1.996,3.108,-4.554])
    v5 = Vector([0,0,0,0])

    print "{:.3f}".format(v1.magnitude())
    print "{:.3f}".format(v2.magnitude())
    print (v3.normalize())
    print (v4.normalize())
    # print v5.normalize()

def quiz3():
    v1 = Vector([7.887,4.138])
    v2 = Vector([-8.802,6.776])
    v3 = Vector([-5.955,-4.904,-1.874])
    v4 = Vector([-4.496,-8.755,7.103])
    v5 = Vector([3.183,-7.627])
    v6 = Vector([-2.668,5.319])
    v7 = Vector([7.35,0.221,5.188])
    v8 = Vector([2.751,8.259,3.985])
    print v1.dotProduct(v2)
    print v3.dotProduct(v4)
    print v5.calcAngle(v6)
    print (v7.calcAngle(v8,True))

def quiz4():
    v1 = Vector([-7.579,-7.88])
    v2 = Vector([22.737,23.64])
    v3 = Vector([-2.029,9.97,4.172])
    v4 = Vector([-9.231,-6.639,-7.245])
    v5 = Vector([-2.328,-7.284,-1.214])
    v6 = Vector([-1.821,1.072,-2.94])
    v7 = Vector([2.118,4.827])
    v8 = Vector([0,0])
    
    print v1.isPar(v2)
    print v3.isPar(v4)
    print v5.isPar(v6)
    print v7.isPar(v8)
    print "-----------"
    print v1.isOrth(v2)
    print v3.isOrth(v4)
    print v5.isOrth(v6)
    print v7.isOrth(v8)

# quiz1()
# quiz2()
# quiz3()
quiz4()
