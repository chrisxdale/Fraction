class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError
        
        self.numerator = numerator
        self.denominator = denominator
        self.greatest_common_divisor = Fraction.gcd(self.numerator, self.denominator)

    def gcd(a, b): 

        if a == 0 and b == 0:
            return 0

        if b == 0:
            return a
        
        return Fraction.gcd(b, a % b)

    def get_numerator(self):
        
        return str( self.numerator / self.greatest_common_divisor)

    def get_denominator(self):
        
        return str( self.denominator / self.greatest_common_divisor)
    
    def get_fraction(self):
        
        if self.denominator == 0:
            return "0"
        
        str_numerator = self.get_numerator()
        str_denominator = self.get_denominator()
        
        if str_denominator == "1":
            return str_numerator
        
        if str_numerator == "0":
            return "0"
            
        if self.denominator < 0:
            if self.numerator > 0:
                str_denominator = str_denominator[1:]
                str_numerator = "-" + str_numerator
            else:
                str_numerator = str_numerator[1:]
                
        return str_numerator + "/" + str_denominator