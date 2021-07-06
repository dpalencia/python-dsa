from pdsa import fibonacci as fib
import unittest
from random import randrange


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        for repeat in range(4):
            i = randrange(10)
            self.assertEqual(fib.fibonacci(i), fib.fibonacci_dynamic(i))
        fiftieth_fib = 12586269025
        self.assertEqual(fib.fibonacci_dynamic(50), fiftieth_fib)
        self.assertEqual(fib.fibonacci_three_var(50), fiftieth_fib)
        # very slow -- self.assertEqual(fibonacci(50), fiftieth_fib)