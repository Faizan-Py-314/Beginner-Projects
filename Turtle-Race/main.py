import random
import turtle

screen = turtle.Screen()

colors = ["Red", "Yellow", "Green", "Blue", "Purple"]
cordinates = [-320, -320/2, 0, 320/2, 320]

turtles = []
def create_turtles():
    for i in range(5):
        t = turtle.Turtle()
        t.color(colors[i])

        t.shape("turtle")
        t.speed(2)
        t.penup()
        t.left(90)

        t.goto(cordinates[i], -300)
        turtles.append(t)

def main():
    create_turtles()

    i = 0
    while True:
        random_speed = random.choice([2, 4, 5, 7, 9])

        if turtles[i].ycor() >= 300:
            print(colors[i], "Turtle Win")
            break
        
        turtles[i].pendown()
        turtles[i].forward(random_speed)

        i += 1

        if i >= 5:
            i = 0
    
main()

screen.mainloop()
