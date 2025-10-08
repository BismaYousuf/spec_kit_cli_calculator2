"""
Mathematical utilities for calculator operations with precision handling.
"""
from decimal import Decimal, getcontext, InvalidOperation
import math


class MathUtils:
    """
    Provides mathematical operations with high precision and accuracy.
    """
    
    # Set precision for decimal operations to 10 decimal places as per spec
    getcontext().prec = 10
    
    @staticmethod
    def add(operand1: str, operand2: str) -> Decimal:
        """Perform addition with decimal precision."""
        num1 = Decimal(operand1)
        num2 = Decimal(operand2)
        return num1 + num2
    
    @staticmethod
    def subtract(operand1: str, operand2: str) -> Decimal:
        """Perform subtraction with decimal precision."""
        num1 = Decimal(operand1)
        num2 = Decimal(operand2)
        return num1 - num2
    
    @staticmethod
    def multiply(operand1: str, operand2: str) -> Decimal:
        """Perform multiplication with decimal precision."""
        num1 = Decimal(operand1)
        num2 = Decimal(operand2)
        return num1 * num2
    
    @staticmethod
    def divide(operand1: str, operand2: str) -> Decimal:
        """Perform division with decimal precision, handling division by zero."""
        num1 = Decimal(operand1)
        num2 = Decimal(operand2)
        
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        
        return num1 / num2
    
    @staticmethod
    def power(operand1: str, operand2: str) -> Decimal:
        """Perform power operation with decimal precision."""
        num1 = Decimal(operand1)
        num2 = Decimal(operand2)
        return num1 ** num2
    
    @staticmethod
    def sqrt(operand1: str) -> Decimal:
        """Perform square root operation with decimal precision."""
        num = Decimal(operand1)
        
        if num < 0:
            raise ValueError("Square root of negative number is not allowed")
        
        return num.sqrt()
    
    @staticmethod
    def percentage(operand1: str, operand2: str) -> Decimal:
        """Calculate percentage: operand1 % of operand2."""
        num1 = Decimal(operand1)
        num2 = Decimal(operand2)
        return (num1 / 100) * num2
    
    @staticmethod
    def factorial(operand1: str) -> int:
        """Calculate factorial of operand1."""
        num = int(Decimal(operand1))
        
        if num < 0:
            raise ValueError("Factorial of negative number is not allowed")
        
        if num > 100:  # Prevent extremely large calculations
            raise ValueError("Factorial input is too large")
        
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result