import random
import math
import datetime
import time

from prettytable import PrettyTable


# Define variables to keep track of the players' positions
diceRoll=0
playerPosition = 1
computerPosition = 1
total_movesPlayer = 0
total_movesComputer=0
moveBlocks=0
diceValue=0
playerCount=0
computerCount=0
player_BH=0
computer_BH=0

blackHoles=[7,14]
boardSize=20


# Define a variable to keep track of the current player
turn=True


# Define the game board
board = [[0 for _ in range(20)] for _ in range(2)]
board[0][6] = 'O'
board[0][13] = 'O'
board[1][6] = 'O'
board[1][13] = 'O'

row1=["H"," "," "," "," "," "," ","O"," "," "," " ," " ," " ," " ,"O" ," " ," " ," " ," " ," " ," " ]
row2=["C"," "," "," "," "," "," ","O"," "," "," " ," " ," " ," " ,"O" ," " ," " ," " ," " ," " ," " ]

def gameBoard():
    board=PrettyTable()
    board.field_names =[" ","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    board.add_row(row1, divider=True)        
    board.add_row(row2)

    print(board)                


# Define to Roll the dice and determine the number of blocks to move
def rollDice():
    diceRoll = random.randint(1, 6)
    return diceRoll


# Define Human player's rolling 
def humanPlayer_roll():
    print("Now you are playing !")
    time.sleep(1)
    input("Press enter key to start : ")
    print("The dice is rolling wait...")
    time.sleep(2)
    diceValue=rollDice()
    if diceValue == 6:
        print("\t\t\tYou rolled a 6! Now you are starting the game!")
        time.sleep(1)
        return True
    else:
        print(f"\t\t\tYou rolled a {diceValue}, Try again.")
        time.sleep(1)
        print(f"\t\t\tYou can\'t start the game with {diceValue}")
        return False
    

# Define Computer player's rolling
def computerPlayer_roll():
    time.sleep(2)
    print('Now It\'s computer\'s turn wait...')
    time.sleep(1)
    print("\t\t\tComputer is rolling the Dice......")
    time.sleep(2)
    diceValue = rollDice()
    if diceValue == 6:
        print("\t\t\tComputer rolled a 6! Now the computer is starting the game!")
        return True
    else:
        print(f"\t\t\tComputer rolled a {diceValue}")
        print(f"\t\t\tComputer can\'t start the game with {diceValue}")
        return False


# Define Human player's position changing
def human_pMove(playerPosition,playerDiceValue):
    global player_BH
    row1[playerPosition]= " "
    currentPosition = playerPosition + (playerDiceValue // 2)
    if currentPosition in blackHoles:
        currentPosition = 1
        player_BH += 1
        print('\t\t\tOops!,You hit a black hole.')
    elif currentPosition > boardSize:
        currentPosition = boardSize
    row1[currentPosition]= "X"
    return currentPosition


# Defining Computer player's position changing
def computer_pMove(playerPosition, playerDiceValue):
    global computer_BH
    row2[playerPosition]= " "
    currentPosition = playerPosition + (playerDiceValue // 2)
    if currentPosition in blackHoles:
        currentPosition = 1
        computer_BH += 1
        print('\t\t\tOops!,Computer hit a black hole.')
    elif currentPosition > boardSize:
        currentPosition = boardSize
    row2[currentPosition]= "X"
    return currentPosition


# Welcome interface 
def welcome():
    name=input("Enter your name : ").capitalize()
    print("------------------------ Hi !", name,",Welcome to the BoardGame (20 x 2) ------------------------")
    print("\n")
    print("Better luck for a 6 !")
    print("\n")
    

#Load the game loop
welcome()

player=humanPlayer_roll()
print()
computer=computerPlayer_roll()


while True:
    if player:
        # player's turn 
        print()
        playerCount += 1
        print(f"This is your turn -- {playerCount} ")
        input("\t\t\tPress enter key to roll the dice...")
        time.sleep(2)
        diceValue = rollDice()
        blocks=(diceValue // 2)
        print("\t\t\tYou rolled ", diceValue)
        time.sleep(1)
        print(f"\t\t\tYou moving {diceValue // 2} blocks forward")
        playerPosition = human_pMove(playerPosition, diceValue)
        print("\t\t\tyour position:", playerPosition)
        time.sleep(1)
        gameBoard()
        if playerPosition == boardSize:
            print("\t\t\tCongratulations, you won!")
            break
    else:
        print()
        player = humanPlayer_roll()


    if computer:
        # computer' turn
        print()
        computerCount += 1
        print(f'This is computer\'s turn ---- {computerCount}.')
        print('\t\t\tComputer is rolling the Dice...')
        time.sleep(2)
        diceValue = rollDice()
        blocks=(diceValue // 2)
        print("\t\t\tComputer rolled a", diceValue)
        time.sleep(1)
        print(f"\t\t\tComputer moving {diceValue // 2} blocks forward")
        computerPosition = computer_pMove(computerPosition, diceValue)
        print("\t\t\tComputer position:", computerPosition)
        time.sleep(1)
        gameBoard()
        
        if computerPosition == boardSize:
            print("\t\t\tSorry,Try again,The computer won this time.")
            break
    else:
        print()
        computer = computerPlayer_roll()


print()
print("Your details")
time.sleep(1)
print(f"\t\tTotal moves : {playerCount}")
print(f"\t\tTotal black hole hits : {player_BH} ")
if playerPosition == boardSize:
    print("\t\tyou won the game! (:")
else:
    print("\t\tYou loss the game,Try again ):")

print()
print("Computer details,")
time.sleep(1)
print(f"\t\t\tTotal moves : {computerCount}")
print(f"\t\t\tTotal black hole hits : {computer_BH}")
if computerPosition == boardSize:
    print("\t\t\tComputer Won the game ")
else:
    print("\t\t\tComputer loss the game")



# Save game details to a file
time = datetime.datetime.now()
file = time.strftime("%Y_%m_%d_%H_%M.txt")
with open(file, "w+") as file:
    file.write("Your details,")
    file.write(f"\n\t\tTotal moves : {playerCount}")
    file.write(f"\n\t\tTotal black hole hits : {player_BH} ")
    if playerPosition == boardSize:
        file.write("\n\t\tyou won! (:")
    else:
        file.write("\n\t\tYou defeated ,Try once again ):")

    file.write("\nComputer details")
    file.write(f"\n\t\tTotal moves : {computerCount}")
    file.write(f"\n\t\tTotal black hole hits : {computer_BH}")
    if computerPosition == boardSize:
        file.write("\n\t\tComputer Won the game ")
    else:
        file.write("\n\t\tComputer loose the game")




















