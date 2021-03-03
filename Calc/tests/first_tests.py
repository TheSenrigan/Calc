import pytest
from app.main import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_mult_calc_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calc_correct (self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtr_calc_correct (self):
        assert self.calc.subtr(self, 5, 2) == 3

    def test_adding_calc_correct (self):
        assert self.calc.adding(self, 1, 4) == 5