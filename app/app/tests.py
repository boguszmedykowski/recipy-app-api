"""
Sample tests
"""

from django.test import SimpleTestCase
from . import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers toghether."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substrac_numbers(self):
        """Test substracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
