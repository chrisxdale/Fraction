class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError
        
        self.numerator = numerator
        self.denominator = denominator

    def gcd(a, b):

        if a == 0 and b == 0:
            return 0

        if b == 0:
            return a
        
        a = b % a
        
        return Fraction.gcd(a, b % a)

    def get_numerator(self):
        
        return str( self.numerator / self.gcd() )

    def get_denominator(self):
        #TODO
        pass
``
    def get_fraction(self):
        #TODO
        pass