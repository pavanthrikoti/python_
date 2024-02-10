class ConnectFour:
    """
    Class for creating a connect four game
    """

    def __init__(self, height=6, width=7):
        self.height = height
        self.width = width
        self.board = [[' ' for x in range(width)] for i in range(height)]

    def get_column(self, index):
        """
        Returns a column at the specified index

        :param index: Index at which column will be returned
        """
        return [i[index] for i in self.board]

    def get_row(self, index):
        """
        Returns a row at the specified index

        :param index: Index at which row will be returned
        """
        return self.board[index]

    def get_diagonals(self):
        """
        Returns all the diagonals in the game
        """

        diagonals = []

        for i in range(self.height + self.width - 1):
            diagonals.append([])
            for j in range(max(i - self.height + 1, 0), min(i + 1, self.height)):
                diagonals[i].append(self.board[self.height - i + j - 1][j])

        for i in range(self.height + self.width - 1):
            diagonals.append([])
            for j in range(max(i - self.height + 1, 0), min(i + 1, self.height)):
                diagonals[i].append(self.board[i - j][j])

        return diagonals

    def make_move(self, team, col):
        """
        Simulates a move and puts a 0/1 in the specified column
        """
        if ' ' not in self.get_column(col):
            return self.board
        i = self.height - 1
        while self.board[i][col] != ' ':
            i -= 1
        self.board[i][col] = team
        return self.board

    def check_win(self):
        """
        Checks self.board if either user has four in a row
        """

        four_in_a_row = [['0', '0', '0', '0'], ['1', '1', '1', '1']]

        # Check rows
        for i in range(self.height):
            for j in range(self.width - 3):
                if self.get_row(i)[j:j + 4] in four_in_a_row:
                    return self.board[i][j]

        # Check columns
        for i in range(self.width):
            for j in range(self.height - 3):
                if self.get_column(i)[j:j + 4] in four_in_a_row:
                    return self.board[j][i]

        # Check diagonals
        for i in self.get_diagonals():
            for j, _ in enumerate(i):
                if i[j:j + 4] in four_in_a_row:
                    return i[j]

        return None


def start_game():
    """
    Starts a game of ConnectFour
    """
    game = ConnectFour()

    while True:

        for i in game.board:
            print(i)
        if game.check_win() is not None:
            break

        col = int(input('Team 0 choose column: ')) - 1
        game.make_move('0', col)

        for i in game.board:
            print(i)
        if game.check_win() is not None:
            break
        col = int(input('Team 1 choose column: ')) - 1
        game.make_move('1', col)

    print('Thank you for playing')


if __name__ == '__main__':
    start_game()
