from enum import Enum



class Card:
	
	_card_Values = {"T":10, "J":11, "Q":12, "K":13, "A":14}

	def __init__(self, card):
		if (len(card) != 2):
			raise Exception("Invalid Card: " + card)

		self.suit = card[1]
		self.card = card

		value = card[0]


		if (value.isdigit()):
			self.card_value = int(value)
		else:
			self.card_value = self._card_Values[value]

		print(f"Suit = {self.suit}.  Value = {self.card_value}")

class Hand:	

	# cards is a list of strings
	def __init__(self, cards):
	#	hand = cards.split()
		self.card_list = []
		self.suit_count = {}
		self.value_count = {}
		
		if (len(cards) != 5):
			raise Exception("Invalid hand")

		for card in cards:
			# add card to the hand
			self.card_list.append(Card(card))

		for card in self.card_list:
			if card.suit not in self.suit_count:
				self.suit_count[card.suit] = 1
			else:
				self.suit_count[card.suit] += 1

			if card.card_value not in self.value_count:
				self.value_count[card.card_value] = 1
			else:
				self.value_count[card.card_value] += 1


	def hand_value(self):
		# Returns the value of the hand,
		# 1 for high cardm
		# 2 for pair
		# 3 for two pair
		# 4 for 3 of a kind
		# 5 for a straight	x
		# 6 for a flush     x
		# 7 for full house
		# 8 for four of a kind
		# 9 for straight flush!	x
		# 2nd return value is high card within the hand.  Used to determine winner if same result (eg. pair of 8s vs pair of 5s)
		# 3rd is a list of cards not in the scoring hand - sorted descending.  Can be used to determine winner by 'high card' in event of a tie.

		all_same_suit = self.is_flush()
		isStright = self.is_stright()

		print(isStright)
		print(all_same_suit)
		if all_same_suit and isStright:
			return 9	#stright flush!

		elif all_same_suit:
			return 6  #flush

		elif isStright:
			return 5
		else:
			return 0


	def is_flush(self):
		return self.card_list[0].suit == self.card_list[1].suit == self.card_list[2].suit == self.card_list[3].suit == self.card_list[4].suit

	def is_stright(self):
		card_values = []
		for card in self.card_list:
			card_values.append(card.card_value)
		
		card_values.sort()
		print(card_values)
		n = card_values[0]

		return (card_values[1] == n + 1) and (card_values[2] == n + 2) and (card_values[3] == n + 3) and (card_values[4] == n + 4)




hand = Hand(["TH", "9H", "2H", "KH","QH"])
print(hand.hand_value())