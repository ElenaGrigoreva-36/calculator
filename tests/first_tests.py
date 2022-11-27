import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

        def test_multiply_calculate_correctly(self):
            assert self.calc.multiply(self, 2, 2) == 4

        def test_division_calculator_correctly(self):
            assert self.calc.division(self, 2, 2) == 0

        def test_subtraction_calculate_correctly(self):
            assert self.calc.subtraction(self, 10, 4) == 6

        def test_adding_calculate_carrectly(self):
            assert self.calc.adding(self, 11, 10) == 21



