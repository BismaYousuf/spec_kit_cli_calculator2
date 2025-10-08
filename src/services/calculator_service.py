"""
Calculator service implementing the business logic for calculations.
"""
import sys
import os
# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from decimal import Decimal
from typing import Optional
from src.models.calculator import Calculator
from src.lib.error_handler import ErrorHandler
from src.lib.performance_monitor import PerformanceMonitor
from src.lib.logger import CalculatorLogger


class CalculatorService:
    """
    Service class that provides calculator functionality with error handling and performance monitoring.
    """
    
    def __init__(self):
        """Initialize the calculator service."""
        self.calculator = Calculator()
        self.error_handler = ErrorHandler()
        self.performance_monitor = PerformanceMonitor()
        self.logger = CalculatorLogger()
    
    @PerformanceMonitor.time_operation("basic_calculation")
    def calculate(self, operation: str, operand1: str, operand2: Optional[str] = None) -> dict:
        """
        Perform a calculation with error handling and performance monitoring.
        
        Args:
            operation: The operation to perform (add, subtract, multiply, divide, power, sqrt, percentage, factorial)
            operand1: First operand as string
            operand2: Second operand as string (optional for unary operations)
            
        Returns:
            Dictionary with result or error information
        """
        try:
            result = self.calculator.calculate(operation, operand1, operand2)
            self.logger.log_calculation(operation, operand1, operand2, str(result), success=True)
            return {
                "result": str(result),
                "status": "success"
            }
        except Exception as e:
            error_message = self.error_handler.handle_error(e)
            self.logger.log_calculation(operation, operand1, operand2, error_message, success=False)
            return {
                "error": error_message,
                "status": "error"
            }
    
    def calculate_with_calculation_object(self, operation: str, operand1: str, operand2: Optional[str] = None) -> dict:
        """
        Perform a calculation and return a Calculation object.
        
        Args:
            operation: The operation to perform (add, subtract, multiply, divide, power, sqrt, percentage, factorial)
            operand1: First operand as string
            operand2: Second operand as string (optional for unary operations)
            
        Returns:
            Dictionary with Calculation object or error information
        """
        try:
            calculation = self.calculator.calculate_with_calculation_object(operation, operand1, operand2)
            self.logger.log_calculation(operation, operand1, operand2, str(calculation.result), success=True)
            return {
                "calculation": calculation.to_dict(),
                "status": "success"
            }
        except Exception as e:
            error_message = self.error_handler.handle_error(e)
            self.logger.log_calculation(operation, operand1, operand2, error_message, success=False)
            return {
                "error": error_message,
                "status": "error"
            }
    
    def calculate_from_expression(self, expression: str) -> dict:
        """
        Parse and calculate from a simple expression string.
        """
        try:
            result = self.calculator.calculate_from_expression(expression)
            self.logger.log_info(f"Expression calculation: {expression} = {result}")
            return {
                "result": str(result),
                "status": "success"
            }
        except Exception as e:
            error_message = self.error_handler.handle_error(e)
            self.logger.log_error(f"Expression calculation failed: {expression} - {error_message}")
            return {
                "error": error_message,
                "status": "error"
            }