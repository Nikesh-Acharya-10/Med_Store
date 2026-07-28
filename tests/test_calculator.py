import unittest
from src.core.calculator import calculate_tablet_sale, calculate_strip_sale


class TestCalculator(unittest.TestCase):
    def test_tablet_sale_no_strips(self):
        result = calculate_tablet_sale(5, 5.0, 45.0, 10)
        self.assertEqual(result["strips"], 0)
        self.assertEqual(result["total"], 25.0)

    def test_strip_sale_with_discount(self):
        result = calculate_strip_sale(2, 45.0, 10)
        self.assertTrue(result["discount_applied"])


if __name__ == "__main__":
    unittest.main()
