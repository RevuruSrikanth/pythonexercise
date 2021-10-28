while True:
    choice = input("Do wanna play a game of Rock-paper-scissor? Y/N\n")
    if choice == 'Y':
        p1=input("Player 1, Enter Your Choice:")
        p2 = input("Player 2, Enter Your Choice:")

        def game(player1,player2):
            if player1 == player2:
                return("Its a tie!!!")

            elif player1 == 'rock':
                if player2 == 'scissors':
                    return("Player 1 wins\n Congrations!!!")
                else:
                    return("Player 2 wins\n Congrations!!!")
            elif player1 == 'scissors':
                if player2 == 'paper':
                    return("Player1 wins\n Congrations!!!")
                else:
                    return("Player 2 wins\n Congrations!!!")
            elif player1 == 'paper':
                if player2 == 'rock':
                    return("Player1 wins\n Congrations!!!")
                else:
                    return("Player2 wins\n Congrations!!!")
        print(game(p1, p2))

    else:
        print("game over")
    if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
        continue
    else:
        print('game over.')
        break