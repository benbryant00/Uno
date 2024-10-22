from deck import create_deck, draw_from_deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [] # List to hold player's cards
    
    def choose_card(self, top_card):
        # Logic for the player to choose which card to play (simplified here).

        for card in self.hand:
            if card.is_playable(top_card):
                return card
        return None # No card can be  played

def initialize_game(players):
    """
    Initialize the game state.
    players: List of player objects
    """
    deck = create_deck()
    game_state = {
        # Initial game state
    }

    #Initialize the first card by drawing from the deck (functionality not shown here)
    game_state['top_card'] = draw_first_card()

    return game_state

def initialize_players(player_names, deck):
    """
    Initialize players with their hand of cards.
    player_names: List of player names
    deeck: The shuffled deck of cards
    """

    players = []
    for name in player_names:
        # Each playe starts with 7 cards
        hand = [draw_from_deck(deck) for _ in range(7)]
        players.append({"name": name, "hand": hand})
    return players

def take_turn(player, game_state):
    """
    Manages the currenet player's turn.
    player: The player whose turn it is
    game_stae: The current state of the game
    """
    pass

def draw_first_card(deck):
    """
    Draw the first card to start the game. This function can handle logic
    to ensure the first card is not a special card like Wild or Draw Four.
    """

    card = draw_from_deck(deck)
    while card.is_special:
        card = draw_from_deck(deck)
    return card
