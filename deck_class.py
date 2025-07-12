from card_class import Card
from random import shuffle, randrange

class Deck():
	suits = ("Heart", "Diamonds", "Clubs", "Spades")
	ranks = (
		"2", "3", "4", 
		"5", "6", "7",
		"8", "9", "10", 
		"J", "Q", "K", "A"
	)

	def __init__(self, cards = []):
		self.cards = cards

	def fill(self):
		'''
		Fill the deck with all the cards
		'''
		for suit in self.suits:
			for rank in self.ranks:
				self.cards.append(Card(suit, rank))

	def deal_cards_to_players(self):
		'''
		Given a deck split it in half
		'''
		shuffle(self.cards)
		half_index = int(len(self.cards)/2)
		
		return (
			Deck(self.cards[0:half_index]),
			Deck(self.cards[half_index:]),
		)

	def no_cards_left(self):
		return len(self.cards) == 0

	def draw_random_cards(self, amount = 1):
		'''
		Gets a card from the deck and removes it
		'''
		drawn_cards = []

		amount_left = min(len(self.cards), amount)

		while amount_left > 0:
			rand_int = randrange(0, len(self.cards))
			drawn_cards.append(self.cards.pop(rand_int))
			amount_left -= 1
		return drawn_cards

	def add_to_deck(self, cards = []):
		self.cards.extend(cards)
		pass

	def __len__(self):
		return len(self.cards)