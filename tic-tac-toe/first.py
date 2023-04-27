import random


# A class to represent the Tic Tac Toe game board
class TicTacToe:
    def __init__(self):
        self.board = ['-'] * 9
        self.human_marker = 'X'
        self.computer_marker = 'O'

    # Display the current state of the game board
    def display_board(self):
        print(self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('--|---|--')
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('--|---|--')
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    # Check if the game board is full
    def is_board_full(self):
        return '-' not in self.board

    # Check if the game is over
    def is_game_over(self):
        return self.is_board_full() or self.check_winner(self.human_marker) or self.check_winner(self.computer_marker)

    # Check if the given marker has won the game
    def check_winner(self, marker):
        return ((self.board[0] == marker and self.board[1] == marker and self.board[2] == marker) or
                (self.board[3] == marker and self.board[4] == marker and self.board[5] == marker) or
                (self.board[6] == marker and self.board[7] == marker and self.board[8] == marker) or
                (self.board[0] == marker and self.board[3] == marker and self.board[6] == marker) or
                (self.board[1] == marker and self.board[4] == marker and self.board[7] == marker) or
                (self.board[2] == marker and self.board[5] == marker and self.board[8] == marker) or
                (self.board[0] == marker and self.board[4] == marker and self.board[8] == marker) or
                (self.board[2] == marker and self.board[4] == marker and self.board[6] == marker))

    # Make the given move on the game board
    def make_move(self, position, marker):
        self.board[position] = marker

    # Get the list of available moves on the game board
    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == '-']

    # Get the best move for the computer player using Minimax algorithm
    def get_computer_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.get_available_moves():
            self.make_move(move, self.computer_marker)
            score = self.minimax(False)
            self.make_move(move, '-')
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    # Minimax algorithm for finding the optimal move for the computer player
    def minimax(self, is_maximizer):
        if self.check_winner(self.human_marker):
            return -10
        elif self.check_winner(self.computer_marker):
            return 10
        elif self.is_board_full():
            return 0
        if is_maximizer:
            best_score = -float('inf')
            for move in self.get_available_moves():
                self.make_move(move, self.computer_marker)
                score = self.minimax(False)
                self.make_move(move, '-')
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves():
                self.make_move(move, self.human_marker)
                score = self.minimax(True)
                self.make_move(move, '-')
                best_score = min(score, best_score)
            return best_score


# Play the game
if __name__ == '__main__':
    game = TicTacToe()
    while not game.is_game_over():
        game.display_board()
        human_move = int(input('Enter your move (0-8)>> '))
        if game.board[human_move] == '-':
            game.make_move(human_move, game.human_marker)
        else:
            print('Invalid move! Try again.')
            continue
        if game.is_game_over():
            break
        print('Computer is making its move...')
        computer_move = game.get_computer_move()
        game.make_move(computer_move, game.computer_marker)
    game.display_board()
    if game.check_winner(game.human_marker):
        print('You win!')
    elif game.check_winner(game.computer_marker):
        print('Computer wins!')
    else:
        print('It\'s a tie!')
