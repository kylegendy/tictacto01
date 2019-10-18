import os
import random
import time
def print_board():
    print(" ")
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("   |   |   ")
v = {'X': 3, 'O': 5, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
def user_choice():
    choice = input("Please choose an available space: ")
    choice = int(choice)
    board[choice] = 'X'    
def comp_choice():
    while True:
        choice = random.randint(1,9)
        if board[choice] != 'X' and board[choice] != 'O' and board[choice] != ' ':
            break
    board[choice] = 'O'
    print_board()
def game():
    while True:
        user_choice()
        if v[board[1]]+v[board[2]]+v[board[3]]==9 or v[board[4]]+v[board[5]]+v[board[6]]==9 or v[board[7]]+v[board[8]]+v[board[9]]==9 or v[board[1]]+v[board[4]]+v[board[7]]==9 or v[board[2]]+v[board[5]]+v[board[8]]==9 or v[board[3]]+v[board[6]]+v[board[9]]==9 or v[board[1]]+v[board[5]]+v[board[9]]==9 or v[board[3]]+v[board[5]]+v[board[7]]==9:
            print_board()
            print("YOU WIN!!!")
            break
        comp_choice()
        if v[board[1]]+v[board[2]]+v[board[3]]==15 or v[board[4]]+v[board[5]]+v[board[6]]==15 or v[board[7]]+v[board[8]]+v[board[9]]==15 or v[board[1]]+v[board[4]]+v[board[7]]==15 or v[board[2]]+v[board[5]]+v[board[8]]==15 or v[board[3]]+v[board[6]]+v[board[9]]==15 or v[board[1]]+v[board[5]]+v[board[9]]==15 or v[board[3]]+v[board[5]]+v[board[7]]==15:
            print_board()
            print("lmao you lost against a computer boi")
            break   
os.system("clear")

while True:
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    game_or_naw = input('\nu wanna play a game? (yeet/na): ')
    if game_or_naw == 'na':
        print('ohp')
        while True:
            time.sleep(1)
            game_or_naw2 = input('seriously? ')
            if game_or_naw2 == 'yeet':
                print('...fine')
                time.sleep(1)
                print('bitch ass')
            elif game_or_naw2 == 'na':
                print('lmao cool')
                print('lemme load it up')
                time.sleep(2)
                os.system("clear")
                break
            else:
                print("bruh this is a computer, either type 'yeet' or 'na', don't be stupid")
        print_board()
        game()
        time.sleep(3)
    elif game_or_naw == 'yeet':
        print('lemme load it up')
        time.sleep(2)
        os.system("clear")
        print_board()
        game()
        time.sleep(3)
    else:
        print("bruh this is a computer, either type 'yeet' or 'na', don't be stupid")
