from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create()

    def create(self):
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            self.segments.append(segment)
        x_cor, y_cor = 0, 0
        for segment in self.segments:
            segment.goto(x_cor, y_cor)
            x_cor -= 20

    def extend(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        new_position = self.segments[-1].position()
        segment.goto(new_position)
        self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)