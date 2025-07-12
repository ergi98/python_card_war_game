from deck_class import Deck
from random import choice

from constants import PLAYER_ONE, PLAYER_TWO

class Game():
	game_deck = Deck()
	p1_round_cards = []
	p2_round_cards = []

	def __init__(self):
		self.game_deck.fill()
		p1_cards, p2_cards = self.game_deck.deal_cards_to_players()
		self.p1_cards = p1_cards
		self.p2_cards = p2_cards

	def get_winner(self):
		winner = None
		print(f'No of cards left for Player 1: {len(self.p1_cards)}')
		print(f'No of cards left for Player 2: {len(self.p2_cards)}')
		if self.p1_cards.no_cards_left():
			winner = PLAYER_TWO
			print('Game is over. Winner is Player 2!')
		elif self.p2_cards.no_cards_left():
			winner = PLAYER_ONE
			print('Game is over. Winner is Player 1!')
		return winner

	def draw_random_cards_for_each_player(self, amount = 1):
		p1_drawn_cards = self.p1_cards.draw_random_cards(amount)
		p2_drawn_cards = self.p2_cards.draw_random_cards(amount)

		self.p1_round_cards.extend(p1_drawn_cards)
		self.p2_round_cards.extend(p2_drawn_cards)

		print(f'Player 1 cards for this round are: {','.join(map(lambda x: str(x), self.p1_round_cards))}')
		print(f'Player 2 cards for this round are: {','.join(map(lambda x: str(x), self.p2_round_cards))}')


	def select_random_card_from_drawn_cards(self):
		'''
		Given that the players have [1, n] cards per turn drawn select one at random
		'''
		p1_card = choice(self.p1_round_cards)
		p2_card = choice(self.p2_round_cards)

		print(f'Player 1 drew: {str(p1_card)}')
		print(f'Player 2 drew: {str(p2_card)}')

		return (p1_card, p2_card)

	def add_cards_to_winner(self, p1_card, p2_card):
		if p1_card.value > p2_card.value:
			print('Round is over. Winner is Player 1!')
			self.p1_cards.add_to_deck(self.p2_round_cards)
		elif p1_card.value < p2_card.value:
			print(f'Round is over. Winner is Player 2!')
			self.p2_cards.add_to_deck(self.p1_round_cards)

		print(f'Player 1 has {len(self.p1_cards)} cards remaining')
		print(f'Player 2 has {len(self.p2_cards)} cards remaining')


	def reset_round_cards(self):
		self.p1_round_cards.clear()
		self.p2_round_cards.clear()
		