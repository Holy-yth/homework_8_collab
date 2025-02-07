import unittest
from exercise_4 import chunking_by


class CodingRoomsUnitTests(unittest.TestCase):

    def setUp(self):
        # Setup code here (if required, replace the 'pass')
        pass

    def tearDown(self):
        # Teardown code here (if required, replace the 'pass')
        pass

    def test_default_case(self):
        # Your test case logic here (replace the example assertion below)
        # You may also rename this to any function in the form of 'test_your_test_name(self):'
        self.assertTrue(True)

    def test_chunking_by(self):

        self.assertEqual(chunking_by([5, 4, 7, 3, 4, 5, 4], 3),
                         [[5, 4, 7], [3, 4, 5], [4]])

        self.assertEqual(chunking_by([3, 4, 5], 1),  [[3], [4], [5]])


if __name__ == '__main__':
    unittest.main()
