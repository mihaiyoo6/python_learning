class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        common_divisor = gcd(new_num, new_den)
        return Fraction(new_num//common_divisor, new_den//common_divisor)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num == second_num


# HELPER greatest common divisor
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n

    return n

myF = Fraction(2, 3)
myF.show()
print(myF)

f1 = Fraction(2, 4)
f2 = Fraction(1, 2)
f3 = f1+f2
print(f3)
print(f1 == f2)
