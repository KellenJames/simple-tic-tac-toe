from board import Board

game_over = False
play_again = 'Y'
while(play_again == 'Y'):
    game = Board()
    while(not game.endgame):
        game.swap_players()
        game.print_current_board()
        user_choice = int(input())
        if(not game.check_for_valid_move(user_choice)):
            continue
        game.open_spaces -= 1
        game.place_token(user_choice)
        game.check_for_endgame(user_choice)

    game.print_current_board()
    print("Play Again? (Y/N)")
    play_again = input().upper()
    while(play_again != 'Y' and play_again != 'N'):
        print("Play Again? (Y/N)")
        play_again = input().upper()
    