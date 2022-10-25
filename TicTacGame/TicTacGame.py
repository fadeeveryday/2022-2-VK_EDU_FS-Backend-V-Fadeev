class TicTacGame():
    global wins_coordinates
    wins_coordinates = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
    ]  # список кортежей с победными комбинациями
    global board
    board =[1, 2, 3, 4, 5, 6, 7, 8, 9]

    def show_board(self):
        print('----------------')
        for i in range(3):
            print(
            '| ', board[0 + i * 3],
            '| ', board[1 + i * 3],
            '| ', board[2 + i * 3],
            '|'
            )
        print('----------------')

    def user_input(self, token):
        user_input = (input('Where to put ' + token + ' ?\n'))
        return user_input

    def validate_input(self, token, user_input):
        if not user_input.isdigit():
            raise TypeError('Error, input a number')
        user_input = int(user_input)
        if not 1 <= user_input <= 9:
            raise ValueError('Error, input a number from 1 to 9')
        if board[user_input - 1] in ['X', 'O']:
            raise ValueError('This square is already occupated')
        board[user_input - 1] = token  # ставим символ в выбранную ячейку
        return user_input

    def check_winner(self):
        for each in wins_coordinates:
            if (board[each[0] - 1] ==
                board[each[1] - 1] ==
                board[each[2] - 1]):
                return board[each[1] - 1]  # возврат знака победителя
        else:
            return False

    def start_game(self):
        counter= 0
        while True:
            try:
                self.show_board()
                if counter % 2 == 0:
                    input = self.user_input('X')
                    self.validate_input('X', input)
                else:
                    input = self.user_input('O')
                    self.validate_input('O', input)
                if counter > 3:
                    winner = self.check_winner()
                    if winner:
                        self.show_board()
                        print(winner, ' Win!')
                        break
                counter += 1
                if counter > 8:
                    self.show_board()
                    print('Draw!')
                    break
            except(ValueError, TypeError) as error:
                print(error)

if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
	