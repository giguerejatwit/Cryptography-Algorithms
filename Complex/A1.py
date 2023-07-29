import math
import numbers


class ComplexNumber:
    def __init__(self, r=0, i=0,):
        self.r = r
        self.i = i
        self.modulus = 0
        
    def toString(self):
        print( f"{self.r} {self.i}i" )

    # C1 + C2
    def add(self, other):
        self.r +=  other.r
        self.i += other.i
        return ComplexNumber((self.r + other.r), (self.i + other.i))
    
    # C1 - C2
    def sub(self, other):
        self.r -=  other.r
        self.i -= other.i
        return ComplexNumber((self.r - other.r), (self.i - other.i))

    # C1 * C2
    def multiply(self, other):
        self.r = ((self.r * other.r) - (self.i * other.i))
        self.i *= ((self.r * other.i) + (other.r * self.i))
        return ComplexNumber(self.r,  self.i)
   
    def pow2(self):
        self.r = math.pow(self.r,2)
        self.i = math.pow(self.i, 2)
        return ComplexNumber(self.r, self.i)
    
    def abs(self):
        self.r = abs(self.r)
        self.i = abs(self.i)

    def sqrt(self):
        try:
            self.r = math.sqrt(self.r)
            self.i = math.sqrt(self.i)
        except ValueError as e:
            print("Error: taking a root. <= 0", e)

        return ComplexNumber(self.r, self.i)
    
    # their modulus: |C1| and |C2|
    def getModulus(self, r, i):
        return math.sqrt(math.pow(r, 2) + math.pow(i, 2))

    def compare(self, other) -> bool:
        if (self.r == other.r and self.i == other.i):
            return True
        else:
            return False

    # C1 / C2
    def divide(self, other):
        divisor = self.getModulus(other.r, other.i)
        return ( (((self.r * other.r) + (self.i * other.i)) / (divisor)) + (((other.r * self.i) - (self.r * other.i)) / (divisor)) )
    
    #  C1's and C2's complex conjugates
    def Conjugate(self):
        self.i *= -1
        return ComplexNumber(self.r, (self.i * -1))
    
    #Convert C1 and C2 to their Polar representation (let us call them P1 and P2 respectively). Then display P1 and P2.
    def getPolarCoords(self):
        return self.getModulus(self.r, self.i), math.degrees(math.atan2(self.i, self.r))
    
    def PolarMultiplication(self, a1=math.sqrt(2), a2=math.sqrt(2), b1 = (math.pi / 4), b2 = (math.pi * 3 / 4)):
        return (a1 * a2), (b1 + b2)
    
    def PolarDivision(self, a1=math.sqrt(10), a2=math.sqrt(17), b1=(1.8925), b2 =(-1.8158)):
        return (a1 / a2), (b1 - b2)

        



def main():
    print(f'{__name__}')
