import random
import game
import sys
import numpy as np
import collections

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

MaxScore, HighScore, MiddleScore, MinScore, NullScore = 4, 3, 2, 1, 0


def find_best_move(board):
    bestmove = -1
    score_for_swipe_right = swipe_right(board)
    score_for_swipe_left = swipe_left(board)
    score_for_swipe_up = swipe_up(board)
    score_for_swipe_down = swipe_down(board)

    max_score = max(score_for_swipe_right, score_for_swipe_down, score_for_swipe_left, score_for_swipe_up)

    if max_score == score_for_swipe_right:
        return RIGHT
    elif max_score == score_for_swipe_down:
        return DOWN
    elif max_score == score_for_swipe_left:
        return LEFT
    else:
        return UP


def find_best_move_random_agent():
    return random.choice([UP, DOWN, LEFT, RIGHT])


def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")


def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return (newboard == board).all()


def swipe_right(board):
    new_board = game.merge_right(board)
    return 0 if board_equals(board, new_board) else get_score_by_board(board, new_board, RIGHT) 


def swipe_left(board):
    new_board = game.merge_left(board)
    return 0 if board_equals(board, new_board) else get_score_by_board(board, new_board, LEFT) 


def swipe_up(board):
    new_board = game.merge_up(board)
    return 0 if board_equals(board, new_board) else get_score_by_board(board, new_board, UP) 


def swipe_down(board):
    new_board = game.merge_down(board)
    return 0 if board_equals(board, new_board) else get_score_by_board(board, new_board, DOWN) 


def get_score_by_board(board, new_board, action):
    score = get_score_for_highest_number_in_right_lower_corner(new_board)
    core = score + get_score_for_empty_cells(board, new_board)
    score = score + get_score_for_no_of_merges(board, action)
    return score



def get_score_for_highest_number_in_right_lower_corner(board):
    score = 0
    number_sorted = np.sort(board, axis=None)
    if board[-1][-1] == number_sorted[-1]:
        score = score + MaxScore
    if board[-1][-2] == number_sorted[-2] or board[-2][-1] == number_sorted[-2]:
        score = score + HighScore
    if board[-1][-2] == number_sorted[-3] or board[-2][-1] == number_sorted[-3]:
        score = score + HighScore
    return score


def get_score_for_empty_cells(board, new_board):
    zeros_in_board = board.size - np.count_nonzero(board)
    zeros_in_new_board = new_board.size - np.count_nonzero(new_board)
    if zeros_in_new_board == zeros_in_board:
        return MiddleScore
    elif zeros_in_new_board > zeros_in_board:
        return MaxScore
    else:
        return NullScore


def get_score_for_no_of_merges(board, action):

    def get_no_of_merges_horizontal(board):
        no_of_merges = 0
        for row in board:
            for index, cell in enumerate(row):
                if index < len(row) - 1:
                    if cell == row[index + 1]:
                        no_of_merges = no_of_merges + 1
        return no_of_merges

    def get_no_of_merges_vertical(board):
        no_of_merges = 0
        for col in board.T:
            for index, cell in enumerate(col):
                if index < len(col) - 1:
                    if cell == col[index + 1]:
                        no_of_merges = no_of_merges + 1
        return no_of_merges

    no_of_horizontal_merges = get_no_of_merges_horizontal(board)
    no_of_vertical_merges = get_no_of_merges_vertical(board)

    if no_of_horizontal_merges > no_of_vertical_merges and (action == RIGHT or action == LEFT):
        return MinScore
    elif no_of_horizontal_merges < no_of_vertical_merges and (action == UP or action == DOWN):
        return MinScore
    else:
        return NullScore

    


