from turtle import Turtle, Screen
import colorsys

tan = Turtle()
tan.width(3)
H = 120
ANGLE = 45

def position():
    tan.penup()
    tan.goto(100, 10)
    tan.pendown()

def loop_run(start, end, tempo):
    global H, ANGLE
    tan.speed(tempo)
    for p in range(start, end):
        color = colorsys.hsv_to_rgb(H, 1, 1)
        tan.color(color)
        H += 0.92
        tan.right(ANGLE)
        tan.circle(-p / 3, 270)
        tan.circle(p / 2, 270)
        tan.circle(p / 5, 180)

def home_run():
    global H
    color = colorsys.hsv_to_rgb(H, 1, 1)
    tan.color(color)
    tan.hideturtle()
    H += 0.92
    tan.right(ANGLE)
    tan.circle((1 - 200) / 3, 90)

def main():
    print(__name__)
    screen = Screen()
    screen.bgcolor("#000020")
    screen.title("Tandala")
    position()
    loop_run(180, 186, 10)
    loop_run(186, 260, 12)
    home_run()
    print("Tandala successfully drawn")

    screen.exitonclick()


if __name__ == '__main__':
    main()
