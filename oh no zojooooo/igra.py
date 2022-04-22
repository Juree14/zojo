import turtle
import random


wn = turtle.Screen()
wn.title("OH NO, Zojoooo!")
# Gal naredi ozadje
# wn.bgpic()
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.addshape('gal2.gif')

#Spremenljivke
atk_button_pressed = False

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
                wn.bgcolor("black")
                pen.clear()
                start.clear()
                mode = "delitev_moci"
                naslov_delitev_moci()    
wn.onclick(start_click)

# Soba za delitev moci
def naslov_delitev_moci():
    roll_stat = turtle.Turtle()
    roll_stat.speed(0)
    roll_stat.color("white")
    roll_stat.penup()
    roll_stat.hideturtle()
    roll_stat.goto(0, 190)
    roll_stat.write("Roll for stats", align="center", font=("Arial", 35, "normal"))

    atk = turtle.Turtle()
    atk.speed(0)
    atk.color("white")
    atk.penup()
    atk.hideturtle()
    atk.goto(-230, 100)
    atk.write("ATK", align="center", font=("Arial", 30, "normal"))

    defense = turtle.Turtle()
    defense.speed(0)
    defense.color("white")
    defense.penup()
    defense.hideturtle()
    defense.goto(-75, 100)
    defense.write("DEF", align="center", font=("Arial", 30, "normal"))

    spd = turtle.Turtle()
    spd.speed(0)
    spd.color("white")
    spd.penup()
    spd.hideturtle()
    spd.goto(75, 100)
    spd.write("SPD", align="center", font=("Arial", 30, "normal"))

    dge = turtle.Turtle()
    dge.speed(0)
    dge.color("white")
    dge.penup()
    dge.hideturtle()
    dge.goto(230, 100)
    dge.write("DGE", align="center", font=("Arial", 30, "normal"))

# atk-kvadrat s stevilkami
    atk_kocka = turtle.Turtle()
    atk_kocka.hideturtle()
    atk_kocka.speed(0)
    atk_kocka.pencolor("black")
    atk_kocka.color("black")

    atk_kocka_x = -280
    atk_kocka_y = -50
    atk_kocka_length = 100
    atk_kocka_width = 100

    
    atk_kocka.penup()
    atk_kocka.fillcolor("white")
    atk_kocka.begin_fill()
    atk_kocka.goto(atk_kocka_x, atk_kocka_y)
    atk_kocka.goto(atk_kocka_x + atk_kocka_length, atk_kocka_y)
    atk_kocka.goto(atk_kocka_x + atk_kocka_length, atk_kocka_y + atk_kocka_width)
    atk_kocka.goto(atk_kocka_x, atk_kocka_y + atk_kocka_width)
    atk_kocka.goto(atk_kocka_x, atk_kocka_y)
    atk_kocka.end_fill()
    atk_kocka.goto(atk_kocka_x + 35, atk_kocka_y + 22)
    

        
# gumb za koncanje metanja kocke
    atk_button = turtle.Turtle()
    atk_button.hideturtle()
    atk_button.speed(0)
    atk_button.pencolor("black")
    atk_button.color("black")

    atk_button_x = -280
    atk_button_y = -200
    atk_button_length = 100
    atk_button_width = 100


    def atk_button_press():
        atk_button.penup()
        atk_button.fillcolor("white")
        atk_button.begin_fill()
        atk_button.goto(atk_button_x, atk_button_y)
        atk_button.goto(atk_button_x + atk_button_length, atk_button_y)
        atk_button.goto(atk_button_x + atk_button_length, atk_button_y + atk_button_width)
        atk_button.goto(atk_button_x, atk_button_y + atk_button_width)
        atk_button.goto(atk_button_x, atk_button_y)
        atk_button.end_fill()
        atk_button.goto(atk_button_x + 17, atk_button_y + 32)
        atk_button.write("ROLL", font=("Arial", 20, "normal"))
    atk_button_press()

    
    def atk_click(x,y):
        global mode
        global atk_button_pressed
        if atk_button_x <= x <= atk_button_x + atk_button_length:
            if atk_button_y <= y <= atk_button_y + atk_button_width:
                if mode == "delitev_moci":
                    atk_button.clear()
                    mode = "spd_kocka"
                    atk_button_pressed = True
    wn.onclick(atk_click)

    
# spd-kvadrat s stevilkami
    


# Igralec #naredi igralca()
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

# loop igre 
while True:
    wn.update()

    if mode == "delitev_moci" and atk_button_pressed == False:
        atk_kocka_value = turtle.Turtle()
        atk_kocka_value.hideturtle()
        atk_kocka_value.speed(0)
        atk_kocka_value.pencolor("black")
        atk_kocka_value.color("black")
        atk_kocka_value.penup()
        atk_kocka_value.goto(-280 + 35, -50 + 22)
        value = int(random.uniform(1,10))
        atk_kocka_value.write( "{}".format(value), font=("Arial", 40, "normal"))
        atk_kocka_value.clear()
    elif mode == "spd_kocka" and atk_button_pressed == True:
        atk_kocka_value.write( "{}".format(value), font=("Arial", 40, "normal"))
        atk_button_pressed == False
        
        


    
    



