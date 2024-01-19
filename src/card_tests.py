import unittest
from Card import *


class TestCardMethods(unittest.TestCase):

    def setUp(self) -> None:
        self._c = Card(39)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_number_name(self):
        self.assertEqual(self._c.number_name(), 'Q')

    def test_number_name(self):
        self.assertEqual(self._c.suit_name(), 'S')


if __name__ == '__main__':
    unittest.main()
