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
        return Fraction(newnum, newden)

myF = Fraction(2,3)
myF.show()
print(myF)

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1+f2
print( f3)