"""
Logging utilities for calculator operations.
"""
import logging
import os
from datetime import datetime


class CalculatorLogger:
    """
    Provides logging functionality for calculator operations.
    """
    
    def __init__(self, log_file: str = "calculator.log", log_level: str = "INFO"):
        """
        Initialize the calculator logger.
        
        Args:
            log_file: Name of the log file
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self.logger = logging.getLogger("Calculator")
        
        # Only configure if not already configured
        if not self.logger.handlers:
            self.logger.setLevel(getattr(logging, log_level.upper()))
            
            # Create file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(getattr(logging, log_level.upper()))
            
            # Create console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(getattr(logging, log_level.upper()))
            
            # Create formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            
            # Add handlers to logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
    
    def log_calculation(self, operation: str, operand1: str, operand2: str, result: str, success: bool = True):
        """
        Log a calculation operation.
        
        Args:
            operation: The operation performed
            operand1: First operand
            operand2: Second operand (can be None for unary operations)
            result: The result of the calculation
            success: Whether the operation was successful
        """
        if success:
            self.logger.info(
                f"Calculation: {operand1} {operation} {operand2 or ''} = {result}"
            )
        else:
            self.logger.error(
                f"Calculation Failed: {operand1} {operation} {operand2 or ''} - {result}"
            )
    
    def log_error(self, error_message: str):
        """Log an error message."""
        self.logger.error(error_message)
    
    def log_info(self, info_message: str):
        """Log an info message."""
        self.logger.info(info_message)
    
    def log_warning(self, warning_message: str):
        """Log a warning message."""
        self.logger.warning(warning_message)