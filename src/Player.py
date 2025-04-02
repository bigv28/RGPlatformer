from Entity import Entity
from Vector import Vector
from Spritesheet import Spritesheet

player_animations = {
    "idle": {
        "path": "assets/player/idle.png",
        "frame_size": (64, 64),
        "frame_count": 4,
        "columns": 4
    },
    "run": {
        "path": "assets/player/run.png",
        "frame_size": (64, 64),
        "frame_count": 6,
        "columns": 0  
}

class Player(Entity):
    def __init__(self):
        super().__init__(position=Vector(100, 300), size=Vector(40, 64), 
                         animations=player_animations)


player_animations = {
    "idle": {
        "path": "assets/sprites/player_idle_2x1.png",  
        "frame_size": (64, 64),  
        "frame_count": 4, 
        "columns": 4  
    },
    "run": {
        "path": "assets/sprites/player_running_8x1.png",
        "frame_size": (64, 64),
        "frame_count": 6,  
        "columns": 0  
    }
}

class Player(Entity):
    def __init__(self):
        super().__init__(position=Vector(100, 300), size=Vector(40, 64), 
                         animations=player_animations)
