#Imports
import random
import simplegui
import Player
#import PySimpleGUI as simplegui # <-- Use this if you're on VSC, then comment out the one above.

class UI:
    def __init__(self):
        #Variable declaration
        self.CANVAS_WIDTH = 600
        self.CANVAS_HEIGHT = 400
        self.player_hp = Player.hp
        #self.player_hp = 100
        self.score = 0
        self.gameover = False
        
        self.frame = simplegui.create_frame("G50 Project", self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.frame.set_draw_handler(self.draw)
        
        #Images
        self.healthbar = simplegui.load_image("https://i.imgur.com/Yc0HiCQ.png")

        #Possibly variable
        self.background = simplegui.load_image("https://nintenscorner.wordpress.com/wp-content/uploads/2018/04/800px-sm64_cg_peachscastle1.png") # <---- Fill with image URL, I've placed a filler one for now.

    def draw(self, canvas):
        #Background
        canvas.draw_image(self.background, (self.CANVAS_WIDTH//2, self.CANVAS_HEIGHT//2), (self.CANVAS_WIDTH, self.CANVAS_HEIGHT), (self.CANVAS_WIDTH//2, self.CANVAS_HEIGHT//2), (self.CANVAS_WIDTH, self.CANVAS_HEIGHT))

        #Display Score
        canvas.draw_text(f"score: {self.score}", (520, 35), 20, "White")

        #Display Health
        #canvas.draw_line((43, 30), (63 + self.player_hp, 30), 20, "#e31717")
        canvas.draw_line((43, 30), (self.player_hp*1.63, 30), 20, "#e31717") #Player HP * 1.63 for scaling to fit the health bar, I'll probably fix this another time.
        canvas.draw_image(self.healthbar, (100,50), (190,53), (90, 30), (158, 44))

        #Display Game Over
        if self.gameover:
            canvas.draw_text("GAME OVER", (self.CANVAS_WIDTH//2, self.CANVAS_HEIGHT//2), 50, "White")

    #Pull Health, score and gameover values from another file probably and feed into this.
    def update_ui(self, new_hp, new_score, is_gameover):
        self.player_hp = new_hp
        self.score = new_score
        self.gameover = self.is_gameover #Make this a function that checks if the objective is completed or Player 'dies'.

    def start(self):
        self.frame.start()
            
#ui = UI()
#ui.start()

if __name__ = "__main__":
    ui = UI()
    ui.start
