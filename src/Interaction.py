from Keyboard import Keyboard
from UI import UI

class Interaction:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies
        self.keyboard = Keyboard(self.player)

    def draw(self):
        pass