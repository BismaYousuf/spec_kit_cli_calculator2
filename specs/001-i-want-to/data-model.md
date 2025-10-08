# Data Model: Calculator with All Arithmetic Operations

## Entities

### Calculation

**Description**: Represents a single mathematical operation with input values, operation type, and result

**Fields**:
- `id`: Unique identifier for the calculation (string/UUID)
- `operand1`: First number in the operation (Decimal)
- `operand2`: Second number in the operation (Decimal, nullable for unary operations)
- `operation`: Mathematical operation symbol (+, -, *, /, ^, sqrt, %, !, etc.) (string)
- `result`: Calculated result (Decimal)
- `timestamp`: When the calculation was performed (datetime)
- `expression`: Full expression as entered by user (string, e.g., "5 + 3")

**Validation Rules**:
- `operand1` and `operand2` must be valid numbers according to precision requirements
- `operation` must be one of the supported mathematical operations
- `result` must match the expected mathematical outcome
- Division by zero must be prevented

**Relationships**:
- Belongs to a History (one-to-many)

### History

**Description**: Represents a collection of past calculations that can be recalled by the user

**Fields**:
- `id`: Unique identifier for the history (string/UUID)
- `calculations`: List of Calculation objects (array of Calculation)
- `max_size`: Maximum number of calculations to retain (integer, default 50)
- `created_at`: When the history was first created (datetime)
- `updated_at`: When the history was last updated (datetime)

**Validation Rules**:
- Must not exceed max_size (maintains performance by limiting history length)
- Oldest calculations should be removed when max_size is reached (FIFO)

**State Transitions**:
- New History starts empty
- After each calculation, if History exists, Calculation is added to the list
- When max_size is reached, oldest Calculation is removed before adding new one

## Data Flow

1. User inputs a calculation (e.g., "5 + 3")
2. System creates a Calculation entity with the provided values
3. System validates the input and performs the calculation
4. System stores the result in the Calculation entity
5. System adds the Calculation to the History entity
6. System returns the result to the user
7. If History exceeds max_size, oldest Calculation is removed