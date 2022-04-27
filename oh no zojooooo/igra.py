
from asyncio.mixins import _global_lock
from glob import glob
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
wn.addshape('slike\inventory.gif')
wn.addshape('slike\woodensword.gif')
wn.addshape('slike\heal_potion.gif')
wn.addshape('slike\stats.gif')
wn.addshape('slike\srcek.gif')
wn.addshape('slike\WEAPONS.gif')
wn.addshape('slike\ITEMS.gif')
wn.addshape('slike\monster_interface.gif')
wn.addshape('slike\svet1.gif')
wn.addshape('slike\prozorno_ozadje.gif')

#Spremenljivke

mode = "zacetek"
curent_mode = ""
inventory_on = False

atk_button_pressed = False
def_button_pressed = False
spd_button_pressed = False
dge_button_pressed = False

min = 1
atk_spremenljivka = False
def_spremenljivka = False
spd_spremenljivka = False




# Zacetna stran

#gal narise title
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("OH NO, Zojoooo!", align="center", font=("gameovercre", 35, "normal"))

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
    start.write("START", font=("gameovercre", 30, "normal"))
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
    roll_stat.write("Roll for stats", align="center", font=("gameovercre", 35, "normal"))

    atk = turtle.Turtle()
    atk.speed(0)
    atk.color("white")
    atk.penup()
    atk.hideturtle()
    atk.goto(-230, 100)
    atk.write("ATK", align="center", font=("gameovercre", 30, "normal"))

    defense = turtle.Turtle()
    defense.speed(0)
    defense.color("white")
    defense.penup()
    defense.hideturtle()
    defense.goto(-75, 100)
    defense.write("DEF", align="center", font=("gameovercre", 30, "normal"))

    spd = turtle.Turtle()
    spd.speed(0)
    spd.color("white")
    spd.penup()
    spd.hideturtle()
    spd.goto(75, 100)
    spd.write("SPD", align="center", font=("gameovercre", 30, "normal"))

    dge = turtle.Turtle()
    dge.speed(0)
    dge.color("white")
    dge.penup()
    dge.hideturtle()
    dge.goto(230, 100)
    dge.write("DGE", align="center", font=("gameovercre", 30, "normal"))

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
        atk_button.write("ROLL", font=("gameovercre", 20, "normal"))
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
        def_button.write("ROLL", font=("gameovercre", 20, "normal"))
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
        spd_button.write("ROLL", font=("gameovercre", 20, "normal"))
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
        dge_button.write("ROLL", font=("gameovercre", 20, "normal"))
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
            begin_button.write("BEGIN", font=("gameovercre", 30, "normal"))
        begin_button_press()

        def begin_click(x,y):
            global inventory_on
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
                        monster_funkcija()
                        naredi_igralca()
                        make_inventory()
                        inventory_on = True
                        make_wooden_sword()
                        make_heal_potion()
                        user_interface_on()
                        make_monster_interface()
        wn.onclick(begin_click)


# igralceva statistika


def user_interface_on():
    global user_interface
    user_interface = turtle.Turtle()
    user_interface.speed(0)
    user_interface.shape('slike\stats.gif')
    user_interface.penup()
    user_interface.goto(-245,258)


    ui_atk = turtle.Turtle()
    ui_atk.hideturtle()
    ui_atk.speed(0)
    ui_atk.pencolor("black")
    ui_atk.color("#FEDA41")
    ui_atk.penup()
    ui_atk.goto(-382, 256)
    ui_atk.write( "{}".format(atk_value), font=("gameovercre", 16, "normal"))

    ui_def = turtle.Turtle()
    ui_def.hideturtle()
    ui_def.speed(0)
    ui_def.pencolor("black")
    ui_def.color("#FEDA41")
    ui_def.penup()
    ui_def.goto(-330, 256)
    ui_def.write( "{}".format(def_value), font=("gameovercre", 16, "normal"))

    ui_spd = turtle.Turtle()
    ui_spd.hideturtle()
    ui_spd.speed(0)
    ui_spd.pencolor("black")
    ui_spd.color("#FEDA41")
    ui_spd.penup()
    ui_spd.goto(-282, 256)
    ui_spd.write( "{}".format(spd_value), font=("gameovercre", 16, "normal"))

    ui_dge = turtle.Turtle()
    ui_dge.hideturtle()
    ui_dge.speed(0)
    ui_dge.pencolor("black")
    ui_dge.color("#FEDA41")
    ui_dge.penup()
    ui_dge.goto(-232, 256)
    ui_dge.write( "{}".format(dge_value), font=("gameovercre", 16, "normal"))

    global ui_srcek1
    ui_srcek1 = turtle.Turtle()
    ui_srcek1.speed(0)
    ui_srcek1.shape('slike\srcek.gif')
    ui_srcek1.penup()
    ui_srcek1.goto(-375, 240)

    global ui_srcek2
    ui_srcek2 = turtle.Turtle()
    ui_srcek2.speed(0)
    ui_srcek2.shape('slike\srcek.gif')
    ui_srcek2.penup()
    ui_srcek2.goto(-345, 240)

    global ui_srcek3
    ui_srcek3 = turtle.Turtle()
    ui_srcek3.speed(0)
    ui_srcek3.shape('slike\srcek.gif')
    ui_srcek3.penup()
    ui_srcek3.goto(-315, 240)


# Inventory

def make_inventory():
    global inventory
    inventory = turtle.Turtle()
    inventory.speed(0)
    inventory.shape('slike\inventory.gif')
    inventory.penup()
    inventory.goto(1000, 1000)

def open_inventory():
    global mode
    global curent_mode
    global inventory
    if inventory_on == True:
        if mode != "weapons" and mode != "items":
            inventory.setx(0)
            inventory.sety(0)
            curent_mode = mode
            mode = "weapons"
            move_wooden_sword()
            inventory_button_on()

        elif mode == "weapons" or mode == "items":
            inventory.setx(1050)
            inventory.sety(1050)
            mode = curent_mode
            move_wooden_sword()
            delete_inventory_buttons()
            move_heal_potion()
            
            
    
# orozje

def make_wooden_sword():
    global wooden_sword
    wooden_sword = turtle.Turtle()
    wooden_sword.speed(0)
    wooden_sword.shape('slike\woodensword.gif')
    wooden_sword.penup()
    wooden_sword.goto(1000,1000)

def move_wooden_sword():
    if inventory_on == True:
        if mode == "weapons":
            wooden_sword.setx(-225) #tuki not bo spremenljivka, ki se bo menjavala glede na kok itemov bo v inventoriju
            wooden_sword.sety(-75)
        elif mode != "weapons":
            wooden_sword.setx(1000)
            wooden_sword.sety(1000)


# items
        
def make_heal_potion():
    global heal_potion
    heal_potion = turtle.Turtle()
    heal_potion.speed(0)
    heal_potion.shape('slike\heal_potion.gif')
    heal_potion.penup()
    heal_potion.goto(1000,1000)

def move_heal_potion():
    if inventory_on == True:
        if mode == "items":
            heal_potion.setx(-225)
            heal_potion.sety(-75)
        elif mode != "items":
            heal_potion.setx(1000)
            heal_potion.sety(1000)


# gumb za inventory iteme

def inventory_button_on():
    global intventory_items_button
    global intventory_items_button_x
    global intventory_items_button_y
    global intventory_items_button_length
    global intventory_items_button_width
    intventory_items_button = turtle.Turtle()
    intventory_items_button.hideturtle()
    intventory_items_button.speed(0)
    intventory_items_button.pencolor("black")
    intventory_items_button.color("black")

    intventory_items_button_x = 20
    intventory_items_button_y = 19
    intventory_items_button_length = 215
    intventory_items_button_width = 56

    
    def intventory_items_button_press():
        intventory_items_button.penup()
        intventory_items_button.fillcolor("#FFFB83")
        intventory_items_button.begin_fill()
        intventory_items_button.goto(intventory_items_button_x, intventory_items_button_y)
        intventory_items_button.goto(intventory_items_button_x + intventory_items_button_length, intventory_items_button_y)
        intventory_items_button.goto(intventory_items_button_x + intventory_items_button_length, intventory_items_button_y + intventory_items_button_width)
        intventory_items_button.goto(intventory_items_button_x, intventory_items_button_y + intventory_items_button_width)
        intventory_items_button.goto(intventory_items_button_x, intventory_items_button_y)
        intventory_items_button.end_fill()
        intventory_items_button.goto(intventory_items_button_x + 55, intventory_items_button_y + 3)
        intventory_items_button.write("ITEMS", font=("gameovercre", 30, "normal"))
    intventory_items_button_press()

# gumb za inventory orozja

    global intventory_weapons_button
    global intventory_weapons_button_x
    global intventory_weapons_button_y
    global intventory_weapons_button_length
    global intventory_weapons_button_width
    intventory_weapons_button = turtle.Turtle()
    intventory_weapons_button.hideturtle()
    intventory_weapons_button.speed(0)
    intventory_weapons_button.pencolor("black")
    intventory_weapons_button.color("black")

    intventory_weapons_button_x = -240
    intventory_weapons_button_y = 19
    intventory_weapons_button_length = 215
    intventory_weapons_button_width = 56

    
    def intventory_weapons_button_press():
        intventory_weapons_button.penup()
        intventory_weapons_button.fillcolor("#FFFB83")
        intventory_weapons_button.begin_fill()
        intventory_weapons_button.goto(intventory_weapons_button_x, intventory_weapons_button_y)
        intventory_weapons_button.goto(intventory_weapons_button_x + intventory_weapons_button_length, intventory_weapons_button_y)
        intventory_weapons_button.goto(intventory_weapons_button_x + intventory_weapons_button_length, intventory_weapons_button_y + intventory_weapons_button_width)
        intventory_weapons_button.goto(intventory_weapons_button_x, intventory_weapons_button_y + intventory_weapons_button_width)
        intventory_weapons_button.goto(intventory_weapons_button_x, intventory_weapons_button_y)
        intventory_weapons_button.end_fill()
        intventory_weapons_button.goto(intventory_weapons_button_x + 20, intventory_weapons_button_y + 3)
        intventory_weapons_button.write("WEAPONS", font=("gameovercre", 30, "normal"))
    intventory_weapons_button_press()




    def intventory_items_click(x,y):
        global mode
        global inventory_on
        if mode == "weapons":
            if intventory_items_button_x <= x <= intventory_items_button_x + intventory_items_button_length:
                if intventory_items_button_y <= y <= intventory_items_button_y + intventory_items_button_width:
                    mode = "items"
                    move_heal_potion()
                    move_wooden_sword()
        if mode == "items":
            if intventory_weapons_button_x <= x <= intventory_weapons_button_x + intventory_weapons_button_length:
                if intventory_weapons_button_y <= y <= intventory_weapons_button_y + intventory_items_button_width:
                    mode = "weapons"
                    move_wooden_sword()
                    move_heal_potion()
                    
        
                
    wn.onclick(intventory_items_click)

def delete_inventory_buttons():
    if mode != "inventory":
        intventory_items_button.clear()
        intventory_weapons_button.clear()
        



# svet

def svet():
    wn.bgpic("slike\svet1.gif")




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

# monster interface
def make_monster_interface():
    global monster_interface
    monster_interface = turtle.Turtle()
    monster_interface.speed(0)
    monster_interface.shape('slike\monster_interface.gif')
    monster_interface.penup()
    monster_interface.goto(1000, 1000)
def move_monster_interface():
    if mode == "svet_desno":
        monster_interface.setx(1000)
        monster_interface.sety(1000)
        monster.setx(1000)
        monster.sety(1000)
    if mode == "start_fight":
        monster_interface.setx(242)
        monster_interface.sety(270)
        monster.setx(250)
        monster.sety(0)
    


# svet desno
def svet_desno():
    wn.bgpic('slike\prozorno_ozadje.gif')
    wn.bgcolor("#57c219")

    monster_premik()

# monster fight screen

def fight_screen_monster():
    global mode 
    
    wn.bgcolor("#c9c9c9")
    monster_premik()
    igralec_premik()
    fight_button_on()
    mode = "start_fight"


# premik gumbov

def delete_button():
    if mode == "svet_desno":
        fight_button.clear()
        dont_fight_button.clear()
        items_button.clear()
        
    

# fight gumb

    
def fight_button_on():
    global fight_button
    global fight_button_x
    global fight_button_y
    global fight_button_length
    global fight_button_width
    fight_button = turtle.Turtle()
    fight_button.hideturtle()
    fight_button.speed(0)
    fight_button.pencolor("black")
    fight_button.color("black")

    fight_button_x = -220
    fight_button_y = -200
    fight_button_length = 130
    fight_button_width = 80

    
    def fight_button_press():
        fight_button.penup()
        fight_button.fillcolor("white")
        fight_button.begin_fill()
        fight_button.goto(fight_button_x, fight_button_y)
        fight_button.goto(fight_button_x + fight_button_length, fight_button_y)
        fight_button.goto(fight_button_x + fight_button_length, fight_button_y + fight_button_width)
        fight_button.goto(fight_button_x, fight_button_y + fight_button_width)
        fight_button.goto(fight_button_x, fight_button_y)
        fight_button.end_fill()
        fight_button.goto(fight_button_x + 30, fight_button_y + 23)
        fight_button.write("FIGHT", font=("gameovercre", 20, "normal"))
    fight_button_press()




# items gumb

    global items_button
    global items_button_x
    global items_button_y
    global items_button_length
    global items_button_width
    items_button = turtle.Turtle()
    items_button.hideturtle()
    items_button.speed(0)
    items_button.pencolor("black")
    items_button.color("black")

    items_button_x = -65
    items_button_y = -200
    items_button_length = 130
    items_button_width = 80

    
    def items_button_press():
        items_button.penup()
        items_button.fillcolor("white")
        items_button.begin_fill()
        items_button.goto(items_button_x, items_button_y)
        items_button.goto(items_button_x + items_button_length, items_button_y)
        items_button.goto(items_button_x + items_button_length, items_button_y + items_button_width)
        items_button.goto(items_button_x, items_button_y + items_button_width)
        items_button.goto(items_button_x, items_button_y)
        items_button.end_fill()
        items_button.goto(items_button_x + 27, items_button_y + 23)
        items_button.write("ITEMS", font=("gameovercre", 20, "normal"))
    items_button_press()

# dont fight gumb
    global dont_fight_button
    global dont_fight_button_x
    global dont_fight_button_y
    global dont_fight_button_length
    global dont_fight_button_width
    dont_fight_button = turtle.Turtle()
    dont_fight_button.hideturtle()
    dont_fight_button.speed(0)
    dont_fight_button.pencolor("black")
    dont_fight_button.color("black")

    dont_fight_button_x = 90
    dont_fight_button_y = -200
    dont_fight_button_length = 130
    dont_fight_button_width = 80

    
    def dont_fight_button_press():
        dont_fight_button.penup()
        dont_fight_button.fillcolor("white")
        dont_fight_button.begin_fill()
        dont_fight_button.goto(dont_fight_button_x, dont_fight_button_y)
        dont_fight_button.goto(dont_fight_button_x + dont_fight_button_length, dont_fight_button_y)
        dont_fight_button.goto(dont_fight_button_x + dont_fight_button_length, dont_fight_button_y + dont_fight_button_width)
        dont_fight_button.goto(dont_fight_button_x, dont_fight_button_y + dont_fight_button_width)
        dont_fight_button.goto(dont_fight_button_x, dont_fight_button_y)
        dont_fight_button.end_fill()
        dont_fight_button.goto(dont_fight_button_x + 20, dont_fight_button_y + 10)
        dont_fight_button.write(" DON'T\n FIGHT", font=("gameovercre", 20, "normal"))
    dont_fight_button_press()
    

# run gumb
    if mode == "in_fight":
        global run_button
        global run_button_x
        global run_button_y
        global run_button_length
        global run_button_width
        run_button = turtle.Turtle()
        run_button.hideturtle()
        run_button.speed(0)
        run_button.pencolor("black")
        run_button.color("black")

        run_button_x = 90
        run_button_y = -200
        run_button_length = 130
        run_button_width = 80

    
        def run_button_press():
            run_button.penup()
            run_button.fillcolor("white")
            run_button.begin_fill()
            run_button.goto(run_button_x, run_button_y)
            run_button.goto(run_button_x + run_button_length, run_button_y)
            run_button.goto(run_button_x + run_button_length, run_button_y + run_button_width)
            run_button.goto(run_button_x, run_button_y + run_button_width)
            run_button.goto(run_button_x, run_button_y)
            run_button.end_fill()
            run_button.goto(run_button_x + 40, run_button_y + 23)
            run_button.write("RUN", font=("gameovercre", 20, "normal"))
        run_button_press()
    
# detektor pritiska  fight gumbov
    def fight_click(x,y):
        global mode
        global inventory_on
        if mode == "start_fight":
            if fight_button_x <= x <= fight_button_x + fight_button_length:
                if fight_button_y <= y <= fight_button_y + fight_button_width:
                    make_fight_weapons()
                    move_fight_weapons()
                    fight_back_button_on()
                    fight_button.clear()
                    items_button.clear()
                    dont_fight_button.clear()
                    mode = "fight_weapons"
                    
        if mode == "start_fight":
            if items_button_x <= x <= items_button_x + items_button_length:
                if items_button_y <= y <= items_button_y + items_button_width:
                    make_fight_items()
                    move_fight_items()
                    fight_back_button_on()
                    fight_button.clear()
                    items_button.clear()
                    dont_fight_button.clear()
                    mode = "fight_items"
        if mode == "in_fight":
            if run_button_x <= x <= run_button_x + run_button_length:
                if run_button_y <= y <= run_button_y + run_button_width:
                    print("hi")
        if mode == "start_fight":
            if dont_fight_button_x <= x <= dont_fight_button_x + dont_fight_button_length:
                if dont_fight_button_y <= y <= dont_fight_button_y + dont_fight_button_width:
                    mode = "svet_desno"
                    move_monster_interface()
                    svet_desno()
                    delete_button()
                    igralec_premik()
                    monster_interface.clear()
                    inventory_on = True
                
    wn.onclick(fight_click)

# weapons

def make_fight_weapons():
    global fight_weapons
    fight_weapons = turtle.Turtle()
    fight_weapons.speed(0)
    fight_weapons.shape('slike\WEAPONS.gif')
    fight_weapons.penup()
    fight_weapons.goto(0,-183)


def move_fight_weapons():
    if mode != "fight_weapons":
        fight_weapons.setx(0)
        fight_weapons.sety(-183)
    if mode == "fight_weapons":
        fight_weapons.setx(1000)
        fight_weapons.sety(1000)

def make_fight_items():
    global fight_items
    fight_items = turtle.Turtle()
    fight_items.speed(0)
    fight_items.shape('slike\ITEMS.gif')
    fight_items.penup()
    fight_items.goto(0,-183)

def move_fight_items():
    if mode != "fight_items":
        fight_items.setx(0)
        fight_items.sety(-183)
    if mode == "fight_items":
        fight_items.setx(1000)
        fight_items.sety(1000)


#back button

def fight_back_button_on():
    global fight_back_button
    global fight_back_button_x
    global fight_back_button_y
    global fight_back_button_length
    global fight_back_button_width
    fight_back_button = turtle.Turtle()
    fight_back_button.hideturtle()
    fight_back_button.speed(0)
    fight_back_button.pencolor("black")
    fight_back_button.color("black")

    fight_back_button_x = 207
    fight_back_button_y = -272
    fight_back_button_length = 130
    fight_back_button_width = 80

    
    def fight_back_button_press():
        fight_back_button.penup()
        fight_back_button.fillcolor("#FEDA41")
        fight_back_button.begin_fill()
        fight_back_button.goto(fight_back_button_x, fight_back_button_y)
        fight_back_button.goto(fight_back_button_x + fight_back_button_length, fight_back_button_y)
        fight_back_button.goto(fight_back_button_x + fight_back_button_length, fight_back_button_y + fight_back_button_width)
        fight_back_button.goto(fight_back_button_x, fight_back_button_y + fight_back_button_width)
        fight_back_button.goto(fight_back_button_x, fight_back_button_y)
        fight_back_button.end_fill()
        fight_back_button.goto(fight_back_button_x + 30, fight_back_button_y + 23)
        fight_back_button.write("BACK", font=("gameovercre", 20, "normal"))
    fight_back_button_press()

    def back_button_click(x,y):
        global mode
        if mode == "fight_weapons":
            if fight_back_button_x <= x <= fight_back_button_x + fight_back_button_length:
                if fight_back_button_y <= y <= fight_back_button_y + fight_back_button_width:
                    move_fight_weapons()
                    fight_back_button.clear()
                    mode = "start_fight"
                    fight_button_on()
        if mode == "fight_items":
            if fight_back_button_x <= x <= fight_back_button_x + fight_back_button_length:
                if fight_back_button_y <= y <= fight_back_button_y + fight_back_button_width:
                    move_fight_items()
                    fight_back_button.clear()
                    mode = "start_fight"
                    fight_button_on()
    wn.onclick(back_button_click)



# premikanje igralca

def igralec_premik():
    if mode == "fight_screen_monster":
        igralec.setx(igralec.xcor() + 300)
        igralec.sety(igralec.ycor() + 300)
    if mode == "svet_desno":
        igralec.setx(igralec.xcor() - 320)
        igralec.sety(igralec.ycor() - 300)




# Igralec #naredi_igralca()
def naredi_igralca():
    global igralec
    igralec = turtle.Turtle()
    igralec.speed(0)
    igralec.shape('slike\zojo.gif')
    igralec.penup()
    igralec.goto(0,-200)

# hoja igralca


    def igralec_up():
        global mode
        if mode == "svet":
            if not (igralec.ycor() > 50 and igralec.xcor() > 65):
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
        global inventory_on
        if mode == "svet":
            if not (igralec.ycor() > 60 and igralec.xcor() > 50):
                x = igralec.xcor()
                x += 5
                igralec.setx(x)
                igralec.shape('slike\Zojoright.gif')
            if igralec.xcor() > 390:
                mode = "svet_desno"
                svet_desno()
                monster_premik()
                igralec.goto(-390,igralec.ycor())
        if mode == "svet_desno":
            x = igralec.xcor()
            x += 5
            igralec.setx(x)
            igralec.shape('slike\Zojoright.gif')
            if (igralec.ycor() > monster.ycor() - 20 and igralec.xcor() > monster.xcor() - 65 and igralec.ycor() < monster.ycor() + 70):
                mode = "fight_screen_monster"
                time.sleep(0.1)
                fight_screen_monster()
                move_monster_interface()
                inventory_on = False

        
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
                monster_premik()
                igralec.goto(390,igralec.ycor())

        


# Tipkovnica
    wn.listen()
    wn.onkeypress(igralec_up, "w")
    wn.onkeypress(igralec_down, "s")
    wn.onkeypress(igralec_right, "d")
    wn.onkeypress(igralec_left, "a")
    wn.onkeypress(igralec_up, "W")
    wn.onkeypress(igralec_down, "S")
    wn.onkeypress(igralec_right, "D")
    wn.onkeypress(igralec_left, "A")

    wn.onkeypress(open_inventory, "e")
    wn.onkeypress(open_inventory, "E")
    

                
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
        atk_kocka_value.write( "{}".format(atk_value), font=("gameovercre", 40, "normal"))
        time.sleep(0.1)
        atk_kocka_value.clear()
        
    if mode == "def_kocka" and atk_button_pressed == True:
        atk_kocka_value.write( "{}".format(atk_value), font=("gameovercre", 40, "normal"))
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
        def_kocka_value.write( "{}".format(def_value), font=("gameovercre", 40, "normal"))
        time.sleep(0.1)
        def_kocka_value.clear()
        
    if mode == "spd_kocka" and def_button_pressed == True:
        def_kocka_value.write( "{}".format(def_value), font=("gameovercre", 40, "normal"))
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
        spd_kocka_value.write( "{}".format(spd_value), font=("gameovercre", 40, "normal"))
        time.sleep(0.1)
        spd_kocka_value.clear()
        
    if mode == "dge_kocka" and spd_button_pressed == True:
        spd_kocka_value.write( "{}".format(spd_value), font=("gameovercre", 40, "normal"))
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
        dge_kocka_value.write( "{}".format(dge_value), font=("gameovercre", 40, "normal"))
        time.sleep(0.1)
        dge_kocka_value.clear()
        
    if mode == "begin" and dge_button_pressed == True:
        dge_kocka_value.write( "{}".format(dge_value), font=("gameovercre", 40, "normal"))
        dge_button_pressed = False

    

    

    
        
