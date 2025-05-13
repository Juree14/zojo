
from tkinter import Y
import turtle
import random
import time
from Model import Game
from Model import Master
from Model import Monster
from Model import Button
import os.path
import os
from Model import InventoryItem
from Model import Ozadje

wn = turtle.Screen()
wn.title("OH NO, Zojoooo!")
#wn.bgpic('oh no zojooooo\slike\svet2.gif')
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.cv._rootwindow.resizable(False, False)

# dodajanje slik
wn.addshape('oh no zojooooo\slike\zojo.gif')
wn.addshape('oh no zojooooo\slike\zojoback.gif')
wn.addshape('oh no zojooooo\slike\Zojoright.gif')
wn.addshape('oh no zojooooo\slike\leftZojo.gif')
wn.addshape('oh no zojooooo\slike\hisa.gif')
wn.addshape('oh no zojooooo\slike\golem.gif')
wn.addshape('oh no zojooooo\slike\inventory.gif')
wn.addshape('oh no zojooooo\slike\woodensword.gif')
wn.addshape('oh no zojooooo\slike\heal_potion.gif')
wn.addshape('oh no zojooooo\slike\stats.gif')
wn.addshape('oh no zojooooo\slike\srcek.gif')
wn.addshape('oh no zojooooo\slike\WEAPONS.gif')
wn.addshape('oh no zojooooo\slike\ITEMS.gif')
wn.addshape('oh no zojooooo\slike\monster_interface.gif')
wn.addshape('oh no zojooooo\slike\svet1.gif')
wn.addshape('oh no zojooooo\slike\prozorno_ozadje.gif')
wn.addshape('oh no zojooooo\slike\menu.gif')
wn.addshape('oh no zojooooo\slike\svet2.gif')
wn.addshape('oh no zojooooo\slike\zacetna_hisa.gif')
wn.addshape('oh no zojooooo\slike\chest.gif')
wn.addshape('oh no zojooooo\slike\chest_inventory.gif')
#Spremenljivke


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



mode = None

hp_value = 100
number_of_hearts = 3

wooden_sword_value = False

have_wooden_sword = True
global atk_button_ui, def_button_ui, spd_button_ui, dge_button_ui
global fight_button_ui, items_button_ui, dont_fight_button_ui, run_button_ui, fight_back_button_ui

atk_kocka_value = None
def_kocka_value = None
spd_kocka_value = None
dge_kocka_value = None

# Zacetna stran


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("OH NO, Zojoooo!", align="center", font=("gameovercre", 35, "normal"))

# Start gumb
start_button = Button(x=-100, y=-50, width=200, height=100, text="START")
start_button.draw()



def start_click(x, y):
    if start_button.is_clicked(x, y):
        if game.mode == "zacetek":
            if not os.path.exists("mastergame.json"):
                master.save_game("mastergame.json")
            pen.clear()
            start_button.clear()
            game.mode = "load_data"
            master.load_game("mastergame.json")
            if master.game1 == 1:
                game.new_load1 = "LOAD GAME 1"
            if master.game2 == 1:
                game.new_load2 = "LOAD GAME 2"
            if master.game3 == 1:
                game.new_load3 = "LOAD GAME 3"
            load_data_room()

                   
wn.onclick(start_click)

# load data
def load_data_room():
    global save_button1, save_button2, save_button3
    save_button1 = Button(
        x=-150, y=100, width=300, height=100,
        text=game.new_load1, font=("gameovercre", 30, "normal"),
        text_offset=(25, 25)
    )
    save_button1.draw()

    save_button2 = Button(
        x=-150, y=-50, width=300, height=100,
        text=game.new_load2, font=("gameovercre", 30, "normal"),
        text_offset=(25, 25)
    )
    save_button2.draw()

    save_button3 = Button(
        x=-150, y=-200, width=300, height=100,
        text=game.new_load3, font=("gameovercre", 30, "normal"),
        text_offset=(25, 25)
    )
    save_button3.draw()

    wn.onclick(load_click)



def load_click(x, y):
    if save_button1.is_clicked(x, y) and game.mode == "load_data":
        game.set_game_n(1)
        master.set_game_1(1)
        clear_save_buttons()
        process_game_slot("game1.json")
    elif save_button2.is_clicked(x, y) and game.mode == "load_data":
        game.set_game_n(2)
        master.set_game_2(1)
        clear_save_buttons()
        process_game_slot("game2.json")
    elif save_button3.is_clicked(x, y) and game.mode == "load_data":
        game.set_game_n(3)
        master.set_game_3(1)
        clear_save_buttons()
        process_game_slot("game3.json")



def clear_save_buttons():
    save_button1.clear()
    save_button2.clear()
    save_button3.clear()



def process_game_slot(filename):
    if not os.path.exists(filename):
        game.mode = "delitev_moci"
        soba_delitev_moci()
    else:
        game.load_game(filename)
        load_data()


def load_data():
    x = game.x
    y = game.y

    make_fight_weapons()
    make_fight_items()
    make_chest()
    make_chest_inventory()
    naredi_igralca()
    make_inventory()
    game.inventory_on = True
    make_wooden_sword()
    make_heal_potion()
    user_interface_on()
    make_menu()

    if game.mode == "svet":
        svet()
    elif game.mode == "svet_desno":
        svet_desno()
    elif game.mode == "zacetna_hisa":
        zacetna_hisa()
    elif game.mode == "svet_levo":
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

    atk_button_ui = Button(x=-280, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    atk_button_ui.draw()

    def_button_ui = Button(x=-125, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    def_button_ui.draw()

    spd_button_ui = Button(x=25, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    spd_button_ui.draw()

    dge_button_ui = Button(x=180, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    dge_button_ui.draw()

    def stat_roll_click(x, y):
        if atk_button_ui.is_clicked(x, y) and game.mode == "delitev_moci":
            atk_button_ui.clear()
            game.mode = "def_kocka"
            game.atk_button_pressed = True
        elif def_button_ui.is_clicked(x, y) and game.mode == "def_kocka":
            def_button_ui.clear()
            game.mode = "spd_kocka"
            game.def_button_pressed = True
        elif spd_button_ui.is_clicked(x, y) and game.mode == "spd_kocka":
            spd_button_ui.clear()
            game.mode = "dge_kocka"
            game.spd_button_pressed = True
        elif dge_button_ui.is_clicked(x, y) and game.mode == "dge_kocka":
            dge_button_ui.clear()
            game.mode = "begin"
            game.dge_button_pressed = True
            begin_button_on(roll_stat, atk_button_ui, def_button_ui, spd_button_ui, dge_button_ui)

    wn.onclick(stat_roll_click)




    
# begin
def begin_button_on(roll_stat, atk_button_ui, def_button_ui, spd_button_ui, dge_button_ui):
    begin_button_ui = Button(
        x=-100, y=-200, width=200, height=100,
        text="BEGIN", font=("gameovercre", 30, "normal"),
        text_offset=(40, 28)
    )
    begin_button_ui.draw()

    def begin_click(x, y):
        if begin_button_ui.is_clicked(x, y) and game.mode == "begin":
            begin_button_ui.clear()
            game.mode = "svet"

            atk_button_ui.clear()
            def_button_ui.clear()
            spd_button_ui.clear()
            dge_button_ui.clear()
            roll_stat.clear()

            

            make_fight_weapons()
            make_fight_items()
            make_chest()
            make_chest_inventory()
            svet()
            naredi_igralca()
            make_inventory()
            game.inventory_on = True
            make_inventory_items()
            user_interface_on()
            make_menu()

    wn.onclick(begin_click)



# igralceva statistika

def user_interface_on():
    user_interface = turtle.Turtle()
    user_interface.speed(0)
    user_interface.shape('oh no zojooooo\\slike\\stats.gif')
    user_interface.penup()
    user_interface.goto(-245, 258)

    def make_stat_turtle(x, value):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pencolor("black")
        t.color("#FEDA41")
        t.penup()
        t.goto(x, 256)
        t.write("{}".format(value), font=("gameovercre", 16, "normal"))
        return t

    make_stat_turtle(-382, game.atk)
    make_stat_turtle(-330, game.defense)
    make_stat_turtle(-282, game.spd)
    make_stat_turtle(-232, game.dge)

    for i, x in enumerate([-375, -345, -315]):
        if i < game.number_of_hearts:
            heart = turtle.Turtle()
            heart.speed(0)
            heart.shape('oh no zojooooo\\slike\\srcek.gif')
            heart.penup()
            heart.goto(x, 240)

    ui_hp = turtle.Turtle()
    ui_hp.hideturtle()
    ui_hp.speed(0)
    ui_hp.pencolor("black")
    ui_hp.color("#FEDA41")
    ui_hp.penup()
    ui_hp.goto(-149, 273)
    ui_hp.write("{}".format(game.hp), font=("gameovercre", 17, "normal"))

    game.ui_hp = ui_hp  # če jo potrebujemo kasneje


# Inventory

def make_inventory():
    game.ozadja["inventory"] = Ozadje("oh no zojooooo\\slike\\inventory.gif")




def open_inventory():
    if game.inventory_on:
        if game.mode not in ["weapons", "items"]:
            game.ozadja["inventory"].show(0, 0)
            game.curent_mode = game.mode
            game.mode = "weapons"
            move_item("wooden_sword", -225, -75)
            hide_item("heal_potion")
            inventory_button_on()
        else:
            game.ozadja["inventory"].hide()
            game.mode = game.curent_mode
            hide_item("wooden_sword")
            hide_item("heal_potion")
            delete_inventory_buttons()  # <-- to je manjkalo

   
            
    
# orozje
# items

def make_inventory_items():
    game.inventory_items["wooden_sword"] = InventoryItem("oh no zojooooo\\slike\\woodensword.gif")
    game.inventory_items["heal_potion"] = InventoryItem("oh no zojooooo\\slike\\heal_potion.gif")


def move_item(name, x, y):
    if name in game.inventory_items:
        game.inventory_items[name].move_to(x, y)

def hide_item(name):
    if name in game.inventory_items:
        game.inventory_items[name].hide()




        





# gumb za inventory iteme

def inventory_button_on():
    # Gumb za ITEMS
    items_button = Button(
        x=20, y=19, width=215, height=56,
        text="ITEMS", font=("gameovercre", 30, "normal"),
        color="#FFFB83", text_offset=(55, 3)
    )
    items_button.draw()

    # Gumb za WEAPONS
    weapons_button = Button(
        x=-240, y=19, width=215, height=56,
        text="WEAPONS", font=("gameovercre", 30, "normal"),
        color="#FFFB83", text_offset=(20, 3)
    )
    weapons_button.draw()

    # Shrani gumbe v game, če jih potrebuješ kasneje
    game.inventory_buttons = {
        "items": items_button,
        "weapons": weapons_button
    }

    wn.onclick(intventory_items_click)

def intventory_items_click(x, y):
    items_btn = game.inventory_buttons["items"]
    weapons_btn = game.inventory_buttons["weapons"]

    if game.mode == "weapons" and items_btn.is_clicked(x, y):
        game.mode = "items"
        move_item("heal_potion", -225, -75)
        hide_item("wooden_sword")

    elif game.mode == "items" and weapons_btn.is_clicked(x, y):
        game.mode = "weapons"
        move_item("wooden_sword", -225, -75)
        hide_item("heal_potion")

def delete_inventory_buttons():
    for btn in game.inventory_buttons.values():
        btn.clear()
    game.inventory_buttons.clear()



def prikazi_ozadje(ime):
    for oz in game.ozadja.values():
        oz.hide()
    game.ozadja[ime].show()

# svet
def svet():
    prikazi_ozadje("svet")
    game.set_mode("svet")
    move_chest()
    draw_monsters()

def svet_desno():
    prikazi_ozadje("svet_desno")
    game.set_mode("svet_desno")
    draw_monsters()

def svet_levo():
    prikazi_ozadje("svet_levo")
    game.set_mode("svet_levo")

# zacetna hisa
def zacetna_hisa():
    prikazi_ozadje("zacetna_hisa")
    game.set_mode("zacetna_hisa")
    igralec.setx(0)
    igralec.sety(-220)
    move_chest()



# chest
def make_chest():
    game.ozadja["chest"] = Ozadje("oh no zojooooo\\slike\\chest.gif")

    


def move_chest():
    if game.mode == "zacetna_hisa":
        game.ozadja["chest"].show(0, 100)
    else:
        game.ozadja["chest"].hide()

        

def make_chest_inventory():
    game.ozadja["chest_inventory"] = Ozadje("oh no zojooooo\\slike\\chest_inventory.gif")


def move_chest_inventory():
    if game.mode == "zacetna_hisa":
        game.ozadja["chest_inventory"].show(0, 200)
    else:
        game.ozadja["chest_inventory"].hide()





# monster interface
def move_monster_interface():
    if mode == "svet_desno":
        game.ozadja["monster_interface"].hide()
        golem_atk.clear()
        golem_def.clear()
        golem_spd.clear()
        golem_dge.clear()
        golem_hp.clear()

def make_monster_interface():
    game.ozadja["monster_interface"] = Ozadje("oh no zojooooo\\slike\\monster_interface.gif")
    game.ozadja["monster_interface"].show(242, 270)

    # Statistični prikaz pošasti ostane enak
    global golem_atk, golem_def, golem_spd, golem_dge, golem_hp
    golem_atk = turtle.Turtle()
    golem_atk.hideturtle()
    golem_atk.speed(0)
    golem_atk.pencolor("black")
    golem_atk.color("#BC1212")
    golem_atk.penup()
    golem_atk.goto(212, 256)
    golem_atk.write(m.monster_atk, font=("gameovercre", 16, "normal"))

    golem_def = turtle.Turtle()
    golem_def.hideturtle()
    golem_def.speed(0)
    golem_def.pencolor("black")
    golem_def.color("#BC1212")
    golem_def.penup()
    golem_def.goto(262, 256)
    golem_def.write(m.monster_def, font=("gameovercre", 16, "normal"))

    golem_spd = turtle.Turtle()
    golem_spd.hideturtle()
    golem_spd.speed(0)
    golem_spd.pencolor("black")
    golem_spd.color("#BC1212")
    golem_spd.penup()
    golem_spd.goto(312, 256)
    golem_spd.write(m.monster_spd, font=("gameovercre", 16, "normal"))

    golem_dge = turtle.Turtle()
    golem_dge.hideturtle()
    golem_dge.speed(0)
    golem_dge.pencolor("black")
    golem_dge.color("#BC1212")
    golem_dge.penup()
    golem_dge.goto(362, 256)
    golem_dge.write(m.monster_dge, font=("gameovercre", 16, "normal"))

    golem_hp = turtle.Turtle()
    golem_hp.hideturtle()
    golem_hp.speed(0)
    golem_hp.pencolor("black")
    golem_hp.color("#BC1212")
    golem_hp.penup()
    golem_hp.goto(149, 273)
    golem_hp.write("{}".format(m.monster_hp), font=("gameovercre", 17, "normal"))





def draw_monsters():
    for m in game.monsters:
        if m.svet == mode:
            m.monster.showturtle()
        else:
            m.monster.hideturtle()
        if m.alive == False:
                m.monster.hideturtle()



# monster fight screen

def fight_screen_monster():
    wn.bgcolor("#c9c9c9")
    prikazi_ozadje("fight_screen_monster")
    game.set_mode("start_fight")
    igralec_premik()
    fight_button_on()



# premik gumbov

def delete_button():
    if mode == "svet_desno":
        fight_button.clear()
        dont_fight_button.clear()
        items_button.clear()

        

# fight gumb

    
def fight_button_on():
    global fight_button_ui, items_button_ui, dont_fight_button_ui, run_button_ui

    # Ustvari gumbe
    fight_button_ui = Button(
        x=-220, y=-200, width=130, height=80,
        text="FIGHT", font=("gameovercre", 20, "normal"),
        text_offset=(30, 23)
    )
    items_button_ui = Button(
        x=-65, y=-200, width=130, height=80,
        text="ITEMS", font=("gameovercre", 20, "normal"),
        text_offset=(27, 23)
    )
    dont_fight_button_ui = Button(
        x=90, y=-200, width=130, height=80,
        text="DON'T\nFIGHT", font=("gameovercre", 20, "normal"),
        text_offset=(20, 10)
    )

    # Nariši gumbe
    fight_button_ui.draw()
    items_button_ui.draw()
    dont_fight_button_ui.draw()

    # Če smo v boju, dodamo še RUN gumb
    if game.mode == "in_fight":
        run_button_ui = Button(
            x=90, y=-200, width=130, height=80,
            text="RUN", font=("gameovercre", 20, "normal"),
            text_offset=(40, 23)
        )
        run_button_ui.draw()

    # Povežemo klik z obravnavo
    wn.onclick(fight_click)





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
    def fight_click(x, y):
        global mode, inventory_on, wooden_sword_value
        print(mode)
        if mode == "start_fight":
            if fight_button_ui.is_clicked(x, y):
                move_fight_weapons()
                fight_back_button_on()
                clear_fight_buttons()
                mode = "fight_weapons"
                move_wooden_sword()

            elif items_button_ui.is_clicked(x, y):
                move_fight_items()
                fight_back_button_on()
                clear_fight_buttons()
                mode = "fight_items"

            elif dont_fight_button_ui.is_clicked(x, y):
                mode = "svet_desno"
                move_monster_interface()
                svet_desno()
                clear_fight_buttons()
                igralec_premik()
                inventory_on = True

        elif mode == "in_fight" and run_button_ui.is_clicked(x, y):
            print("RUN clicked (v prihodnje: logika pobega)")

def clear_fight_buttons():
    fight_button_ui.clear()
    items_button_ui.clear()
    dont_fight_button_ui.clear()
    if mode == "in_fight":
        run_button_ui.clear()

# weapons

def make_fight_weapons():
    global fight_weapons
    fight_weapons = turtle.Turtle()
    fight_weapons.speed(0)
    fight_weapons.shape('oh no zojooooo\slike\WEAPONS.gif')
    fight_weapons.penup()
    fight_weapons.goto(1000,1000)


def move_fight_weapons():
    if mode != "fight_weapons":
        fight_weapons.setx(0)
        fight_weapons.sety(-183)
    if mode == "fight_weapons":
        fight_weapons.setx(1000)
        fight_weapons.sety(1000)
    if mode == "svet_desno":
        fight_weapons.setx(1000)
        fight_weapons.sety(1000)

def make_fight_items():
    global fight_items
    fight_items = turtle.Turtle()
    fight_items.speed(0)
    fight_items.shape('oh no zojooooo\slike\ITEMS.gif')
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
            if have_wooden_sword == True:
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
    global monster_attacked
    global player_attacked
    if spd_value >= m.monster_spd:
        player_attacked = True
        player_attack()
    else:
        monster_attacked = True
        monster_attack()
        
monster_attacked = False
player_attacked = False

def player_attack():
    global wooden_sword_value
    global monster_attacked
    if wooden_sword_value == True:
        damage =  roll_d4(3) + (atk_value // 2)
        print(damage)
    if int(random.uniform(1,101)) < m.monster_dge :
        print("u missed")
    else:
        m.monster_hp = m.monster_hp -(damage - m.monster_def // 2)
        golem_hp.clear()
        golem_hp.write( "{}".format(m.monster_hp), font=("gameovercre", 17, "normal"))
    if monster_attacked == True:
        check_hp()
    else:
        monster_attack()


def monster_attack():
    global hp_value
    damage =  roll_d4(1) + (m.monster_atk)
    print(damage)
    if int(random.uniform(1,101)) < m.monster_dge :
        print("it missed")
    else:
        hp_value = hp_value -(damage - def_value // 2)
        ui_hp.clear()
        ui_hp.write( "{}".format(hp_value), font=("gameovercre", 17, "normal"))
    if player_attacked == True:
        check_hp()
    else:
        player_attack()





def check_hp():
    global mode
    global inventory_on
    global hp_value
    global number_of_hearts
    if hp_value <= 0:
        print("you lost")
        fight_back_button.clear()
        mode = "svet_desno"
        delete_button()
        move_fight_weapons()
        move_wooden_sword()
        move_monster_interface()
        svet_desno()
        igralec_premik()
        inventory_on = True
        ui_hp.clear()
        hp_value = 100
        ui_hp.write( "{}".format(hp_value), font=("gameovercre", 17, "normal"))
        if number_of_hearts == 3:
            ui_srcek3.setx(1000)
            number_of_hearts = 2
        elif number_of_hearts == 2:
            ui_srcek2.setx(1000)
            number_of_hearts = 1
        elif number_of_hearts == 1:
            ui_srcek1.setx(1000)
            number_of_hearts = 0
        elif number_of_hearts == 0:
            print("game over")

    elif m.monster_hp <= 0:
        print("you win")
        fight_back_button.clear()
        fight_button_on()
        m.set_alive(False)
        mode = "svet_desno"
        move_fight_weapons() 
        move_wooden_sword()
        move_monster_interface()
        svet_desno()
        delete_button()
        igralec_premik()
        draw_monsters()
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
    igralec.shape('oh no zojooooo\slike\zojo.gif')
    igralec.penup()
    igralec.goto(0,-200)
    
    
# hoja igralca
    collisions = {
        "svet" : [(65, 300, 400, 50),(-400,-80,-364, -237),(-392, -219,391, -291),(362, -80, 400, -300),(-396, 297,-311, 20),(-330, 295,-100, 201)],
        "zacetna_hisa" : [(1000,1000,1000,1000)],
        "svet_desno" : [(-395, 293,-378, 5),(-394, 294,-136, 103),(-169, 290,44, 169),(55, 176,389, 93),(-397, -83,-385, -286),(-383, -209,-199, -290),(-227, -133,-167, -289),(-163, -55,23, -169),(29, -131,389, -287),(379, -50,400, -300)],
        "svet_levo" : [(1000,1000,1000,1000)],
        'start_fight' : [(-400,300,400,-300)],
        'fight_screen_monster' : [(-400,300,400,-300)]
    }


    def can_move(mode, x, y):
        ovire = collisions[mode]
        for xmin , ymax , xmax, ymin in ovire:
            if (xmin < x < xmax and ymin < y < ymax):
                return False
        return True
        
        
    def detection(mode, x, y):
        global object_detection
        ovire = game.objects[mode]
        hit = False
        object_detection = ""
        for xmin , ymax , xmax, ymin, object_name in ovire:
            if (xmin < x < xmax and ymin < y < ymax):
                hit = True
                object_detection = object_name
        return object_detection and hit
    
    def fight_detection(x,y):
        global m
        for m in game.monsters:
            if m.fight_monster(x,y, mode):
                return m
        return None
        
        

    
    def igralec_up():
        global x
        global y
        global mode
        global inventory_on
        x = igralec.xcor()
        y = igralec.ycor()
        if can_move(game.mode, x, y+5):
            y += 5
            x += 0
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('oh no zojooooo\slike\zojoback.gif')
        if detection(game.mode, x, y+5):
            if object_detection == "zacetna_hisa":
                mode = "zacetna_hisa"
                time.sleep(0.1)
                zacetna_hisa()
            if object_detection == "chest":
                print("hi")
                move_chest_inventory()
                open_inventory()
        if fight_detection(x,y+5):
            mode = "fight_screen_monster"
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
        if can_move(game.mode, x, y-5):
            y -= 5
            x += 0
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('oh no zojooooo\slike\zojo.gif')
        if detection(game.mode, x, y-5):
            if object_detection == "svet":
                time.sleep(0.1)
                igralec.setx(270)
                igralec.sety(41)
                mode = "svet"
                svet()
        if fight_detection(x,y-5):
            mode = "fight_screen_monster"
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
        if can_move(game.mode, x+5, y):
            y -= 0
            x += 5
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('oh no zojooooo\slike\Zojoright.gif')
        if detection(game.mode, x+5, y):
            if object_detection == "svet_desno":
                mode = "svet_desno"
                svet_desno()
                igralec.goto(-390,igralec.ycor()) 
            if object_detection == "svet":
                igralec.goto(-390,igralec.ycor())
                mode = "svet"
                svet()  
        if fight_detection(x+5,y):
            mode = "fight_screen_monster"
            fight_screen_monster()
            make_monster_interface()
            inventory_on = False

    
    def igralec_left():
        global x
        global y
        global mode
        global inventory_on
        x = igralec.xcor()
        y = igralec.ycor()
        if can_move(game.mode, x-5, y):
            y -= 0
            x -= 5
            igralec.sety(y)
            igralec.setx(x)
            igralec.shape('oh no zojooooo\slike\leftZojo.gif')
        if detection(game.mode, x-5, y):
            if object_detection == "svet_levo":
                mode = "svet_levo"
                svet_levo()
                igralec.goto(390,igralec.ycor())
            if object_detection == "svet":
                mode = "svet"
                svet()
                igralec.goto(390,igralec.ycor())
        if fight_detection(x-5,y):
            mode = "fight_screen_monster"
            fight_screen_monster()
            make_monster_interface()
            inventory_on = False
            
        


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
    menu.shape('oh no zojooooo\slike\menu.gif')
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
    game.set_hp(hp_value)
    game.save_game(f"game{game.game_n}.json")
    master.save_game("mastergame.json")
    

# quit game

def quit_game():
    global running
    running = False

# from turtle import *
# import turtle as tur
# def position(event):
#     a, b = (event.x - 400), 0-(event.y - 300)
#     print('{}, {}'.format(a, b))

# ws = tur.getcanvas()
# ws.bind('<Motion>', position)
# tur.done()


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



