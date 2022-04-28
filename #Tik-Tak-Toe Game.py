#Tik-Tak-Toe Game
#Author: Spencer Barbre

'''My code has a few objectives, the first being a functioning game of Tic Tac Toe, and to do that the steps include:
Designing a board,
Designating 2 players,
Allowing for inputs into locations on board (marks),
checking for win conditions,
Check for draw conditions,
Name decisive player the victor,
Allow for replay.'''

# I used the reference after about an hour of fighting changing different characters that are printed. once I saw the solution I added the list to create the board and adjusted things to fit with that solution.



def main():
    player = player_turn("")
    welcoming = welcome()
    numboard = create_board()
    print()
    print(welcoming)
    while not (win_cons(numboard) or draw(numboard)):
        board(numboard)
        player = player_turn(player)
        marks(player, numboard)
    board(numboard)
    repeat = input("Thank you for playing, would you like to play again? (y/n): ").lower()
    if repeat == "y":
        print()
        main()
    elif repeat == "n":
        print("Enjoy your day!") 
        exit() 
    else:
        print("Sorry I don't understand that so I'll take it as a yes!")
        print()
        main() 



def welcome():
    #quick introduction to the game and really basic rules
    print("Welcome to Tic-Tac-Toe. You and an opponent will take turns placing a marker on the field (represented by and 'x' or an 'o')")
    print("First player to 3 markers in a row wins the game (this includes diaginal angles)")
    print("Good luck players!")

def create_board():
    #creating a list to diplaynumbers that are adjustable on the field
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def board(numboard):
    #how the board will be displayed
    print()
    print(f"{numboard[0]}|{numboard[1]}|{numboard[2]}")
    print("-+-+-")
    print(f"{numboard[3]}|{numboard[4]}|{numboard[5]}")
    print("-+-+-")
    print(f"{numboard[6]}|{numboard[7]}|{numboard[8]}")
    print()

def player_turn(player):
    #Defining the players marker per turn
    if player == "" or player == "o":
        return "x"
    elif player == "x":
        return "o"    
    else:
        print("An Error has occured")    
    

def marks(player, boardview):
    #placing markers on field
    mark = int(input(f"It is now {player}'s turn, please enter an availible number (1-9): "))
    boardview[mark - 1] = player

def win_cons(numboard):
    #telling the program when it is complete with a win condition
        return (numboard[0] == numboard[1] == numboard[2] or
                numboard[3] == numboard[4] == numboard[5] or
                numboard[6] == numboard[7] == numboard[8] or
                numboard[0] == numboard[3] == numboard[6] or
                numboard[1] == numboard[4] == numboard[7] or
                numboard[2] == numboard[5] == numboard[8] or
                numboard[0] == numboard[4] == numboard[8] or
                numboard[2] == numboard[4] == numboard[6])


def draw(numboard):
    #telling the program when it is complete with a draw condition
    for square in range(9):
        if numboard[square] != "x" and numboard[square] != "o":
            return False
    return True   

if __name__ == "__main__":
    main()