
from tkinter import Y
import turtle
import random
import time
from Model import Game
from Model import Master
import os.path

wn = turtle.Screen()
wn.title("OH NO, Zojoooo!")
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
wn.addshape('slike\golem.gif')
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
wn.addshape('slike\menu.gif')
wn.addshape('slike\svet2.gif')
wn.addshape('slike\zacetna_hisa.gif')
wn.addshape('slike\chest.gif')
#Spremenljivke

mode = "zacetek"
curent_mode = ""
inventory_on = False
menu_True = False

atk_button_pressed = False
def_button_pressed = False
spd_button_pressed = False
dge_button_pressed = False

min = 1
atk_spremenljivka = False
def_spremenljivka = False
spd_spremenljivka = False

game = Game()
master = Master()

new_load1 = "NEW GAME"
new_load2 = "NEW GAME"
new_load3 = "NEW GAME"


hp_value = 100

wooden_sword_value = False
# Zacetna stran


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
    global new_load1
    global new_load2
    global new_load3
    if start_x <= x <= start_x + start_length:
        if start_y <= y <= start_y + start_width:
            if mode == "zacetek":
                file_exists = os.path.exists("mastergame.json")
                if not file_exists:
                    master.save_game("mastergame.json")
                pen.clear()
                start.clear()
                mode = "load_data"
                master.load_game("mastergame.json")
                if master.game1 == 1:
                    new_load1 = "LOAD GAME 1"
                if master.game2 == 1:
                    new_load2 = "LOAD GAME 2"
                if master.game3 == 1:
                    new_load3 = "LOAD GAME 3"
                load_data_room()
                   
wn.onclick(start_click)

# load data

def load_data_room():
    global new_load1
    new_save_1 = turtle.Turtle()
    new_save_1.hideturtle()
    new_save_1.speed(0)
    new_save_1.pencolor("black")
    new_save_1.color("black")

    new_save_1_x = -150
    new_save_1_y = 100
    new_save_1_length = 300
    new_save_1_width = 100


    def new_save_1_press():
        new_save_1.penup()
        new_save_1.fillcolor("white")
        new_save_1.begin_fill()
        new_save_1.goto(new_save_1_x, new_save_1_y)
        new_save_1.goto(new_save_1_x + new_save_1_length, new_save_1_y)
        new_save_1.goto(new_save_1_x + new_save_1_length, new_save_1_y + new_save_1_width)
        new_save_1.goto(new_save_1_x, new_save_1_y + new_save_1_width)
        new_save_1.goto(new_save_1_x, new_save_1_y)
        new_save_1.end_fill()
        new_save_1.goto(new_save_1_x + 25, new_save_1_y + 25)
        new_save_1.write(new_load1, font=("gameovercre", 30, "normal"))
    new_save_1_press()


    new_save_2 = turtle.Turtle()
    new_save_2.hideturtle()
    new_save_2.speed(0)
    new_save_2.pencolor("black")
    new_save_2.color("black")

    new_save_2_x = -150
    new_save_2_y = -50
    new_save_2_length = 300
    new_save_2_width = 100


    def new_save_2_press():
        new_save_2.penup()
        new_save_2.fillcolor("white")
        new_save_2.begin_fill()
        new_save_2.goto(new_save_2_x, new_save_2_y)
        new_save_2.goto(new_save_2_x + new_save_2_length, new_save_2_y)
        new_save_2.goto(new_save_2_x + new_save_2_length, new_save_2_y + new_save_2_width)
        new_save_2.goto(new_save_2_x, new_save_2_y + new_save_2_width)
        new_save_2.goto(new_save_2_x, new_save_2_y)
        new_save_2.end_fill()
        new_save_2.goto(new_save_2_x + 25, new_save_2_y + 25)
        new_save_2.write(new_load2, font=("gameovercre", 30, "normal"))
    new_save_2_press()



    new_save_3 = turtle.Turtle()
    new_save_3.hideturtle()
    new_save_3.speed(0)
    new_save_3.pencolor("black")
    new_save_3.color("black")

    new_save_3_x = -150
    new_save_3_y = -200
    new_save_3_length = 300
    new_save_3_width = 100


    def new_save_3_press():
        new_save_3.penup()
        new_save_3.fillcolor("white")
        new_save_3.begin_fill()
        new_save_3.goto(new_save_3_x, new_save_3_y)
        new_save_3.goto(new_save_3_x + new_save_3_length, new_save_3_y)
        new_save_3.goto(new_save_3_x + new_save_3_length, new_save_3_y + new_save_3_width)
        new_save_3.goto(new_save_3_x, new_save_3_y + new_save_3_width)
        new_save_3.goto(new_save_3_x, new_save_3_y)
        new_save_3.end_fill()
        new_save_3.goto(new_save_3_x + 25, new_save_3_y + 25)
        new_save_3.write(new_load3, font=("gameovercre", 30, "normal"))
    new_save_3_press()



    def load_click(x,y):
        global mode
        if new_save_1_x <= x <= new_save_1_x + new_save_1_length:
            if new_save_1_y <= y <= new_save_1_y + new_save_1_width:
                if mode == "load_data":
                    game.set_game_n(1)
                    master.set_game_1(1)
                    new_save_1.clear()
                    new_save_2.clear()
                    new_save_3.clear()
                    file_exists1 = os.path.exists("game1.json")
                    if not file_exists1:
                        mode = "delitev_moci"
                        soba_delitev_moci()
                    else:
                        game.load_game(f"game{game.game_n}.json")
                        load_data()
                
        if new_save_2_x <= x <= new_save_2_x + new_save_2_length:
            if new_save_2_y <= y <= new_save_2_y + new_save_2_width:
                if mode == "load_data":
                    game.set_game_n(2)
                    master.set_game_2(1)
                    new_save_1.clear()
                    new_save_2.clear()
                    new_save_3.clear()
                    file_exists2 = os.path.exists("game2.json")
                    if not file_exists2:
                        mode = "delitev_moci"
                        soba_delitev_moci()
                    else:
                        game.load_game(f"game{game.game_n}.json")
                        load_data()
                    
                    
        if new_save_3_x <= x <= new_save_3_x + new_save_3_length:
            if new_save_3_y <= y <= new_save_3_y + new_save_3_width:
                if mode == "load_data":
                    game.set_game_n(3)
                    master.set_game_3(1)
                    new_save_1.clear()
                    new_save_2.clear()
                    new_save_3.clear()
                    file_exists3 = os.path.exists("game3.json")
                    if not file_exists3:
                        mode = "delitev_moci"
                        soba_delitev_moci()
                    else:
                        game.load_game(f"game{game.game_n}.json")
                        load_data()
                                 
    wn.onclick(load_click)

def load_data():
    global mode
    global inventory_on
    global atk_value
    global def_value
    global spd_value
    global dge_value

    mode = game.mode
    atk_value = game.atk
    def_value = game.defense
    spd_value = game.spd
    dge_value = game.dge
    y = game.y
    x = game.x
    
    make_fight_weapons()
    make_fight_items()
    monster_funkcija()
    make_chest()
    naredi_igralca()
    make_inventory()
    inventory_on = True
    make_wooden_sword()
    make_heal_potion()
    user_interface_on()
    make_menu()
    
    if mode == "svet":
        svet()
    if mode == "svet_desno":
        svet_desno()
    if mode == "zacetna_hisa":
        zacetna_hisa()
    if mode == "svet_levo":
        svet_levo()
    igralec.setx(x)
    igralec.sety(y)
    




# Soba za delitev moci
def soba_delitev_moci():
    wn.bgcolor("black")
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
                        make_fight_weapons()
                        make_fight_items()
                        make_chest()
                        svet()
                        monster_funkcija()
                        naredi_igralca()
                        make_inventory()
                        inventory_on = True
                        make_wooden_sword()
                        make_heal_potion()
                        user_interface_on()
                        make_menu()
        wn.onclick(begin_click)


# igralceva statistika


def user_interface_on():
    global user_interface
    global ui_hp

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


    ui_hp = turtle.Turtle()
    ui_hp.hideturtle()
    ui_hp.speed(0)
    ui_hp.pencolor("black")
    ui_hp.color("#FEDA41")
    ui_hp.penup()
    ui_hp.goto(-149, 273)
    ui_hp.write( "{}".format(hp_value), font=("gameovercre", 17, "normal"))



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
            wooden_sword.setx(-225) 
            wooden_sword.sety(-75)
        elif mode != "weapons":
            wooden_sword.setx(1000)
            wooden_sword.sety(1000)
    elif mode == "fight_weapons":
        wooden_sword.setx(-345) 
        wooden_sword.sety(-135)
    elif mode != "fight_weapons":
        wooden_sword.setx(1005) 
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
    game.set_mode(mode)
    move_chest()

# zacetna hisa
def zacetna_hisa():
    wn.bgpic('slike\zacetna_hisa.gif')
    game.set_mode(mode)
    igralec.setx(0)
    igralec.sety(-220)
    move_chest()


# chest
def make_chest():
    global chest
    chest = turtle.Turtle()
    chest.speed(0)
    chest.shape('slike\chest.gif')
    chest.penup()
    chest.goto(1000, 1000)
    


def move_chest():
    if mode == "zacetna_hisa":
        chest.setx(0)
        chest.sety(100)
    if mode == "svet":
        chest.setx(1000)
        chest.sety(1000)
        





#monster
def monster_funkcija():
    global monster
    monster = turtle.Turtle()
    monster.speed(0)
    monster.shape('slike\golem.gif')
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
    if golem_hp_value <= 0:
        monster.setx(1000)
        monster.sety(1000)



# monster interface
def move_monster_interface():
    if mode == "svet_desno":
        monster_interface.setx(1000)
        monster_interface.sety(1000)
        golem_atk.clear()
        golem_def.clear()
        golem_spd.clear()
        golem_dge.clear()
        golem_hp.clear()

golem_atk_value = 5
golem_def_value = 5
golem_spd_value = 5
golem_dge_value = 5
golem_hp_value = 50

def make_monster_interface():
    global monster_interface
    global golem_atk
    global golem_def
    global golem_spd
    global golem_dge
    global golem_hp

    monster_interface = turtle.Turtle()
    monster_interface.speed(0)
    monster_interface.shape('slike\monster_interface.gif')
    monster_interface.penup()
    monster_interface.goto(242, 270)


    golem_atk = turtle.Turtle()
    golem_atk.hideturtle()
    golem_atk.speed(0)
    golem_atk.pencolor("black")
    golem_atk.color("#BC1212")
    golem_atk.penup()
    golem_atk.goto(212, 256)
    golem_atk.write( golem_atk_value , font=("gameovercre", 16, "normal"))

    golem_def = turtle.Turtle()
    golem_def.hideturtle()
    golem_def.speed(0)
    golem_def.pencolor("black")
    golem_def.color("#BC1212")
    golem_def.penup()
    golem_def.goto(262, 256)
    golem_def.write( golem_def_value , font=("gameovercre", 16, "normal"))

    golem_spd = turtle.Turtle()
    golem_spd.hideturtle()
    golem_spd.speed(0)
    golem_spd.pencolor("black")
    golem_spd.color("#BC1212")
    golem_spd.penup()
    golem_spd.goto(312, 256)
    golem_spd.write( golem_spd_value, font=("gameovercre", 16, "normal"))

    golem_dge = turtle.Turtle()
    golem_dge.hideturtle()
    golem_dge.speed(0)
    golem_dge.pencolor("black")
    golem_dge.color("#BC1212")
    golem_dge.penup()
    golem_dge.goto(362, 256)
    golem_dge.write( golem_dge_value , font=("gameovercre", 16, "normal"))


    golem_hp = turtle.Turtle()
    golem_hp.hideturtle()
    golem_hp.speed(0)
    golem_hp.pencolor("black")
    golem_hp.color("#BC1212")
    golem_hp.penup()
    golem_hp.goto(149, 273)
    golem_hp.write( "{}".format(golem_hp_value), font=("gameovercre", 17, "normal"))
    


# svet desno
def svet_desno():
    wn.bgpic('slike\svet2.gif')
    game.set_mode(mode)

    monster_premik()

#svet levo
def svet_levo():
    wn.bgcolor("green")
    wn.bgpic('slike\prozorno_ozadje.gif')
    game.set_mode(mode)

# monster fight screen

def fight_screen_monster():
    global mode 
    wn.bgpic('slike\prozorno_ozadje.gif')
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
                    move_fight_weapons()
                    fight_back_button_on()
                    fight_button.clear()
                    items_button.clear()
                    dont_fight_button.clear()
                    mode = "fight_weapons"
                    move_wooden_sword()
                    
        if mode == "start_fight":
            if items_button_x <= x <= items_button_x + items_button_length:
                if items_button_y <= y <= items_button_y + items_button_width:
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
                    inventory_on = True
                
    wn.onclick(fight_click)

# weapons

def make_fight_weapons():
    global fight_weapons
    fight_weapons = turtle.Turtle()
    fight_weapons.speed(0)
    fight_weapons.shape('slike\WEAPONS.gif')
    fight_weapons.penup()
    fight_weapons.goto(1000,1000)


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
    fight_items.goto(1000,-1803)

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
        global wooden_sword_value
        if mode == "fight_weapons":
            if fight_back_button_x <= x <= fight_back_button_x + fight_back_button_length:
                if fight_back_button_y <= y <= fight_back_button_y + fight_back_button_width:
                    move_fight_weapons() 
                    fight_back_button.clear()
                    mode = "start_fight"
                    fight_button_on()
                    move_wooden_sword()
            if -390 < x < -320:
                if -180 < y < -100:
                    wooden_sword_value = True
                    fight()
        if mode == "fight_items":
            if fight_back_button_x <= x <= fight_back_button_x + fight_back_button_length:
                if fight_back_button_y <= y <= fight_back_button_y + fight_back_button_width:
                    move_fight_items()
                    fight_back_button.clear()
                    mode = "start_fight"
                    fight_button_on()
    wn.onclick(back_button_click)


# rolling dice

def roll_d4(times_rolled):
    dice = 0
    while times_rolled > 0:
        dice += int(random.uniform(1,5))
        times_rolled -= 1
    return dice
        

# fight

def fight():
    global golem_attacked
    global player_attacked
    if spd_value >= golem_spd_value:
        player_attacked = True
        player_attack()
    else:
        golem_attacked = True
        golem_attack()
        
golem_attacked = False
player_attacked = False

def player_attack():
    global wooden_sword_value
    global golem_hp_value
    global golem_attacked
    if wooden_sword_value == True:
        damage =  roll_d4(2) + atk_value
        print(damage)
    if int(random.uniform(1,101)) < golem_dge_value :
        print("u missed")
    else:
        golem_hp_value = golem_hp_value -(damage - golem_def_value // 2)
        golem_hp.clear()
        golem_hp.write( "{}".format(golem_hp_value), font=("gameovercre", 17, "normal"))
    if golem_attacked == True:
        check_hp()
    else:
        golem_attack()


def golem_attack():
    global hp_value
    damage =  roll_d4(2) + golem_atk_value
    print(damage)
    if int(random.uniform(1,101)) < golem_dge_value :
        print("it missed")
    else:
        hp_value = hp_value -(damage - def_value // 2)
        ui_hp.clear()
        ui_hp.write( "{}".format(hp_value), font=("gameovercre", 17, "normal"))
    if player_attacked == True:
        check_hp()
    else:
        golem_attack()





def check_hp():
    global mode
    global inventory_on
    if hp_value <= 0:
        print("you lost")
        move_fight_weapons() 
        fight_back_button.clear()
        fight_button_on()
        mode = "svet_desno"
        move_wooden_sword()
        move_monster_interface()
        svet_desno()
        delete_button()
        igralec_premik()
        inventory_on = True
    if golem_hp_value <= 0:
        print("you win")
        move_fight_weapons() 
        fight_back_button.clear()
        fight_button_on()
        mode = "svet_desno"
        move_wooden_sword()
        move_monster_interface()
        svet_desno()
        delete_button()
        igralec_premik()
        inventory_on = True
    else:
        move_fight_weapons()
        fight_back_button.clear()
        mode = "start_fight"
        move_wooden_sword()
        fight_button_on()






# premikanje igralca

def igralec_premik():
    if mode == "fight_screen_monster":
        igralec.setx(1000)
        igralec.sety(1000)
    if mode == "svet_desno":
        igralec.setx(150)
        igralec.sety(0)




# Igralec #naredi_igralca()
def naredi_igralca():
    global igralec
    igralec = turtle.Turtle()
    igralec.speed(0)
    igralec.shape('slike\zojo.gif')
    igralec.penup()
    igralec.goto(0,-200)
    
    
# hoja igralca
    collisions = {
        "svet" : [(65, 300, 400, 50),(-400, -150, 400, -300)],
        "zacetna_hisa" : [(1000,1000,1000,1000)],
        "svet_desno" : [(1000,1000,1000,1000)],
        "svet_levo" : [(1000,1000,1000,1000)],
        'start_fight' : [(-400,300,400,-300)],
        'fight_screen_monster' : [(-400,300,400,-300)]
    }


    def can_move(mode, x, y):
        ovire = collisions[mode]
        hit = False
        for xmin , ymax , xmax, ymin in ovire:
            if  not (xmin < x < xmax and ymin < y < ymax):
                hit = True
        return hit
        
        
    objects = {
        "svet" : [(230, 50, 310, 44, "zacetna_hisa"), (390, 100, 400, -100,"svet_desno"),(-400, 100, -390, -100,"svet_levo")],
        "zacetna_hisa" : [(-50, -245, 50, -1000,"svet")],
        "svet_desno" : [(-400, 100, -390, -100,"svet"),(180, 100, 400, -50, "fight")],
        "svet_levo" : [(390, 100, 400, -100,"svet")],
        'start_fight' : [(1000,1000,1000,1000,"neki")],
        'fight_screen_monster' : [(1000,1000,1000,1000,"neki")]
    }

    def detection(mode, x, y):
        global object_detection
        ovire = objects[mode]
        hit = False
        object_detection = ""
        for xmin , ymax , xmax, ymin, object_name in ovire:
            if (xmin < x < xmax and ymin < y < ymax):
                hit = True
                object_detection = object_name
        return object_detection and hit
        

    
    def igralec_up():
        global x
        global y
        global mode
        global inventory_on
        x = igralec.xcor()
        y = igralec.ycor()
        if can_move(mode, x, y+5):
            y += 5
            x += 0
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('slike\zojoback.gif')
        if detection(mode, x, y+5):
            if object_detection == "zacetna_hisa":
                mode = "zacetna_hisa"
                time.sleep(0.1)
                zacetna_hisa()
            if object_detection == "fight":
                mode = "fight_screen_monster"
                time.sleep(0.1)
                fight_screen_monster()
                make_monster_interface()
                inventory_on = False

    
    def igralec_down():
        global x
        global y
        global mode
        global inventory_on
        x = igralec.xcor()
        y = igralec.ycor()
        if can_move(mode, x, y-5):
            y -= 5
            x += 0
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('slike\zojo.gif')
        if detection(mode, x, y-5):
            if object_detection == "svet":
                time.sleep(0.1)
                igralec.setx(270)
                igralec.sety(41)
                mode = "svet"
                svet()
            if object_detection == "fight":
                mode = "fight_screen_monster"
                time.sleep(0.1)
                fight_screen_monster()
                make_monster_interface()
                inventory_on = False


    
    def igralec_right():
        global x
        global y
        global mode
        global inventory_on
        x = igralec.xcor()
        y = igralec.ycor()
        if can_move(mode, x+5, y):
            y -= 0
            x += 5
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('slike\Zojoright.gif')
        if detection(mode, x+5, y):
            if object_detection == "svet_desno":
                mode = "svet_desno"
                svet_desno()
                monster_premik()
                igralec.goto(-390,igralec.ycor()) 
            if object_detection == "svet":
                igralec.goto(-390,igralec.ycor())
                mode = "svet"
                svet()  
        if object_detection == "fight":
            mode = "fight_screen_monster"
            time.sleep(0.1)
            fight_screen_monster()
            make_monster_interface()
            inventory_on = False
        

    
    def igralec_left():
        global x
        global y
        global mode
        x = igralec.xcor()
        y = igralec.ycor()
        if can_move(mode, x-5, y):
            y -= 0
            x -= 5
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('slike\leftZojo.gif')
        if detection(mode, x-5, y):
            if object_detection == "svet_levo":
                mode = "svet_levo"
                svet_levo()
                igralec.goto(390,igralec.ycor())
            if object_detection == "svet":
                mode = "svet"
                svet()
                igralec.goto(390,igralec.ycor())
                monster_premik()
            
        


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


    wn.onkeypress(menu_on, "Escape")

# menu

def make_menu():
    global menu
    menu = turtle.Turtle()
    menu.speed(0)
    menu.shape('slike\menu.gif')
    menu.penup()
    menu.goto(1000,1000)
def menu_on():
    global curent_mode
    global mode
    global inventory_on
    global menu_True
    if inventory_on == True:
        if menu_True == False:
            curent_mode = mode
            mode = ("menu")
            menu.setx(0)
            menu.sety(0)
            save_and_quit_on()
            menu_True = True
            ui_hp.clear()
        elif menu_True == True:
            mode = curent_mode
            menu_True = False
            menu.setx(1000)
            menu.sety(1000)
            save_and_quit.clear()
            ui_hp.write( "{}".format(hp_value), font=("gameovercre", 17, "normal"))
        



def save_and_quit_on():
    global save_and_quit
    global save_and_quit_x
    global save_and_quit_y
    global save_and_quit_length
    global save_and_quit_width
    save_and_quit = turtle.Turtle()
    save_and_quit.hideturtle()
    save_and_quit.speed(0)
    save_and_quit.pencolor("black")
    save_and_quit.color("black")

    save_and_quit_x = -150
    save_and_quit_y = -100
    save_and_quit_length = 300
    save_and_quit_width = 80

    
    def save_and_quit_press():
        save_and_quit.penup()
        save_and_quit.fillcolor("#FEDA41")
        save_and_quit.begin_fill()
        save_and_quit.goto(save_and_quit_x, save_and_quit_y)
        save_and_quit.goto(save_and_quit_x + save_and_quit_length, save_and_quit_y)
        save_and_quit.goto(save_and_quit_x + save_and_quit_length, save_and_quit_y + save_and_quit_width)
        save_and_quit.goto(save_and_quit_x, save_and_quit_y + save_and_quit_width)
        save_and_quit.goto(save_and_quit_x, save_and_quit_y)
        save_and_quit.end_fill()
        save_and_quit.goto(save_and_quit_x + 50, save_and_quit_y + 23)
        save_and_quit.write("SAVE AND QUIT", font=("gameovercre", 20, "normal"))
    save_and_quit_press()

    def menu_button_click(x,y):
        global mode
        if mode == "menu":
            if save_and_quit_x <= x <= save_and_quit_x + save_and_quit_length:
                if save_and_quit_y <= y <= save_and_quit_y + save_and_quit_width:
                    save_game()
                    quit_game()
                    
    wn.onclick(menu_button_click)

# save

def save_game():
    game.set_x(x)
    game.set_y(y)
    game.save_game(f"game{game.game_n}.json")
    master.save_game("mastergame.json")

# quit game

def quit_game():
    global running
    running = False




# loop igre 

running = True
while running:
    wn.update()

# vrtenje atk kocke

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
        game.set_atk(atk_value)
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
        game.set_def(def_value)
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
        game.set_spd(spd_value)
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
        game.set_dge(dge_value)



