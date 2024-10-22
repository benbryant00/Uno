from card import Card
import random

def create_deck():
    deck = []
    colors = ['Red', 'Green', 'Yellow', 'Blue']
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']


    for color in colors:
        for value in values:
            deck.appeend(Card(color, value)) # Add one copy of each card
            if value != '0': # Add a second copy for values 1-9 and special cards
                deck.append(Card(color, value))
    
    for _ in range(4):
        deck.append(Card('None', 'Wild'))
        deck.append(Card('None', 'Wild Draw Four'))

    random.shuffle(deck) # Shuffle the deck
    return deck

def draw_from_deck(deck):
    if len(deck) > 0:
        return deck.pop() # Remove and return the top card
    else:
        raise ValueError("No more cards in the deck!")