class Card:
    """ Class to store card information """

    def __init__(self,rank,suit):
        """ Construct the card """

        self.rank = str(rank)
        self.suit = suit
        
    @property
    def value(self):
        """ Determine the value of the card """

        cards = {
            "Two":2,
            "Three":3,
            "Four":4,
            "Five":5,
            "Six":6,
            "Seven":7,
            "Eight":8,
            "Nine":9,
            "Ten":10,
            "Jack":10,
            "Queen":10,
            "King":10,
            "Ace":11,
        }

        return cards[self.rank]

    @property
    def suit_symbol(self):
        """ Turn suit name into suit symbol """

        suits = {
            "Spades":"♠",
            "Hearts":"♡",
            "Clubs":"♣",
            "Diamonds":"♢"
        }
        return suits[self.suit]

    def to_json(self):
        """ Convert card data into json to send over server """

        data = {}

        data["rank"] = self.rank
        data["suit"] = self.suit

        return data

    def from_json(data):
        """ Reconstruct card from json """

        rank = data["rank"]
        suit = data["suit"]

        return Card(rank,suit)

    def __str__(self):
        """ Format card data """

        if self.rank in ["Jack","Queen","King","Ace"]:
            abbr = self.rank[0]
        else:
            abbr = str(self.value)

        card = abbr + self.suit_symbol

        return card
    
    def image_path(self):
        return f"cards_png/card_{self.rank.lower()}_{self.suit.lower()}.png"
    
    def __repr__(self):
        """ Representation of card """

        if self.rank in ["Jack","Queen","King","Ace"]:
            abbr = self.rank[0]
        else:
            abbr = str(self.value)
        return abbr + self.suit_symbol