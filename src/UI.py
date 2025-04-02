#Imports
import simplegui
from Player import Player
from Enemy import Enemy

class UI:
    def __init__(self):
        #Variable Assignment

        self.CANVAS_WIDTH = 600
        self.CANVAS_HEIGHT = 400
        
        self.player = player
        self.player_hp = self.player.hp
        self.enemy = enemy
        
        #Game state
        self.score = 0
        self.gameover = False
        
        self.frame = simplegui.create_frame("G50", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw)
        
        self._load_assets()
        
    def _load_assets(self):
        self.tile = simplegui.load_image("https://i.imgur.com/ZFp2uUg.png")
        self.scoreboard = simplegui.load_image("https://i.imgur.com/TzglCC4.png")
        self.healthbar = simplegui.load_image("https://i.imgur.com/Yc0HiCQ.png")
        self.background = simplegui.load_image("https://i.imgur.com/qmxkE9B.png")

    def draw(self, canvas):
        canvas.draw_image(self.background, 
                            (self.CANVAS_WIDTH//2, self.CANVAS_HEIGHT//2),
                            (self.CANVAS_WIDTH, self.CANVAS_HEIGHT),
                            (self.CANVAS_WIDTH//2, self.CANVAS_HEIGHT//2),
                            (self.CANVAS_WIDTH, self.CANVAS_HEIGHT))

        self._draw_health(canvas)
        self._draw_score(canvas)
        self.draw_floor(canvas)
        
        if self.gameover:
            text_width = 200
            canvas.draw_text("GAME OVER", 
                             (self.CANVAS_WIDTH//2 - text_width//2, self.CANVAS_HEIGHT//2),
                             50, "White")

    def _draw_health(self, canvas):
        
        healthbar = self.healthbar
        healthbar_width = healthbar.get_width()
        healthbar_height = healthbar.get_height()
        
        canvas.draw_line((43, 30), (self.player_hp * 1.80, 30), 20, "#e31717")  
        
        canvas.draw_image(healthbar, (healthbar_width / 2,
                          healthbar_height / 2),
                          (healthbar_width, healthbar_height),
                          (100, 30), (healthbar_width*0.9, healthbar_height*0.9))

    def _draw_score(self, canvas):
        scoreboard = self.scoreboard
        canvas.draw_image(scoreboard, (scoreboard.get_width() / 2,
                          scoreboard.get_height() / 2),
                          (scoreboard.get_width(), scoreboard.get_height()),
                          (505, 32), (scoreboard.get_width()*2.5, scoreboard.get_height()*3))
                          
        canvas.draw_text(f"SCORE:{self.score}", 
                         (self.CANVAS_WIDTH - 140, 40), 
                         24, "White", "monospace")
        
    def draw_floor(self, canvas):
        floor_height = 70
        floor_color = "Green"
        tile = self.tile
        position = (0,self.CANVAS_HEIGHT - floor_height)
        
        for i in range(self.CANVAS_WIDTH // 32):
            canvas.draw_image(tile, (tile.get_width() / 2,
                              tile.get_height() / 2),
                              (tile.get_width(), tile.get_height()),
                              position, (tile.get_width()*2, tile.get_height()*2))
            position = (position[0] + 64, position[1])
        
        canvas.draw_polygon([(0, self.CANVAS_HEIGHT - floor_height), 
                             (self.CANVAS_WIDTH, self.CANVAS_HEIGHT - floor_height),
                             (self.CANVAS_WIDTH, self.CANVAS_HEIGHT),
                             (0, self.CANVAS_HEIGHT)], 
                             1, "Black", floor_color)

    def update_ui(self, new_hp, new_score, is_gameover):
        self.player_hp = new_hp
        self.score = new_score
        self.gameover = is_gameover

    def start(self):
        self.frame.start()

ui = UI()
ui.start()
