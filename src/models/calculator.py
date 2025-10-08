"""
Base calculator model implementing core calculation operations.
"""
import sys
import os
# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from decimal import Decimal
from typing import Optional, Union
from src.lib.math_utils import MathUtils
from src.lib.validation import Validation
from .calculation import Calculation


class Calculator:
    """
    Base calculator model implementing core calculation operations with validation.
    """
    
    def __init__(self):
        """Initialize the calculator."""
        self.math_utils = MathUtils()
        self.validation = Validation()
    
    def calculate(self, operation: str, operand1: str, operand2: Optional[str] = None) -> Decimal:
        """
        Perform a calculation based on the operation and operands.
        
        Args:
            operation: The operation to perform (add, subtract, multiply, divide, power, sqrt, percentage, factorial)
            operand1: First operand as string
            operand2: Second operand as string (optional for unary operations)
            
        Returns:
            Decimal result of the calculation
        """
        # Validate the operation and operands
        self.validation.validate_operation(operation)
        self.validation.validate_operand(operand1)
        
        if operation not in ['sqrt', 'factorial']:
            if operand2 is None:
                raise ValueError(f"Operation '{operation}' requires two operands")
            self.validation.validate_operand(operand2)
        
        # Perform the appropriate calculation based on the operation
        if operation == "add":
            return self.math_utils.add(operand1, operand2)
        elif operation == "subtract":
            return self.math_utils.subtract(operand1, operand2)
        elif operation == "multiply":
            return self.math_utils.multiply(operand1, operand2)
        elif operation == "divide":
            return self.math_utils.divide(operand1, operand2)
        elif operation == "power":
            return self.math_utils.power(operand1, operand2)
        elif operation == "sqrt":
            # For square root, we only use operand1
            return self.math_utils.sqrt(operand1)
        elif operation == "percentage":
            return self.math_utils.percentage(operand1, operand2)
        elif operation == "factorial":
            # For factorial, we only use operand1 and convert to int
            return self.math_utils.factorial(operand1)
        else:
            raise ValueError(f"Unsupported operation: {operation}")
    
    def calculate_with_calculation_object(self, operation: str, operand1: str, operand2: Optional[str] = None) -> Calculation:
        """
        Perform a calculation and return a Calculation object.
        
        Args:
            operation: The operation to perform (add, subtract, multiply, divide, power, sqrt, percentage, factorial)
            operand1: First operand as string
            operand2: Second operand as string (optional for unary operations)
            
        Returns:
            Calculation object representing the operation
        """
        calculation = Calculation(operand1, operand2, operation)
        calculation.execute()
        return calculation
    
    def calculate_from_expression(self, expression: str) -> Decimal:
        """
        Parse and calculate from an expression string.
        Supports basic format: "number operator number" (e.g., "5 + 3")
        Supports unary format: "operation(number)" (e.g., "sqrt(16)")
        """
        expression = expression.strip()
        
        # Handle unary operations like sqrt(16), factorial(5)
        import re
        unary_pattern = r'(\w+)\(([^)]+)\)'
        match = re.match(unary_pattern, expression)
        
        if match:
            operation_name, operand = match.groups()
            operation_map = {
                'sqrt': 'sqrt',
                'factorial': 'factorial'
            }
            
            if operation_name in operation_map:
                return self.calculate(operation_map[operation_name], operand)
            else:
                raise ValueError(f"Unsupported unary operation: {operation_name}")
        
        # Handle binary operations like "5 + 3"
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError(f"Invalid expression format: {expression}")
        
        operand1, operator, operand2 = parts
        
        # Map string operators to operation names
        operator_map = {
            '+': 'add',
            '-': 'subtract',
            '*': 'multiply', 
            '/': 'divide',
            '^': 'power',
            '**': 'power',
            '%': 'percentage'  # Note: This would be for percentage calculation
        }
        
        if operator in operator_map:
            operation = operator_map[operator]
            return self.calculate(operation, operand1, operand2)
        else:
            raise ValueError(f"Unsupported operator: {operator}")