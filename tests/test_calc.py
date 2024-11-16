import math
import unittest
from parameterized import parameterized
from app.main import Calculator
from math import inf


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    @parameterized.expand(
        # 1. arrange
        [
            ("integers", 2, 3, 6),
            ("floats", 2.5, 3.1, 5.6),
            ("negative", -2.5, 3.0, 0.5)
        ]
    )
    def test_sum(self, name, a, b, expected_result):
        # 2. act
        actual_result = self.calc.sum(a, b)

        # 3. assert
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("strings", 'aaa', 'bbb', TypeError),
        ("int_None", 1, None, TypeError),
        ("None_float", None, 1.1, TypeError),
        ("None_None", None, None, TypeError)

    ])
    def test_sum_invalid_values(self, name, a, b, expected_result):
        with self.assertRaises(expected_result):
            self.calc.sum(a, b)

    @parameterized.expand([
        ("list_integers", [1, 2, 3, 4], 10),
        ("list_empty", [], 0),
        ("list_single", [1], 1)
    ])
    def test_sum_list(self, name, a, expected_result):
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("tuple_integers", (1, 2, 3, 4), 10),
        ("tuple_empty", (), 0),
        ("tuple_single", (1,), 1),
        ("set_integers", {1, 2, 3, 4}, 10),
        ("set_empty", {}, 0),
        ("set_single", {1}, 1),
    ])
    def test_sum_tuple(self, name, a, expected_result):
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    def test_multiply(self):
        a = 5
        b = 0.000000005

        actual_result = self.calc.multiply(a, b)
        expected_result = 1

        self.assertAlmostEqual(actual_result, expected_result)

    def test_divide(self):
        a = 5
        b = 0

        expected_result = ZeroDivisionError

        with self.assertRaises(expected_result):
            self.calc.divide(a, b)

    def test_divide_inf(self):
        a = inf
        b = inf

        expected_result = None
        actual_result = self.calc.divide(a, b)

        self.assertNotEqual(actual_result, expected_result)
        self.assertIsInstance(actual_result, type(math.inf))
        self.assertIsInstance(actual_result, float)


if __name__ == "__main__":
    unittest.main()
