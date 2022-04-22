import turtle

wn = turtle.Screen()
wn.title("OH NO, Zojoooo!")
# Gal naredi ozadje
# wn.bgpic()
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.addshape('gal2.gif')

# Zacetna stran
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("OH NO, Zojoooo!", align="center", font=("Arial", 35, "normal"))

# Start gumb
start = turtle.Turtle()
start.hideturtle()
start.speed(0)
start.pencolor("black")
start.color("black")

start_x = -100
start_y = -50
start_length = 200
start_width = 100



def start_button():
    start.penup()
    start.fillcolor("white")
    start.begin_fill()
    start.goto(start_x, start_y)
    start.goto(start_x + start_length, start_y)
    start.goto(start_x + start_length, start_y + start_width)
    start.goto(start_x, start_y + start_width)
    start.goto(start_x, start_y)
    start.end_fill()
    start.goto(start_x + 35, start_y + 25)
    start.write("START", font=("Arial", 30, "normal"))
start_button()

mode = "zacetek"
def start_click(x,y):
    global mode
    if start_x <= x <= start_x + start_length:
        if start_y <= y <= start_y + start_width:
            if mode == "zacetek":
                naredi_igralca()
                wn.bgcolor("green")
                pen.clear()
                start.clear()
                mode = "v igri"      

wn.onclick(start_click)



# Igralec
def naredi_igralca():
    igralec = turtle.Turtle()
    igralec.speed(0)
# Gal naredi sliko
    igralec.shape('gal2.gif')
    igralec.penup()
    igralec.goto(0,-250)

#Premikanje igralca

    def igralec_up():
        y = igralec.ycor()
        y += 5
        igralec.sety(y)

    def igralec_down():
        y = igralec.ycor()
        y -= 5
        igralec.sety(y)

    def igralec_right():
        x = igralec.xcor()
        x += 5
        igralec.setx(x)

    def igralec_left():
        x = igralec.xcor()
        x -= 5
        igralec.setx(x)

# Tipkovnica
    wn.listen()
    wn.onkeypress(igralec_up, "w")
    wn.onkeypress(igralec_down, "s")
    wn.onkeypress(igralec_right, "d")
    wn.onkeypress(igralec_left, "a")

# igra    
while True:
    wn.update()