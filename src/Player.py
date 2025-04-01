import Entity


class Player(Entity.Entity):
    pass

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
        "columns": 0  # Horizontal strip
    }
}

class Player(Entity):
    def __init__(self):
        super().__init__(position=Vector(100, 300), size=Vector(40, 64), 
                     animations=player_animations)