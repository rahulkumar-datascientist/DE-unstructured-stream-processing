import os
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(True, False)  # add assertion here
        self.assertEqual(os.getenv("PRJ"), "unstructurednew")
        self.assertEqual(os.getenv("NEW_ENV"), "True")


if __name__ == '__main__':
    unittest.main()
