"""
Unit tests for mathematical utilities ensuring accuracy.
"""
import pytest
from decimal import Decimal
from src.lib.math_utils import MathUtils


class TestMathUtils:
    """Test mathematical operations with high precision."""
    
    def test_addition(self):
        """Test addition operation with precision."""
        result = MathUtils.add("5", "3")
        assert result == Decimal("8")
    
    def test_subtraction(self):
        """Test subtraction operation with precision."""
        result = MathUtils.subtract("10", "3")
        assert result == Decimal("7")
    
    def test_multiplication(self):
        """Test multiplication operation with precision."""
        result = MathUtils.multiply("4", "5")
        assert result == Decimal("20")
    
    def test_division(self):
        """Test division operation with precision."""
        result = MathUtils.divide("10", "2")
        assert result == Decimal("5")
    
    def test_division_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            MathUtils.divide("10", "0")
    
    def test_power(self):
        """Test power operation."""
        result = MathUtils.power("2", "3")
        assert result == Decimal("8")
    
    def test_sqrt(self):
        """Test square root operation."""
        result = MathUtils.sqrt("16")
        assert result == Decimal("4")
    
    def test_sqrt_negative_raises_error(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Square root of negative number is not allowed"):
            MathUtils.sqrt("-16")
    
    def test_percentage(self):
        """Test percentage calculation."""
        result = MathUtils.percentage("20", "100")
        assert result == Decimal("20")
    
    def test_factorial(self):
        """Test factorial calculation."""
        result = MathUtils.factorial("5")
        assert result == 120
    
    def test_factorial_zero(self):
        """Test factorial of zero."""
        result = MathUtils.factorial("0")
        assert result == 1
    
    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial of negative number is not allowed"):
            MathUtils.factorial("-5")
    
    def test_factorial_large_input_raises_error(self):
        """Test that factorial of very large number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial input is too large"):
            MathUtils.factorial("200")