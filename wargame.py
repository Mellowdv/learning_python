'''
War card game

Importing random to shuffle decks. :)
'''
import random

# Card class, has a suit (Hearts, Diamonds, Clubs, Spades) and a rank (from 2 to Ace).

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f'{self.rank} of {self.suit}'

	def __repr__(self):
		return f'{self.rank} of {self.suit}'

# Deck class that's essentialy a container for a list of cards of each player.
# Has methods for manipulating the cards on the list and ones for printing the content for testing purposes.

class Deck:

	def __init__(self, card_list):
		self.card_list = card_list

	def __repr__(self):
		return f'{self.card_list}'	

	def __len__(self):
		return len(self.card_list)

	def add_card(self, card):
		self.card_list += card 

	def remove_card(self, i = -1):
		self.card_list.pop(i)

# Player class that has a hand of active cards, methods for adding and removing said cards (in two varieties, 2 or 5)
# Has a method for clearing the hand and for taking all the cards on the table for winning.

class Player:

	def __init__(self, deck):
		self.hand = []
		self.deck = deck

	def take_two(self):
		for i in range(0,2):
			self.hand.append(self.deck.card_list[-1])
			self.deck.remove_card()

	def take_five(self):
		for i in range(0,5):
			self.hand.append(self.deck.card_list[-1])
			self.deck.remove_card()

	def take_cards(self, active_cards):
		self.deck.add_card(active_cards)

	def clear_hand(self):
		self.hand = []

	#testing and printing stuff

	def __repr__(self):
		return f'{self.deck}, total of {len(self.deck)} cards.'


# Temp space for logic and testing
# What it does so far (to be factored into functions of course): there's a dictionary for comparing values,
# generates the initial deck, shuffles it and splits it into 2 decks that are actually of the Deck class.
# The decks contain 26 Card objects each.

def deck_creation(suit_list, rank_list):

	initial_deck = []

	for suit in suit_list:
		for i in range(0, 13):
			initial_deck.append(Card(suit, rank_list[i]))

	return initial_deck

def deck_splitter(deck):

	return Deck(deck[0:26]), Deck(deck[26:52])


# Here is the part that needs to basically be game logic.
# There already are functions for creating player decks.
# It needs a function to compare the topmost cards and decide which one wins, in case of ties - draw 5 more and decide the victor.
# Winner takes all. Losing the game is equivalent to having 0 cards in your deck.
# The dictionary and 2 lists are necessary for the game to function.

rank_value_dic = {'2':2,'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
rank_list = list(rank_value_dic.keys())
suit_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

initial_deck = deck_creation(suit_list, rank_list)

random.shuffle(initial_deck)

deck1, deck2 = deck_splitter(initial_deck)

player1 = Player(deck1)
player2 = Player(deck2)

player1.take_two()
player2.take_two()

active_cards = player1.hand + player2.hand

if rank_value_dic[player1.hand[-1].rank] != rank_value_dic[player2.hand[-1].rank]:
	if rank_value_dic[player1.hand[-1].rank] > rank_value_dic[player2.hand[-1].rank]:
		print('Player1 wins this round!')
		player1.take_cards(active_cards)
		print(player1)
	else:
		print('Player2 wins this round!')
else:
	print('The cards are equal value!')