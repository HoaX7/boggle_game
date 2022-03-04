import copy
import random

class Graph(object):
    def __init__(self, board):
        self.board = board
        self.letters = {}
        self.adj_list = {}
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(4):
            for j in range(4):
                if board[i][j] not in self.letters:
                    self.letters[board[i][j]] = []
                self.letters[board[i][j]].append((i, j))
                self.adj_list[(board[i][j], i, j)] = []
                for d1, d2 in directions:
                    k = i+d1
                    l = j+d2
                    if k >= 0 and k < 4 and l >= 0 and l < 4:
                        self.adj_list[(board[i][j], i, j)].append((board[k][l], k, l))

    def dfs(self, word):
        # print(self.letters)
        if len(word) < 4:
            return False
        stack = []
        if word[0] not in self.letters:
            return False
        for i, j in self.letters[word[0]]:
            stack.append((word[0], word, (word[0], i, j), set([(i, j)])))
        while len(stack) > 0:
            sub, word, let, positions = stack.pop()
            if sub == word:
                return True
            next_letter = word[len(sub)]
            for l, i, j in self.adj_list[let]:
                if l == next_letter and (i, j) not in positions:
                    p2 = copy.deepcopy(positions)
                    p2.add((i, j))
                    stack.append((sub+next_letter, word, (l, i, j), p2))
        return False
    

class Endgame:
    def __init__(self):
        self.__init_vars()

    def __init_vars(self):
        self.__bank = [] # Words found by computer
        self.__total_score = 0 # Computer Score

    def set_dict(self, dict):
        # Should be in boggle.py
        self.__dict = dict

    def set_board(self, board):
        self.__board = board

    def invoke(self, word_bank):
        return self.compute_boggle(word_bank), self.__total_score


    def compute_boggle(self, word_bank = []):
        words = self.find_words(self.__board)
        total_points = 0
        w = []
        # Search for words the player was not able to identify
        dict_words = set(words)
        player_word_bank = set(word_bank)
        for word, points in list(dict_words.difference(player_word_bank)):
            total_points += points
            w.append(word)

        self.__total_score = total_points
        return w

    # Traverse through dict_list to find all possible words
    def find_words(self, board):
        g = Graph(board)
        words = []
        for word in self.__dict:
            if g.dfs(word):
                words.append((word, self.points(word)))
        return words

    # Points for each word identified
    def points(self, word):
        if len(word) == 4:
            return 1
        if len(word) == 5:
            return 2
        if len(word) == 6:
            return 3
        if len(word) == 7:
            return 5
        if len(word) >= 8:
            return 11
        return 0



