from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", font= FONT, align= ALIGNMENT)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", font= FONT, align= ALIGNMENT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()