import unittest
from Float import Float

class FloatTest(unittest.TestCase):
    def test_caculate_error(self):
        a = Float(0.21)
        self.assertAlmostEquals(a.get_error(), 0.005)
        a = Float(0)
        self.assertAlmostEquals(a.get_error(), 0.5)
        a = Float(0.00105)
        self.assertAlmostEquals(a.get_error(), 0.000005)

    def test_add(self):
        a = Float(1.994, 0.000068)
        b = Float(1.24, 0.002)
        c = a + b
        self.assertAlmostEqual(c.get_error(), 0.0021)
        self.assertAlmostEquals(c.get_value(), 3.234)

        a = Float(1.994, 0.000068)
        b = Float(1.24, 0.02)
        c = a + b
        self.assertAlmostEqual(c.get_error(), 0.021)
        self.assertAlmostEquals(c.get_value(), 3.23)
        



if __name__ == "__main__":
    unittest.main()