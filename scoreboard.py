from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.pencolor("white")
        self.penup()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.goto(0, 270)
        self.write(f"Score : {self.score} High Score : {self.high_score}", move=False, align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        if self.score > int(self.high_score):
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Courier", 24, "normal"))