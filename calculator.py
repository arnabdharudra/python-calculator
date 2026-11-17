"""A simple command-line calculator."""

import math

OPERATIONS = {
    "1": ("Add", "+"),
    "2": ("Subtract", "-"),
    "3": ("Multiply", "*"),
    "4": ("Divide", "/"),
    "5": ("Power", "^"),
    "6": ("Modulo (remainder)", "%"),
    "7": ("Square root", "sqrt"),
}
EXIT_CHOICE = "0"


def calculate(op, a, b=None):
    """Return the result of applying `op` to the numbers. Raises ValueError on bad input."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    if op == "^":
        return a**b
    if op == "%":
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")
        return a % b
    if op == "sqrt":
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
    raise ValueError(f"Unknown operation: {op}")


def format_number(value):
    """Show 5.0 as 5, keep decimals otherwise."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(round(value, 10))


def read_number(prompt, input_fn=input):
    """Keep asking until the user types a valid number."""
    while True:
        raw = input_fn(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' is not a number, please try again.")


def main(input_fn=input):
    print("=== Python Calculator ===")
    while True:
        print()
        for key, (name, _) in OPERATIONS.items():
            print(f"  {key}. {name}")
        print(f"  {EXIT_CHOICE}. Exit")

        choice = input_fn("Choose an option: ").strip()
        if choice == EXIT_CHOICE:
            print("Goodbye!")
            return
        if choice not in OPERATIONS:
            print("Invalid choice, please pick a number from the menu.")
            continue

        _, op = OPERATIONS[choice]
        a = read_number("First number: ", input_fn)
        b = None if op == "sqrt" else read_number("Second number: ", input_fn)

        try:
            result = calculate(op, a, b)
        except ValueError as err:
            print(f"Error: {err}")
            continue

        expression = f"sqrt({format_number(a)})" if op == "sqrt" else f"{format_number(a)} {op} {format_number(b)}"
        print(f"Result: {expression} = {format_number(result)}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
