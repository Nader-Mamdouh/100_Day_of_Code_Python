from turtle import Turtle
ALIGENMENT = "center"
FONT = "Arial"
FONTTYPE = "normal"
FONTSIZE = 16


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(f"L_Score : {self.l_score}", align=ALIGENMENT, font=(FONT, FONTSIZE, FONTTYPE))
        self.goto(100, 200)
        self.write(f"R_Score : {self.l_score}", align=ALIGENMENT, font=(FONT, FONTSIZE, FONTTYPE))

    def increase_R_score(self):
        self.r_score+=1
        self.clear()
        self.update_score()

    def increase_L_score(self):
        self.l_score+=1
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(f"L_Score : {self.l_score}", align=ALIGENMENT, font=(FONT, FONTSIZE, FONTTYPE))
        self.goto(100, 200)
        self.write(f"R_Score : {self.r_score}", align=ALIGENMENT, font=(FONT, FONTSIZE, FONTTYPE))


