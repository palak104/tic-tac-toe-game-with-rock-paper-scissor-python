#I palak depani,student number,000787449,certify that all code submitted is
#my own work;that i have not copied from any other source.I also certify that
#i have not allowed my work to be copied by others.



import random
def tic_tac_toe():
    #in python index start from 0 so to make convinent according to coding i put values from 0 to 8 in tic tac toe box
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    winSituation = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    end = False
     #draw board for tic tac toe game
    def drawBoard():
        print(board[0],'|', board[1],'|' ,board[2])
        print("---------")
        print(board[3],'|' ,board[4],'|' ,board[5])
        print("---------")
        print(board[6],'|' ,board[7],'|' ,board[8])
        print()


    
    #player 1 function
    def player1():
        p = numChoice()
        if(board[p] == "X" or board[p] == "O"):
            print("Position is already occupied. Please select another position.")
            player1()
        elif(gamerspls()==True):
            board[p] = "X"
        else:
            board[p] = "O"
            
        
        
    #player 2 function
    def player2():
        p = numChoice()
        if board[p] == "X" or board[p] == "O":
            print("Position is already occupied. Please select another position.")
            player2()
        elif(gamerspls()==True):
            board[p] = "O"
        else:
            board[p] = "X"
            board


            
    def numChoice():
        while True:
            i= input()
            i=int(i)
            if i in range(0, 9):
                return i
            else:
                print("Position number you enter is not on board so please try again and use position number which is in range")
                continue

    #implementation of rock scissor paper lizard spock game inside tic tac toe      
    def gamerspls():
        #user input from paper scissor lizard spock rock
        player=input("Make your selection from Rock,Paper,Scissor,Lizard,spock= ")
        player=player.lower()
        if(player=="rock"):
            return rockfun()
        if(player=="scissor"):
            return scissorfun()
        if(player=="paper"):
            return paperfun()
        if(player=="lizard"):
            return lizardfun()
        if(player=="spock"):
            return spockfun()
        else:
            print("Enter valid input")

    def rockfun():
        item=["Rock","Paper","Scissor","Lizard","Spock"]
        select=(random.choice(item)).lower()
        print("Input from computer is= ", select)


        if(select=="scissor"):
            print("Rock crush the Scissor,Hence you win so, you get your desired position")
            return True
        elif(select=="paper"):
            print("Paper covers Rock,you lost so, your desired position goes to your opponent player")
            return False
        elif(select=="lizard"):
            print("Rock crush the lizard,Hence you win so, you get your desired position")
            return True
        elif(select=="spock"):
            print("Spoke vaporizes rock,you lost so, your desired position goes to your opponent player")
            return False
        else:
            print("Input is same as player's input so it is not valid,Try again")
            return rockfun()


    def scissorfun():
        item=["Rock","Paper","Scissor","Lizard","Spock"]
        select=(random.choice(item)).lower()
        print("Input from computer is= ", select)

        if(select=="rock"):
            print("Rock crush the Scissor,you lost so, your desired position goes to your opponent player")
            return False
        elif(select=="paper"):
            print("Scissor cut Paper,Hence you win so, you get your desired position")
            return True
        elif(select=="lizard"):
            print("Scissor decapitate Lizard,Hence you win so, you get your desired position")
            return True
        elif(select=="spock"):
            print("Spock smashes Scissor,you lost so, your desired position goes to your opponent player")
            return False
        else:
            print("Input is same as player's input so it is not valid,Try again")
            return scissorfun()



    def paperfun():
        item=["Rock","Paper","Scissor","Lizard","Spock"]
        select=(random.choice(item)).lower()
        print("Input from computer is= ", select)
        if(select=="rock"):
            print("Paper covers Rock,Hence you win so, you get your desired position")
            return True
        elif(select=="scissor"):
            print("Scissor cut Paper,you lost so, your desired position goes to your opponent player")
            return False
        elif(select=="lizard"):
            print("Lizars eats Paper,you lost so, your desired position goes to your opponent player")
            return False
        elif(select=="spock"):
            print("Paper disproves Spock,Hence you win so, you get your desired position")
            return True
        else:
            print("Input is same as player's input so it is not valid,Try again")
            return paperfun()



    def lizardfun():
        item=["Rock","Paper","Scissor","Lizard","Spock"]
        select=(random.choice(item)).lower()
        print("Input from computer is= ", select)

        if(select=="rock"):
            print("Rock crushes Lizard,you lost so, your desired position goes to your opponent player")
            return False
        elif(select=="scissor"):
            print("Scissor desapitates Lizard,you lost so, your desired position goes to your opponent player")
            return False
        elif(select=="paper"):
            print("Lizars eats Paper,Hence you win so, you get your desired position")
            return True
        elif(select=="spock"):
            print("Lizard poisons Spock,Hence you win so, you get your desired position")
            return True
        else:
            print("Input is same as player's input so it is not valid,Try again")
            return lizardfun()


    def spockfun():
        item=["Rock","Paper","Scissor","Lizard","Spock"]
        select=(random.choice(item)).lower()
        print("Input from computer is= ", select)


        if(select=="rock"):
            print("Spock vaporizes Rock,Hence you win so, you get your desired position")
            return True
        elif(select=="scissor"):
            print("Spock smashes Scissor,Hence you win so, you get your desired position")
            return True
        elif(select=="paper"):
            print("Paper disproves Spock,you lost so, your desired position goes to your opponent player")
            return False
        elif(select=="lizard"):
            print("Lizard poisons Spock,you lost so, your desired position goes to your opponent player")
            return False
        else:
            print("Input is same as player's input so it is not valid,Try again")
            return spockfun()



    #board input position     
    def boardPosition():
        count = 0
        for i in winSituation:
            if board[i[0]] == board[i[1]] == board[i[2]] == "X":
                print("Player 1 Wins this round of Tic Tac Toe game,player 2 loose this game")
                return True

            if board[i[0]] == board[i[1]] == board[i[2]] == "O":
                print("Player 2 Wins this round of Tic Tac Toe game,player 1 loose this game")
                return True
        for i in range(9):
            if board[i] == "X" or board[i] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True



    while not end:
        drawBoard()
        end = boardPosition()
        if(end == True):
            break
        print("Player 1 choice for X position on board : ")
        player1()
        print()
        drawBoard()
        end = boardPosition()
        if(end == True):
            break
        print("Player 2 choice for O position on board : ")
        player2()
        print()

    choice=input("Want to play again ? (give ans in yes or no) ")
    choice=choice.lower()
    if(choice=="yes"):
        print()
        tic_tac_toe()
    else:
        end 

tic_tac_toe()
