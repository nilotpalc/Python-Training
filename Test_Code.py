# Showcasing two sections of the code to indicate the use of \
# return and print functions in __str__


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (f'{self.suit} of {self.rank}')


s = Card('Heart', 'Two')

d = []
d.append(s)
