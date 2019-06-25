from unittest import TestCase
import task2


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_is_year_4(self):
        """Test for is _prime"""
        self.assertFalse(task2.is_year_4(1983))
        self.assertTrue(task2.is_year_4(1984))

    def test_is_year_400(self):
        """Test for is _prime"""
        self.assertFalse(task2.is_year_400(1900))
        self.assertTrue(task2.is_year_400(2000))

    def test_is_year_100(self):
        """Test for is _prime"""
        self.assertFalse(task2.is_year_400(1900))
        self.assertTrue(task2.is_year_400(2050))

    def test_is_year_leap(self):
        """Test for is _prime"""
        self.assertFalse(task2.is_year_leap(1900))
        self.assertFalse(task2.is_year_leap(1983))
        self.assertTrue(task2.is_year_leap(2000))
        self.assertTrue(task2.is_year_leap(1984))

    def tearDown(self):
        """Finish"""
