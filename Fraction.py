"""
This is a Fraction Module

This module implements functions that gets the numerator, denominator, and
the lowest term fraction from a given fraction or creates a fraction given
two integers
"""

class Fraction(object):

    def __init__(self, numerator=0, denominator=1):

        self.valid = True

        #if the given is a string fraction already
        if isinstance(numerator, str):
            numbers = numerator.strip().split("/")

            if len(numbers) == 2:
                if not numbers[0].strip("-").isnumeric() or not numbers[1].strip("-").isnumeric():
                    self.valid = False
                else:
                    self.numerator = int(numbers[0])
                    self.denominator = int(numbers[1])

                    if self.denominator == 0:
                        self.valid = False
                        raise ZeroDivisionError
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
        '''     
        @fn gcd
        @brief returns the greatest common denominator of the two numbers
        @param a numerator
        @param b denominator

        ''' 

        if a == 0 or b == 0:
            return 0

        if a % b == 0:
            return b
        
        return Fraction.gcd(b, a % b)

    def get_numerator(self):
        '''     
        @fn get_numerator
        @brief Returns 0 if the Fraction is not valid or if the greatest_common_divisor
        is 0 else returns the lowest form of the numerator

        '''
        if not self.valid or self.greatest_common_divisor == 0:
            return "0"
        
        return str( self.numerator // self.greatest_common_divisor)

    def get_denominator(self):
        '''     
        @fn get_denominator
        @brief Returns 0 if the Fraction is not valid or if the greatest_common_divisor
        is 0 else returns the lowest form of the denominator

        '''
        if not self.valid or self.greatest_common_divisor == 0:
            return "0"
        
        return str( self.denominator // self.greatest_common_divisor)
    
    def get_fraction(self):
        '''     
        @fn get_fraction
        @brief Returns 0 if the Fraction is not valid. Returns the fraction in its lowest form
        with consideration of negative numerators and denominators in the format:
        numerator / denominator

        '''
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