"""
History model representing a collection of past calculations that can be recalled by the user.
"""
from typing import List, Dict, Optional
from datetime import datetime


class History:
    """
    Represents a collection of past calculations that can be recalled by the user.
    """
    
    def __init__(self, max_size: int = 50):
        """
        Initialize the history.
        
        Args:
            max_size: Maximum number of calculations to retain (default 50)
        """
        self._id = self._generate_id()
        self._calculations: List[Dict] = []
        self._max_size = max_size
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
    
    def _generate_id(self) -> str:
        """Generate a unique identifier for the history."""
        import uuid
        return str(uuid.uuid4())
    
    def add_item(self, calculation_data: Dict):
        """
        Add a calculation to the history.
        
        Args:
            calculation_data: Dictionary containing calculation information
        """
        # Update the timestamp
        self._updated_at = datetime.now()
        
        # Add the calculation
        self._calculations.append(calculation_data)
        
        # If we exceed max size, remove the oldest item (FIFO)
        if len(self._calculations) > self._max_size:
            self._calculations.pop(0)
    
    def get_items(self) -> List[Dict]:
        """
        Get all calculations in the history.
        
        Returns:
            List of calculation dictionaries
        """
        # Return a copy to prevent external modification
        return self._calculations.copy()
    
    def get_item(self, index: int) -> Optional[Dict]:
        """
        Get a specific calculation by index.
        
        Args:
            index: Index of the calculation to retrieve
            
        Returns:
            Calculation dictionary or None if index out of range
        """
        if 0 <= index < len(self._calculations):
            return self._calculations[index]
        return None
    
    def clear(self):
        """Clear all calculations from the history."""
        self._calculations.clear()
        self._updated_at = datetime.now()
    
    def remove_item(self, index: int):
        """
        Remove a calculation at the specified index.
        
        Args:
            index: Index of the calculation to remove
        """
        if 0 <= index < len(self._calculations):
            self._calculations.pop(index)
            self._updated_at = datetime.now()
    
    def size(self) -> int:
        """Get the current number of calculations in history."""
        return len(self._calculations)
    
    def is_empty(self) -> bool:
        """Check if the history is empty."""
        return len(self._calculations) == 0
    
    @property
    def id(self) -> str:
        """Get the unique identifier for the history."""
        return self._id
    
    @property
    def max_size(self) -> int:
        """Get the maximum size of the history."""
        return self._max_size
    
    @max_size.setter
    def max_size(self, value: int):
        """Set the maximum size of the history."""
        if value <= 0:
            raise ValueError("Max size must be greater than 0")
        
        self._max_size = value
        # If the new max size is smaller, remove excess items
        while len(self._calculations) > self._max_size:
            self._calculations.pop(0)
    
    @property
    def created_at(self) -> datetime:
        """Get the creation timestamp."""
        return self._created_at
    
    @property
    def updated_at(self) -> datetime:
        """Get the last update timestamp."""
        return self._updated_at
    
    def to_dict(self) -> Dict:
        """Convert the history to a dictionary representation."""
        return {
            "id": self.id,
            "calculations": self._calculations,
            "max_size": self._max_size,
            "created_at": self._created_at.isoformat(),
            "updated_at": self._updated_at.isoformat(),
            "total_count": len(self._calculations)
        }