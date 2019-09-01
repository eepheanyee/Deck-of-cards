from random import shuffle
from cards import Card

class Deck():

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            'A',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'J',
            'Q',
            'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt!")
        cards = self.cards[-actual:] #slice to get from -actual to the end as dealt hand
        self.cards = self.cards[:-actual] #slice to get from beginning to -actual as remaining cards
        return cards
    def reset(self):
            suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
            values = [
                'A',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
                '10',
                'J',
                'Q',
                'K']
            self.cards = [Card(suit, value) for suit in suits for value in values]
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


# print("DECK OF CARDS!!!\n\n")
# deck1 = Deck()
# deck1.shuffle()
# print(deck1.cards)
# print(deck1.deal_card())
# print(deck1.count())
# print(deck1.deal_hand(20))
# print(deck1.count())
# print(deck1.cards)

# # my_deck = Deck()
# for x in my_deck:
#     print(x)