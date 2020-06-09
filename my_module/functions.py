"""A collection of function for doing my project."""

import random


class GameBoard():

    def __init__(self, width=10, height=10):
        """Initializes the game board to play the game.

        Parameters
        ----------
        width: int
            The width of the board
        height: int
            The height of the board

        Returns
        -------
        The game board is now initialized with the proper width and height
        """
        # If the width of the board is too small, set back to default width
        if width < 5:
            self.width = 10
        else:
            self.width = width

        # If the height of the board is too small, set back to default width
        if height < 5:
            self.height = 10
        else:
            self.height = height

        # Creates grid to be the size of board that is empty
        self.grid = [[' '] * width for ncols in range(height)]
        self.grid[0][0] = 'S'  # marks top left as starting point
        # marks bottom right as ending point
        self.grid[height - 1][width - 1] = 'F'

        # Keeps track of the current row you are on
        self.currentRow = 0
        # Keeps track of the current column y ou are on
        self.currentColumn = 0

    def move_right(self):
        """Moves the player as far right as possible.

        Returns
        -------
        True if the player moved and false if they remained in the same place
        """
        moved = False  # player has not moved yet

        # Checks whether or not the player can still move right on the board
        # and if so moves the player to the updated position.
        while self.currentColumn + 1 != width and self.grid[self.currentRow][self.currentColumn + 1] == ' ':
            self.currentColumn += 1
            self.grid[self.currentRow][self.currentColumn] == '.'
            moved = True

        return moved

    def move_left(self):
        """Moves the player as far left as possible.

        Returns
        -------
        True if the player moved and false if they remained in the same place
        """

        moved = False  # player has not moved yet

        # Checks whether or not the player can still move to the left of the board
        # and if possible update the position.
        while self.currentColumn - 1 != - 1 and self.grid[self.currentRow][self.currentColumn - 1] == ' ':
            self.currentColumn -= 1
            self.grid[self.currentRow][self.currentColumn] == '.'
            moved = True

        return moved

    def move_up(self):
        """Moves the player as far up as possible.

        Returns
        -------
        True if the player moved and false if they remained in the same place
        """

        moved = False  # player has not moved yet

        # Checks whether or not the player can still move up on the board
        # and if possible update the position.
        while self.Row + 1 != height and self.grid[self.currentRow + 1][self.currentColumn] == ' ':
            self.currentRow += 1
            self.grid[self.currentRow][self.currentColumn] == '.'
            moved = True

        return moved

    def move_down(self):
        """Moves the player as far down as possible.

        Returns
        -------
        True if the player moved and false if they remained in the same place
        """

        moved = False  # player has not moved yet

        # Checks whether or not the player can still move down on the board
        # and if possible update the position.
        while self.Row - 1 != - 1 and self.grid[self.currentRow - 1][self.currentColumn] == ' ':
            self.currentRow -= 1
            self.grid[self.currentRow][self.currentColumn] == '.'
            moved = True

        return moved

    def add_random_obstacles(self, num_obstacles=3):
        """Adds random obstacles on the board to prevent the player from reaching the finish

        Parameters
        ----------
        num_obstacles: int
            The number of obstacles to add onto the board

        Returns
        -------
        True if all obstacles were successfully added and false otherwise
        """

        # If you try to generate more obstacles than availabe space on the board, return False
        if num_obstacles > self.width * self.height - 2:
            return False

        # While loop that will create num_obstacles amount of obstacles on the board
        while num_obstacles != 0:
            row = 0
            column = 0

            # Pick a random row and column until we find an empty square to place our obstacle
            while self.grid[row][column] != ' ':
                row = random.choice(range(0, self.height))
                width = random.choice(range(0, self.width))

            self.grid[row][column] = 'X'
            num_obstacles -= 1

        return True

    def is_game_over(self):
        """Determines whether or not the gamme is over. A game is over if 
        there are no more possible moves you can make

        Returns
        -------
        True if the game is over and false otherwise.
        """

        if self.move_left() or self.move_right() or self.move_down() or self.move_up():
            return True

        return False

    def play_game():
