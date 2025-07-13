"""
engine.py

Game engine logic for managing game state and win conditions.
*Main contribution:* Customized win condition logic to change game strategy,
making the game more balanced and challenging.

Author: [Your Name]

Note: This file builds on provided starter code. My work focused on modifying
the win condition checks and scoring rules to encourage different player strategies.
"""

def check_win_condition(board):
    """
    Checks if the current board state meets the custom winning condition.

    Args:
        board (Board): The current game board state.

    Returns:
        bool: True if the win condition is met, False otherwise.
    """
    # Example custom win condition:
    # Instead of a standard fixed goal, require a minimum score difference.
    player1_score = board.get_score(player=1)
    player2_score = board.get_score(player=2)
    score_diff = abs(player1_score - player2_score)

    # Custom rule: win requires at least 5-point margin
    return score_diff >= 5


def evaluate_move(board, move):
    """
    Evaluates the move's impact on the board using the custom strategy.

    Args:
        board (Board): Current game board.
        move (Move): Proposed move.

    Returns:
        float: Evaluation score for this move.
    """
    # Basic example: prioritize moves increasing score difference
    simulated_board = board.simulate_move(move)
    p1 = simulated_board.get_score(player=1)
    p2 = simulated_board.get_score(player=2)
    score_diff = abs(p1 - p2)

    # Encourage moves that increase score difference
    return score_diff
