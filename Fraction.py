class Fraction(object):

    def __init__(self, numerator=0, denominator=1):

        self.valid = True

        #if the given is a string fraction already
        if isinstance(numerator, str):
            numbers = numerator.strip().split("/")

            if len(numbers) == 2:
                pass
            else:
                self.valid = False
        else:
            if not isinstance(numerator, int) or not isinstance(denominator, int):
                self.valid = False

            else:
                self.numerator = numerator
                self.denominator = denominator

                if self.denominator == 0:
                    self.valid = False
                    raise ZeroDivisionError

        if self.valid:
            self.greatest_common_divisor = Fraction.gcd(self.numerator, self.denominator)

    def gcd(a, b): 

        if a == 0 or b == 0:
            return 0

        if a % b == 0:
            return b
        
        return Fraction.gcd(b, a % b)

    def get_numerator(self):
        if not self.valid or self.greatest_common_divisor == 0:
            return "0"
        
        return str( self.numerator // self.greatest_common_divisor)

    def get_denominator(self):
        if not self.valid or self.greatest_common_divisor == 0:
            return "0"
        
        return str( self.denominator // self.greatest_common_divisor)
    
    def get_fraction(self):

        if not self.valid:
            return "0"
        
        str_numerator = self.get_numerator()
        str_denominator = self.get_denominator()
        
        if str_denominator == "1":
            return str_numerator
        
        if str_numerator == "0":
            return "0"
        
        if str_denominator == "-1":
            if int(str_numerator) < 0:
                return str_numerator[1:]
            return "-" + str_numerator
            
        if int(str_denominator) < 0:
            if int(str_numerator) > 0:
                str_denominator = str_denominator[1:]
                str_numerator = "-" + str_numerator
            else:
                str_numerator = str_numerator[1:]
                
        return str_numerator + "/" + str_denominator