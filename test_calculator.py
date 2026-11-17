import unittest

from calculator import calculate, format_number, main


class CalculateTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate("+", 2, 3), 5)
        self.assertEqual(calculate("-", 2, 3), -1)
        self.assertEqual(calculate("*", 4, 2.5), 10)
        self.assertEqual(calculate("/", 7, 2), 3.5)
        self.assertEqual(calculate("^", 2, 10), 1024)
        self.assertEqual(calculate("%", 10, 3), 1)
        self.assertEqual(calculate("sqrt", 81), 9)

    def test_errors(self):
        for op, a, b in [("/", 1, 0), ("%", 1, 0), ("sqrt", -4, None), ("?", 1, 1)]:
            with self.assertRaises(ValueError):
                calculate(op, a, b)

    def test_format_number(self):
        self.assertEqual(format_number(5.0), "5")
        self.assertEqual(format_number(0.1 + 0.2), "0.3")


class MenuTests(unittest.TestCase):
    def run_menu(self, inputs):
        answers = iter(inputs)
        printed = []
        import builtins

        original = builtins.print
        builtins.print = lambda *a, **k: printed.append(" ".join(map(str, a)))
        try:
            main(input_fn=lambda _prompt: next(answers))
        finally:
            builtins.print = original
        return "\n".join(printed)

    def test_full_session(self):
        out = self.run_menu(["1", "2", "3", "4", "abc", "8", "0", "9", "7", "16", "0"])
        self.assertIn("Result: 2 + 3 = 5", out)
        self.assertIn("'abc' is not a number", out)
        self.assertIn("Error: Division by zero", out)
        self.assertIn("Invalid choice", out)
        self.assertIn("Result: sqrt(16) = 4", out)
        self.assertIn("Goodbye!", out)


if __name__ == "__main__":
    unittest.main()
