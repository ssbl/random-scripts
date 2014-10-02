#!/usr/bin/python
# Basic tic-tac-toe game

import random

board = ['-'] * 9

def printBoard():
    for i in range(0,9,3):
        print board[i], board[i+1], board[i+2]

def valid_moves():
    moves = [i for i in range(9) if board[i] == '-']
    return moves

def full():
    if '-' in board:
        return False
    else:
        return True
        
def is_valid(move):
    if move > 8:
        return False
    elif board[move] != '-':
        return False
    else:
        return True

def end_game(token, board):
    if board[0] == board[1] == board[2] == token:
        return True
    elif board[3] == board[4] == board[5] == token:
        return True
    elif board[6] == board[7] == board[8] == token:
        return True
    elif board[0] == board[3] == board[6] == token:
        return True
    elif board[1] == board[4] == board[7] == token:
        return True
    elif board[2] == board[5] == board[8] == token:
        return True
    elif board[0] == board[4] == board[8] == token:
        return True
    elif board[2] == board[4] == board[6] == token:
        return True
    else:
        return False
    
def first_move(comp_token, player_token):
    if random.randint(0,1): return comp_token, player_token
    else: return player_token, comp_token

def set_characters():
    token = raw_input('Your token: ')
    while token != 'X' and token != 'O':
        token = raw_input('Please enter X or O: ')
    if token == 'X':
        cp_token = 'O'
    elif token == 'O':
        cp_token = 'X'
    return token, cp_token

def play_again(choice):
    if choice[0] == 'y' or choice[0] == 'Y':
        for i in range(9):
            board[i] = '-'
        return True
    else:
        print 'Stop.'
        return False

def player_move(token):
    pos = int(raw_input('Your move: '))

    while not is_valid(pos):
        pos = int(raw_input('Please enter a valid move: '))
    board[pos] = token
    
def comp_move(token):
    moves = valid_moves()
    pl_token = 'O' if token == 'X' else 'X'
    move_set = False
    
    # Stop player from winning
    for x in moves:
        board_copy = board[:]
        board_copy[x] = pl_token
        if end_game(pl_token, board_copy):
            board[x] = token
            move_set = True
            break
        
    # Make winning move
    for x in moves:
        if move_set: break
        
        board_copy = board[:]
        board_copy[x] = token
        if end_game(token, board_copy):
            board[x] = token
            move_set = True
            break

    # Nothing interesting
    if not move_set:
        board[moves[random.randrange(0,len(moves)-1)]] = token

if __name__ == '__main__':
    # Game starts
    playing = True
    while True:
        player_token, comp_token = set_characters()
        print 'You:', player_token, 'Computer:', comp_token

        first, second = first_move(comp_token, player_token)
        if (first, second) == (player_token, comp_token):
            print 'You play first.'
        else: print 'Computer plays first.'
            
        while playing:
            if first == player_token:
                player_move(player_token)
            else:
                comp_move(comp_token)
                printBoard()

            if end_game(first, board):
                if first == player_token:
                    print 'You win!'
                    printBoard()
                else: print 'Computer wins!'
                
                playing = False
                continue
            
            if second == comp_token:
                comp_move(comp_token)
                printBoard()
            else:
                player_move(player_token)

            if end_game(second, board):
                if second == comp_token: print 'Computer wins!'
                else:
                    print 'You win!'
                    printBoard()

                playing = False
                continue
                
            if full():
                playing = False

        if not playing:
            print 'Game ends!'
            choice = raw_input('Play again? ')

            if play_again(choice):
                playing = True
                continue
            else:
                break
