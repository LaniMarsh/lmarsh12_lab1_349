import unittest
from lmarsh12_lab1 import singleton

class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        self.assertEqual(singleton("unique-64"), -64)

    def test_singleton_01(self):
        self.assertEqual(singleton("unique-12"), -12)

    def test_singleton_02(self):
        self.assertEqual(singleton("unique-3"), -3)

    def test_singleton_03(self):
        self.assertEqual(singleton("unique39"), 39)

    def test_singleton_04(self):
        self.assertEqual(singleton("unique18"), 18)

if __name__ == "__main__":
    unittest.main()
