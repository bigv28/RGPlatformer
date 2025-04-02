import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector


class Keyboard:
    def __init__(self, player):
        self.player = player

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.player.velocity = Vector(2, 0)
        if key == simplegui.KEY_MAP['a']:
            self.player.velocity = Vector(-2, 0)

        if key == simplegui.KEY_MAP['space']:
            self.player.velocity += Vector(0, -5)
