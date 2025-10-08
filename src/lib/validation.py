"""
Input validation utilities for calculator operations.
"""
import re
from decimal import Decimal, InvalidOperation


class Validation:
    """
    Provides input validation for calculator operations.
    """
    
    @staticmethod
    def is_valid_number(value: str) -> bool:
        """Check if the input string represents a valid number."""
        if not value:
            return False
        
        # Allow numbers with optional decimal point and sign
        pattern = r'^[-+]?(\d+\.?\d*|\.\d+)$'
        return bool(re.match(pattern, value))
    
    @staticmethod
    def is_valid_operation(operation: str) -> bool:
        """Check if the operation string is one of the supported operations."""
        valid_operations = {'add', 'subtract', 'multiply', 'divide', 'power', 'sqrt', 'percentage', 'factorial'}
        return operation in valid_operations
    
    @staticmethod
    def validate_operand(operand: str) -> Decimal:
        """Validate and convert operand string to Decimal."""
        if not Validation.is_valid_number(operand):
            raise ValueError(f"Invalid number format: {operand}")
        
        try:
            decimal_value = Decimal(operand)
            return decimal_value
        except (InvalidOperation, ValueError):
            raise ValueError(f"Cannot convert to number: {operand}")
    
    @staticmethod
    def validate_operation(operation: str) -> str:
        """Validate operation string."""
        if not Validation.is_valid_operation(operation):
            raise ValueError(f"Invalid operation: {operation}")
        return operation
    
    @staticmethod
    def validate_format(operand1: str, operand2: str = None, operation: str = None) -> tuple:
        """Validate the format of operation components."""
        # Validate operation type if provided
        if operation:
            Validation.validate_operation(operation)
        
        # Validate operand1
        Validation.validate_operand(operand1)
        
        # Validate operand2 if provided (not for unary operations like sqrt, factorial)
        if operand2 and operation not in ['sqrt', 'factorial']:
            Validation.validate_operand(operand2)
        
        return True