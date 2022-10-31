


board = [ ' ' for x in range(10)]  #created board with bunch of gaps



def insertLetter(letter, pos): #pos is position
    board[pos] = letter #puts letter into board 
    

def spaceIsFree(pos): #if the position that is being used is already being used 
    return board[pos] == ' ' #gives true or false value if in the postion there is a space

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' |'  + board[3])
    print('   |   |')
    print("-----------")
    print(' ' + board[4] + ' | ' + board[5] + ' |'  + board[6])
    print("-----------")
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' |'  + board[9])
    print('   |   |')


    
def isWinner (bo, le): #bo is baord le is letter 
    return (bo[7] == le  and  bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le)
    #goes through all the combinations on the board to see if the letters are equal in that place
    

def playerMove ():
    run = True
    while run:
        move = input("Please select a postiiton to place an \'X\' (1-9")
        try:
            move = int(move) #input has to be an integer
            if move >0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter ("x", move)      #puts x into grid and run no longer needs to be true 


                else:
                    print("This space has already been used")       #these two elses are lined up with the ifs so it gives out the correct error message 
            else:
                print("Please insert a number within the range")
                    
        except:
            print("Please a number (not letters)")


                
def compMove():
    pass

def selectRandom(board):
    pass

def isBoardFull (board):               #creats true or false is the board is full
    if board.count (' ') > 1:           #if the board has 0 gaps return true (it is full)
        return True 
    else:
        return False 

def main():
    print("Welcome to noughts and crosses")
    printBoard() #shows the player the board

    while not (isBoardFull(board)): #while loop until the board is full (draw)
        if not(isWinner (board, 'O')): #O is the computer so if the compiter has not won then the player can move
            playerMove()
            printBoard()
        else:
            ("The Computer Wins!")
            break #stops loop so we can ask if they want to play again
        

        if not(isWinner (board, 'X')): 
            compMove()
            printBoard()
        else:
            ("Congradulations You Win!")
            break 


        

        


    if isBoardFull (board):
        print("It's a Draw")

main()
