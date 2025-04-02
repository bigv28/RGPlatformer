from Keyboard import Keyboard
from UI import UI

class Interaction:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies #!!! enemies need to be a list so that line 28 works !!!
        self.keyboard = Keyboard(self.player)

    def check_collision(self, entity_1, entity_2):
        temp_size_1_x = entity_1.size.x / 2
        temp_size_1_y = entity_1.size.y / 2
        temp_size_2_x = entity_2.size.x / 2
        temp_size_2_y = entity_2.size.y / 2
        
        return (
            entity_1.position.x < entity_2.position.x + temp_size_2_x and
            entity_1.position.x + temp_size_1_x > entity_2.position.x and
            entity_1.position.y < entity_2.position.y + temp_size_2_y and
            entity_1.position.y + temp_size_1_y > entity_2.position.y
        )

    def detect_collision(self, entity):
        if entity != self and self.collision(entity):
            return

    def enemy_collision(self):
        for enemy in self.enemies:
            if self.check_collision(self.player, enemy):
                self.player.take_damage(10)
    

    def draw(self):
        pass
