import unittest
import connect4_shell
from unittest.mock import patch
import connect4
import contextlib
import io


class TestConnect4Shell(unittest.TestCase):
    @patch("connect4_shell.input", return_value='12x12')
    def test_board_size(self, mocked_input):
        connect4_shell.board_size()
        expected = connect4.new_game(12, 12), ['12', '12']
        self.assertEqual(connect4_shell.board_size(), expected)

    @patch("connect4_shell.input", return_value='3x3')
    def test_board_size_invalid_input(self, mocked_input):
        with self.assertRaises(ValueError):
            connect4_shell.board_size()

    @patch("connect4_shell.input", return_value='5')
    def test_board_size_incorrect_format(self, mocked_input):
        with self.assertRaises(ValueError):
            connect4_shell.board_size()