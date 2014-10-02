#!/usr/bin/python
# Basic tic-tac-toe game

import random
from operator import itemgetter

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
    try:
        move = int(move)
    except:
        return False
    if move > 8:
        return False
    elif board[move] != '-':
        return False
    else:
        return True

def end_game(token, board):
    f = lambda x, y, z: itemgetter(x, y, z)(board)
    if all(x == token for x in f(0, 1, 2)):
        return True
    elif all(x == token for x in f(3, 4, 5)):
        return True
    elif all(x == token for x in f(6, 7, 8)):
        return True
    elif all(x == token for x in f(0, 3, 6)):
        return True
    elif all(x == token for x in f(1, 4, 7)):
        return True
    elif all(x == token for x in f(2, 5, 8)):
        return True
    elif all(x == token for x in f(0, 4, 8)):
        return True
    elif all(x == token for x in f(2, 4, 6)):
        return True
    else:
        return False

def first_move(comp_token, player_token):
    if random.randint(0, 1):
        return comp_token, player_token
    else:
        return player_token, comp_token

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
    if choice.startswith(('y', 'Y')):
        for i in range(9):
            board[i] = '-'
        return True
    else:
        print 'Stop.'
        return False

def player_move(token):
    pos = raw_input('Your move: ')
    while not is_valid(pos):
        pos = raw_input('Please enter a valid move: ')
    pos = int(pos)
    board[pos] = token

def comp_move(token):
    moves = valid_moves()
    pl_token = 'O' if token == 'X' else 'X'
    move_set = False

    # Make winning move
    for x in moves:
        if move_set:
            break
        board_copy = board[:]
        board_copy[x] = token
        if end_game(token, board_copy):
            board[x] = token
            move_set = True
            break

    # Stop player from winning
    for x in moves:
        board_copy = board[:]
        board_copy[x] = pl_token
        if end_game(pl_token, board_copy):
            board[x] = token
            move_set = True
            break

    # Nothing interesting
    if not move_set:
        board[moves[random.randrange(0, len(moves)-1)]] = token

if __name__ == '__main__':
    # Game starts
    playing = True
    while True:
        player_token, comp_token = set_characters()
        print 'You:', player_token, 'Computer:', comp_token

        first, second = first_move(comp_token, player_token)
        if (first, second) == (player_token, comp_token):
            print 'You play first.'
        else:
            print 'Computer plays first.'

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
