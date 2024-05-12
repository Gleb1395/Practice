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
        self.assertEqual(self.fibonacci(1), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(3.14)

    def test_empty_value(self):
        with self.assertRaises(TypeError):
            self.fibonacci()
    def test_big_value(self):
        with self.assertRaises(RecursionError):
            self.fibonacci(500000)
    def test_non_string_value(self):
        with self.assertRaises(ValueError):
            self.fibonacci('asde')

    def test_check_cache(self):
        self.fibonacci(5)
        self.assertEqual(self.fibonacci.cache, [0, 1, 1, 2, 3, 5])

        self.fibonacci(7)
        self.assertEqual(self.fibonacci.cache, [0, 1, 1, 2, 3, 5, 8, 13])




