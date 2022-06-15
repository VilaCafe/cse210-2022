#printa a velha
def print_velha(valores):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(valores[0], valores[1], valores[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(valores[3], valores[4], valores[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(valores[6], valores[7], valores[8]))
    print("\t     |     |")
    print("\n")
 
 #################
###prints scoreboard####
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\tSCOREBOARD")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
################## 
##checks winner of game
def check_winner(player_pos, cur_player):
 
    #winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    #loop to wining combinationn
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            
            return True
           
    return False       
############### 
#def draws
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 #############
#game function
def single_game(cur_player):
 
    #rep for values
    valores = [' ' for x in range(9)]
     
    #stores position
    player_pos = {'X':[], 'O':[]}
     
    
    while True:
        print_velha(valores)
         
        #moves
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Please Try Again")
            continue
 
        
        if move < 1 or move > 9:
            print("Wrong Input!!! Please Try Again")
            continue
 
        
        if valores[move-1] != ' ':
            print("Place already filled. Please Try Again!!")
            continue
 
        
 
        #updates grid 
        valores[move-1] = cur_player
 
        #updates plyer position
        player_pos[cur_player].append(move)
 
        #winner check
        if check_winner(player_pos, cur_player):
            print_velha(valores)
            print("Player ", cur_player, " WON!!")     
            print("\n")
            return cur_player
 
        #draw
        if check_draw(player_pos):
            print_velha(valores)
            print("Draw")
            print("\n")
            return 'D'
 
        #next move
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
########################### 
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input("Enter your name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter your name : ")
    print("\n")
     
    #Stores player X or O
    cur_player = player1
 
    #Storeplayer choice
    player_choice = {'X' : "", 'O' : ""}
 
    #Store the option
    options = ['X', 'O']
 
    #Store the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    
    while True:
 
        #the menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
 
        #if input is wrong
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Please Try Again\n")
            continue
 
        #player choice conditions  
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Scores")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Wrong Choice!!!! Please Try Again\n")
 
        #Stores winner
        winner = single_game(options[choice-1])
         
        #Edits the scoreboard 
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        #Switch players
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1