
import turtle
import random
import time





wn = turtle.Screen()
wn.title("OH NO, Zojoooo!")
# Gal naredi ozadje
# wn.bgpic()
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.cv._rootwindow.resizable(False, False)

# dodajanje slik
wn.addshape('slike\zojo.gif')
wn.addshape('slike\zojoback.gif')
wn.addshape('slike\Zojoright.gif')
wn.addshape('slike\leftZojo.gif')
wn.addshape('slike\hisa.gif')
wn.addshape('slike\gal3.gif')

#Spremenljivke

mode = "zacetek"

atk_button_pressed = False
def_button_pressed = False
spd_button_pressed = False
dge_button_pressed = False

min = 1
atk_spremenljivka = False
def_spremenljivka = False
spd_spremenljivka = False

neki = True


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


def start_click(x,y):
    global mode
    if start_x <= x <= start_x + start_length:
        if start_y <= y <= start_y + start_width:
            if mode == "zacetek":
                wn.bgcolor("black")
                pen.clear()
                start.clear()
                mode = "delitev_moci"
                soba_delitev_moci()    
wn.onclick(start_click)

# Soba za delitev moci
def soba_delitev_moci():
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

# atk-kocka
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
    

        
# atk-gumb za metanje kocke
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
        global def_button_pressed
        global spd_button_pressed
        global dge_button_pressed
        if atk_button_x <= x <= atk_button_x + atk_button_length:
            if atk_button_y <= y <= atk_button_y + atk_button_width:
                if mode == "delitev_moci":
                    atk_button.clear()
                    mode = "def_kocka"
                    atk_button_pressed = True
        if def_button_x <= x <= def_button_x + def_button_length:
            if def_button_y <= y <= def_button_y + def_button_width:
                if mode == "def_kocka":
                    def_button.clear()
                    mode = "spd_kocka"
                    def_button_pressed = True
        if spd_button_x <= x <= spd_button_x + spd_button_length:
            if spd_button_y <= y <= spd_button_y + spd_button_width:
                if mode == "spd_kocka":
                    spd_button.clear()
                    mode = "dge_kocka"
                    spd_button_pressed = True
        if dge_button_x <= x <= dge_button_x + dge_button_length:
            if dge_button_y <= y <= dge_button_y + dge_button_width:
                if mode == "dge_kocka":
                    dge_button.clear()
                    mode = "begin"
                    dge_button_pressed = True
                    begin_button_on()
        
                
    wn.onclick(atk_click)
# def-kocka

    
    def_kocka = turtle.Turtle()
    def_kocka.hideturtle()
    def_kocka.speed(0)
    def_kocka.pencolor("black")
    def_kocka.color("black")

    def_kocka_x = -125
    def_kocka_y = -50
    def_kocka_length = 100
    def_kocka_width = 100

    
    def_kocka.penup()
    def_kocka.fillcolor("white")
    def_kocka.begin_fill()
    def_kocka.goto(def_kocka_x, def_kocka_y)
    def_kocka.goto(def_kocka_x + def_kocka_length, def_kocka_y)
    def_kocka.goto(def_kocka_x + def_kocka_length, def_kocka_y + def_kocka_width)
    def_kocka.goto(def_kocka_x, def_kocka_y + def_kocka_width)
    def_kocka.goto(def_kocka_x, def_kocka_y)
    def_kocka.end_fill()
    def_kocka.goto(def_kocka_x + 35, def_kocka_y + 22)
    

# def-gumb za metanje kocke

    def_button = turtle.Turtle()
    def_button.hideturtle()
    def_button.speed(0)
    def_button.pencolor("black")
    def_button.color("black")

    def_button_x = -125
    def_button_y = -200
    def_button_length = 100
    def_button_width = 100
    

    def def_button_press():
        def_button.penup()
        def_button.fillcolor("white")
        def_button.begin_fill()
        def_button.goto(def_button_x, def_button_y)
        def_button.goto(def_button_x + def_button_length, def_button_y)
        def_button.goto(def_button_x + def_button_length, def_button_y + def_button_width)
        def_button.goto(def_button_x, def_button_y + def_button_width)
        def_button.goto(def_button_x, def_button_y)
        def_button.end_fill()
        def_button.goto(def_button_x + 17, def_button_y + 32)
        def_button.write("ROLL", font=("Arial", 20, "normal"))
    def_button_press()



# spd-kocka


    spd_kocka = turtle.Turtle()
    spd_kocka.hideturtle()
    spd_kocka.speed(0)
    spd_kocka.pencolor("black")
    spd_kocka.color("black")

    spd_kocka_x = 25
    spd_kocka_y = -50
    spd_kocka_length = 100
    spd_kocka_width = 100

    
    spd_kocka.penup()
    spd_kocka.fillcolor("white")
    spd_kocka.begin_fill()
    spd_kocka.goto(spd_kocka_x, spd_kocka_y)
    spd_kocka.goto(spd_kocka_x + spd_kocka_length, spd_kocka_y)
    spd_kocka.goto(spd_kocka_x + spd_kocka_length, spd_kocka_y + spd_kocka_width)
    spd_kocka.goto(spd_kocka_x, spd_kocka_y + spd_kocka_width)
    spd_kocka.goto(spd_kocka_x, spd_kocka_y)
    spd_kocka.end_fill()
    spd_kocka.goto(spd_kocka_x + 35, spd_kocka_y + 22)


# spd-gumb za metanje kocke


    spd_button = turtle.Turtle()
    spd_button.hideturtle()
    spd_button.speed(0)
    spd_button.pencolor("black")
    spd_button.color("black")

    spd_button_x = 25
    spd_button_y = -200
    spd_button_length = 100
    spd_button_width = 100


    def spd_button_press():
        spd_button.penup()
        spd_button.fillcolor("white")
        spd_button.begin_fill()
        spd_button.goto(spd_button_x, spd_button_y)
        spd_button.goto(spd_button_x + spd_button_length, spd_button_y)
        spd_button.goto(spd_button_x + spd_button_length, spd_button_y + spd_button_width)
        spd_button.goto(spd_button_x, spd_button_y + spd_button_width)
        spd_button.goto(spd_button_x, spd_button_y)
        spd_button.end_fill()
        spd_button.goto(spd_button_x + 17, spd_button_y + 32)
        spd_button.write("ROLL", font=("Arial", 20, "normal"))
    spd_button_press()


# dge kocka
    dge_kocka = turtle.Turtle()
    dge_kocka.hideturtle()
    dge_kocka.speed(0)
    dge_kocka.pencolor("black")
    dge_kocka.color("black")

    dge_kocka_x = 180
    dge_kocka_y = -50
    dge_kocka_length = 100
    dge_kocka_width = 100

    
    dge_kocka.penup()
    dge_kocka.fillcolor("white")
    dge_kocka.begin_fill()
    dge_kocka.goto(dge_kocka_x, dge_kocka_y)
    dge_kocka.goto(dge_kocka_x + dge_kocka_length, dge_kocka_y)
    dge_kocka.goto(dge_kocka_x + dge_kocka_length, dge_kocka_y + dge_kocka_width)
    dge_kocka.goto(dge_kocka_x, dge_kocka_y + dge_kocka_width)
    dge_kocka.goto(dge_kocka_x, dge_kocka_y)
    dge_kocka.end_fill()
    dge_kocka.goto(dge_kocka_x + 35, dge_kocka_y + 22)

# dge-gumb za metanje kocke


    dge_button = turtle.Turtle()
    dge_button.hideturtle()
    dge_button.speed(0)
    dge_button.pencolor("black")
    dge_button.color("black")

    dge_button_x = 180
    dge_button_y = -200
    dge_button_length = 100
    dge_button_width = 100


    def dge_button_press():
        dge_button.penup()
        dge_button.fillcolor("white")
        dge_button.begin_fill()
        dge_button.goto(dge_button_x, dge_button_y)
        dge_button.goto(dge_button_x + dge_button_length, dge_button_y)
        dge_button.goto(dge_button_x + dge_button_length, dge_button_y + dge_button_width)
        dge_button.goto(dge_button_x, dge_button_y + dge_button_width)
        dge_button.goto(dge_button_x, dge_button_y)
        dge_button.end_fill()
        dge_button.goto(dge_button_x + 17, dge_button_y + 32)
        dge_button.write("ROLL", font=("Arial", 20, "normal"))
    dge_button_press()
    
# begin
    def begin_button_on():
        begin_button = turtle.Turtle()
        begin_button.hideturtle()
        begin_button.speed(0)
        begin_button.pencolor("black")
        begin_button.color("black")

        begin_button_x = -100
        begin_button_y = -200
        begin_button_length = 200
        begin_button_width = 100

    
        def begin_button_press():
            begin_button.penup()
            begin_button.fillcolor("white")
            begin_button.begin_fill()
            begin_button.goto(begin_button_x, begin_button_y)
            begin_button.goto(begin_button_x + begin_button_length, begin_button_y)
            begin_button.goto(begin_button_x + begin_button_length, begin_button_y + begin_button_width)
            begin_button.goto(begin_button_x, begin_button_y + begin_button_width)
            begin_button.goto(begin_button_x, begin_button_y)
            begin_button.end_fill()
            begin_button.goto(begin_button_x + 40, begin_button_y + 28)
            begin_button.write("BEGIN", font=("Arial", 30, "normal"))
        begin_button_press()

        def begin_click(x,y):
            global mode
            if begin_button_x <= x <= begin_button_x + begin_button_length:
                if begin_button_y <= y <= begin_button_y + begin_button_width:
                    if mode == "begin":
                        begin_button.clear()
                        mode = "svet"
                        atk_kocka.clear()
                        def_kocka.clear()
                        dge_kocka.clear()
                        spd_kocka.clear()
                        roll_stat.clear()
                        atk.clear()
                        defense.clear()
                        spd.clear()
                        dge.clear()
                        atk_kocka_value.clear()
                        def_kocka_value.clear()
                        spd_kocka_value.clear()
                        dge_kocka_value.clear()
                        svet()
                        hisa_funkcija()
                        monster_funkcija()
                        naredi_igralca()
        wn.onclick(begin_click)

# svet

def svet():
    wn.bgcolor("#c9c9c9")

#hisa
def hisa_funkcija():
    global hisa
    hisa = turtle.Turtle()
    hisa.speed(0)
    hisa.shape('slike\hisa.gif')
    hisa.penup()
    hisa.goto(250, 150)
def hisa_premik():
    if mode == "svet":
        hisa.setx(250)
        hisa.sety(150)
    if mode == "svet_desno":
        hisa.setx(1000)
        hisa.sety(1000)

#monster
def monster_funkcija():
    global monster
    monster = turtle.Turtle()
    monster.speed(0)
    monster.shape('slike\gal3.gif')
    monster.penup()
    monster.goto(1000, 1000)

def monster_premik():
    if mode == "svet_desno":
        monster.setx(250)
        monster.sety(0)
    if mode == "svet":
        monster.setx(1000)
        monster.sety(1000)
    if mode == "fight_screen_monster":
        monster.setx(1000)
        monster.sety(1000)
# svet desno
def svet_desno():
    wn.bgcolor("green")

    monster_premik()

# fight screen monster

def fight_screen_monster():
    wn.bgcolor("#c9c9c9")
    monster_premik()
    igralec_premik()


# premikanje igralca

def igralec_premik():
    if mode == "fight_screen_monster":
        igralec.setx(igralec.xcor() + 300)
        igralec.sety(igralec.ycor() + 300)
    if mode == "svet_desno":
        igralec.setx(igralec.xcor() - 300)
        igralec.sety(igralec.ycor() - 300)




# Igralec #naredi_igralca()
def naredi_igralca():
    global igralec
    igralec = turtle.Turtle()
    igralec.speed(0)
    igralec.shape('slike\zojo.gif')
    igralec.penup()
    igralec.goto(0,-250)

# hoja igralca

    def igralec_up():
        global mode
        if mode == "svet":
            if not (igralec.ycor() > 50 and igralec.xcor() > 110):
                y = igralec.ycor()
                y += 5
                igralec.sety(y)
                igralec.shape('slike\zojoback.gif')
        if mode == "svet_desno":
            y = igralec.ycor()
            y += 5
            igralec.sety(y)
            igralec.shape('slike\zojoback.gif')


    def igralec_down():
        global mode
        if mode == "svet":
            if not( igralec.ycor() > 60 and igralec.xcor() > 110):
                y = igralec.ycor()
                y -= 5
                igralec.sety(y)
                igralec.shape('slike\zojo.gif')
        if mode == "svet_desno":
            y = igralec.ycor()
            y -= 5
            igralec.sety(y)
            igralec.shape('slike\zojo.gif')
            

    def igralec_right():
        global mode
        if mode == "svet":
            if not (igralec.ycor() > 60 and igralec.xcor() > 105):
                x = igralec.xcor()
                x += 5
                igralec.setx(x)
                igralec.shape('slike\Zojoright.gif')
            if igralec.xcor() > 390:
                mode = "svet_desno"
                svet_desno()
                hisa_premik()
                monster_premik()
                igralec.goto(-390,igralec.ycor())
        if mode == "svet_desno":
            x = igralec.xcor()
            x += 5
            igralec.setx(x)
            igralec.shape('slike\Zojoright.gif')
            if (igralec.ycor() > monster.ycor() - 20 and igralec.xcor() > monster.xcor() - 65 and igralec.ycor() < monster.ycor() + 70):
                mode = "fight_screen_monster"
                fight_screen_monster()

        
    def igralec_left():
        global mode
        if mode == "svet":
            if  not (igralec.ycor() > 60 and igralec.xcor() > 110):
                x = igralec.xcor()
                x -= 5
                igralec.setx(x)
                igralec.shape('slike\leftZojo.gif')
        if mode == "svet_desno":
            x = igralec.xcor()
            x -= 5
            igralec.setx(x)
            igralec.shape('slike\leftZojo.gif')
            if igralec.xcor() < -390:
                mode = "svet"
                svet()
                hisa_premik()
                monster_premik()
                igralec.goto(390,igralec.ycor())
    
        


# Tipkovnica
    wn.listen()
    wn.onkeypress(igralec_up, "w")
    wn.onkeypress(igralec_down, "s")
    wn.onkeypress(igralec_right, "d")
    wn.onkeypress(igralec_left, "a")

    

                
# loop igre 
while True:
    wn.update()
# vertenje atk kocke

    if mode == "delitev_moci" and atk_button_pressed == False:
        atk_kocka_value = turtle.Turtle()
        atk_kocka_value.hideturtle()
        atk_kocka_value.speed(0)
        atk_kocka_value.pencolor("black")
        atk_kocka_value.color("black")
        atk_kocka_value.penup()
        atk_kocka_value.goto(-245, -28)
        atk_value = int(random.uniform(1,10))
        atk_kocka_value.write( "{}".format(atk_value), font=("Arial", 40, "normal"))
        time.sleep(0.1)
        atk_kocka_value.clear()
        
    if mode == "def_kocka" and atk_button_pressed == True:
        atk_kocka_value.write( "{}".format(atk_value), font=("Arial", 40, "normal"))
        atk_button_pressed == False
        if atk_value < 4 and atk_spremenljivka == False:
            min += (5 - atk_value)
            atk_spremenljivka = True
        
# vrtenje def kocke      

    if mode == "def_kocka" and def_button_pressed == False:
        def_kocka_value = turtle.Turtle()
        def_kocka_value.hideturtle()
        def_kocka_value.speed(0)
        def_kocka_value.pencolor("black")
        def_kocka_value.color("black")
        def_kocka_value.penup()
        def_kocka_value.goto(-90, -28)
        def_value = int(random.uniform(min,10))
        def_kocka_value.write( "{}".format(def_value), font=("Arial", 40, "normal"))
        time.sleep(0.1)
        def_kocka_value.clear()
        
    if mode == "spd_kocka" and def_button_pressed == True:
        def_kocka_value.write( "{}".format(def_value), font=("Arial", 40, "normal"))
        def_button_pressed == False
        if def_value < 4 and def_spremenljivka == False:
            min += (5 - def_value)
            def_spremenljivka = True
# vrtenje spd kocke

    if mode == "spd_kocka" and spd_button_pressed == False:
        spd_kocka_value = turtle.Turtle()
        spd_kocka_value.hideturtle()
        spd_kocka_value.speed(0)
        spd_kocka_value.pencolor("black")
        spd_kocka_value.color("black")
        spd_kocka_value.penup()
        spd_kocka_value.goto(60, -28)
        spd_value = int(random.uniform(min,10))
        spd_kocka_value.write( "{}".format(spd_value), font=("Arial", 40, "normal"))
        time.sleep(0.1)
        spd_kocka_value.clear()
        
    if mode == "dge_kocka" and spd_button_pressed == True:
        spd_kocka_value.write( "{}".format(spd_value), font=("Arial", 40, "normal"))
        spd_button_pressed == False
        if spd_value < 4 and spd_spremenljivka == False:
            min += (5 - spd_value)
            spd_spremenljivka = True
#vrtenje dge kocke
    if mode == "dge_kocka" and dge_button_pressed == False:
        dge_kocka_value = turtle.Turtle()
        dge_kocka_value.hideturtle()
        dge_kocka_value.speed(0)
        dge_kocka_value.pencolor("black")
        dge_kocka_value.color("black")
        dge_kocka_value.penup()
        dge_kocka_value.goto(215, -28)
        dge_value = int(random.uniform(min,10))
        dge_kocka_value.write( "{}".format(dge_value), font=("Arial", 40, "normal"))
        time.sleep(0.1)
        dge_kocka_value.clear()
        
    if mode == "begin" and dge_button_pressed == True:
        dge_kocka_value.write( "{}".format(dge_value), font=("Arial", 40, "normal"))
        dge_button_pressed = False

    

    

    
        
