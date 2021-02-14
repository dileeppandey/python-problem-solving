"""
Battleship is a game in which one player (Player One) places ships, and the other player (Player Two) guesses their
location (this is a simplified version of children's game)

Game Details:

The game is played on a 6x6 grid. Squares are referenced by a letter and number like the following:

  | 1 2 3 4 5 6
--+------------
A |
B |
C |
D |
E |
F |

B3 Refers tho 3rd cell on the second row

Sample Input:

[A1, A3, D5, F5], [A2, A3, A4, F4, A1, D5, E5, F5]

Sample Output:

Player One entered 2 ships.




"""

class Cell:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val

    def __str__(self) -> str:
        return f'{self.row}{self.col} = {self.val}'

class BattleshipBoard():
    """
    """

    def __init__(self, rows, cols) -> None:
        self._board = [[Cell(row, col, '.') for col in cols] for row in rows]
        self._rows = {k:v-1 for v, k in enumerate(rows)}
        self._cols = cols

    def __getitem__(self, position):
        if type(position) == str:
            r,c = position[0], int(position[1])
            return self._board[self._rows[r]][c-1]
        elif type(position) == tuple:
            return self._board[position[0]][position[1]]

    def __setitem__(self, position, new_val):
        if type(position) == tuple:
            self._board[position[0]][position[1]].val = new_val
        else:
            r, c = position[0], int(position[1])
            self._board[self._rows[r]][c-1] = new_val

    def __str__(self) -> str:
        return '\n'.join([''.join([cell.val for cell in row]) for row in self._board])

    def is_valid_cell(self, position):
        """Check if a position of a board is valid input

        Args:
            position: str, A1 - A6 ...

        Returns:
            bool
        """
        return len(position) == 2 and position[0] in self._rows and int(position) in self._cols

class Battleship:

    def __init__(self, board) -> None:
        self.board = board

    def is_valid_move(self, position):
        return self.board.is_valid_cell(position)

    def play(self, player_one_ships, player_two_guesses):
        # sanitize inputs
        pass



bs = BattleshipBoard(['A', 'B', 'C', 'D', 'E', 'F'], range(1, 7))
print(bs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
