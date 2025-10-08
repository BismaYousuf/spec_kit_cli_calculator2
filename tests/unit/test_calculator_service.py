"""
Unit tests for calculator service basic operations (+, -, *, /).
"""
import pytest
from src.services.calculator_service import CalculatorService


class TestCalculatorServiceBasicOperations:
    """Test basic calculator operations with accuracy."""
    
    def setup_method(self):
        """Set up calculator service for each test."""
        self.service = CalculatorService()
    
    def test_addition(self):
        """Test addition operation: 5 + 3 = 8"""
        result = self.service.calculate("add", "5", "3")
        assert result["status"] == "success"
        assert result["result"] == "8"
    
    def test_subtraction(self):
        """Test subtraction operation: 10 - 3 = 7"""
        result = self.service.calculate("subtract", "10", "3")
        assert result["status"] == "success"
        assert result["result"] == "7"
    
    def test_multiplication(self):
        """Test multiplication operation: 4 * 5 = 20"""
        result = self.service.calculate("multiply", "4", "5")
        assert result["status"] == "success"
        assert result["result"] == "20"
    
    def test_division(self):
        """Test division operation: 10 / 2 = 5"""
        result = self.service.calculate("divide", "10", "2")
        assert result["status"] == "success"
        assert result["result"] == "5"
    
    def test_division_by_zero(self):
        """Test division by zero error handling."""
        result = self.service.calculate("divide", "10", "0")
        assert result["status"] == "error"
        assert "Cannot divide by zero" in result["error"]
    
    def test_invalid_operation(self):
        """Test invalid operation error handling."""
        result = self.service.calculate("invalid_op", "5", "3")
        assert result["status"] == "error"
        assert "Invalid operation" in result["error"]
    
    def test_invalid_operand(self):
        """Test invalid operand error handling."""
        result = self.service.calculate("add", "5", "abc")
        assert result["status"] == "error"
        assert "Invalid number format" in result["error"]
    
    def test_expression_calculation(self):
        """Test expression calculation: '5 + 3' -> 8"""
        result = self.service.calculate_from_expression("5 + 3")
        assert result["status"] == "success"
        assert result["result"] == "8"
    
    def test_expression_subtraction(self):
        """Test expression calculation: '10 - 3' -> 7"""
        result = self.service.calculate_from_expression("10 - 3")
        assert result["status"] == "success"
        assert result["result"] == "7"
    
    def test_expression_multiplication(self):
        """Test expression calculation: '4 * 5' -> 20"""
        result = self.service.calculate_from_expression("4 * 5")
        assert result["status"] == "success"
        assert result["result"] == "20"
    
    def test_expression_division(self):
        """Test expression calculation: '10 / 2' -> 5"""
        result = self.service.calculate_from_expression("10 / 2")
        assert result["status"] == "success"
        assert result["result"] == "5"