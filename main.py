from flask import Flask, render_template
from deck import Deck
import random

app = Flask(__name__)

@app.route('/')
def game():
    deck = Deck()

    p1_cards = []
    p2_cards = []

    for _ in range(9):
        p1_cards.append(deck.draw())
        p2_cards.append(deck.draw())


    p1_cards = enumerate(p1_cards)
    p2_cards = enumerate(p2_cards)

    direction = random.randint(0,1) * 180

    return render_template('game.html',p1_cards=p1_cards,p2_cards=p2_cards,direction=direction)