#Imports
import random
import simplegui
import Player
#import PySimpleGUI as simplegui # <-- Use this if you're on VSC, then comment out the one above.

import simplegui

class UI:
    def __init__(self, player, entities):
        # Configuration
        self.CANVAS_WIDTH = 600
        self.CANVAS_HEIGHT = 400
        self.player = player
        self.entities = entities  # List of all drawable entities
        
        # Game state
        self.score = 0
        self.gameover = False
        
        # Setup frame
        self.frame = simplegui.create_frame("Rogue Platformer", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw)
        
        # Load assets (local files recommended)
        self._load_assets()
        
    def _load_assets(self):
        """Load all UI images with local fallbacks"""
        try:
            self.healthbar_bg = simplegui.load_image("assets/ui/healthbar_bg.png")
            self.healthbar_fg = simplegui.load_image("assets/ui/healthbar_fg.png")
            self.background = simplegui.load_image("assets/backgrounds/level1.png")
        except:
            print("Error loading images! Using fallback colors")
            self.healthbar_bg = None
            self.healthbar_fg = None
            self.background = None

    def draw(self, canvas):
        # Clear screen
        if self.background:
            canvas.draw_image(self.background, 
                             (self.CANVAS_WIDTH//2, self.CANVAS_HEIGHT//2),
                             (self.CANVAS_WIDTH, self.CANVAS_HEIGHT),
                             (self.CANVAS_WIDTH//2, self.CANVAS_HEIGHT//2),
                             (self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        else:
            canvas.draw_polygon([[0,0], [self.CANVAS_WIDTH,0],
                              [self.CANVAS_WIDTH,self.CANVAS_HEIGHT],
                              [0,self.CANVAS_HEIGHT]], 1, "Black", "Gray")

        # Draw entities
        for entity in self.entities:
            self._draw_entity(canvas, entity)

        # Draw HUD
        self._draw_health(canvas)
        self._draw_score(canvas)
        
        # Game over overlay
        if self.gameover:
            canvas.draw_text("GAME OVER", 
                            (self.CANVAS_WIDTH//2 - 150, self.CANVAS_HEIGHT//2),
                            50, "Red")

    def _draw_entity(self, canvas, entity):
        """Draw an entity with its current animation frame"""
        if entity.current_animation in entity.animations:
            anim = entity.animations[entity.current_animation]
            frame_data = anim.get_frame(entity.animation_frame)
            
            if frame_data and anim.image:
                canvas.draw_image(
                    anim.image,
                    frame_data[0],  # Source center
                    frame_data[1],  # Source size
                    (entity.position.x, entity.position.y),  # Dest center
                    (entity.size.x * abs(entity.direction), entity.size.y)  # Flip based on direction
                )

    def _draw_health(self, canvas):
        max_hp = self.player.max_hp
        current_hp = max(0, min(self.player.hp, max_hp))
        
        # Health bar dimensions
        bg_width = 158  # Match your healthbar_bg.png size
        bg_height = 44
        fg_width = (current_hp / max_hp) * bg_width

        # Draw health bar background
        if self.healthbar_bg:
            canvas.draw_image(self.healthbar_bg,
                            (100, 50), (190, 53),  # Source dimensions
                            (90, 30), (bg_width, bg_height))
        
        # Draw health fill
        canvas.draw_line((43, 30), 
                        (43 + fg_width, 30), 
                        20, "#e31717")
        
        # Draw health bar foreground (decorative elements)
        if self.healthbar_fg:
            canvas.draw_image(self.healthbar_fg,
                            (100, 50), (190, 53),
                            (90, 30), (bg_width, bg_height))

    def _draw_score(self, canvas):
        canvas.draw_text(f"SCORE: {self.score}", 
                        (self.CANVAS_WIDTH - 200, 40), 
                        24, "White", "sans-serif")

    def update_ui(self, new_hp, new_score, is_gameover):
        self.player.hp = new_hp
        self.score = new_score
        self.gameover = is_gameover  # Fixed variable name

    def start(self):
        self.frame.start()
#ui = UI()
#ui.start()

if __name__ = "__main__":
    ui = UI()
    ui.start
