from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}',
                   align=ALIGNMENT,
                   font=FONT)

    def load_high_score(self):
        with open("data.txt") as data:
            return int(data.read())

    def save_high_score(self):
        with open("data.txt", mode='w') as file:
            file.write(f"{self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER',
    #                align=ALIGNMENT,
    #                font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
