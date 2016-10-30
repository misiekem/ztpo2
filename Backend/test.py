import unittest
from app.GetUserId import GetUserId

class TestGetUserId(unittest.TestCase):
    def test_getId(self):
        x = GetUserId()
        self.assertEqual(x.getId("Krupa", "Krzysztof"), '926')


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetUserId)
    unittest.TextTestRunner().run(suite)