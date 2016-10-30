import unittest
import Backend.app
from unittest import *
from Backend.app.GetUserId import GetUserId


class TestGetUserId(TestCase):
    def test_getId2(self):
        x = GetUserId()
        self.assertEqual(x.getId("Krupa", "Krzysztof"), '926')


if __name__ == '__test__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetUserId)
    unittest.TextTestRunner().run(suite)