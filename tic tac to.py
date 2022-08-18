board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
visited = []
print("**** Tic Tac To ****")
print("\n")
print("Enter a position from 1 to 9")


def printBoard(board):            # print board in 3x3 table
    num = 0
    for i in board:
        if num == 3:              # print new line after 3 points
            print("\n")
            print(i, end="  ")
            num = 1
        else:
            print(i, end="  ")
            num += 1


def replaceElement(potion, player):     # for replacing '-' with 'x' or 'O'

    if potion not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        print("Enter a value from 1 to 9")
        return 0                       # if position is not in range of 1 to 9 it will return 0

    for i in range(len(board)):
        if i == (potion - 1):           # find the position in the board
            if i not in visited:
                board[i] = player      # replace the element
                visited.append(i)
                return 1               # if all is ok then it will place the element and return 1
            else:
                print("position is already taken")
                return 0               # if the position is already taken then it will return 0


def winingCondition(board, player):

    if board[0] == board[4] == board[8] == player:  # diagonally check from front if all the elements are same
        return 1

    if board[2] == board[4] == board[6] == player:  # diagonally check from back if all the elements are same
        return 1

    n = 0
    x = 0
    while n < 3:            # row check if all the elements are same
        if board[x] == board[x + 1] == board[x + 2] == player:
            return 1
        x += 3              # increment it by the 3 because of row
        n += 1

    n = 0
    x = 0
    while n < 3:  # column check if all the elements are same
        if board[x] == board[x + 3] == board[x + 6] == player:
            return 1
        x += 1            # increment it by 1 because of column
        n += 1
    return 0


def movesLeft():                         # it checks how many moves left
    if len(board) == len(visited):
        print("\n No One Win The Game")
        return 0                    # return 0 if no moves left
    else:
        return 1                    # return 1 if moves left


def main():                         # main code which use all the function
    i = 0
    while True:
        player_one = 'x'
        player_two = 'O'
        # for player one
        while True:
            potion1 = int(input("\nPlayer one :"))

            if replaceElement(potion1, player_one) == 0:    # position is already taken
                print("Error enter again")
            else:                                   # position is available
                break

        printBoard(board)
        if winingCondition(board, player_one) == 1:
            print("\n **** Player One Win The Game *****")
            break
        if movesLeft() == 0:
            break

        # for player two
        while True:
            potion2 = int(input("\nPlayer Two :"))

            if replaceElement(potion2, player_two) == 0:   # position is already taken
                print("Error enter again")
            else:                                   # position is available
                break

        printBoard(board)
        if winingCondition(board, player_two) == 1:
            print("\n **** Player Two Win The Game *****")
            break

        if movesLeft() == 0:
            break


if __name__ == '__main__':
    printBoard(board)
    main()
