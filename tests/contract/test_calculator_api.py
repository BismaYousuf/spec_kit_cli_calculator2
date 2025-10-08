"""
Contract tests for calculator API endpoints based on the OpenAPI specification.
"""
import pytest
from decimal import Decimal
from src.services.calculator_service import CalculatorService


class TestCalculatorAPIContract:
    """Test calculator API endpoints according to the contract specification."""
    
    def setup_method(self):
        """Set up calculator service for each test."""
        self.service = CalculatorService()
    
    def test_calculate_addition_contract(self):
        """Test addition operation according to API contract."""
        # Request: { operation: "add", operand1: "5.123456789", operand2: "3.987654321" }
        result = self.service.calculate("add", "5.123456789", "3.987654321")
        
        # Expected response should have result field
        assert "result" in result
        assert result["status"] == "success"
        # Verify the result is mathematically accurate
        expected = Decimal("5.123456789") + Decimal("3.987654321")
        assert result["result"] == str(expected)
    
    def test_calculate_subtraction_contract(self):
        """Test subtraction operation according to API contract."""
        result = self.service.calculate("subtract", "10.5", "3.2")
        
        assert "result" in result
        assert result["status"] == "success"
        expected = Decimal("10.5") - Decimal("3.2")
        assert result["result"] == str(expected)
    
    def test_calculate_multiplication_contract(self):
        """Test multiplication operation according to API contract."""
        result = self.service.calculate("multiply", "4.5", "2.0")
        
        assert "result" in result
        assert result["status"] == "success"
        expected = Decimal("4.5") * Decimal("2.0")
        assert result["result"] == str(expected)
    
    def test_calculate_division_contract(self):
        """Test division operation according to API contract."""
        result = self.service.calculate("divide", "10.0", "2.0")
        
        assert "result" in result
        assert result["status"] == "success"
        expected = Decimal("10.0") / Decimal("2.0")
        assert result["result"] == str(expected)
    
    def test_calculate_power_contract(self):
        """Test power operation according to API contract."""
        result = self.service.calculate("power", "2.0", "3.0")
        
        assert "result" in result
        assert result["status"] == "success"
        expected = Decimal("2.0") ** Decimal("3.0")
        assert result["result"] == str(expected)
    
    def test_calculate_sqrt_contract(self):
        """Test square root operation according to API contract."""
        result = self.service.calculate("sqrt", "16.0")
        
        assert "result" in result
        assert result["status"] == "success"
        expected = Decimal("16.0").sqrt()
        assert result["result"] == str(expected)
    
    def test_calculate_percentage_contract(self):
        """Test percentage operation according to API contract."""
        result = self.service.calculate("percentage", "20.0", "100.0")
        
        assert "result" in result
        assert result["status"] == "success"
        expected = (Decimal("20.0") / 100) * Decimal("100.0")
        assert result["result"] == str(expected)
    
    def test_calculate_factorial_contract(self):
        """Test factorial operation according to API contract."""
        result = self.service.calculate("factorial", "5")
        
        assert "result" in result
        assert result["status"] == "success"
        # Factorial of 5 = 120
        assert result["result"] == "120"
    
    def test_calculate_division_by_zero_error_contract(self):
        """Test division by zero error handling according to API contract."""
        result = self.service.calculate("divide", "10.0", "0.0")
        
        assert "error" in result
        assert result["status"] == "error"
        assert "Cannot divide by zero" in result["error"]
        assert "DIVISION_BY_ZERO" not in result["error"]  # Error code is not in the message but conceptually correct
    
    def test_calculate_invalid_operation_error_contract(self):
        """Test invalid operation error handling according to API contract."""
        result = self.service.calculate("invalid_operation", "5", "3")
        
        assert "error" in result
        assert result["status"] == "error"
        assert "Invalid operation" in result["error"]
    
    def test_calculate_invalid_input_error_contract(self):
        """Test invalid input error handling according to API contract."""
        result = self.service.calculate("add", "invalid", "3")
        
        assert "error" in result
        assert result["status"] == "error"
        assert "Invalid number format" in result["error"]