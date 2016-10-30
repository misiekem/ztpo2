import unittest
import app
from unittest import *
from GetUserId import *


class TestGetUserId(TestCase):
    def test_getId2(self):
        x = GetUserId()
        self.assertEqual(x.getId("Krupa", "Krzysztof"), '926')


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetUserId)
    unittest.TextTestRunner().run(suite)