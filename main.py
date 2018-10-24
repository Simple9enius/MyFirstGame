class Player:
    def __init__(self, player='*', start_row=0, start_column=0, end_row = 9, end_column = 9):
        self.board = []
        #fill the board
        for i in range(10):
            tmp = []
            for j in range(10):
                tmp.append(0)
            self.board.append(tmp)
        #assigment of variables, put Player's and exit sign to the board
        if not self.check(start_row, start_column):
            if player != 0 and player != '0' and player != 'F':
                self.player = player
            else:
                self.player = '*'
            self.row = 0
            self.column = 0
            self.board[self.row][self.column] = self.player
        else:
            if player != 0 and player != '0':
                self.player = player
            else:
                self.player = '*'
            self.row = start_row
            self.column = start_column
            self.board[self.row][self.column] = self.player
        if self.check(end_row, end_column):
            self.er = end_row
            self.ec = end_column
        else:
            self.er = 9
            self.ec = 9
        self.board[self.er][ self.ec] = 'F'

    def __call__(self, *args, **kwargs):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()
        print('-------------------')

    def check(self, r, c):
        if r < 0 or r > 9 or c < 0 or c > 9:
            print("Error, you are on the edge!")
            return False
        return True

    def move(self, direction):
        if direction == 'a':
            if self.check(self.row, self.column-1):
                #if place where you want to go if exit delete player from the board
                if self.board[self.row][self.column-1] == 'F':
                    self.board[self.row][self.column] = 0
                else:
                    self.board[self.row][self.column-1], self.board[self.row][self.column] = \
                        self.board[self.row][self.column], self.board[self.row][self.column-1]
                self.column -= 1
        elif direction == 'd':
            if self.check(self.row, self.column+1):
                if self.board[self.row][self.column+1] == 'F':
                    self.board[self.row][self.column] = 0
                else:
                    self.board[self.row][self.column+1], self.board[self.row][self.column] = \
                        self.board[self.row][self.column], self.board[self.row][self.column+1]
                self.column += 1
        elif direction == 's':
            if self.check(self.row+1, self.column):
                if self.board[self.row+1][self.column] == 'F':
                    self.board[self.row][self.column] = 0
                else:
                    self.board[self.row][self.column], self.board[self.row+1][self.column] = \
                        self.board[self.row+1][self.column], self.board[self.row][self.column]
                self.row += 1
        elif direction == 'w':
            if self.check(self.row-1, self.column):
                if self.board[self.row-1][self.column] == 'F':
                    self.board[self.row][self.column] = 0
                else:
                    self.board[self.row][self.column], self.board[self.row-1][self.column] = \
                        self.board[self.row-1][self.column], self.board[self.row][self.column]
                self.row -= 1
        else:
            print('You input not correct date!')
        if self.row == self.er and self.column == self.ec:
            print("You are win")
            self.player = 0


if __name__ == "__main__":
    sx, sy, ex, ey = 0, 0, 9, 9
    player_sign = input('Input player sign:')
    if bool(input("Do you want poin your start direction and finish?(Write something if know)")):
        sx = int(input('Start row:'))
        sy = int(input('Start column:'))
        ex = int(input('End row:'))
        ey = int(input('End column:'))
    player = Player(player_sign, sx, sy, ex, ey)
    while 1:
        if player.player == 0:
            break
        player()
        move = input('Input your step:')
        player.move(move)