import unittest

class TestHelloUnitTest(unittest.TestCase):

    def test_add(self):
        actual = 1 + 1
        expected = 2
        self.assertEqual(expected, actual)

    def setUp(self):
        print('do something before test')
    def tearDown(self):
        print('do something after test')

if __name__ == '__main__':
    # execute methonds of test_**
    unittest.main()
