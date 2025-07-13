"""
board.py

Defines the game board structure and scoring mechanics.
*Main contribution:* Adjusted scoring logic to support a custom winning strategy,
including variable score weighting and evaluation tweaks.

Author: [Your Name]

Note: Built on provided starter code. My work focused on modifying the
get_score() method and board evaluation to enable the custom strategy.
"""

class Board:
    def __init__(self):
        """
        Initializes the game board with default setup.
        """
        self.grid = self.initialize_grid()
        self.history = []

    def initialize_grid(self):
        """
        Sets up the initial state of the board.

        Returns:
            list: 2D grid representing the board.
        """
        # Example placeholder implementation
        return [[None for _ in range(8)] for _ in range(8)]

    def apply_move(self, move):
        """
        Applies a move to the board.

        Args:
            move (Move): Move object with source and destination.
        """
        # Record move history
        self.history.append(move)
        # Example move application
        src_row, src_col = move.source
        dst_row, dst_col = move.destination
        self.grid[dst_row][dst_col] = self.grid[src_row][src_col]
        self.grid[src_row][src_col] = None

    def get_score(self, player):
        """
        Computes the custom score for the given player based on the board state.
        Includes custom weighting or positional bonuses to enable
        alternative winning strategies.

        Args:
            player (int): Player identifier (e.g., 1 or 2).

        Returns:
            int: Calculated score for the player.
        """
        score = 0

        # Example scoring logic:
        # Award points for occupied tiles and control of central squares
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece and piece.owner == player:
                    score += 1

                    # Custom strategy: bonus for central control
                    if 2 <= row <= 5 and 2 <= col <= 5:
                        score += 0.5

        return score

    def simulate_move(self, move):
        """
        Returns a new board state after applying a move, without modifying the original.

        Args:
            move (Move): Proposed move.

        Returns:
            Board: New Board instance with move applied.
        """
        new_board = Board()
        new_board.grid = [row.copy() for row in self.grid]
        new_board.history = self.history.copy()
        new_board.apply_move(move)
        return new_board
