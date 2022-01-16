# Initialize chess code
import chess
import random
board = chess.Board()
print(board)
#loop forever
while True:
    # Players turn happens
    while board.turn == chess.WHITE:
        # Checks board for legal moves
        print(board.legal_moves)
        str1 = str(board.legal_moves)
        # Initializes strings and one list
        tempStr = str("")
        moveList = list("")
        #converts str1 into moveList, with tempStr being temp variable to store letters within a move
        for i in range(38,len(str1)-2):
            # Removes ( and spaces
            if str1[i] != "(" and str1[i] != " ":
                #checks for commas and ), if not, it adds current letter to tempStr
                if str1[i] != "," and str1[i] != ")":
                    tempStr = tempStr + str1[i]
                else:
                    # Adds tempStr to moveList
                    moveList.append(tempStr)
                    # Clears tempStr
                    tempStr = str('')
        print(moveList)
        move1 = input("Please enter a valid move!")
        if move1 in moveList:
            board.push_san(move1)
            print(board)
        else:
            print("You can't do that dumdumhead!")
    # A.I turn happens
    while board.turn == chess.BLACK:
        # Checks board for legal moves
        str1 = str(board.legal_moves)
        # Initializes strings and one list
        tempStr = str("")
        moveList = list("")
        #converts str1 into moveList, with tempStr being temp variable to store letters within a move
        for i in range(38,len(str1)-2):
            # Removes ( and spaces
            if str1[i] != "(" and str1[i] != " ":
                #checks for commas and ), if not, it adds current letter to tempStr
                if str1[i] != "," and str1[i] != ")":
                    tempStr = tempStr + str1[i]
                else:
                    # Adds tempStr to moveList
                    moveList.append(tempStr)
                    # Clears tempStr
                    tempStr = str('')
        # Activates a random move from the moveList
        print(board.legal_moves)
        board.push_san(moveList[random.randint(0,len(moveList) - 1)])
        print(board.legal_moves)
        print(board)