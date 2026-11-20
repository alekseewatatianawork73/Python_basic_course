import turtle


screen = turtle.Screen()
screen.setup(900, 750)
screen.title("С Днём матери!")
screen.bgcolor("#FFF5F7")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def draw_circle(x, y, radius, color):
    pen.setheading(0)
    move_to(x, y - radius)
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def draw_heart(x, y, size, color):
    move_to(x, y)
    pen.color(color)
    pen.setheading(140)
    pen.begin_fill()
    pen.forward(size)
    pen.circle(-size / 2, 200)
    pen.left(120)
    pen.circle(-size / 2, 200)
    pen.forward(size)
    pen.end_fill()

    pen.setheading(0)


def draw_leaf(x, y, angle):
    move_to(x, y)
    pen.setheading(angle)
    pen.color("#70A879")
    pen.begin_fill()
    pen.circle(30, 60)
    pen.left(120)
    pen.circle(30, 60)
    pen.left(120)
    pen.end_fill()

    pen.setheading(0)


def draw_flower(x, y, petal_color):
    # Стебель
    move_to(x, y)
    pen.setheading(270)
    pen.pencolor("#568B60")
    pen.pensize(5)
    pen.forward(105)
    pen.pensize(1)

    # Листья
    draw_leaf(x, y - 65, 25)
    draw_leaf(x, y - 85, 145)

    # Шесть лепестков вокруг центра
    for angle in range(0, 360, 60):
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle)
        pen.forward(20)
        petal_x = pen.xcor()
        petal_y = pen.ycor()
        draw_circle(petal_x, petal_y, 17, petal_color)

    # Серединка
    draw_circle(x, y, 13, "#F5C85B")


def write_text(x, y, text, size, color, style="normal"):
    pen.penup()
    pen.goto(x, y)
    pen.pencolor(color)
    pen.write(text, align="center", font=("Arial", size, style))


move_to(-415, -340)
pen.setheading(0)
pen.pencolor("#E6B7C7")
pen.pensize(3)

for i in range(2):
    pen.forward(830)
    pen.left(90)
    pen.forward(680)
    pen.left(90)

pen.pensize(1)


write_text(0, 255, "С Днём матери!", 38, "#A83F65", "bold")
for x in range(-60, 61, 30):
    draw_circle(x, 235, 3, "#D897AD")

draw_heart(0, -35, 150, "#E7809D")
write_text(0, 95, "Мамочка,", 25, "#FFFFFF", "bold")
write_text(0, 55, "я тебя люблю!", 23, "#FFFFFF", "bold")

draw_heart(-295, 110, 30, "#F2B0C3")
draw_heart(285, 130, 36, "#EBA0B8")
draw_heart(-240, -25, 23, "#EBA0B8")
draw_heart(245, -15, 25, "#F2B0C3")

draw_flower(-300, -145, "#F2A5BA")
draw_flower(-225, -180, "#D7B5E8")
draw_flower(225, -180, "#F2A5BA")
draw_flower(300, -145, "#D7B5E8")

write_text(0, -140, "Спасибо за твою любовь,", 23, "#92516A")
write_text(0, -178, "заботу и тепло!", 23, "#92516A")
write_text( 0, -320, "Оставайся такой же доброй и чаще улыбайся!", 21, "#A83F65", "italic")

turtle.done()
