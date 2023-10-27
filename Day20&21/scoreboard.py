from turtle import Turtle, Screen
ALIGENMENT = "center"
FONT = "Arial"
FONTTYPE = "normal"
FONTSIZE = 16
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()


    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGENMENT, font=(FONT, FONTSIZE,FONTTYPE ))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!", align=ALIGENMENT, font=(FONT, FONTSIZE,FONTTYPE ))
