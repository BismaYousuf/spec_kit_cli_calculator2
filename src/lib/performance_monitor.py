"""
Performance monitoring for calculator operations.
"""
import time
from typing import Callable, Any
from functools import wraps


class PerformanceMonitor:
    """
    Provides performance monitoring for calculator operations.
    """
    
    @staticmethod
    def time_operation(operation_name: str = None) -> Callable:
        """
        Decorator to time calculator operations.
        
        Args:
            operation_name: Name of the operation being timed (optional)
        """
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    end_time = time.time()
                    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                    if operation_name:
                        print(f"DEBUG: Operation '{operation_name}' took {execution_time:.2f} ms")
                    else:
                        print(f"DEBUG: Operation took {execution_time:.2f} ms")
            return wrapper
        return decorator
    
    @staticmethod
    def check_performance_threshold(execution_time_ms: float, threshold_ms: float = 100) -> bool:
        """
        Check if execution time is within acceptable threshold.
        
        Args:
            execution_time_ms: Execution time in milliseconds
            threshold_ms: Threshold in milliseconds (default: 100ms for basic ops)
            
        Returns:
            True if within threshold, False otherwise
        """
        return execution_time_ms <= threshold_ms