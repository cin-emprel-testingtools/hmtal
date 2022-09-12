import pytest
from src.calculator import Calculator

class TestCalculator():

    def setup_class(self):
        self.calc = Calculator()
    
    def test_addition(self):
        assert self.calc.addition(2,2) == 4
    
    def test_addition2(self):
        assert self.calc.addition(4,4) == 8
    
    @pytest.mark.skip(reason="Duplicated test!")
    def test_subtraction(self):        
        assert self.calc.subtraction(10,1) == 9
    
    def test_multiplication(self):
        assert self.calc.multiplication(3,4) == 12
    
    def test_division(self):
        assert self.calc.division(10,2) == 5

    def test_division2(self):
        assert self.calc.division(12,4) == 3

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(10,0)