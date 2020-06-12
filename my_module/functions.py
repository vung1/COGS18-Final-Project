"""A collection of function for doing my project."""

import random
import keyboard
from IPython.display import clear_output


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
        The game board is now initialized with the proper width and height. 
        The Start and Finishing locations is also populated onto the grid.
        The current location that the player will start any game will always
        be at the coordinate (0, 0)
        """

        # If the width of the board is too small, set back to default width
        if width < 2:
            self.width = 10
        else:
            self.width = width

        # If the height of the board is too small, set back to default width
        if height < 2:
            self.height = 10
        else:
            self.height = height

        # Creates grid to be the size of board that is empty
        self.grid = [[" "] * self.width for ncols in range(self.height)]
        self.grid[0][0] = "S"  # marks top left as starting point
        # marks bottom right as ending point
        self.grid[self.height - 1][self.width - 1] = "F"

        # Keeps track of the current column you are on
        self.currentColumn = 0
        # Keeps track of the current row you are on
        self.currentRow = 0

    def set_player_location(self):
        """
        Marks the current location of the player with the "O" symbol
        """

        self.grid[self.currentRow][self.currentColumn] = "O"

    def move_right(self):
        """Moves the player as far right on the grid as possible. The player
        will stop if is at the boundary, hits an obstacle, or is at the finish
        """

        # checks if the player can still move right on the board
        if self.can_move_right():
            self.grid[self.currentRow][self.currentColumn] = "."

        # Continues to move as far right on the board as possible and updates
        # the grid with "." for each spot the player has visited.
        while self.can_move_right():
            self.currentColumn += 1
            self.grid[self.currentRow][self.currentColumn] = "."

        self.set_player_location()  # marks the current loocatioon of the player

    def move_left(self):
        """Moves the player as far left on the grid as possible. The player
        will stop if is at the boundary, hits an obstacle, or is at the finish
        """

        # cheecks if the player can still move left on the board
        if self.can_move_left():
            self.grid[self.currentRow][self.currentColumn] == "."

        # Continues to move as far left on the board as possible and updates
        # the grid with  for each spot the player has visited.
        while self.can_move_left():
            self.currentColumn -= 1
            self.grid[self.currentRow][self.currentColumn] = "."

        self.set_player_location()  # marks the current loocatioon of the player

    def move_down(self):
        """Moves the player as far down on the grid as possible. The player
        will stop if is at the boundary, hits an obstacle, or is at the finish
        """

        # checks if the player can still move down on the board
        if self.can_move_down():
            self.grid[self.currentRow][self.currentColumn] = "."

        # Continues to move as far down on the board as possible and updates
        # the grid with  for each spot the player has visited.
        while self.can_move_down():
            self.currentRow += 1
            self.grid[self.currentRow][self.currentColumn] = "."

        self.set_player_location()  # marks the current loocatioon of the player

    def move_up(self):
        """Moves the player as far up on the grid as possible. The player
        will stop if is at the boundary, hits an obstacle, or is at the finish
        """

        # checks if the player can still move up on the board
        if self.can_move_up():
            self.grid[self.currentRow][self.currentColumn] = "."

        # Continues to move as far left on the board as possible and updates
        # the grid with  for each spot the player has visited.
        while self.can_move_up():
            self.currentRow -= 1
            self.grid[self.currentRow][self.currentColumn] = "."

        self.set_player_location()  # marks the current loocatioon of the player

    def can_move_left(self):
        """Determines if the player can still move left.

        Returns
        _______
        True if the player can still move left and false otherwise.
        """

        # If the player has not hit the left most boundary on the board or
        # the left position is empty/finish location, then they can still
        # move left.
        if (self.currentColumn - 1 != - 1
            and (self.grid[self.currentRow][self.currentColumn - 1] == " "
                 or self.grid[self.currentRow][self.currentColumn] == "F")):
            return True

        return False

    def can_move_right(self):
        """Determines if the player can still move right.

        Returns
        _______
        True if the player can still move right and false otherwise.
        """

        # If the player has not hit the right most boundary on the board or
        # the right position is empty/finish location, then they can still
        # move right.
        if (self.currentColumn + 1 != self.width
            and (self.grid[self.currentRow][self.currentColumn + 1] == " "
                 or self.grid[self.currentRow][self.currentColumn + 1] == "F")):
            return True

        return False

    def can_move_up(self):
        """Determines if the player can still move up.
        Returns
        _______
        True if the player can still move up and false otherwise
        """

        # If the player has not hit the top most boundary on the board or
        # the top position is empty/finish location, then they can still
        # move up.
        if (self.currentRow - 1 != - 1
            and (self.grid[self.currentRow - 1][self.currentColumn] == " "
                 or self.grid[self.currentRow - 1][self.currentColumn] == "F")):
            return True

        return False

    def can_move_down(self):
        """Determines if the player can still move down.

        Returns
        _______
        True if the player can still move down and false otherwise
        """

        # If the player has not hit the bottom most boundary on the board or
        # the bottom position is empty/finish location, then they can still
        # move down.
        if (self.currentRow + 1 != self.height
            and (self.grid[self.currentRow + 1][self.currentColumn] == " "
                 or self.grid[self.currentRow + 1][self.currentColumn] == "F")):
            return True

        return False

    def add_random_obstacles(self, num_obstacles=3):
        """Adds random obstacles on the board to prevent the player from
        reaching the finish. The obstacles can only be placed on empty 
        squares.

        Parameters
        ----------
        num_obstacles: int
            The number of obstacles to add onto the board

        Returns
        -------
        True if all obstacles were successfully added and false otherwise
        """

        # counter for the number of free space on the board (" ")
        available_space = 0

        # goes through the board and counts the number of free space
        for row in self.grid:
            for element in row:
                if element == " ":
                    available_space += 1

        # If you try to generate more obstacles than availabe space on the
        # board, return False. The number of obstacles added cannot be
        # negative.
        if num_obstacles > available_space or num_obstacles < 0:
            return False

        # Create num_obstacles amount of obstacles on the board and place them
        # randomly.
        while num_obstacles != 0:
            # Generate a random row and column for the obstacle
            row = random.choice(range(0, self.height))
            column = random.choice(range(0, self.width))

            # Continues generating a random row and column until we find an
            # empty square to place the obstacle
            while self.grid[row][column] != " ":
                # generate a new random row and column
                row = random.choice(range(0, self.height))
                column = random.choice(range(0, self.width))

            self.grid[row][column] = "X"  # places the random obstacle
            num_obstacles -= 1

        return True

    def is_game_over(self):
        """Determines whether or not the gamme is over. A game is over if
        there are no more possible moves you can make in any direction.

        Returns
        -------
        True if the game is over and false otherwise.
        """

        # check to see if you can move in any direction
        if (self.can_move_down() or self.can_move_left()
                or self.can_move_right() or self.can_move_up()):
            return False

        return True

    def won_game(self):
        """Determines whether or not the player has won the game. If the player
        has won the game, then the player symbol "O" should be at bottom right
        corner.

        Returns
        _______
        True if the player has won the game and false otherwise
        """

        # checks to see if the player is at the bottom right corner
        if (self.currentColumn == self.width - 1
                and self.currentRow == self.height - 1):
            return True

        return False

    def print_board(self):
        """Prints the state of the current board"""

        print("\n".join([" ".join(lst) for lst in self.grid]))

    def play_game(self):
        """ Allows the user to play the game"""

        message = "The objective of the game is to start at S on the board " \
                  "and move to F. Use the arrow keys on your keyboard to " \
                  "move up, left, down, and right. To add an obstacle to " \
                  "make the game more challenging, press X and input the " \
                  "number of obstacles (int). To quit the game, press q."
        print(message)

        game_over = False
        game_won = False

        # game continues as long as you have not won or no further moves can
        # be made
        while(not game_over and not game_won):
            self.print_board()  # prints the current board

            # checks which keys are pressed on the keyboard
            while True:
                # if the left arrow key is pressed, move left
                if keyboard.is_pressed("left arrow"):
                    self.move_left()
                    break
                # if the right arrow key key is pressed, move right
                if keyboard.is_pressed("right arrow"):
                    self.move_right()
                    break
                # if the up arrow key is pressed, move up
                elif keyboard.is_pressed("up arrow"):
                    self.move_up()
                    break
                # if the down arrow key is pressed, move down
                elif keyboard.is_pressed("down arrow"):
                    self.move_down()
                    break
                # if the "X" key is pressed, add random obstacles
                elif keyboard.is_pressed("X"):
                    # ask the user for the amount of obstacles they want to add
                    num_obstacles = int(input(
                        "Enter the number of obstacles you want to add"))
                    # must enter a valid number of obstacles to add. If not
                    # it will prompt the user to enter another number
                    while not self.add_random_obstacles(num_obstacles):
                        print("The number you entered is too high or too low")
                        num_obstacles = int(input(
                            "Enter the number of obstacles you want to add"))
                    break
                # if the "Q" or "q" key is pressed, the game quits
                elif keyboard.is_pressed("q") or keyboard.is_pressed("Q"):
                    print("You have quit the game!")
                    return

            clear_output(True)

            # Checks to see if the game will continue on
            game_over = self.is_game_over()
            game_won = self.won_game()

        self.print_board()

        if game_won:
            print("Congratulations, you have won the game!")
        else:
            print("Unfortunately, you did not beat the game :(")
