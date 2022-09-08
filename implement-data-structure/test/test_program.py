import unittest.mock
from unittest import TestCase, mock

from program import get_user_input


@unittest.mock.patch('builtins.input', side_effect=['4 '])
class Test(TestCase):
    def test_get_user_input_int(self, mock):
        self.assertTrue(get_user_input(), 4)

        # This would work if I didn't have an infinite loop checking the input
        # with mock.patch('builtins.input', return_value="n"):
        #     assert get_user_input() == "Your input was not a valid integer. Please enter a valid integer"

