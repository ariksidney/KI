import random
import game
import sys
import numpy as np

# Author:      chrn (original by nneonneo)
# Date:        11.11.2016
# Copyright:   Algorithm from https://github.com/nneonneo/2048-ai
# Description: The logic to beat the game. Based on expectimax algorithm.

maxRecursionDepth = 2
probabilityOfFour = 0.1
probabilityOfTwo = 0.9
MaxScore, HighScore, MiddleScore, MinScore, NullScore = 4, 3, 2, 1, 0

def find_best_move(board):
    """
    find the best move for the next turn.
    """
    bestmove = -1
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    move_args = [UP,DOWN,LEFT,RIGHT]
    
    result = [score_toplevel_move(i, board) for i in range(len(move_args))]
    
    bestmove = result.index(max(result))
    for m in move_args:
        print(result[m])
    
    return bestmove
    
def score_toplevel_move(move, board):
    """
    Entry Point to score the first move.
    """
    depth = 1
    newboard = execute_move(move, board)


    if board_equals(board,newboard):
        return 0
    return calculate(board, newboard, depth)
	# TODO:
	# Implement the Expectimax Algorithm.
	# 1.) Start the recursion until it reach a certain depth
	# 2.) When you don't reach the last depth, get all possible board states and 
	#		calculate their scores dependence of the probability this will occur. (recursively)
	# 3.) When you reach the leaf calculate the board score with your heuristic.


def calculate(board, new_board,  depth):
    if(depth == maxRecursionDepth):
        erwartungswert = 0
        zeros_in_board = board.size - np.count_nonzero(board)
        for i in range(0, 4):
            for j in range(0, 4):
                if board[i][j] == 0:
                    modifiedNewBoard = board
                    modifiedNewBoard[i][j] = 2
                    scoreForNewTwo = calculate_if_two(board, modifiedNewBoard, zeros_in_board)
                    erwartungswert += scoreForNewTwo
                    modifiedNewBoard[i][j] = 4
                    scoreForNewFour = calculate_if_four(board, modifiedNewBoard, zeros_in_board)
                    erwartungswert += scoreForNewFour
        return erwartungswert
    else:
        variablä = 0
        for i in range(0, 4):
            new_board = execute_move(i, board)
            variablä2 = calculate(board, new_board, depth + 1)
            if variablä2 > variablä:
                variablä = variablä2
        return variablä



def calculate_if_two(board, new_board, numberOfZeros):
    return 1 / numberOfZeros * probabilityOfTwo * get_score_for_all_heuristics(board, new_board)


def calculate_if_four(board, new_board, numberOfZeros):
    return 1 / numberOfZeros * probabilityOfFour * get_score_for_all_heuristics(board, new_board)


def get_score_for_all_heuristics(board, new_board):
    score = 0
    score += get_score_for_highest_number_in_right_lower_corner(new_board)
    score += get_score_for_empty_cells(board, new_board)
    return score


def get_score_for_highest_number_in_right_lower_corner(board):
    score = 0
    number_sorted = np.sort(board, axis=None)
    if board[-1][-1] == number_sorted[-1]:
        score += MaxScore
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


def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

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
    return  (newboard == board).all()  
