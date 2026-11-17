# Python Calculator

A friendly command-line calculator written in plain Python, with no extra installs.

![CI](https://github.com/arnabdharudra/python-calculator/actions/workflows/ci.yml/badge.svg)

## Features

- Add, subtract, multiply, divide, power, modulo, square root
- Asks again when you type something that isn't a number
- Clear error messages (division by zero, square root of a negative number)
- Clean output: `5` instead of `5.0`, and `0.3` instead of `0.30000000000000004`
- Automated tests run on every push

## Run it

Requires Python 3.8 or newer.

```bash
python calculator.py
```

```
=== Python Calculator ===

  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Power
  6. Modulo (remainder)
  7. Square root
  0. Exit
Choose an option: 4
First number: 7
Second number: 2
Result: 7 / 2 = 3.5
```

## Run the tests

```bash
python -m unittest -v
```
