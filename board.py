class Board:
    def __init__(self):
        self.board = [[1,2,3], [4,5,6], [7,8,9]]
        self.current_player = 'O'
        self.endgame = False
        self.open_spaces = 9

    def print_current_board(self):
        for x in self.board:
            print("|", end='')
            for y in x:
                print(y, "|",sep='', end='')
            print("\n", end='')
    
    def check_for_valid_move(self, user_input):
        if(user_input > 0 and user_input < 4):
            for x in self.board[0]:
                if(user_input == x):
                    return True
        elif(user_input > 3 and user_input < 7):
            for x in self.board[1]:
                if(user_input == x):
                    return True
        elif(user_input > 6 and user_input < 10):
            for x in self.board[2]:
                if(user_input == x):
                    return True
        else:
            print("Please choose a position between 1-9.")
            return False
        print("Position is already taken.")
        return False

    def place_token(self, user_input):
        if(user_input > 0 and user_input < 4):
            for x in range(3):
                if(user_input == self.board[0][x]):
                    self.board[0][x] = self.current_player
        elif(user_input > 3 and user_input < 7):
            for x in range(3):
                if(user_input == self.board[1][x]):
                    self.board[1][x] = self.current_player
        elif(user_input > 6 and user_input < 10):
            for x in range(3):
                if(user_input == self.board[2][x]):
                    self.board[2][x] = self.current_player

    def check_horizontal_win(self, user_input):
        if(user_input > 0 and user_input < 4):
            if(self.board[0].count(self.current_player) == 3):
                return True
        elif(user_input > 3 and user_input < 7):
            if(self.board[1].count(self.current_player) == 3):
                return True
        elif(user_input > 6 and user_input < 10):
            if(self.board[2].count(self.current_player) == 3):
                return True
        return False

    def check_vertical_win(self, user_input):
        if(user_input == 1 or user_input == 4 or user_input == 7):
            if([self.board[0][0], self.board[1][0], self.board[2][0]].count(self.current_player) == 3):
                return True
        elif(user_input == 2 or user_input == 5 or user_input == 8):
            if([self.board[0][1], self.board[1][1], self.board[2][1]].count(self.current_player) == 3):
                return True
        elif(user_input == 3 or user_input == 6 or user_input == 9):
            if([self.board[0][2], self.board[1][2], self.board[2][2]].count(self.current_player) == 3):
                return True
        return False

    def check_diagonal_win(self, user_input):
        if([self.board[0][0], self.board[1][1], self.board[2][2]].count(self.current_player) == 3):
            return True
        if([self.board[2][0], self.board[1][1], self.board[0][2]].count(self.current_player) == 3):
            return True
        pass

    def check_for_win(self, user_input):
        if(self.check_horizontal_win(user_input)):
            print("Player ", self.current_player, " wins!", sep='')
            self.endgame = True
            return
        if(self.check_vertical_win(user_input)):
            print("Player ", self.current_player, " wins!", sep='')
            self.endgame = True
            return
        if(self.check_diagonal_win(user_input)):
            print("Player ", self.current_player, " wins!", sep='')
            self.endgame = True
            return
        return

    def check_for_endgame(self, user_input):
        self.check_for_win(user_input)
        if(self.open_spaces == 0 and self.endgame == False):
            print("The game has ended in a tie.")
            self.endgame = True

    def swap_players(self):
        if(self.current_player == 'X'):
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        print("Player ", self.current_player, "'s turn", sep='')
        