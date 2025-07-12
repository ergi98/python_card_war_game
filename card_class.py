from constants import RANKS

class Card():
	def __init__(self, suit, rank):
		self.rank = rank
		self.suit = suit
		self.value = RANKS.index(self.rank)

	def __str__(self):
		return f'{self.rank} of {self.suit}'