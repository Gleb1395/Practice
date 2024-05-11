import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_fibonacci_numbers(self):
        self.assertEqual(self.fibonacci(0), 0)
        self.assertEqual(self.fibonacci(1), 1)
        self.assertEqual(self.fibonacci(2), 1)
        self.assertEqual(self.fibonacci(3), 2)
        self.assertEqual(self.fibonacci(4), 3)
        self.assertEqual(self.fibonacci(5), 5)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(3.14)


