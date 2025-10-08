"""
Calculation model representing a single mathematical operation with input values, operation type, and result.
"""
import sys
import os
# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from datetime import datetime
from decimal import Decimal
from typing import Optional
from src.lib.validation import Validation
from src.lib.math_utils import MathUtils


class Calculation:
    """
    Represents a single mathematical operation with input values, operation type, and result.
    """
    
    def __init__(self, operand1: str, operand2: Optional[str], operation: str, 
                 result: Decimal = None, expression: str = None):
        """
        Initialize a calculation object.
        
        Args:
            operand1: First number in the operation (as string to preserve precision)
            operand2: Second number in the operation (as string to preserve precision, nullable for unary operations)
            operation: Mathematical operation symbol (+, -, *, /, ^, sqrt, %, !, etc.)
            result: Calculated result (optional)
            expression: Full expression as entered by user (optional)
        """
        self._id = self._generate_id()
        self._operand1 = self._validate_operand(operand1, "operand1")
        self._operand2 = self._validate_operand(operand2, "operand2") if operand2 is not None else None
        self._operation = self._validate_operation(operation)
        self._result = result
        self._timestamp = datetime.now()
        self._expression = expression if expression else self._create_expression()
    
    def _generate_id(self) -> str:
        """Generate a unique identifier for the calculation."""
        import uuid
        return str(uuid.uuid4())
    
    def _validate_operand(self, operand: str, operand_name: str) -> Decimal:
        """Validate an operand according to requirements."""
        if operand is None:
            return None
        
        if not Validation.is_valid_number(operand):
            raise ValueError(f"Invalid number format for {operand_name}: {operand}")
        
        return Validation.validate_operand(operand)
    
    def _validate_operation(self, operation: str) -> str:
        """Validate the operation according to requirements."""
        if not Validation.is_valid_operation(operation):
            raise ValueError(f"Invalid operation: {operation}")
        return operation
    
    def _create_expression(self) -> str:
        """Create an expression string from the operation components."""
        if self._operation == 'sqrt':
            return f"sqrt({self._operand1})"
        elif self._operation == 'factorial':
            return f"factorial({self._operand1})"
        elif self._operand2 is not None:
            op_symbol_map = {
                'add': '+',
                'subtract': '-',
                'multiply': '*',
                'divide': '/',
                'power': '^',
                'percentage': '% of'
            }
            symbol = op_symbol_map.get(self._operation, self._operation)
            return f"{self._operand1} {symbol} {self._operand2}"
        else:
            return f"{self._operand1} {self._operation}"
    
    def execute(self) -> Decimal:
        """
        Execute the calculation and store the result.
        
        Returns:
            The calculated result as a Decimal
        """
        calc_service = MathUtils()
        
        if self._operation == "add":
            self._result = calc_service.add(str(self._operand1), str(self._operand2))
        elif self._operation == "subtract":
            self._result = calc_service.subtract(str(self._operand1), str(self._operand2))
        elif self._operation == "multiply":
            self._result = calc_service.multiply(str(self._operand1), str(self._operand2))
        elif self._operation == "divide":
            self._result = calc_service.divide(str(self._operand1), str(self._operand2))
        elif self._operation == "power":
            self._result = calc_service.power(str(self._operand1), str(self._operand2))
        elif self._operation == "sqrt":
            self._result = calc_service.sqrt(str(self._operand1))
        elif self._operation == "percentage":
            self._result = calc_service.percentage(str(self._operand1), str(self._operand2))
        elif self._operation == "factorial":
            self._result = calc_service.factorial(str(self._operand1))
        else:
            raise ValueError(f"Unsupported operation: {self._operation}")
        
        return self._result
    
    @property
    def id(self) -> str:
        """Get the unique identifier for the calculation."""
        return self._id
    
    @property
    def operand1(self) -> Decimal:
        """Get the first operand."""
        return self._operand1
    
    @property
    def operand2(self) -> Optional[Decimal]:
        """Get the second operand."""
        return self._operand2
    
    @property
    def operation(self) -> str:
        """Get the operation type."""
        return self._operation
    
    @property
    def result(self) -> Decimal:
        """Get the calculation result."""
        if self._result is None:
            # Execute the calculation if not already done
            self.execute()
        return self._result
    
    @property
    def timestamp(self) -> datetime:
        """Get the calculation timestamp."""
        return self._timestamp
    
    @property
    def expression(self) -> str:
        """Get the expression string."""
        return self._expression
    
    def to_dict(self) -> dict:
        """Convert the calculation to a dictionary representation."""
        return {
            "id": self.id,
            "operand1": str(self.operand1),
            "operand2": str(self.operand2) if self.operand2 is not None else None,
            "operation": self.operation,
            "result": str(self.result),
            "timestamp": self.timestamp.isoformat(),
            "expression": self.expression
        }
    
    def __str__(self) -> str:
        """String representation of the calculation."""
        return f"{self.expression} = {self.result}"