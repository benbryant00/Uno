# Define the possible card colors
COLORS = ['Red', 'Green', 'Yellow', 'Blue', 'None'] # 'None' is for Wild Cards

# Numbers & special cards

VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']

# Wild Cards
WILD_CARDS = ['Wild', 'Wild Draw Four']

class Card:
    def __init__(self, color, value):
        self.color = color 
        self.value = value
        self.is_special = value in ['Skip', 'Reverse', 'Draw Two', 'Wild', 'Wild Draw Four']

    def __repr__(self):
        return f"{self.color} {self.value}"
    
    def is_playable(self, other_card):
        """
        Checks if this cald can be played on top of another card.
        """
        if self.color == 'None': # Wild and Wild Draw Four 
            return True
        
        return self.color == other_card.color or self.value == other_card.value
    
    def apply_affect(self, game_state):
        """
        Applies the effect of the card to the game state. 
        game_state: A dictionary holding the current game status. 
        """
        if self.value == 'Skip':
            game_state['skip_next_player'] = True
        elif self.value == 'Reverse':
            game_state['reverse_order'] = not game_state.get('reverse_order', False)
        elif self.value == 'Draw Two':
            game_state['draw_cards'] = 2
        elif self.value == 'Wild':
            game_state['wild_card_played'] = True
        elif self.value == 'Wild Draw Four':
            game_state['wild_card_played'] = True
            game_state['draw_cards'] = 4


# card.py test cases     
if __name__ == "__main__":
    card1 = Card('Red', '5')
    card2 = Card('Green', '5')
    card3 = Card('Red', 'Skip')
    card4 = Card('None', 'Wild')

    print(f"Card 1: {card1}")
    print(f"Card 2: {card2}")
    print(f"Card 3: {card3}")
    print(f"Card 4: {card4}\n")

    # Check if card2 can be played on card1 (same value)
    print(f"Can card2 be played on card1? {card2.is_playable(card1)}")

    # Check if card3 can be played on card1 (same color)
    print(f"Can card3 be played on card1? {card3.is_playable(card1)}")

    # Check if card4 (Wild) can be played on any card
    print(f"Can card4 be played on card1? {card4.is_playable(card1)}")