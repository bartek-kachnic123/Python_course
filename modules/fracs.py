from math import gcd, lcm
import unittest


def add_frac(frac1, frac2):  # frac1 + frac2
    _simplify(frac1, frac2)

    least_common_multiple = lcm(frac1[1], frac2[1])
    try:
        num1 = int((frac1[0] * (least_common_multiple / frac1[1])
                + frac2[0] * (least_common_multiple / frac2[1])))
    except ZeroDivisionError:
        raise ZeroDivisionError("frac1 or frac2 have 0 as denominator")

    frac3 = [num1, least_common_multiple]
    _simplify(frac3)

    return frac3


def _simplify(*fracs):
    for frac in fracs:
        greatest_common_div = gcd(frac[0], frac[1])
        frac[0] //= greatest_common_div
        frac[1] //= greatest_common_div

        if frac[1] < 0:
            frac[0], frac[1] = -frac[0], -frac[1]


def sub_frac(frac1, frac2):     # frac1 - frac2
    _simplify(frac1, frac2)

    least_common_multiple = lcm(frac1[1], frac2[1])
    try:
        num1 = int((frac1[0] * (least_common_multiple / frac1[1])
                    - frac2[0] * (least_common_multiple / frac2[1])))
    except ZeroDivisionError:
        raise ZeroDivisionError("frac1 or frac2 have 0 as denominator")

    frac3 = [num1, least_common_multiple]
    _simplify(frac3)

    return frac3


def mul_frac(frac1, frac2):       # frac1 * frac2
    _simplify(frac1, frac2)

    frac3 = [frac1[0] * frac2[0],
             frac1[1] * frac2[1]]

    if frac3[1] == 0:
        raise ZeroDivisionError("frac1 or frac2 has 0 as denominator")

    _simplify(frac3)

    return frac3


def div_frac(frac1, frac2):       # frac1 / frac2
    _simplify(frac1, frac2)

    frac3 = [frac1[0] * frac2[1],
             frac1[1] * frac2[0]]

    if frac3[1] == 0:
        raise ZeroDivisionError("frac1 or frac2 has 0 as denominator")

    _simplify(frac3)

    return frac3


def is_positive(frac):             # bool, czy dodatni
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):                # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2):       # -1 | 0 | +1
    least_common_multiple = lcm(frac1[1], frac2[1])
    try:
        num1 = int(frac1[0] * (least_common_multiple / frac1[1]))
        num2 = int(frac2[0] * (least_common_multiple / frac2[1]))
    except ZeroDivisionError:
        raise ZeroDivisionError("frac1 or frac2 have 0 as denominator")

    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1


def frac2float(frac):   # konwersja do float
    try:
        return frac[0] / frac[1]
    except ZeroDivisionError:
        raise ZeroDivisionError("frac has 0 as denominator")

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
        self.assertEqual(add_frac([10, 100], self.zero), [1, 10])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])
        self.assertEqual(add_frac([5, -4], [3, -5]),  [-37, 20])
        self.assertEqual(add_frac([-5, -4], [-2, -2]), [9, 4])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 4]), [1, 4])

        self.assertEqual(sub_frac([1, 2], [3, 4]), [-1, 4])

        self.assertEqual(sub_frac(self.zero, [0, 2]), self.zero)

        self.assertEqual(sub_frac([2, 1], [1, 1]), [1, 1])

        self.assertEqual(sub_frac([3, 4], [1, 4]), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 4]), [1, 8])
        self.assertEqual(mul_frac([0, 1], [3, 4]), [0, 1])
        self.assertEqual(mul_frac([-1, 2], [1, 4]), [-1, 8])
        self.assertEqual(mul_frac([2, 3], [3, 2]), [1, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])

        self.assertEqual(div_frac([1, 2], [2, 1]), [1, 4])

        self.assertEqual(div_frac([-1, 2], [1, 4]), [-2, 1])

        self.assertEqual(div_frac([2, 3], [2, 3]), [1, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive(self.zero))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero([1, 1]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 3]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([2, 3], [1, 2]), 1)
        self.assertEqual(cmp_frac([-1, 2], [-1, 3]), -1)
        self.assertEqual(cmp_frac([-1, 2], [1, 2]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5, places=5)

        self.assertAlmostEqual(frac2float([-1, 2]), -0.5, places=5)

        self.assertAlmostEqual(frac2float([0, 1]), 0.0, places=5)

        self.assertAlmostEqual(frac2float([1, 3]), 1 / 3, places=5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
