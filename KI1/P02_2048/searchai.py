import random
import game
import sys
import numpy as np

# Author:      chrn (original by nneonneo)
# Date:        11.11.2016
# Copyright:   Algorithm from https://github.com/nneonneo/2048-ai
# Description: The logic to beat the game. Based on expectimax algorithm.

MaxScore, HighScore, MiddleScore, MinScore, NullScore = 4, 3, 2, 1, 0
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
move_args = [UP,DOWN,LEFT,RIGHT]
recursion_max_depth = 3;


def find_best_move(board):
    """
    find the best move for the next turn.
    """
    depth = 1
    
    return get_best_move(board, depth)
    
    
    
def get_best_move(board, depth):
    result = [score_toplevel_move(i, board) for i in range(len(move_args))]
    
    bestmove = result.index(max(result))
    
    for m in move_args:
        print(m)
        print(result[m])
    
    return bestmove

def score_toplevel_move(move, board):
    """
    Entry Point to score the first move.
    """
    newboard = execute_move(move, board)

    if board_equals(board,newboard):
        return 0
    
    currentDepth = 1
    
    return calculate_max(move, newboard, currentDepth)
	# TODO:
	# Implement the Expectimax Algorithm.
	# 1.) Start the recursion until it reach a certain depth
	# 2.) When you don't reach the last depth, get all possible board states and 
	#		calculate their scores dependence of the probability this will occur. (recursively)
	# 3.) When you reach the leaf calculate the board score with your heuristic.

def calculate_max(move, board, depth):  
    return calculate_experience_value(move, board, depth)  

def calculate_experience_value(move, board, depth):
    probability_of_two = 0.9;
    probability_of_four = 0.1;
    experience_value = 0
    zeros_in_board = board.size - np.count_nonzero(board)
    
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == 0:
                modifiedNewBoard = board
                modifiedNewBoard[i][j] = 2
                print(board, modifiedNewBoard, depth)
                scoreForNewTwo = probability_of_two * (1/zeros_in_board) * calculate_score_next_max(board, modifiedNewBoard, depth)
                experience_value += scoreForNewTwo
                
                modifiedNewBoard[i][j] = 4
                scoreForNewFour = probability_of_four * (1/zeros_in_board) * calculate_score_next_max(board, modifiedNewBoard, depth)
                experience_value += scoreForNewFour

    return experience_value

def calculate_score_next_max(board, new_board, depth):  
    if (depth == recursion_max_depth): 
        score = get_score_for_last_node(board, new_board)
        return score
    
    else:
        get_best_move(board, depth)
    

def get_score_for_last_node(board, new_board):    
    score = 0
    score += get_score_for_highest_number_in_right_lower_corner(new_board)
    score += get_score_for_empty_cells(board, new_board)
        
    return score

         

def get_score_for_highest_number_in_right_lower_corner(board):
    score = 0
    number_sorted = np.sort(board, axis=None)
    if board[-1][-1] == number_sorted[-1]:
        score = MiddleScore

    return score
    
def get_score_for_empty_cells(board, new_board):
    zeros_in_board = board.size - np.count_nonzero(board)
    zeros_in_new_board = new_board.size - np.count_nonzero(new_board)
    if zeros_in_new_board == zeros_in_board:
        return HighScore
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
