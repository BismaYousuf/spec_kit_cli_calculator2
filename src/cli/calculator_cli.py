"""
Command-line interface for the calculator application.
"""
import sys
import argparse
import os
# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.calculator_service import CalculatorService
from src.models.history import History
from typing import Optional


class CalculatorCLI:
    """
    Command-line interface for the calculator application.
    """
    
    def __init__(self):
        """Initialize the CLI interface."""
        self.calculator_service = CalculatorService()
        self.history = History()
    
    def run(self, args: Optional[list] = None):
        """
        Run the calculator CLI with the given arguments.
        
        Args:
            args: Command line arguments (for testing purposes, otherwise uses sys.argv)
        """
        if args is None:
            args = sys.argv[1:]
        
        # If no arguments, run in interactive mode
        if not args:
            self.interactive_mode()
        else:
            self.parse_and_execute(args)
    
    def interactive_mode(self):
        """Run the calculator in interactive mode."""
        print("Calculator CLI - Interactive Mode")
        print("Commands:")
        print("  <expression> (e.g., '5 + 3', 'sqrt(16)')")
        print("  history - Show calculation history")
        print("  clear - Clear calculation history")
        print("  quit or exit - Exit the calculator")
        print()
        
        while True:
            try:
                user_input = input("calc> ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                elif user_input.lower() == 'history':
                    self.show_history()
                elif user_input.lower() == 'clear':
                    self.clear_history()
                elif user_input:
                    result = self.calculator_service.calculate_from_expression(user_input)
                    
                    if result["status"] == "success":
                        print(f"Result: {result['result']}")
                        
                        # Add to history
                        # Note: For simplicity, we'll just store the expression and result
                        # In a real implementation, we'd create a proper Calculation object
                        self.history.add_item({
                            "expression": user_input,
                            "result": result["result"]
                        })
                    else:
                        print(f"Error: {result['error']}")
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break
    
    def parse_and_execute(self, args: list):
        """
        Parse command line arguments and execute the appropriate action.
        
        Args:
            args: Command line arguments
        """
        parser = argparse.ArgumentParser(description="Calculator CLI")
        parser.add_argument("--operation", "-op", help="Operation to perform")
        parser.add_argument("--operand1", "-o1", help="First operand")
        parser.add_argument("--operand2", "-o2", help="Second operand (optional for unary operations)")
        parser.add_argument("--history", action="store_true", help="Show calculation history")
        
        parsed_args = parser.parse_args(args)
        
        if parsed_args.history:
            self.show_history()
        elif parsed_args.operation and parsed_args.operand1:
            # Perform validation before calculation
            try:
                from src.lib.validation import Validation
                Validation.validate_operation(parsed_args.operation)
                Validation.validate_operand(parsed_args.operand1)
                if parsed_args.operand2:
                    Validation.validate_operand(parsed_args.operand2)
            except ValueError as e:
                print(f"Validation Error: {str(e)}")
                return
            
            # Perform calculation with operation and operands
            result = self.calculator_service.calculate(
                parsed_args.operation, 
                parsed_args.operand1, 
                parsed_args.operand2
            )
            
            if result["status"] == "success":
                print(f"Result: {result['result']}")
                
                # Add to history
                self.history.add_item({
                    "expression": f"{parsed_args.operand1} {parsed_args.operation} {parsed_args.operand2 or ''}",
                    "result": result["result"]
                })
            else:
                print(f"Error: {result['error']}")
        elif len(args) == 1 and not parsed_args.history:
            # If single argument that is not --history, try to parse as expression
            expression = args[0]
            result = self.calculator_service.calculate_from_expression(expression)
            
            if result["status"] == "success":
                print(f"Result: {result['result']}")
                
                # Add to history
                self.history.add_item({
                    "expression": expression,
                    "result": result["result"]
                })
            else:
                print(f"Error: {result['error']}")
        else:
            parser.print_help()
    
    def show_history(self):
        """Show the calculation history."""
        history_data = self.history.get_items()
        if not history_data:
            print("No calculation history available.")
        else:
            print(f"Calculation History (last {len(history_data)} items):")
            for i, entry in enumerate(history_data, 1):
                print(f"  {i}. {entry['expression']} = {entry['result']}")
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history.clear()
        print("History cleared.")


if __name__ == "__main__":
    cli = CalculatorCLI()
    cli.run()