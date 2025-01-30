import unittest

from Fraction import Fraction

class FractionUnitTest(unittest.TestCase):

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_gcd_zero_inputs(self):
        self.assertEqual(Fraction.gcd(0,0), 0)
        self.assertEqual(Fraction.gcd(0,1), 0)
        self.assertEqual(Fraction.gcd(1,0), 0)

    def test_gcd_correct_inputs(self):
        self.assertEqual(Fraction.gcd(3,5), 1)
        self.assertEqual(Fraction.gcd(2,4), 2)
        self.assertEqual(Fraction.gcd(6,9), 3)

    def test_fraction_zero_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            self.fraction = Fraction(0,0)

        with self.assertRaises(ZeroDivisionError):
            self.fraction = Fraction(1,0)

        self.fraction = Fraction(0, 1)
        self.assertEqual(self.fraction.get_fraction(), "0")

    def test_fraction_invalid_inputs(self):
        self.fraction = Fraction("not a number")
        self.assertEqual(self.fraction.get_fraction(), "0")

        self.fraction = Fraction("abc/def")
        self.assertEqual(self.fraction.get_fraction(), "0")

        self.fraction = Fraction("1.23")
        self.assertEqual(self.fraction.get_fraction(), "0")

        self.fraction = Fraction("1/2/3")
        self.assertEqual(self.fraction.get_fraction(), "0")

        self.fraction = Fraction(1.23)
        self.assertEqual(self.fraction.get_fraction(), "0")

    def test_fraction_negative_inputs(self):
        self.fraction = Fraction(-2, 4)
        self.assertEqual(self.fraction.get_fraction(), "-1/2")

        self.fraction = Fraction(2, -4)
        self.assertEqual(self.fraction.get_fraction(), "-1/2")

        self.fraction = Fraction(-2, -4)
        self.assertEqual(self.fraction.get_fraction(), "1/2")

    def test_fraction_negative_string_inputs(self):
        self.fraction = Fraction("-2/4    ")
        self.assertEqual(self.fraction.get_fraction(), "-1/2")

        self.fraction = Fraction("   2/-4")
        self.assertEqual(self.fraction.get_fraction(), "-1/2")

        self.fraction = Fraction("   -2/-4   ")
        self.assertEqual(self.fraction.get_fraction(), "1/2")

    def test_fraction_positive_string_inputs(self):
        self.fraction = Fraction("2/4")
        self.assertEqual(self.fraction.get_fraction(), "1/2")


if __name__ == '__main__':
    unittest.main()