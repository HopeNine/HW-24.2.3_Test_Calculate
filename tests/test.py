import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_divizion(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_substraction_success(self):
        assert self.calc.subtraction(self, 1, 1) == 0

    def test_substraction_unsuccess(self):
        assert self.calc.subtraction(self, 10, 1) != 9

    def test_division_success(self):
        assert self.calc.division(self, 1, 1) == 1

    def test_division_unsuccess(self):
        assert self.calc.division(self, 8, 2) != 4

    def test_multiply_success(self):
        assert self.calc.multiply(self, 100, 10) == 10

    def test_multiply_unsuccess(self):
        assert self.calc.multiply(self, 100, 10) == 1

    def teardown(self):
        print("Выполнение метода Teardown")
