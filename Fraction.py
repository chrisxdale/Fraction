# Gregorio Delfin P. Pascua
# 234835
#
# Antonth Chrisdale C. Lopez 
# 233714
#
# January 30, 2025
#
# We hereby attest to the truth of the following facts:
#
# We have not discussed the Python language code in our program
# with anyone other than our instructor or the teaching assistants
# assigned to this course.
#
# We have not used Python language code obtained from another student,
# or any other unauthorized source, either modified or unmodified.
#
# If any Python language code or documentation used in our program
# was obtained from another source, such as a textbook or website,
# that has been clearly noted with a proper citation in the comments
# of our program.

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
            try:
                numbers = map(int, numerator.strip().split("/"))
                self.numerator, self.denominator = numbers
            except ValueError:
                self.valid = False

        else:
            if isinstance(numerator, int) and isinstance(denominator, int):
                self.numerator = numerator
                self.denominator = denominator
            else:
                self.valid = False

        if self.valid:
            if self.denominator != 0:
                self.greatest_common_divisor = Fraction.gcd(self.numerator, self.denominator)
            else:
                raise ZeroDivisionError

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
        # This checks whether the fraction is a not a valid fraction or if the greatest 
        # common divisor is equal to 0 which returns 0 if one is true
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
        # This checks whether the fraction is a valid fraction before
        # proceeding with getting the fraction
        if not self.valid:
            return "0"
        
        numerator = int(self.get_numerator())
        denominator = int(self.get_denominator())
        
        # This returns the string of numerator if the denominator is 1 since
        # dividing by 1 is just the number itself
        if denominator == 1:
            return self.get_numerator()
        
        # This returns the string of numerator if the denominator is 1 since
        # dividing by 1 is just the number itself
        
        if numerator == 0:
            return "0"
        
        # This returns the negative string of numerator if the denominator is -1
        if denominator == -1:
            return str(-numerator)
        
        # This negates the numerator and denominator if the denominator is negative
        # to account for the sign position switching if the numerator is originally positive
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        return str(numerator) + "/" + str(denominator)
