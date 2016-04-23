class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom


    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)


    def __add__(self, other):
        newnum = self.num * other.den + other.num * self.den
        newden = self.den * other.den
        commonDivisor = gcd(newnum, newden)
        return Fraction(newnum//commonDivisor, newden//commonDivisor)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum

#HELPER greatest common divisor

def gcd(m,n):
    while m%n !=0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n



myF = Fraction(2,3)
myF.show()
print(myF)

f1 = Fraction(2,4)
f2 = Fraction(1,2)
f3 = f1+f2
print( f3)
print( f1 == f2)