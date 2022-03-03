import random

def randomize_board():
    letters = [
        ['L','R','Y','T','T','E'],
        ['V','T','H','R','W','E'],
        ['E','G','H','W','N','E'],
        ['S','E','O','T','I','S'],
        ['A','N','A','E','E','G'],
        ['I','D','S','Y','T','T'],
        ['O','A','T','T','O','W'],
        ['M','T','O','I','C','U'],
        ['A','F','P','K','F','S'],
        ['X','L','D','E','R','I'],
        ['H','C','P','O','A','S'],
        ['E','N','S','I','E','U'],
        ['Y','L','D','E','V','R'],
        ['Z','N','R','N','H','L'],
        ['N','M','I','Q','H','U'],
        ['O','B','B','A','O','J']
    ]
    
    board = []
    for i in range(4):
        row = []
        for j in range(4):
            letter = random.choice(letters[i*4 +j])
            row.append(letter)
        board.append(row)
    return board
