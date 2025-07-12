'''
	Implementation of Card War Game
	https://en.wikipedia.org/wiki/War_(card_game)
'''
from game_class import Game

def main():

	game = Game()
	game_winner = game.get_winner()

	# Continue playing until one of the decks empties up
	while game_winner == None:
		game.draw_random_cards_for_each_player(amount = 1)
		p1_card, p2_card  = game.select_random_card_from_drawn_cards()
		# As long as we keep getting same value cards
		while p1_card.value == p2_card.value:
			print('Both cards have the same value! Drawing 3 more cards for each player!')
			game.draw_random_cards_for_each_player(amount = 3)
			p1_card, p2_card  = game.select_random_card_from_drawn_cards()

		# At this point we have a winner
		game.add_cards_to_winner(p1_card, p2_card)
		game.reset_round_cards()
		game_winner = game.get_winner()

		print('\n')
		print('\n')
		
if __name__ == "__main__":
	main()