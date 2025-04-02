from Entity import Entity
from Vector import Vector
from Spritesheet import Spritesheet

player_animations = {
    "idle": {
        "path": "assets/sprites/player_idle_2x1.png",
        "frame_size": (32, 32),
        "frame_count": 2,
        "columns": 0
    },
    "running": {
        "path": "assets/sprites/player_running_8x1.png",
        "frame_size": (32, 32),
        "frame_count": 6,
        "columns": 0
    },
    "attacking": {
        "path": "assets/sprites/player_attacking_8x1.png",
        "frame_size": (32, 32),
        "frame_count": 8,
        "columns": 0
    },
    "death": {
        "path": "assets/sprites/player_death_5x1.png",
        "frame_size": (32, 32),
        "frame_count": 5,
        "columns": 0
    },
    "jump": {
        "path": "assets/sprites/player_jump_8x1.png",
        "frame_size": (32, 32),
        "frame_count": 8,
        "columns": 0
    }}


class Player(Entity):
    def __init__(self):
        super().__init__(position=Vector(100, 300), size=Vector(40, 64),
                         animations=player_animations)
