import unittest
from inc_dec import increment, decrement


class Test_IncDec(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(10), 11)

    def test_decrement(self):
        self.assertEqual(decrement(20), 19)


if __name__ == '__main__':
    unittest.main()
