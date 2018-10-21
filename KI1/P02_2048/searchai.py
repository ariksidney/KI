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
recursion_max_depth = 3
number_of_cells_in_board = 16

def find_best_move(board):
    """
    find the best move for the next turn.
    """
    depth = 1
    
    return get_best_move(board, depth) 
    
def get_best_move(board, depth):
    result = get_score_for_all_movements(board, depth)
    
    bestmove = result.index(max(result))
    
    return bestmove

def get_score_for_all_movements(board, depth):
    return [move_and_score(i, board, depth) for i in range(len(move_args))]

def move_and_score(move, board, depth):
    """
    Entry Point to score the first move.
    """
    newboard = execute_move(move, board)

    if board_equals(board,newboard):
        return 0
    
    return calculate_board_score(board, newboard, depth)

def calculate_board_score(prev_board, new_board, depth):
    score_of_new_board = get_points_for_new_board(prev_board, new_board)
    
    if (depth <= recursion_max_depth):
        zeros_in_new_board = new_board.size - np.count_nonzero(new_board)
             
        if zeros_in_new_board <= (number_of_cells_in_board / 4):
            return calculate_experience_value_and_next_move(new_board, depth+1) + score_of_new_board    

        return calculate_experience_value_and_next_move(new_board, depth+2) + score_of_new_board    
    else:
        return score_of_new_board
    
def calculate_experience_value_and_next_move(newBoard, depth):
    probability_of_two = 0.9;
    probability_of_four = 0.1;
    
    experience_value = 0
    zeros_in_board = newBoard.size - np.count_nonzero(newBoard)
    
    for i in range(0, 4):
        for j in range(0, 4):
            if newBoard[i][j] == 0:
                modifiedNewBoard = newBoard.copy()         
                modifiedNewBoard[i][j] = 2   
                best_score_for_all_movement = max(get_score_for_all_movements(modifiedNewBoard, depth))   
                scoreForNewTwo = probability_of_two * (1/zeros_in_board) * best_score_for_all_movement
                experience_value += scoreForNewTwo
  
                modifiedNewBoard = newBoard.copy()              
                modifiedNewBoard[i][j] = 4
                best_score_for_all_movement = max(get_score_for_all_movements(modifiedNewBoard, depth))   
                scoreForNewFour = probability_of_four * (1/zeros_in_board) * best_score_for_all_movement
                experience_value += scoreForNewFour

    return experience_value



def calculate_score_next_max(board, new_board, depth):  
    if (depth == recursion_max_depth): 
        score = get_score_for_last_node(board, new_board)
        return score
    
    else:
        return get_best_move(new_board, depth+1)
    

def get_score_for_last_node(board, new_board):    
    score = 0
    #score += get_score_for_highest_number_in_right_lower_corner(new_board)
    #score += get_score_for_empty_cells(board, new_board)
    score += get_points_for_new_board(board, new_board)
    
    return score   

def get_score_for_highest_number_in_right_lower_corner(board):
    score = 0
    number_sorted = np.sort(board, axis=None)
    
    if board[-1][-1] == number_sorted[-1]:
        score = MinScore

    return score

def get_points_for_new_board(prev_board, new_board):
    max_number_in_new_board = np.max(new_board)
        
    current_number = 2
    points = 0;

    while current_number <= max_number_in_new_board:      
        occurence_of_current_number_in_prev_board = np.count_nonzero(prev_board == current_number)   
        occurence_of_current_number_in_new_board = np.count_nonzero(new_board == current_number)

        if occurence_of_current_number_in_new_board > occurence_of_current_number_in_prev_board:
            factor = occurence_of_current_number_in_new_board - occurence_of_current_number_in_prev_board

            points += current_number * factor
            
        current_number = current_number * 2
        
    return points
    
    
def get_score_for_empty_cells(board, new_board):
    zeros_in_board = board.size - np.count_nonzero(board)
    zeros_in_new_board = new_board.size - np.count_nonzero(new_board)
    
    if zeros_in_new_board == zeros_in_board:
        return MinScore
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
