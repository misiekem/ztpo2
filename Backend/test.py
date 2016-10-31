import unittest
from app.GetUserId import GetUserId
from app.GetNumberOfPubs import GetNumberOfPublications


class TestGetUserId(unittest.TestCase):
    '''Check if the getId method returns correct user id for given surname and name'''

    def test_getId(self):
        x = GetUserId()
        self.assertEqual(x.getId("Krupa", "Krzysztof"), '926')
        self.assertEqual(x.getId("Góra", "Marta"), '3322')
        self.assertEqual(x.getId("Czyżycki", "Wojciech"), '3205')


class TestGetNumberOfPublications(unittest.TestCase):
    '''Check if the getNumberOfPublications method works properly'''

    def test_getNumberOfPublications(self):
        z = GetNumberOfPublications()
        self.assertEqual(z.getNumberOfPublications('926'),'36')
        self.assertEqual(z.getNumberOfPublications('3322'),'14')
        self.assertEqual(z.getNumberOfPublications('1386'), '24')
        self.assertEqual(z.getNumberOfPublications('3438'), '22')

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetUserId)
    unittest.TextTestRunner().run(suite)
