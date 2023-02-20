"""
Unit tests for the calculator library
"""

from calculator import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 5 == calculator.divide(10, 2)

    def test_division_by_self(self):
        assert 1 == calculator.divide(10, 10)

    def test_division_negative_numbers(self):
        assert -5 == calculator.divide(-10, 2)

    def test_division_decimal_numbers(self):
        assert 0.5 == calculator.divide(1, 2)
