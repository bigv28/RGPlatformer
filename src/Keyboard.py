import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector


class Keyboard:
    def __init__(self, player):
        self.player = player
        self.space_pressed = False


    def keyDown(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.player.velocity = Vector(2, 0)
            self.player.current_animation = "running"
        if key == simplegui.KEY_MAP['a']:
            self.player.velocity = Vector(-2, 0)
            self.player.current_animation = "running"

        if key == simplegui.KEY_MAP['space']:
            if not self.space_pressed:
                self.space_pressed = True
                self.player.velocity += Vector(0, -5)
                self.player.current_animation = "jump"

        if key == simplegui.KEY_MAP['f']:
            self.player.current_animation = 'attacking'

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.player.velocity.x = 0
        if key == simplegui.KEY_MAP['a']:
            self.player.velocity.y = 0

        if key == simplegui.KEY_MAP['space']:
            self.space_pressed = False
            self.player.velocity = Vector(0, 0)

        if key == simplegui.KEY_MAP['f']:
            self.player.current_animation = 'attacking'
