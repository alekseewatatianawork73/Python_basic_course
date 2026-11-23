import turtle

# ============================================================
# Создание окна и черепашки
# ============================================================

screen = turtle.Screen()
screen.setup(900, 700)
screen.title("Навигатор черепашки")
screen.bgcolor("lightyellow")

# основная черепашка
tur = turtle.Turtle()
tur.shape("turtle")
tur.speed(3)
tur.pensize(3)
tur.pencolor("darkblue")

# черепашка для записи координат
pen = turtle.Turtle()
pen.speed(0)
pen.color("darkblue")
pen.pensize(3)
pen.hideturtle()

user_name = ""  # имя пользователя (пока нет)


# ============================================================
# Функции
# ============================================================


# Показывает имя пользователя и координаты черепашки в точке (-400, 270).
def show_info():

    # Получаем координаты x и y
    x = tur.xcor()
    y = tur.ycor()

    # Перемещаем ручку в левый верхний угол и очищаем предыдущую надпись
    pen.goto(-400, 270)
    pen.clear()

    # Создаём сообщение о координатах и имени и выводим на экран
    info = f"Имя: {user_name}\nX: {round(x)}\nY: {round(y)}"
    pen.write(info, align="left", font=("Courier", 15, "bold"))

    #  Возвращаем обработку клавиш окну turtle (после создания всплывающих окон обязательно)
    screen.listen()


# Запрашивает имя пользователя и показывает информацию.
def enter_name():
    global user_name  # # разрешаем функции изменять глобальную переменную user_name (созданную снаружи этой функции)

    # Создаём всплывающее окно для ввода имени и обновляем информацию при помощи show_info()
    user_name = screen.textinput("Имя пользователя", "Как тебя зовут?")
    show_info()


# Функции движения черепашки
def move_forward():
    tur.forward(50)


def move_backward():
    tur.backward(50)


# Функции поворота черепашки
def look_right():
    tur.setheading(0)  # вправо


def look_up():
    tur.setheading(90)  # вверх


def look_left():
    tur.setheading(180)  # влево


def look_down():
    tur.setheading(270)  # вниз


# Перемещает черепашку в точку клика
def go_to_click(x, y):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()


# ============================================================
# Основная программа: подключение клавиш и мыши
# ============================================================

screen.listen()  # подключаем обработку клавиш в главном окне screen

# Ввод имени
screen.onkey(enter_name, "n")

# Движение - стрелки
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")

# Направление черепашки - WASD
screen.onkey(look_right, "d")
screen.onkey(look_up, "w")
screen.onkey(look_left, "a")
screen.onkey(look_down, "s")

# Перемещение по клику мыши
screen.onscreenclick(go_to_click)

# Информация о координатах при нажатии на пробел
screen.onkey(show_info, "space")

turtle.done()
