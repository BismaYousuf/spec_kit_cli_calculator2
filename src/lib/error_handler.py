"""
Error handling utilities for calculator operations.
"""


class CalculatorError(Exception):
    """Base exception class for calculator errors."""
    pass


class DivisionByZeroError(CalculatorError):
    """Exception raised when attempting to divide by zero."""
    def __init__(self, message="Error: Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)


class InvalidOperationError(CalculatorError):
    """Exception raised for invalid operations."""
    def __init__(self, message="Invalid operation"):
        self.message = message
        super().__init__(self.message)


class InvalidInputError(CalculatorError):
    """Exception raised for invalid input values."""
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)


class ErrorHandler:
    """
    Provides centralized error handling for calculator operations.
    """
    
    @staticmethod
    def handle_error(error: Exception) -> str:
        """
        Convert an exception to an appropriate error message.
        
        Args:
            error: The exception that occurred
            
        Returns:
            A user-friendly error message
        """
        if isinstance(error, ValueError) and "Division by zero" in str(error):
            return "Error: Cannot divide by zero"
        elif isinstance(error, ValueError) and "Square root of negative number" in str(error):
            return "Error: Cannot calculate square root of negative number"
        elif isinstance(error, ValueError) and "Factorial of negative number" in str(error):
            return "Error: Cannot calculate factorial of negative number"
        elif isinstance(error, ValueError) and "Factorial input is too large" in str(error):
            return "Error: Factorial input is too large"
        elif isinstance(error, ValueError):
            # Generic value error with the original message
            return f"Error: {str(error)}"
        else:
            # General error case
            return f"Unexpected error: {str(error)}"