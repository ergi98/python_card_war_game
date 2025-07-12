class Card():
	value_system = (
		"2", "3", "4", 
		"5", "6", "7", 
		"8", "9", "10", 
		"J", "Q", "K", "A"
	)

	def __init__(self, suit, rank):
		self.rank = rank
		self.suit = suit
		self.value = self.value_system.index(self.rank)

	def __str__(self):
		return f'{self.rank} of {self.suit}'