class Card:

    def __init__(self, _suit, _rank):
        self._suit = _suit
        self._rank = _rank

    def __str__(self):
        return (f'{self._suit} of {self._rank}')


s = Card('Heart', 'Two')

# Using a custom-defined Card class object in a dictionary

d = {}
d['k1'] = s
d
