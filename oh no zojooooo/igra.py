
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
wn.addshape(r'oh no zojooooo\slike\zojo.gif')
wn.addshape(r'oh no zojooooo\slike\zojoback.gif')
wn.addshape(r'oh no zojooooo\slike\Zojoright.gif')
wn.addshape(r'oh no zojooooo\slike\leftZojo.gif')
wn.addshape(r'oh no zojooooo\slike\hisa.gif')
wn.addshape(r'oh no zojooooo\slike\golem.gif')
wn.addshape(r'oh no zojooooo\slike\inventory.gif')
wn.addshape(r'oh no zojooooo\slike\woodensword.gif')
wn.addshape(r'oh no zojooooo\slike\heal_potion.gif')
wn.addshape(r'oh no zojooooo\slike\stats.gif')
wn.addshape(r'oh no zojooooo\slike\srcek.gif')
wn.addshape(r'oh no zojooooo\slike\WEAPONS.gif')
wn.addshape(r'oh no zojooooo\slike\ITEMS.gif')
wn.addshape(r'oh no zojooooo\slike\monster_interface.gif')
wn.addshape(r'oh no zojooooo\slike\svet1.gif')
wn.addshape(r'oh no zojooooo\slike\prozorno_ozadje.gif')
wn.addshape(r'oh no zojooooo\slike\menu.gif')
wn.addshape(r'oh no zojooooo\slike\svet2.gif')
wn.addshape(r'oh no zojooooo\slike\zacetna_hisa.gif')
wn.addshape(r'oh no zojooooo\slike\chest.gif')
wn.addshape(r'oh no zojooooo\slike\chest_inventory.gif')

#Spremenljivke

game = Game()
master = Master()


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
    make_inventory_items()
    user_interface_on()
    make_menu()
    povezi_tipke()

    if game.mode == "svet":
        svet()
    elif game.mode == "svet_desno":
        svet_desno()
    elif game.mode == "zacetna_hisa":
        zacetna_hisa()
    elif game.mode == "svet_levo":
        svet_levo()

    game.igralec.setx(x)
    game.igralec.sety(y)

    
def narisi_kvadrat(x, y=0, velikost=100):
    kvadrat = turtle.Turtle()
    kvadrat.hideturtle()
    kvadrat.speed(0)
    kvadrat.penup()
    kvadrat.goto(x - velikost // 2, y - velikost // 2)
    kvadrat.pendown()
    kvadrat.fillcolor("white")
    kvadrat.begin_fill()
    for _ in range(4):
        kvadrat.forward(velikost)
        kvadrat.left(90)
    kvadrat.end_fill()
    game.stat_roll["kvadrati"].append(kvadrat)


def soba_delitev_moci():
    wn.bgcolor("black")
    roll_stat = turtle.Turtle()
    roll_stat.speed(0)
    roll_stat.color("white")
    roll_stat.penup()
    roll_stat.hideturtle()
    roll_stat.goto(0, 190)
    roll_stat.write("Roll for stats", align="center", font=("gameovercre", 35, "normal"))
    game.stat_roll["roll_stat"] = roll_stat
    # Nariši kvadrate nad vsakim gumbom (y = 0)
    narisi_kvadrat(-230, y=0)  # ATK
    narisi_kvadrat(-75, y=0)   # DEF
    narisi_kvadrat(75, y=0)    # SPD
    narisi_kvadrat(230, y=0)   # DGE

    # Gumbi
    global atk_button_ui, def_button_ui, spd_button_ui, dge_button_ui
    atk_button_ui = Button(x=-280, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    atk_button_ui.draw()
    def_button_ui = Button(x=-125, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    def_button_ui.draw()
    spd_button_ui = Button(x=25, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    spd_button_ui.draw()
    dge_button_ui = Button(x=180, y=-200, width=100, height=100, text="ROLL", font=("gameovercre", 20, "normal"), text_offset=(17, 32))
    dge_button_ui.draw()
    game.stat_roll["atk_button_ui"] = atk_button_ui
    game.stat_roll["def_button_ui"] = def_button_ui
    game.stat_roll["spd_button_ui"] = spd_button_ui
    game.stat_roll["dge_button_ui"] = dge_button_ui

    def stat_roll_click(x, y):
        if atk_button_ui.is_clicked(x, y) and game.mode == "delitev_moci":
            atk_button_ui.clear()
            game.mode = "def_kocka"
            game.stat_roll["atk_pressed"] = True
            t, value = animiraj_kocko(-230, -30)
            game.stat_roll["atk_value"] = value
            game.stat_roll["atk_turtle"] = t
            game.set_atk(value)
            if value < 4 and not game.stat_roll["atk_adjusted"]:
                game.stat_roll["min"] += (5 - value)
                game.stat_roll["atk_adjusted"] = True

        elif def_button_ui.is_clicked(x, y) and game.mode == "def_kocka":
            def_button_ui.clear()
            game.mode = "spd_kocka"
            game.stat_roll["def_pressed"] = True
            t, value = animiraj_kocko(-75, -30, min_val=game.stat_roll["min"])
            game.stat_roll["def_value"] = value
            game.stat_roll["def_turtle"] = t
            game.set_def(value)
            if value < 4 and not game.stat_roll["def_adjusted"]:
                game.stat_roll["min"] += (5 - value)
                game.stat_roll["def_adjusted"] = True

        elif spd_button_ui.is_clicked(x, y) and game.mode == "spd_kocka":
            spd_button_ui.clear()
            game.mode = "dge_kocka"
            game.stat_roll["spd_pressed"] = True
            t, value = animiraj_kocko(75, -30, min_val=game.stat_roll["min"])
            game.stat_roll["spd_value"] = value
            game.stat_roll["spd_turtle"] = t
            game.set_spd(value)
            if value < 4 and not game.stat_roll["spd_adjusted"]:
                game.stat_roll["min"] += (5 - value)
                game.stat_roll["spd_adjusted"] = True

        elif dge_button_ui.is_clicked(x, y) and game.mode == "dge_kocka":
            dge_button_ui.clear()
            game.mode = "begin"
            game.stat_roll["dge_pressed"] = True
            t, value = animiraj_kocko(230, -30, min_val=game.stat_roll["min"])
            game.stat_roll["dge_value"] = value
            game.stat_roll["dge_turtle"] = t
            game.set_dge(value)
            begin_button_on()



    wn.onclick(stat_roll_click)





    
# begin
def begin_button_on():
    begin_button_ui = Button(
        x=-100, y=-200, width=200, height=100,
        text="BEGIN", font=("gameovercre", 30, "normal"),
        text_offset=(40, 28)
    )
    begin_button_ui.draw()

    def begin_click(x, y):
        if begin_button_ui.is_clicked(x, y) and game.mode == "begin":
            # Počisti vse kvadrate
            for kv in game.stat_roll.get("kvadrati", []):
                kv.clear()
            game.stat_roll["kvadrati"].clear()

            # Počisti vse številke
            for t in game.stat_roll.get("turtles", []):
                t.clear()
            game.stat_roll["turtles"].clear()

            # Počisti naslov
            if "roll_stat" in game.stat_roll and game.stat_roll["roll_stat"]:
                game.stat_roll["roll_stat"].clear()

            # Počisti gumbe
            begin_button_ui.clear()
            game.stat_roll["atk_button_ui"].clear()
            game.stat_roll["def_button_ui"].clear()
            game.stat_roll["spd_button_ui"].clear()
            game.stat_roll["dge_button_ui"].clear()

            # Nadaljuj igro
            make_monsters()
            game.mode = "svet"
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
            povezi_tipke()

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

    # Shrani srca v game.ui_srcka
    game.ui_srcka = []
    for i, x in enumerate([-375, -345, -315]):
        if i < game.number_of_hearts:
            heart = turtle.Turtle()
            heart.speed(0)
            heart.shape('oh no zojooooo\\slike\\srcek.gif')
            heart.penup()
            heart.goto(x, 240)
            game.ui_srcka.append(heart)

    # Prikaz HP
    ui_hp = turtle.Turtle()
    ui_hp.hideturtle()
    ui_hp.speed(0)
    ui_hp.pencolor("black")
    ui_hp.color("#FEDA41")
    ui_hp.penup()
    ui_hp.goto(-149, 273)
    ui_hp.write("{}".format(game.hp), font=("gameovercre", 17, "normal"))

    game.ui_hp = ui_hp



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
    game.igralec.setx(0)
    game.igralec.sety(-220)
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


def make_monsters():
    game.monsters = [
        Monster(
            hp=50,
            atk=5,
            defense=5,
            spd=5,
            dge=5,
            x=250,
            y=0,
            svet="svet_desno",
            slika="oh no zojooooo\\slike\\golem.gif",
            alive=True
        )
    ]



# monster interface
def move_monster_interface():
    if game.mode == "svet_desno":
        game.ozadja["monster_interface"].hide()
        if hasattr(game, "monster_stats_ui"):
            for t in game.monster_stats_ui.values():
                t.clear()
            game.monster_stats_ui.clear()


def make_monster_interface():
    monster = game.current_monster
    if not monster:
        return

    game.ozadja["monster_interface"] = Ozadje("oh no zojooooo\\slike\\monster_interface.gif")
    game.ozadja["monster_interface"].show(242, 270)

    # Ustvari in shrani prikaz statistike v game
    game.monster_stats_ui = {}

    def create_stat_turtle(x, value):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pencolor("black")
        t.color("#BC1212")
        t.penup()
        t.goto(x, 256)
        t.write(str(value), font=("gameovercre", 16, "normal"))
        return t

    game.monster_stats_ui["atk"] = create_stat_turtle(212, monster.monster_atk)
    game.monster_stats_ui["def"] = create_stat_turtle(262, monster.monster_def)
    game.monster_stats_ui["spd"] = create_stat_turtle(312, monster.monster_spd)
    game.monster_stats_ui["dge"] = create_stat_turtle(362, monster.monster_dge)

    hp_turtle = turtle.Turtle()
    hp_turtle.hideturtle()
    hp_turtle.speed(0)
    hp_turtle.pencolor("black")
    hp_turtle.color("#BC1212")
    hp_turtle.penup()
    hp_turtle.goto(149, 273)
    hp_turtle.write(str(monster.monster_hp), font=("gameovercre", 17, "normal"))
    game.monster_stats_ui["hp"] = hp_turtle



def draw_monsters():
    for m in game.monsters:
        if m.svet == game.mode:
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
    pozicioniraj_za_boj()
    fight_button_on()

def pozicioniraj_za_boj():
    game.igralec.goto(-200, 0)
    game.current_monster.monster.goto(200, 0)


# premik gumbov

def delete_button():
    if game.mode == "svet_desno":
        for key in ["fight", "dont_fight", "items"]:
            btn = game.fight_buttons.get(key)
            if btn:
                btn.clear()
        # Počisti tudi slovar
        for key in ["fight", "dont_fight", "items"]:
            game.fight_buttons.pop(key, None)

        

# fight gumb

def fight_button_on():
    # Ustvari gumbe
    fight_btn = Button(x=-220, y=-200, width=130, height=80, text="FIGHT", font=("gameovercre", 20, "normal"), text_offset=(30, 23))
    items_btn = Button(x=-65, y=-200, width=130, height=80, text="ITEMS", font=("gameovercre", 20, "normal"), text_offset=(27, 23))
    dont_fight_btn = Button(x=90, y=-200, width=130, height=80, text="DON'T\nFIGHT", font=("gameovercre", 20, "normal"), text_offset=(20, 10))

    # Nariši gumbe
    fight_btn.draw()
    items_btn.draw()
    dont_fight_btn.draw()

    # Shrani v slovar
    game.fight_buttons = {
        "fight": fight_btn,
        "items": items_btn,
        "dont_fight": dont_fight_btn
    }

    # Če smo v boju, dodamo še RUN gumb
    if game.mode == "in_fight":
        run_btn = Button(x=90, y=-200, width=130, height=80, text="RUN", font=("gameovercre", 20, "normal"), text_offset=(40, 23))
        run_btn.draw()
        game.fight_buttons["run"] = run_btn

    # Povežemo klik
    wn.onclick(fight_click)

def fight_click(x, y):
    fight_btn = game.fight_buttons.get("fight")
    items_btn = game.fight_buttons.get("items")
    dont_fight_btn = game.fight_buttons.get("dont_fight")
    run_btn = game.fight_buttons.get("run")
    print(game.mode)
    if game.mode == "start_fight":      
        if fight_btn and fight_btn.is_clicked(x, y):
            clear_fight_buttons()
            game.mode = "fight_weapons"
            move_fight_weapons()
            move_item("wooden_sword", -345, -135)
            fight_back_button_on()
            

        elif items_btn and items_btn.is_clicked(x, y):
            clear_fight_buttons()
            game.mode = "fight_items"
            move_fight_items()
            fight_back_button_on()


        elif dont_fight_btn and dont_fight_btn.is_clicked(x, y):
            game.mode = "svet_desno"
            move_monster_interface()
            svet_desno()
            clear_fight_buttons()
            igralec_premik()
            game.inventory_on = True

    elif game.mode == "in_fight" and run_btn and run_btn.is_clicked(x, y):
        print("RUN clicked (v prihodnje: logika pobega)")



def clear_fight_buttons():
    for btn in game.fight_buttons.values():
        btn.clear()
    game.fight_buttons.clear()


# weapons

def make_fight_weapons():
    game.ozadja["fight_weapons"] = Ozadje("oh no zojooooo\\slike\\WEAPONS.gif")



def move_fight_weapons():
    if game.mode == "fight_weapons":
        game.ozadja["fight_weapons"].show(0, -183)
    else:
        game.ozadja["fight_weapons"].hide()


def make_fight_items():
    game.ozadja["fight_items"] = Ozadje("oh no zojooooo\\slike\\ITEMS.gif")
    

def move_fight_items():
    if game.mode == "fight_items":
        game.ozadja["fight_items"].show(0, -183)
    else:
        game.ozadja["fight_items"].hide()


#back button

def fight_back_button_on():
    back_btn = Button(
        x=207, y=-272, width=130, height=80,
        text="BACK", font=("gameovercre", 20, "normal"),
        color="#FEDA41", text_offset=(30, 23)
    )
    back_btn.draw()
    game.fight_buttons["back"] = back_btn

    def combined_click(x, y):
        back_button_click(x, y)
        fight_weapon_click(x, y)

    wn.onclick(combined_click)


def back_button_click(x, y):
    back_btn = game.fight_buttons.get("back")
    if not back_btn or not back_btn.is_clicked(x, y):
        return

    if game.mode == "fight_weapons":
        back_btn.clear()
        game.fight_buttons.pop("back", None)
        game.mode = "start_fight"
        move_fight_weapons()
        fight_button_on()
        hide_item("wooden_sword")

    elif game.mode == "fight_items":
        back_btn.clear()
        game.fight_buttons.pop("back", None)
        game.mode = "start_fight"
        move_fight_items()
        fight_button_on()

def fight_weapon_click(x, y):
    if game.mode == "fight_weapons":
        # Koordinate orožja (wooden_sword) – prilagodi po potrebi
        sword_x, sword_y = -345, -135
        width, height = 60, 60  # približno območje klika

        if sword_x - width//2 < x < sword_x + width//2 and sword_y - height//2 < y < sword_y + height//2:
            game.wooden_sword_value = True
            game.mode = "in_fight"
            hide_item("wooden_sword")
            move_fight_weapons()
            game.fight_buttons.get("back", Button(0, 0, 0, 0, "")).clear()
            game.fight_buttons.pop("back", None)
            fight()

# rolling dice

def roll_d4(times_rolled):
    dice = 0
    while times_rolled > 0:
        dice += int(random.uniform(1,5))
        times_rolled -= 1
    return dice
        

# fight
def animiraj_igralca_napad():
    for _ in range(10):
        game.igralec.setx(game.igralec.xcor() + 25)
        wn.update()
        time.sleep(0.02)
    for _ in range(10):
        game.igralec.setx(game.igralec.xcor() - 25)
        wn.update()
        time.sleep(0.02)

def animiraj_posast_napad():
    monster = game.current_monster.monster
    for _ in range(10):
        monster.setx(monster.xcor() - 25)
        wn.update()
        time.sleep(0.02)
    for _ in range(10):
        monster.setx(monster.xcor() + 25)
        wn.update()
        time.sleep(0.02)


def fight():
    monster = game.current_monster
    if not monster:
        return

    if game.spd_value >= monster.monster_spd:
        game.player_attacked = True
        game.monster_attacked = False
        player_attack()
    else:
        game.monster_attacked = True
        game.player_attacked = False
        monster_attack()


        
def player_attack():
    monster = game.current_monster
    if not monster:
        return

    if game.wooden_sword_value:
        damage = roll_d4(3) + (game.atk_value // 2)
        print(damage)

        if int(random.uniform(1, 101)) < monster.monster_dge:
            print("u missed")
        else:
            animiraj_igralca_napad()
            monster.monster_hp -= (damage - monster.monster_def // 2)

            if "hp" in game.monster_stats_ui:
                game.monster_stats_ui["hp"].clear()
                game.monster_stats_ui["hp"].write(str(monster.monster_hp), font=("gameovercre", 17, "normal"))

    if game.monster_attacked:
        check_hp()
    else:
        monster_attack()




def monster_attack():
    monster = game.current_monster
    if not monster:
        return

    damage = roll_d4(1) + monster.monster_atk
    print(damage)

    if int(random.uniform(1, 101)) < game.dge:
        print("it missed")
    else:
        animiraj_posast_napad()
        game.hp -= (damage - game.def_value // 2)
        game.ui_hp.clear()
        game.ui_hp.write(str(game.hp), font=("gameovercre", 17, "normal"))

    if game.player_attacked:
        check_hp()
    else:
        player_attack()






def check_hp():
    monster = game.current_monster
    if not monster:
        return

    if game.hp <= 0:
        print("you lost")
        game.fight_buttons.get("back", Button(0, 0, 0, 0, "")).clear()
        game.mode = "svet_desno"
        delete_button()
        move_fight_weapons()
        hide_item("wooden_sword")
        move_monster_interface()
        svet_desno()
        igralec_premik()
        game.inventory_on = True
        game.ui_hp.clear()
        game.hp = 100
        game.ui_hp.write(str(game.hp), font=("gameovercre", 17, "normal"))

        if game.number_of_hearts > 0:
            game.ui_srcka[game.number_of_hearts - 1].setx(1000)
            game.number_of_hearts -= 1
        else:
            print("game over")

    elif monster.monster_hp <= 0:
        print("you win")
        game.fight_buttons.get("back", Button(0, 0, 0, 0, "")).clear()
        fight_button_on()
        monster.set_alive(False)
        game.mode = "svet_desno"
        move_fight_weapons()
        hide_item("wooden_sword")
        move_monster_interface()
        svet_desno()
        delete_button()
        igralec_premik()
        draw_monsters()
        game.inventory_on = True

    else:
        move_fight_weapons()
        game.fight_buttons.get("back", Button(0, 0, 0, 0, "")).clear()
        game.mode = "start_fight"
        fight_button_on()







# premikanje igralca

def igralec_premik():
    if game.mode == "fight_screen_monster":
        game.igralec.setx(1000)
        game.igralec.sety(1000)
    elif game.mode == "svet_desno":
        game.igralec.setx(150)
        game.igralec.sety(0)
    elif game.mode == "svet_levo":
        game.igralec.setx(-150)
        game.igralec.sety(0)
    elif game.mode == "zacetna_hisa":
        game.igralec.setx(0)
        game.igralec.sety(-220)
    elif game.mode == "svet":
        game.igralec.setx(0)
        game.igralec.sety(-200)





def naredi_igralca():
    igralec = turtle.Turtle()
    igralec.speed(0)
    igralec.shape('oh no zojooooo\\slike\\zojo.gif')
    igralec.penup()
    igralec.goto(0, -200)
    game.igralec = igralec

    
    

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
    for xmin, ymax, xmax, ymin, object_name in ovire:
        if xmin < x < xmax and ymin < y < ymax:
            hit = True
            object_detection = object_name
    return object_detection and hit

    
def fight_detection(x, y):
    for monster in game.monsters:
        if monster.fight_monster(x, y, game.mode):
            game.current_monster = monster
            return monster
    return None


        

    
def igralec_up():
    x = game.igralec.xcor()
    y = game.igralec.ycor()
    if can_move(game.mode, x, y + 5):
        y += 5
        game.igralec.sety(y)
        game.igralec.shape('oh no zojooooo\\slike\\zojoback.gif')

        if detection(game.mode, x, y):
            if object_detection == "zacetna_hisa":
                game.set_mode("zacetna_hisa")
                time.sleep(0.1)
                zacetna_hisa()
            elif object_detection == "chest":
                print("hi")
                move_chest_inventory()
                open_inventory()

        if fight_detection(x, y):
            game.set_mode("fight_screen_monster")
            fight_screen_monster()
            make_monster_interface()
            game.inventory_on = False

            
            
def igralec_down():
    x = game.igralec.xcor()
    y = game.igralec.ycor()
    if can_move(game.mode, x, y - 5):
        y -= 5
        game.igralec.sety(y)
        game.igralec.shape('oh no zojooooo\\slike\\zojo.gif')

        if detection(game.mode, x, y):
            if object_detection == "svet":
                time.sleep(0.1)
                game.igralec.setx(270)
                game.igralec.sety(41)
                game.set_mode("svet")
                svet()

        if fight_detection(x, y):
            game.set_mode("fight_screen_monster")
            fight_screen_monster()
            make_monster_interface()
            game.inventory_on = False


    
def igralec_right():
    x = game.igralec.xcor()
    y = game.igralec.ycor()
    if can_move(game.mode, x + 5, y):
        x += 5
        game.igralec.setx(x)
        game.igralec.shape('oh no zojooooo\\slike\\Zojoright.gif')

        if detection(game.mode, x, y):
            if object_detection == "svet_desno":
                game.set_mode("svet_desno")
                svet_desno()
                game.igralec.goto(-390, y)
            elif object_detection == "svet":
                game.set_mode("svet")
                svet()
                game.igralec.goto(-390, y)

        if fight_detection(x, y):
            game.set_mode("fight_screen_monster")
            fight_screen_monster()
            make_monster_interface()
            game.inventory_on = False


    
def igralec_left():
    x = game.igralec.xcor()
    y = game.igralec.ycor()
    if can_move(game.mode, x - 5, y):
        x -= 5
        game.igralec.setx(x)
        game.igralec.shape('oh no zojooooo\\slike\\leftZojo.gif')

        if detection(game.mode, x, y):
            if object_detection == "svet_levo":
                game.set_mode("svet_levo")
                svet_levo()
                game.igralec.goto(390, y)
            elif object_detection == "svet":
                game.set_mode("svet")
                svet()
                game.igralec.goto(390, y)

        if fight_detection(x, y):
            game.set_mode("fight_screen_monster")
            fight_screen_monster()
            make_monster_interface()
            game.inventory_on = False

        


# Tipkovnica
def povezi_tipke():
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
    menu = turtle.Turtle()
    menu.speed(0)
    menu.shape('oh no zojooooo\\slike\\menu.gif')
    menu.penup()
    menu.goto(1000, 1000)
    game.menu = menu

def menu_on():
    if game.inventory_on:
        if not game.menu_open:
            game.curent_mode = game.mode  # shrani trenutni način
            # NE nastavljamo več game.mode = "menu"
            game.menu.setx(0)
            game.menu.sety(0)
            save_and_quit_on()
            wn.onclick(menu_button_click)
            game.menu_open = True
            game.ui_hp.clear()
        else:
            # povrnemo prejšnji način igre
            game.menu_open = False
            game.menu.setx(1000)
            game.menu.sety(1000)
            if hasattr(game, "save_button"):
                game.save_button.clear()
            game.ui_hp.write(str(game.hp), font=("gameovercre", 17, "normal"))




def save_and_quit_on():
    # Ustvari gumb kot objekt razreda Button
    save_button = Button(
        x=-150, y=-100, width=300, height=80,
        text="SAVE AND QUIT", font=("gameovercre", 20, "normal"),
        color="#FEDA41", text_offset=(50, 23)
    )
    save_button.draw()
    game.save_button = save_button  # Shrani v game

def menu_button_click(x, y):
    if game.menu_open and hasattr(game, "save_button"):
        if game.save_button.is_clicked(x, y):
            save_game()
            quit_game()



# save

def save_game():
    game.set_x(game.igralec.xcor())
    game.set_y(game.igralec.ycor())
    game.set_hp(game.hp)
    game.save_game(f"game{game.game_n}.json")
    master.save_game("mastergame.json")


# quit game

def quit_game():
    game.running = False

def animiraj_kocko(x, y, min_val=1, max_val=10, rolls=12, font=("gameovercre", 40, "normal")):
    animator = turtle.Turtle()
    animator.hideturtle()
    animator.speed(0)
    animator.penup()
    animator.goto(x, y)
    animator.color("black")
    koncna_vrednost = None

    for _ in range(rolls):
        vrednost = random.randint(min_val, max_val)
        animator.clear()
        animator.write(str(vrednost), align="center", font=font)
        wn.update()  # <-- dodano za takojšnjo osvežitev
        time.sleep(0.10)
        koncna_vrednost = vrednost

    animator.clear()  # počisti zadnjo animacijo

    # Ustvari turtle za končno vrednost
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.color("black")
    t.write(str(koncna_vrednost), align="center", font=font)
    game.stat_roll["turtles"].append(t)
    return t, koncna_vrednost




# loop igre 

game.running = True
while game.running:
    wn.update()
    





