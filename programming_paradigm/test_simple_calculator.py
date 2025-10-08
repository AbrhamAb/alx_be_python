import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ------------------------
    # Test addition
    # ------------------------
    def test_addition(self):
        """Test the add method with different inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    # ------------------------
    # Test subtraction
    # ------------------------
    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)

    # ------------------------
    # Test multiplication
    # ------------------------
    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(-3, -5), 15)
        self.assertEqual(self.calc.multiply(0, 999), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    # ------------------------
    # Test division
    # ------------------------
    def test_division(self):
        """Test the divide method, including division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero returns None
        self.assertIsNone(self.calc.divide(0, 0))  # Edge case: 0 divided by 0
        self.assertEqual(self.calc.divide(0, 5), 0)  # 0 divided by nonzero should be 0


if __name__ == "__main__":
    unittest.main()
