# -*- coding: utf-8 -*-

import random


board = [1,2,3,4,5,6,7,8,9]


def show():
    print board[0], "|", board[1], "|", board[2]
    print "---------"
    print board[3], "|", board[4], "|", board[5]
    print "---------"
    print board[6], "|", board[7], "|", board[8]
    print "---------"


def check_winner(player):
    if player == "x":
        if board[0] == "x" and board[1] == "x" and board[2] == "x":
            return True

        elif board[3] == "x" and board[4] == "x" and board[5] == "x":
            return True

        elif board[6] == "x" and board[7] == "x" and board[8] == "x":
            return True

        elif board[0] == "x" and board[3] == "x" and board[6] == "x":
            return True

        elif board[1] == "x" and board[4] == "x" and board[7] == "x":
            return True

        elif board[2] == "x" and board[5] == "x" and board[8] == "x":
            return True

        elif board[0] == "x" and board[4] == "x" and board[8] == "x":
            return True

        elif board[2] == "x" and board[4] == "x" and board[6] == "x":
            return True

        else:
            return False

    elif player == "o":
        if board[0] == "o" and board[1] == "o" and board[2] == "o":
            return True

        elif board[3] == "o" and board[4] == "o" and board[5] == "o":
            return True

        elif board[6] == "o" and board[7] == "o" and board[8] == "o":
            return True

        elif board[0] == "o" and board[3] == "o" and board[6] == "o":
            return True

        elif board[1] == "o" and board[4] == "o" and board[7] == "o":
            return True

        elif board[2] == "o" and board[5] == "o" and board[8] == "o":
            return True

        elif board[0] == "o" and board[4] == "o" and board[8] == "o":
            return True

        elif board[2] == "o" and board[4] == "o" and board[6] == "o":
            return True

        else:
            return False


def main():
    while True:
        print ""
        print "Select a spot!"

        input = int(raw_input("-->")) - 1
        print ""

        if board[input] != "x" and board[input] != "o":
            board[input] = "x"

            if check_winner("x"):
                print "You win!"
                break

            while True:
                ki = random.randint(0,8)

                if board[ki] != "x" and board[ki] != "o":
                    board[ki] = "o"
                    break

            if check_winner("o"):
                print "You loose!"
                break

        else:
            print "Try again, noob! Wrong numer!"
            print ""

        show()


if __name__ == '__main__':
    try:
        show()
        main()
    except KeyboardInterrupt:
        pass