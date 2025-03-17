from Vector import Vector
from Spritesheet import Spritesheet


class Entity:
    def __init__(self, position, size, spritesheets, hp=100):
        self.position = position    # Vector Instance
        self.size = size
        self.velocity = Vector()
        self.direction = 1      # 1 to face right, -1 to face left

        self.hp = hp
        self.max_hp = hp
        self.alive = True
        self.state = "idle"     # Could also be "running" and "attacking"
        self.animations = {}    # Will store the processed Spritesheets for each state
        for filename in spritesheets:
            if "idle" in filename:
                self.animations["idle"] = Spritesheet(filename)
            elif "running" in filename:
                self.animations["running"] = Spritesheet(filename)
            elif "attacking" in filename:
                self.animations["attacking"] = Spritesheet(filename)

    def move(self, distance):
        self.position.add(self.velocity)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        self.alive = False

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def set_animation(self, state):
        if state not in self.animations:
            print("No such animation state for this Entity")
            return

        self.state = state

    def attack(self):
        if "attacking" in self.animations:
            self.state = "attacking"
        else:
            print("This entity cannot attack")
