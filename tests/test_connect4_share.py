import connect4_share
import connect4
import unittest
import contextlib
import io


class TestConnect4Share(unittest.TestCase):
    def setUp(self) -> None:
        self.game_state = connect4.new_game(12, 12)

    def test_print_board(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.print_board(self.game_state, connect4.columns(self.game_state))
        self.assertEquals(output.getvalue(), '1  2  3  4  5  6  7  8  9 10 11 12\n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                             '.  .  .  .  .  .  .  .  .  .  .  .  \n')

    def test_drop(self):
        game_state_drop = connect4_share.drop(self.game_state, 4)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.print_board(game_state_drop, connect4.columns(self.game_state))
        self.assertEqual(output.getvalue(), '1  2  3  4  5  6  7  8  9 10 11 12\n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  R  .  .  .  .  .  .  .  .  \n')

    def test_drop_value_error(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.drop(self.game_state, 13)
        self.assertEqual(output.getvalue(), "That column doesn't exist, please choose another column\n")

    def test_drop_invalid_move_error(self):
        new_game_state = self.game_state
        for i in range(13):
            new_game_state = connect4_share.drop(new_game_state, 4)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.drop(new_game_state, 4)
        self.assertEqual(output.getvalue(), "That column is full, please choose another column\n")

    def test_drop_game_over_error(self):
        new_game_state = self.game_state
        for i in range(4):
            new_game_state = connect4_share.drop(new_game_state, 4)
            new_game_state = connect4_share.drop(new_game_state, 8)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.drop(new_game_state, 4)
        self.assertEqual(output.getvalue(), "The game is over, you cannot make another move\n")

    def test_pop(self):
        game_state_drop = connect4_share.drop(self.game_state, 4)
        game_state_drop = connect4_share.drop(game_state_drop, 4)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.pop(game_state_drop, 4)
        self.assertEqual(output.getvalue(), '1  2  3  4  5  6  7  8  9 10 11 12\n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  .  .  .  .  .  .  .  .  .  \n'
                                            '.  .  .  Y  .  .  .  .  .  .  .  .  \n')

    def test_pop_vaLue_error(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.pop(self.game_state, 13)
        self.assertEqual(output.getvalue(), "That column doesn't exist, please choose another column\n")

    def test_pop_game_over_error(self):
        new_game_state = self.game_state
        for i in range(4):
            new_game_state = connect4_share.drop(new_game_state, 4)
            new_game_state = connect4_share.drop(new_game_state, 8)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.pop(new_game_state, 4)
        self.assertEqual(output.getvalue(), "The game is over, you cannot make another move\n")

    def test_pop_invalid_move_error(self):
        new_game_state = self.game_state
        for i in range(2):
            new_game_state = connect4_share.drop(new_game_state, 4)
            new_game_state = connect4_share.drop(new_game_state, 6)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            connect4_share.pop(new_game_state, 6)
        self.assertEqual(output.getvalue(), "That column is empty or does not have one of your pieces, please choose "
                                            "another column\n")

    def test_get_winner(self):
        new_game_state = self.game_state
        for i in range(3):
            new_game_state = connect4_share.drop(new_game_state, 4)
            new_game_state = connect4_share.drop(new_game_state, 8)
        new_game_state = connect4_share.drop(new_game_state, 4)
        self.assertEqual(connect4_share.get_winner(new_game_state), "Red Won")

    def test_get_winner_with_no_winner(self):
        self.assertEqual(connect4_share.get_winner(self.game_state), None)