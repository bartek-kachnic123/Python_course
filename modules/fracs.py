from math import gcd, lcm
import unittest

def add_frac(frac1, frac2):  # frac1 + frac2
    if frac1[0] == 0:
        return frac2.copy()
    elif frac2[0] == 0:
        return frac1.copy()

    if frac1[1] == frac2[1]:
        return [frac1[0] + frac2[0], frac1[1]]

    least_common_multiple = lcm(frac1[1], frac2[1])
    num1 = int((frac1[0] * (least_common_multiple / frac1[1])
            + frac2[0] * (least_common_multiple / frac2[1])))

    return [ num1, least_common_multiple]



def sub_frac(frac1, frac2): pass        # frac1 - frac2


def mul_frac(frac1, frac2): pass        # frac1 * frac2



def div_frac(frac1, frac2): pass        # frac1 / frac2


def is_positive(frac): pass             # bool, czy dodatni


def is_zero(frac): pass                 # bool, typu [0, x]


def cmp_frac(frac1, frac2): pass        # -1 | 0 | +1


def frac2float(frac): pass              # konwersja do float

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([10, 100], self.zero), [10, 100])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 2])
        self.assertEqual(add_frac([5, -4], [3, -5]),  [-37, 20])
        self.assertEqual(add_frac([-5, -4], [-2, -2]), [9, 4])

    def test_sub_frac(self): pass

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
