# Quickstart Guide: Calculator with All Arithmetic Operations

## Prerequisites

- Python 3.11 or higher
- pip package manager

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the calculator:
   ```bash
   python -m src.cli.calculator_cli
   ```

## Development

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Run tests:
   ```bash
   pytest
   ```

3. Run specific test for calculator service:
   ```bash
   pytest tests/unit/test_calculator_service.py
   ```

## Running Calculations

The calculator supports the following operations:
- Basic: addition (+), subtraction (-), multiplication (*), division (/)
- Advanced: power (^ or **), square root (sqrt), percentage (%), factorial (!)

Examples:
- `5 + 3` → `8`
- `4 ^ 2` → `16`
- `sqrt(16)` → `4`

## Error Handling

The calculator handles the following errors:
- Division by zero: Shows "Error: Cannot divide by zero"
- Invalid operations: Shows descriptive error message
- Malformed expressions: Shows "Invalid expression format"

## Project Structure

```
src/
├── models/
│   ├── calculation.py     # Calculation entity
│   └── history.py         # History entity
├── services/
│   ├── calculator_service.py   # Core calculation logic
│   └── history_service.py      # History management
├── cli/
│   └── calculator_cli.py       # Command-line interface
└── lib/
    └── math_utils.py           # Mathematical utilities

tests/
├── unit/                     # Unit tests
├── integration/             # Integration tests
└── contract/                # Contract tests
```

## Testing

Run the full test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src
```

The project follows Test-First (TDD) principle, so all mathematical operations must have comprehensive unit tests covering accuracy requirements.