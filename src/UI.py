#Imports
import random
import simplegui
#import PySimpleGUI as simplegui # <-- Use this if you're on VSC, then comment out the one above.


#Variable declaration
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
player_hp = 100
score = 0
gameover = False

#Images
healthbar = simplegui.load_image("https://i.imgur.com/Yc0HiCQ.png")

#Possibly variable
background = simplegui.load_image("https://nintenscorner.wordpress.com/wp-content/uploads/2018/04/800px-sm64_cg_peachscastle1.png") # <---- Fill with image URL, I've placed a filler one for now.

def draw(canvas):
    global score, player_hp, gameover

    #Background
    canvas.draw_image(background, (CANVAS_WIDTH//2, CANVAS_HEIGHT//2), (CANVAS_WIDTH, CANVAS_HEIGHT), (CANVAS_WIDTH//2, CANVAS_HEIGHT//2), (CANVAS_WIDTH, CANVAS_HEIGHT))

    #Display Score
    canvas.draw_text(f"score: {score}", (520, 35), 20, "White")

    #Display Health
    #canvas.draw_line((43, 30), (63 + player_hp, 30), 20, "#e31717")
    canvas.draw_line((43, 30), (player_hp*1.63, 30), 20, "#e31717") #Player HP * 1.63 for scaling to fit the health bar, I'll probably fix this another time.
    canvas.draw_image(healthbar, (100,50), (190,53), (90, 30), (158, 44))

    #Display Game Over
    if gameover:
        canvas.draw_text("GAME OVER", (CANVAS_WIDTH//2, CANVAS_HEIGHT//2), 50, "White")

#Pull Health, score and gameover values from another file probably and feed into this.
def update_ui(new_hp, new_score, is_gameover):
    global player_hp, score, gameover
    player_hp = new_hp
    score = new_score
    gameover = is_gameover #Make this a function that checks if the objective is completed or Player 'dies'.
        
frame = simplegui.create_frame("G50 Project", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)

if __name__ = "__main__":
    frame.start()
