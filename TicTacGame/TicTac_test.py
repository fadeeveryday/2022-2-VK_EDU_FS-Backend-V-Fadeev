from TicTacGame import TicTacGame
from unittest import TestCase, main

class TicTacGameTest(TestCase):
    """Test class"""
    global game
    game = TicTacGame()

    def test_correct_input(self):
        self.assertEqual(game.validate_input('X', '1'), 1)

    def test_correct_input(self):
        self.assertEqual(game.validate_input('O', '9'), 9)

    def test_not_list_number(self):
        with self.assertRaises(ValueError) as error:
            game.validate_input('X', '12')
        self.assertEqual('Error, input a number from 1 to 9', error.exception.args[0])

    def test_not_a_number(self):
        with self.assertRaises(TypeError) as error:
            game.validate_input('O', 'qwe')
        self.assertEqual('Error, input a number', error.exception.args[0])
    

    
if __name__ == '__main__':
    main()