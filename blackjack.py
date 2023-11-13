############### Blackjack Project #####################
#from art import logo
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


    
def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    if play == 'y':
        continue_game = True
        
    def get_card():
        card = random.choice(cards)
        return card

    def generate_player_first_cards():
        player_cards = []
        player_cards.append(get_card())
        player_cards.append(get_card())
        player_total = sum(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_total}")
        return player_cards, player_total

    def generate_dealer_first_cards():
        dealer_cards = []
        dealer_cards.append(get_card())
        dealer_cards.append(get_card())
        dealer_total = sum(dealer_cards)
        print(f"Dealer's first card: {dealer_cards[0]}")
        return dealer_cards, dealer_total

    def generate_player_card(player_cards):
        player_cards.append(get_card())
        player_total = sum(player_cards)
        print(f"Player cards: {player_cards}, current score {player_total}")
        if player_total > 21:
            declare_winner("Busted, Dealer wins")
        

    def calculate_results(player_sum, dealer_sum):
        if player_sum > dealer_sum:
            winner = "player"
        elif dealer_sum > player_sum:
            winner = "dealer"
        else:
            winner = "It's a draw"
        return winner

    def declare_winner(winner):
        print(f"The winner is {winner}")
        play_again = input("Do you want to play again? Type 'y' or 'n': ")
        #print(f"Play again value: {play_again}")
        return play_again

    another_card = True

    while continue_game:
        player_sum = generate_player_first_cards()
        dealer_sum = generate_dealer_first_cards()
        #print(player_sum)
        if dealer_sum[1] == 21:
            declare_winner(winner)
        else:
            while another_card == True:
                another = input("Type 'y' to get another card, type 'n' to pass: ")
                if another == 'n':
                    another_card = False
                else:
                    generate_player_card(player_sum[0])
        winner = calculate_results(player_sum[1], dealer_sum[1])
        
        if declare_winner(winner) == 'n':
            continue_game = False
        else:
            play_game()
        
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == 'y':
    play_game()
