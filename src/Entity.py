from Vector import Vector
from Spritesheet import Spritesheet


class Entity:
    def __init__(self, position, size, animations, hp=100):
        self.position = position  # Vector Instance
        self.size = size
        self.velocity = Vector()
        self.direction = 1  # 1 = right, -1 = left

        self.hp = hp
        self.max_hp = hp
        self.alive = True

        self.animations = {}
        self.current_animation = "idle"
        self.animation_frame = 0
        self.animation_timer = 0

        for state, config in animations.items():
            self.animations[state] = Spritesheet(
                filename=config["path"],
                frame_size=config["frame_size"],
                frame_count=config["frame_count"],
                columns=config.get("columns", 0)
            )

    def set_animation(self, state):
        if state != self.current_animation:
            self.current_animation = state
            self.animation_frame = 0
            self.animation_timer = 0

    def update_animation(self, delta_time):
        if self.current_animation not in self.animations:
            return

        anim = self.animations[self.current_animation]
        self.animation_timer += delta_time

        if self.animation_timer > 0.1:
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % anim.frame_count

    def move(self, distance):
        self.position.add(self.velocity)
        self.set_animation("running")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def jump(self):
        self.set_animation("jump")

    def die(self):
        self.alive = False
        self.set_animation("death")

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def set_animation(self, state):
        if state not in self.animations:
            print("No such animation state for this Entity")
            return

        self.current_animation = state

    def attack(self):
        self.set_animation("attacking")

    def update_animation(self, delta_time):
        self.animation_timer += delta_time
        frame_duration = 0.1  # 100ms per frame

        if self.animation_timer > frame_duration:
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % \
                                   self.animations[self.current_animation].frame_count
